# Projet Django pour Déploiement

Une application Django simple créée spécifiquement pour tester différentes méthodes de déploiement.

## Caractéristiques

- Django 5.2.6
- Base de données SQLite
- Page d'accueil statique
- Configuration simplifiée pour le déploiement
- **Configuration Nixpacks pour Coolify**
- WhiteNoise pour servir les fichiers statiques
- Gunicorn comme serveur WSGI

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

### Déploiement avec Coolify et Nixpacks (Recommandé)

Ce projet est configuré avec **Nixpacks** pour un déploiement simple sur **Coolify** :

1. **Créer un nouveau projet** dans Coolify
2. **Connecter votre repository Git**
3. **Sélectionner Nixpacks** comme buildpack (automatiquement détecté grâce au fichier `nixpacks.toml`)
4. **Configurer les variables d'environnement** :
   - `SECRET_KEY` : Une clé secrète Django sécurisée
   - `DEBUG` : `False` pour la production
5. **Déployer** 🚀

#### Variables d'environnement requises

```bash
SECRET_KEY=votre-clé-secrète-django-ici
DEBUG=False
```

#### Fichiers de configuration Nixpacks

- `nixpacks.toml` : Configuration simplifiée du build et démarrage
- `Procfile` : Commande de démarrage (standard)
- `build.sh` : Script de build pour collecter les fichiers statiques
- `.env.example` : Variables d'environnement de référence

### Autres plateformes supportées

Ce projet peut aussi être déployé sur :

- VPS traditionnel
- Docker
- Heroku
- DigitalOcean App Platform
- Etc.

## Structure du projet

```
web-deployment-project/
├── deploymentapp/          # Configuration principale Django
│   ├── settings.py         # Paramètres configurés pour la production
│   ├── urls.py
│   └── wsgi.py
├── homepage/               # Application pour la page d'accueil
├── templates/             # Templates HTML
├── staticfiles/           # Fichiers statiques collectés
├── nixpacks.toml          # Configuration Nixpacks simplifiée
├── Procfile               # Commande de démarrage
├── build.sh               # Script de build
├── requirements.txt       # Dépendances Python (Django, Gunicorn, WhiteNoise)
├── .env.example          # Variables d'environnement de référence
├── manage.py             # Script de gestion Django
├── db.sqlite3            # Base de données SQLite (créée après migration)
└── README.md            # Ce fichier
```
