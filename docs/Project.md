# Projet de base de données « Spotifi »
*Groupe 3a/3b/1a, Enseignant Yannick Dégardin*
<br>

## Jalon 1 : faire le SEA (+dictionnaire de données) et en déduire le modèle relationnel.

Nous allons construire une base de données « Spotifi » dédiée à la location en streaming de musique.

La base va contenir :
- Plusieurs titres (de musique), chaque titre appartenant à un genre musical.
- Un titre est défini par son nom ; son auteur, sa durée, sa date de création.
- Un genre musical est simplement défini par un nom (« pop », « rock », « latino » etc).
- Des utilisateurs (nom prénom, date de naissance), liés à des contrats (un contrat par utilisateur mais plusieurs utilisateurs par contrat). Un contrat a une date de début et une date de fin et un nombre d’utilisateurs simultanés autorisés.
- Un utilisateur écoute (ou a écouté) plusieurs titres. On mémorisera la date d’écoute et la durée écoutée (pour savoir si l’utilisateur « zappe » de morceau).

## Jalon 2 : Créer la base, y mettre quelques données qui permettent des résultats aux requêtes suivantes :

1. Combien de titre et de genre sont disponibles dans la base ?
2. Combien de titres M. Dupond a-t-il écouté ?
3. Quel est le genre musical le plus écouté par M. Dupond ?
4. Quelle est la durée moyenne d’écoute des morceaux (en % : durée écoutée/durée du morceau *100) ?
5. Quel est le nombre de personnes maximum liées à un même contrat qui ont écouté de la musique **le même jour** ?
6. Quel est le nombre de fois où personnes liées à un même contrat qui ont écouté de la musique **simultanément** le 14/10/2024 ?

**On souhaite proposer des playlists automatiques aux utilisateurs, voici plusieurs stratégies :**
7. Ecrire une requête qui donnent les titres du genre musical le plus écouté par M. Dupond parmi les titres non encore écoutés dans ce genre.
8. A partir du genre musical le plus écouté de Mr Dupont et des titres les plus souvent écoutés par tous les **autres** utilisateurs (Mr Dupont exclu donc) dans ce même genre, écrire une requête qui propose une playlist.
9. Ecrire une requête qui crée une playlist pour M. Dupont en se basant sur les titres les plus écoutés par tous les utilisateurs ayant un écart d’âge de plus ou moins 5 ans.
10. Ecrire une requête qui crée une playlist pour M. Dupont en se basant sur les titres les plus écoutés par tous les utilisateurs en excluant les genres musicaux des titres que M. Dupont n’a pas écouté en entier.
