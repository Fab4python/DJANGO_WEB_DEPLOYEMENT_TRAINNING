#!/usr/bin/env python3
"""
Script de test pour valider la configuration de déploiement
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Exécute une commande et affiche le résultat"""
    print(f"\n🧪 Test: {description}")
    print(f"Commande: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Succès")
            if result.stdout:
                print(f"Output: {result.stdout.strip()}")
        else:
            print("❌ Échec")
            print(f"Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False
    
    return True

def main():
    print("🚀 Tests de validation pour le déploiement Django avec Nixpacks")
    
    # Tests de base
    tests = [
        ("python manage.py check", "Vérification de la configuration Django"),
        ("python manage.py collectstatic --noinput --dry-run", "Test de collecte des fichiers statiques"),
        ("gunicorn --check-config deploymentapp.wsgi:application", "Test de la configuration Gunicorn"),
    ]
    
    success_count = 0
    total_tests = len(tests)
    
    for cmd, description in tests:
        if run_command(cmd, description):
            success_count += 1
    
    # Vérification des fichiers de configuration
    print("\n🔍 Vérification des fichiers de configuration:")
    config_files = ["nixpacks.toml", ".env.example", "requirements.txt", "Procfile", "build.sh"]
    
    for file in config_files:
        if os.path.exists(file):
            print(f"✅ {file} présent")
            success_count += 0.5
        else:
            print(f"❌ {file} manquant")
    
    total_tests += len(config_files) * 0.5
    
    print(f"\n📊 Résultats: {success_count}/{total_tests} tests réussis")
    
    if success_count == total_tests:
        print("🎉 Tous les tests sont passés ! Le projet est prêt pour le déploiement sur Coolify.")
    else:
        print("⚠️  Certains tests ont échoué. Vérifiez la configuration.")
        sys.exit(1)

if __name__ == "__main__":
    main()
