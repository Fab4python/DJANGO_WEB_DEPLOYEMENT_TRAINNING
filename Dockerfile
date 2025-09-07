# Utilise l'image officielle Python
FROM python:3.11-slim

# Définit le répertoire de travail
WORKDIR /app

# Installe les dépendances système
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Copie les fichiers de requirements et installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le code de l'application
COPY . .

# Collecte les fichiers statiques
RUN python manage.py collectstatic --noinput

# Effectue les migrations
RUN python manage.py migrate

# Crée un utilisateur non-root et change les permissions
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser:appuser /app
USER appuser

# Expose le port 8000
EXPOSE 8000

# Commande pour lancer l'application avec Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "deploymentapp.wsgi:application"]
