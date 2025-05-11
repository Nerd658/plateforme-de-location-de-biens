# 🏠 Plateforme de Location B2B

**Plateforme web robuste et évolutive pour la location de biens entre entreprises et particuliers**, avec gestion des rôles (client/propriétaire), réservation, paiements, avis, et plus encore. Optimisée pour un grand nombre de connexions simultanées, cette application Django propose une architecture modulaire et scalable adaptée aux environnements professionnels.

---

## 🚀 Fonctionnalités principales

- 🔐 Authentification sécurisée et gestion des profils utilisateurs
- 🧍‍♂️ Rôle double : utilisateur peut être **client** ou **propriétaire**
- 📦 Module complet de gestion des **biens à louer**
- 📅 Système de **réservations** avec suivi en temps réel
- 💳 Intégration des **paiements**
- 📝 Gestion des **avis** pour renforcer la confiance
- ✅ Système de **validation** des profils et des biens
- 📂 Interfaces dédiées et séparées pour chaque rôle

---

## 🧱 Structure des modules

| Dossier                  | Description |
|--------------------------|-------------|
| `biens/`                 | Gestion des biens mis en location |
| `reservations/`          | Réservation des biens, calendrier, statut |
| `paiements/`             | Paiements et historiques des transactions |
| `profile_utilisateur/`   | Fiches profils, rôles, paramètres utilisateur |
| `avis/`                  | Système de notation et commentaires |
| `validation/`            | Workflow de validation des annonces |
| `users/`                 | Système d’authentification personnalisé |
| `plateforme_location/`   | Configuration globale Django du projet |

---

## 🛠️ Technologies utilisées

- **Backend** : Django, Django REST Framework  
- **Base de données** : SQLite (dev), PostgreSQL recommandé en prod  
- **Paiement** : Stripe (ou autre à intégrer)  
- **Auth** : JWT / Sessions (selon le contexte)  
- **Frontend** : HTML/CSS (peut être remplacé ou complété par Flutter ou React)

---

## ⚙️ Lancer le projet en local

```bash
# Cloner le dépôt
git clone https://github.com/ton-utilisateur/plateforme-location.git
cd plateforme-location

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # sous Linux/Mac
venv\Scripts\activate     # sous Windows

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate

# Lancer le serveur
python manage.py runserver
