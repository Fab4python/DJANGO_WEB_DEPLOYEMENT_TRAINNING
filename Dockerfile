# Utilise l'image officielle Python
FROM python:3.11-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie les fichiers de requirements et installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le code de l'application
COPY . .

# Collecte les fichiers statiques
RUN python manage.py collectstatic --noinput

# Effectue les migrations
RUN python manage.py migrate

# Expose le port 8000
EXPOSE 8000

# Commande pour lancer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
