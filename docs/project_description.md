Projet de veille cyber automatisée avec MISP.


Description
===========
Ce projet permet de mettre en place une veille cyber automatisée en utilisant MISP (Malware Information Sharing Platform) pour collecter et exploiter les indicateurs de compromission (IOC).

L’objectif est de faciliter le travail des équipes SOC, CERT, CSIRT ou Threat Intelligence en automatisant la collecte, le filtrage et l’export des IOC.

Fonctionnalités
================
Connexion à l’API MISP : récupération sécurisée des IOC.

Extraction automatique des IOC récents (ex : les 30 derniers événements).

Export CSV des IOC pour analyse ou intégration dans d’autres outils.

Filtrage TLP (Traffic Light Protocol) pour respecter la confidentialité et les niveaux de partage.

Automatisation via cron pour une mise à jour régulière.

Compatible SOC / CERT / CSIRT / Threat Intelligence pour enrichir vos outils de détection et corrélation.

Cas d’utilisation
=================
Collecter automatiquement les IOC depuis MISP sans intervention manuelle.

Alimenter des bases de données internes ou des outils SIEM/SOAR avec les IOC récents.

Générer des rapports CSV filtrés par TLP pour distribution interne.

Déclencher des actions automatiques via d’autres scripts ou playbooks de sécurité.

Avantages
=========
Réduction du travail manuel dans la veille cyber.

Meilleure réactivité face aux menaces récentes.

Centralisation et structuration des IOC pour exploitation rapide.



En resumé
=========

- Connexion API MISP
- Extraction IOC
- Export CSV
- Filtrage TLP
- Automatisation cron

Utilisation :

SOC / CERT / CSIRT / Threat Intel
