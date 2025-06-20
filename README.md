# 🔍 Nmap Vuln Scanner

> **Scanner de vulnérabilités réseau utilisant Nmap + Python | Génération de rapports JSON**

![License](https://img.shields.io/github/license/hamazos/nmap-vuln-scanner) 
![Python](https://img.shields.io/badge/python->=3.6-blue.svg) 
![Nmap](https://img.shields.io/badge/dependency-nmap-orange) 

---

## 🛠️ Fonctionnalités

- Scan réseau avec détection des hôtes actifs
- Détection des ports ouverts et services associés
- Exécution de scripts NSE pour identifier les vulnérabilités
- Génération d’un rapport JSON structuré
- Interface graphique simple avec Tkinter

---

## 🚀 Installation

```bash
git clone https://github.com/hamazos/nmap-vuln-scanner.git 
cd nmap-vuln-scanner
pip install -r requirements.txt
sudo apt install nmap  # Linux

💻 Utilisation
CLI :
bash
python main.py -t 192.168.1.1 --ports 20-100 -o results.json

1
python main.py -t 192.168.1.1 --ports 20-100 -o results.json
GUI :
bash
python gui/app.py

1
python gui/app.py


📦 Prérequis
Python 3.x
python-nmap, PyYAML
Nmap installé sur le système
📄 Licence
MIT License – voir LICENSE
