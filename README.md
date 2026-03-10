# MISP IOC Threat Intelligence Automation

Projet de veille cyber automatisée utilisant l'API MISP pour extraire les IOC (Indicators of Compromise) et générer des fichiers exploitables pour un SOC / SIEM.

## Features

- Connexion API MISP
- Extraction automatique des IOC
- Export CSV
- Filtrage TLP
- Automatisation via cron
- Compatible SOC / SIEM / Threat Intel

## Requirements

- Linux / Ubuntu
- Python 3.9+
- Accès API MISP
- Git

## Installation

Clone repository:

git clone https://github.com/USER/misp-ioc-threat-intel.git

cd misp-ioc-threat-intel

Run setup:

bash setup.sh

Edit configuration:

nano .env

Run script:

bash run.sh

## Cron automation

Edit crontab:

crontab -e

Example:

0 8 * * * $HOME/misp-ioc-threat-intel/run.sh >> $HOME/misp-ioc-threat-intel/cron.log 2>&1

Replace path if project installed elsewhere.

## Use case

- SOC monitoring
- Threat intelligence
- SIEM feed
- Cyber threat monitoring
- IOC collection

## Author

Cybersecurity lab project – MISP Threat Intelligence automation
