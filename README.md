# Projet Django pour Déploiement

Une application Django simple créée spécifiquement pour tester différentes méthodes de déploiement.

## Caractéristiques

- Django 5.2.6
- Base de données SQLite
- Page d'accueil statique
- Configuration simplifiée pour le déploiement

## Installation en local

1. Cloner le projet
2. Créer un environnement virtuel :
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```
3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
4. Effectuer les migrations :
   ```bash
   python manage.py migrate
   ```
5. Lancer le serveur de développement :
   ```bash
   python manage.py runserver
   ```

L'application sera accessible sur http://127.0.0.1:8000/

## Déploiement

Ce projet a été conçu pour être facilement déployé sur différentes plateformes :

- VPS traditionnel
- Coolify
- Docker
- Heroku
- DigitalOcean App Platform
- Etc.

## Structure du projet

```
web-deployment-project/
├── deploymentapp/          # Configuration principale Django
├── homepage/               # Application pour la page d'accueil
├── templates/             # Templates HTML
├── manage.py             # Script de gestion Django
├── requirements.txt      # Dépendances Python
├── db.sqlite3           # Base de données SQLite (créée après migration)
└── README.md           # Ce fichier
```
