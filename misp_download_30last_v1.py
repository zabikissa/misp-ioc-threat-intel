import os
from pymisp import PyMISP
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

load_dotenv()

url = os.getenv("MISP_URL")
key = os.getenv("MISP_KEY")
verifycert = os.getenv("MISP_VERIFYCERT", "False").lower() in ["true", "1", "yes"]

if not url or not key:
    raise ValueError("❌ Veuillez définir MISP_URL et MISP_KEY dans .env")

print(f"🌐 Connexion à MISP sur {url} (verifycert={verifycert})")

misp = PyMISP(url, key, verifycert)

NB_EVENTS = 30

print("📥 Téléchargement des événements avec attributs...")

events = misp.search(
    controller="events",
    limit=NB_EVENTS,
    pythonify=True,
    includeAttributes=True
)

ioc_list = []

for event in events:

    event_id = getattr(event, "id", "")
    event_info = getattr(event, "info", "")
    event_date = getattr(event, "date", "")

    event_tags = []
    if hasattr(event, "tags"):
        event_tags = [t.name for t in event.tags]

    for attr in getattr(event, "attributes", []):

        ioc_list.append({
            "event_id": event_id,
            "event_info": event_info,
            "attribute_type": attr.type,
            "attribute_value": attr.value,
            "category": attr.category,
            "tlp": next((t for t in event_tags if "tlp" in t.lower()), ""),
            "tags": ",".join(event_tags),
            "date": event_date
        })

df = pd.DataFrame(ioc_list)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"ioc_last_{NB_EVENTS}_events_{timestamp}.csv"

df.to_csv(output_file, index=False)

print(f"✅ Export terminé : {output_file} ({len(df)} IOC)")
