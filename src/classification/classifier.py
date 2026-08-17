"""
VIGIE — Volet LOGICIEL — Classification IA (implementation reelle)

Transposition directe de collecteurs/collecteur_rss.py (Sentinelle) :
meme cascade Groq -> Gemini -> repli, meme garde-fou cote code qui
ne fait jamais une confiance aveugle a la sortie du LLM.

Ne PAS reutiliser les cles GROQ_API_KEY/GEMINI_API_KEY de Sentinelle
en production -- quotas/couts separes. Cles a configurer specifiquement
pour ce repo (GitHub Actions secrets, une fois l'automatisation activee).
"""

import os
import json
import time
import requests

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

NATURES_VALIDES = ["incident_confirme", "fausse_alerte", "anomalie", "a_verifier"]
PAUSE_ENTRE_APPELS = 2.5  # meme marge que Sentinelle

etat = {"echecs_groq": 0, "echecs_gemini": 0, "groq_coupe": False, "gemini_coupe": False}
MAX_ECHECS = 4

def construire_prompt(evenement):
    return (
        "Tu classes un evenement de surete aeroportuaire pour le systeme VIGIE. "
        "Categories possibles :\n"
        "- incident_confirme : menace ou anomalie reelle averee, corroboree par "
        "des details concrets (position, horodatage coherent, signature technique).\n"
        "- fausse_alerte : signal capte mais sans danger reel (ex: drone autorise "
        "connu, appareil non lie a un drone, doublon d'un evenement deja traite).\n"
        "- anomalie : ecart notable mais nature incertaine, necessite verification "
        "humaine avant toute conclusion.\n"
        "- a_verifier : donnees insuffisantes pour trancher dans un sens ou l'autre.\n\n"
        "CONTEXTE DE RIGUEUR : ce systeme alimente une decision de surete "
        "aeroportuaire. En cas de doute reel, prefere 'a_verifier' a une "
        "affirmation trop confiante dans un sens ou l'autre.\n\n"
        "Evenement :\n"
        "Source : " + evenement.get("source_type", "inconnue") + "\n"
        "Titre : " + evenement.get("titre", "") + "\n"
        "Description : " + (evenement.get("description") or "")[:400] + "\n\n"
        'Reponds UNIQUEMENT en JSON : {"nature": "<categorie>", '
        '"criticite": <0-100>, "raison": "<1 phrase en francais>"}'
    )

def extraire_json(texte):
    """Meme garde-fou defense-en-profondeur que Sentinelle."""
    texte = texte.replace("```json", "").replace("```", "").strip()
    data = json.loads(texte)
    nature = str(data.get("nature", "")).strip().lower()
    criticite = int(data.get("criticite", 0))
    raison = str(data.get("raison", ""))[:250]
    if nature not in NATURES_VALIDES:
        nature = "a_verifier"
        criticite = min(criticite, 30)
    return nature, criticite, raison

def classifier_groq(evenement):
    if not GROQ_API_KEY or etat["groq_coupe"]:
        return None
    try:
        r = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": "Bearer " + GROQ_API_KEY, "Content-Type": "application/json"},
            json={
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "user", "content": construire_prompt(evenement)}],
                "temperature": 0.2,
                "response_format": {"type": "json_object"},
            },
            timeout=30,
        )
        rep = r.json()
        if "choices" not in rep:
            etat["echecs_groq"] += 1
            if etat["echecs_groq"] >= MAX_ECHECS:
                etat["groq_coupe"] = True
            return None
        etat["echecs_groq"] = 0
        return extraire_json(rep["choices"][0]["message"]["content"])
    except Exception as e:
        etat["echecs_groq"] += 1
        print("    [!] Erreur Groq : " + str(e)[:120])
        if etat["echecs_groq"] >= MAX_ECHECS:
            etat["groq_coupe"] = True
        return None

def classifier_gemini(evenement):
    if not GEMINI_API_KEY or etat["gemini_coupe"]:
        return None
    try:
        r = requests.post(
            "https://generativelanguage.googleapis.com/v1beta/models/"
            "gemini-2.0-flash:generateContent",
            headers={"x-goog-api-key": GEMINI_API_KEY, "Content-Type": "application/json"},
            json={"contents": [{"parts": [{"text": construire_prompt(evenement)}]}]},
            timeout=30,
        )
        rep = r.json()
        if "candidates" not in rep:
            etat["echecs_gemini"] += 1
            if etat["echecs_gemini"] >= MAX_ECHECS:
                etat["gemini_coupe"] = True
            return None
        etat["echecs_gemini"] = 0
        return extraire_json(rep["candidates"][0]["content"]["parts"][0]["text"])
    except Exception as e:
        etat["echecs_gemini"] += 1
        print("    [!] Erreur Gemini : " + str(e)[:120])
        if etat["echecs_gemini"] >= MAX_ECHECS:
            etat["gemini_coupe"] = True
        return None

def classifier(evenement):
    """Cascade complete -- jamais bloquant, meme en absence totale de cle API
    (utile pour tester le pipeline hors-ligne avec generate_test_events.py)."""
    time.sleep(PAUSE_ENTRE_APPELS if (GROQ_API_KEY or GEMINI_API_KEY) else 0)
    resultat = classifier_groq(evenement)
    source = "groq"
    if not resultat:
        resultat = classifier_gemini(evenement)
        source = "gemini"
    if not resultat:
        return "a_verifier", 20, "Repli -- IA indisponible ou non configuree ce cycle", "repli"
    nature, criticite, raison = resultat
    return nature, criticite, raison, source

if __name__ == "__main__":
    exemple = {
        "source_type": "rf_drone",
        "titre": "Signature RF drone detectee",
        "description": "Frequence: 2437 MHz, force: -45 dB, hors zone autorisee",
    }
    print(classifier(exemple))
