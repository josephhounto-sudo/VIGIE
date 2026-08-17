"""
VIGIE — Volet MATERIEL — Capture Remote ID (squelette, couche 1)

Objectif : recevoir les signaux Remote ID (ASTM F3411 / OpenDroneID)
diffuses par les drones conformes en WiFi Beacon / Bluetooth, via un
ESP32, et produire un evenement conforme au schema commun.

Contrairement a rf_capture_stub.py (couche 2, detection d'energie RF
generique), cette couche ne necessite AUCUNE chaine RF additionnelle
(pas de downconverter) -- l'ESP32 recoit nativement WiFi/BT.

Le code ESP32 lui-meme (firmware C/C++) n'est PAS dans ce fichier --
il s'appuie sur un projet existant a adapter (voir docs/construction_rf.md
pour les references : opendroneid-core-c, ArduRemoteID cote reception,
projets derives comme Mesh-Mapper). Ce fichier Python cote serveur
recoit les detections (typiquement via port serie ou MQTT selon le
firmware choisi) et les met au format du schema commun.
"""

import json
from datetime import datetime

def construire_evenement(id_drone, lat, lon, altitude_m=None, source_id="remoteid_esp32_01"):
    """Construit un dict pret a inserer dans la table `evenements`.
    A appeler depuis le code qui lit le flux serie/MQTT de l'ESP32."""
    return {
        "source_type": "remote_id",
        "source_id": source_id,
        "titre": "Drone Remote ID detecte",
        "description": (
            "ID: " + str(id_drone) +
            (", altitude: " + str(altitude_m) + "m" if altitude_m is not None else "")
        ),
        "latitude": lat,
        "longitude": lon,
        "horodatage": datetime.now().isoformat(),
        "statut": "nouveau",
    }

def lire_flux_esp32():
    """TODO -- a implementer une fois le firmware ESP32 choisi et
    flashe. Deux options typiques :
    1. Port serie (USB) : pyserial, lecture ligne par ligne de JSON
       envoye par le firmware.
    2. MQTT si le firmware publie sur un broker local.
    Chercher le format de sortie exact du firmware retenu avant
    d'ecrire cette fonction -- ne pas deviner le format."""
    raise NotImplementedError("A implementer une fois le firmware ESP32 choisi")

def envoyer_vers_supabase(evenement):
    """TODO -- meme pattern que rf_capture_stub.py et Sentinelle."""
    print("[STUB] evenement Remote ID pret a inserer :", json.dumps(evenement, ensure_ascii=False))

if __name__ == "__main__":
    # Exemple de test SANS materiel : valide le format seulement.
    exemple = construire_evenement(id_drone="FA3ABCDEF12345", lat=6.1656, lon=1.2545, altitude_m=45)
    envoyer_vers_supabase(exemple)
