# README technique - GESTEMP (Gestion des Emplois du Temps)

Ce README technique fournit des informations sur le projet GESTEMP, un système de gestion des emplois du temps pour l'Université de Yaoundé I.

## Description du projet
GESTEMP est une application web destinée à faciliter la planification des cours, la gestion des salles de classe et des ressources au sein de l'université. Il permet de générer des emplois du temps précis tout en tenant compte des contraintes spécifiques liées aux enseignants, aux salles et aux équipements. L'objectif principal de ce projet est d'améliorer l'efficacité des opérations et de réduire les conflits liés à l'allocation des salles de cours.

## Fonctionnalités principales
- Saisie et gestion des horaires des cours, des disponibilités des enseignants et des ressources.
- Analyse des contraintes et génération automatique des emplois du temps en respectant les préférences des enseignants et des étudiants.
- Possibilité de modifications manuelles de l'emploi du temps initial par les responsables de département et les enseignants.
- Validation de l'emploi du temps finalisé par les parties prenantes concernées.
- Diffusion de l'emploi du temps via une interface en ligne, des impressions en PDF et des notifications par e-mail.
- Gestion des modifications ultérieures de l'emploi du temps en cas de changements de dernière minute ou d'événements imprévus.

## Technologies utilisées
- Backend : Django Rest Framework (Python)
- Frontend : React JS (JavaScript)
- Base de données : PostgreSQL

## Liens
- [Cahier des charges](lien_vers_le_cahier_de_charges)
- [Diagrammes UML](lien_vers_les_diagrammes_UML)

## Procédure pour lancer le serveur React en local
1. Assurez-vous d'avoir Node.js et npm installés sur votre machine.
2. Clonez le dépôt Git de GESTEMP sur votre machine locale.
3. Accédez au répertoire du frontend à l'aide de la ligne de commande.
4. Exécutez la commande `npm install` pour installer les dépendances.
5. Ensuite, exécutez la commande `npm start` pour lancer le serveur React.
6. Vous pouvez maintenant accéder à GESTEMP en ouvrant votre navigateur et en visitant `http://localhost:3000`.

## Procédure pour lancer le backend
1. Assurez-vous d'avoir Python et pip installés sur votre machine.
2. Clonez le dépôt Git de GESTEMP sur votre machine locale.
3. Accédez au répertoire du backend à l'aide de la ligne de commande.
4. Créez un environnement virtuel en exécutant la commande `python -m venv env`.
5. Activez l'environnement virtuel avec la commande spécifique à votre système d'exploitation.
6. Installez les dépendances en exécutant la commande `pip install -r requirements.txt`.
7. Configurez les paramètres du backend selon vos besoins (base de données, etc.).
8. Effectuez les migrations de la base de données avec la commande `python manage.py migrate`.
9. Enfin, lancez le serveur backend avec la commande `python manage.py runserver`.
