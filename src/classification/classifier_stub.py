"""
VIGIE — Volet LOGICIEL — Classification IA (squelette)

Transposition directe de collecteurs/collecteur_rss.py (Sentinelle) :
meme cascade Groq -> Gemini -> repli, meme principe "classer la
NATURE avant de noter" avec garde-fou cote code.

Difference de fond avec Sentinelle : ici on classe des evenements
de surete (texte court + metadonnees), pas des offres freelance --
le prompt change, l'architecture cascade ne change pas.
"""

import os
import json

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

NATURES_VALIDES = ["incident_confirme", "fausse_alerte", "anomalie", "a_verifier"]

def construire_prompt(evenement):
    """TODO -- affiner avec l'equipe une fois le vocabulaire de
    nature/criticite valide avec l'encadrant. Structure de base
    calquee sur le prompt Sentinelle (classer la nature avant de
    noter, exemples few-shot, contexte de rarete)."""
    return (
        "Tu classes un evenement de surete aeroportuaire. Categories "
        "possibles :\n"
        "- incident_confirme : menace ou anomalie reelle averee.\n"
        "- fausse_alerte : signal capte mais sans danger reel "
        "(ex: drone autorise, appareil non lie a un drone).\n"
        "- anomalie : ecart notable mais nature incertaine, a verifier "
        "par un humain.\n"
        "- a_verifier : donnees insuffisantes pour trancher.\n\n"
        "Evenement :\n"
        "Titre : " + evenement.get("titre", "") + "\n"
        "Description : " + evenement.get("description", "")[:400] + "\n\n"
        'Reponds UNIQUEMENT en JSON : {"nature": "<categorie>", '
        '"criticite": <0-100>, "raison": "<1 phrase>"}'
    )

def extraire_json(texte):
    """Meme garde-fou defense-en-profondeur que Sentinelle : ne fait
    jamais une confiance aveugle a l'IA, recorrige si incoherent."""
    texte = texte.replace("```json", "").replace("```", "").strip()
    data = json.loads(texte)
    nature = str(data.get("nature", "")).strip().lower()
    criticite = int(data.get("criticite", 0))
    raison = str(data.get("raison", ""))[:250]
    if nature not in NATURES_VALIDES:
        nature = "a_verifier"
        criticite = min(criticite, 30)  # prudence si nature douteuse
    return nature, criticite, raison

def classifier_groq(evenement):
    """TODO -- copier telle quelle la fonction score_groq() de
    collecteurs/collecteur_rss.py, changer juste le prompt utilise
    et le parsing (nature+criticite au lieu de score+raison)."""
    raise NotImplementedError("A brancher sur la cle GROQ_API_KEY une fois l'equipe formee")

def classifier_gemini(evenement):
    """TODO -- meme transposition depuis score_gemini()."""
    raise NotImplementedError("Secours si Groq indisponible")

def classifier(evenement):
    """Cascade -- meme structure que evaluer() dans Sentinelle.
    TODO : brancher les deux fonctions ci-dessus une fois les cles
    API configurees pour ce projet (NE PAS reutiliser les cles
    Sentinelle en prod -- couts/quotas separes)."""
    try:
        return classifier_groq(evenement)
    except NotImplementedError:
        pass
    try:
        return classifier_gemini(evenement)
    except NotImplementedError:
        pass
    # Repli : jamais bloquant, meme logique que Sentinelle
    return "a_verifier", 20, "Repli -- IA indisponible ce cycle"

if __name__ == "__main__":
    exemple = {
        "titre": "Signature RF drone detectee",
        "description": "Frequence: 2437 MHz, force: -45 dB",
    }
    print(classifier(exemple))
