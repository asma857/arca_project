# Politique d’Accès et d’Autorisation

## 1. Objet
La présente politique définit les règles relatives à la gestion des accès aux systèmes, infrastructures, applications, plateformes cloud, réseaux internes et données de l’entreprise. Elle vise à garantir la confidentialité, l’intégrité et la disponibilité des ressources en appliquant des contrôles d’accès stricts et conformes aux normes de sécurité internationales.

## 2. Portée
Sont concernés par cette politique :
- Tous les employés, CDI, CDD, alternants et stagiaires.
- Les prestataires externes disposant d’un accès aux systèmes.
- Les fournisseurs ou partenaires ayant accès à des données ou applications.
- Les comptes techniques, comptes de service et comptes API.

L’application de cette politique est obligatoire sans exception.

## 3. Principe du Moindre Privilège
L’accès aux données et systèmes doit être strictement limité :
- À ce qui est nécessaire pour accomplir la mission de l'utilisateur.
- Aux ressources autorisées explicitement par la hiérarchie.
- Aux actions strictement requises dans le cadre du poste.

Aucun employé ne doit disposer de droits supérieurs à ce qui est justifié.

## 4. Accès Basés sur les Rôles (RBAC)
Les accès doivent être attribués selon un modèle **Role-Based Access Control**, incluant :
- Des permissions standardisées par département.
- Des niveaux d’accès pré-définis : lecture, écriture, exécution, administration.
- Une documentation de référence pour chaque rôle métier.
- Une révision trimestrielle des rôles et privilèges associés.

Tout accès non conforme doit être immédiatement retiré.

## 5. Processus d’Attribution des Accès
Tout accès doit respecter les exigences suivantes :
- Validation par le manager.
- Validation par l’équipe sécurité pour les accès sensibles.
- Journalisation automatique de la demande.
- Conservation d’un historique des modifications d'accès.

Aucun accès ne doit être créé sans ticket ou demande formelle.

## 6. Comptes Administrateurs
Les comptes administrateurs (‘admin’, ‘root’, ‘superuser’) doivent être soumis à :
- Une double validation (manager + sécurité).
- Une authentification multifacteur obligatoire.
- Un suivi régulier de leur utilisation.
- Un cloisonnement entre comptes admin et comptes utilisateurs.

## 7. Comptes Partagés
Les comptes partagés sont **strictement interdits**.  
Toute exception doit être documentée, approuvée et surveillée.

## 8. Comptes Temporaires
Les comptes temporaires doivent respecter :
- Une durée de validité maximale de 48h.
- Une expiration automatique programmée.
- Un accès limité au strict minimum.
- Une justification documentée.

## 9. Accès aux Données Sensibles
Les accès aux données sensibles (RH, finance, stratégie, données clients) doivent suivre ces règles :
- Restriction aux employés explicitement autorisés.
- Traçabilité complète des consultations.
- Chiffrement obligatoire au repos et en transit.
- Interdiction d’export non autorisé (PDF, Excel, mail).

Toute exportation doit être documentée et approuvée.

## 10. Accès aux Systèmes Critiques
Les systèmes critiques nécessitent :
- Un VPN sécurisé.
- Un dispositif MFA renforcé.
- Une validation hiérarchique + sécurité.
- Une surveillance temps réel des connexions.

## 11. Accès Externe (Prestataires)
Les accès fournis à des tiers doivent :
- Être limités à la durée du contrat.
- Avoir des permissions minimales.
- Être surveillés en continu.
- Être immédiatement révoqués à la fin du projet.

Aucun prestataire ne peut disposer d’un accès admin sauf exception documentée.

## 12. Révision des Droits d’Accès
Les revues d'accès doivent être réalisées :
- Tous les 3 mois pour les accès standards.
- Tous les 15 jours pour les accès administrateurs.
- Immédiatement après tout incident de sécurité.

La revue doit être documentée et approuvée par la direction.

## 13. Suspension des Accès
Les accès doivent être suspendus immédiatement dans les cas suivants :
- Démission ou départ.
- Absence prolongée non justifiée.
- Suspicion de comportement malveillant.
- Enquête interne en cours.

La suspension doit être traçable et enregistrée.

## 14. Révocation des Accès
Dans les 24h suivant le départ d’un employé :
- Tous les comptes doivent être désactivés.
- Les accès VPN doivent être coupés.
- Les clés API personnelles doivent être révoquées.
- Les sessions actives doivent être terminées.

## 15. Authentification Multifacteur
L’authentification MFA est obligatoire pour :
- Les comptes administrateurs.
- Les accès distants.
- Les applications critiques (RH, Finance, CRM).
- Tout accès à données sensibles.

## 16. Journalisation et Suivi
Tous les événements liés aux accès doivent être journalisés :
- Connexions réussies
- Connexions échouées
- Modifications des privilèges
- Accès aux ressources sensibles

Les logs doivent être conservés au moins 180 jours.

## 17. Sanctions
Toute violation de cette politique peut entraîner :
- Avertissement officiel
- Suspension d’accès
- Mise à pied
- Licenciement pour faute grave
- Action judiciaire si vol ou fuite de données

## 18. Révision
Cette politique doit être révisée tous les 12 mois et approuvée par le comité de sécurité.


