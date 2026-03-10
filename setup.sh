#!/bin/bash

echo "=== Installation projet MISP IOC ==="

sudo apt update
sudo apt install -y python3 python3-venv python3-pip

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

if [ ! -f .env ]; then
    cp .env.example .env
    echo ".env créé, modifier avec ta clé API"
fi

echo "Installation terminée"
