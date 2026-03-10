# MISP IOC Threat Intel Automation

Projet de veille cyber automatisée utilisant MISP API.

Fonctionnalités :

- Extraction des IOC
- Export CSV
- Filtrage TLP
- Automatisation cron
- Compatible SOC / SIEM

Installation

git clone https://github.com/USER/misp-ioc-threat-intel.git
cd misp-ioc-threat-intel

bash setup.sh

Modifier .env

bash run.sh

Automatisation

crontab -e

0 8 * * * /home/user/misp-ioc-threat-intel/run.sh >> cron.log 2>&1# MISP IOC Threat Intel Automation

Projet de veille cyber automatisée utilisant MISP API.

Fonctionnalités :

- Extraction des IOC
- Export CSV
- Filtrage TLP
- Automatisation cron
- Compatible SOC / SIEM

Installation

git clone https://github.com/USER/misp-ioc-threat-intel.git
cd misp-ioc-threat-intel

bash setup.sh

Modifier .env

bash run.sh

Automatisation

crontab -e

0 8 * * * /home/user/misp-ioc-threat-intel/run.sh >> cron.log 2>&1
