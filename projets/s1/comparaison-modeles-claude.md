# Comparaison des modèles Claude

Anthropic propose plusieurs modèles parce qu'aucun contexte d'usage n'est universel : un outil de chat rapide n'a pas besoin de la même puissance qu'un agent d'analyse juridique. Multiplier les modèles permet d'optimiser selon trois axes en tension permanente — capacité, vitesse et coût — sans sacrifier l'un pour l'autre.

---

## Tableau comparatif

| Modèle | Force principale | Cas d'usages idéaux | Quand l'éviter | Utilisateurs visés |
|---|---|---|---|---|
| **Opus 4.8** | Raisonnement complexe, nuance | Recherche, analyse multi-étapes, tâches autonomes longues | Requêtes simples, budget serré, latence critique | Chercheurs, équipes IA avancées |
| **Sonnet 4.6** | Équilibre performance/coût | Développement, rédaction, assistants, pipelines | Tâches ultra-légères où Haiku suffit | Développeurs, usages production généraux |
| **Haiku 4.5** | Vitesse et économie | Classification, résumé court, réponses temps réel | Problèmes complexes nécessitant du recul | Produits à fort volume, prototypes |

---

## Critères de sélection

- **Complexité de la tâche** : raisonnement multi-étapes ou ambiguïté élevée → Opus ; tâche claire et délimitée → Haiku ou Sonnet.
- **Contrainte de latence** : réponse en temps réel ou UX réactive → Haiku ou Sonnet.
- **Volume et coût** : millions de requêtes ou budget limité → Haiku ; usage modéré avec qualité exigée → Sonnet.
- **Autonomie de l'agent** : tâche déléguée sans supervision humaine → Opus pour minimiser les erreurs de jugement.
- **Défaut sûr** : en cas de doute, Sonnet. Il couvre la majorité des cas sans sur-dépenser.

---

## Claude Code : quel modèle, et pourquoi

**Modèle par défaut : Sonnet 4.6.**

Claude Code tourne sur Sonnet parce que le développement logiciel quotidien exige un bon raisonnement de code, une compréhension du contexte sur de longs fichiers, et une latence acceptable — sans justifier le coût d'Opus sur chaque complétion.

**Mode Fast (`/fast`) : bascule sur Opus, pas une variante de Sonnet.**

Activer `/fast` change de modèle : on passe de Sonnet 4.6 à Opus 4.x, avec une génération de tokens plus rapide. Ce n'est pas une dégradation vers un modèle plus petit, ni une simple optimisation de vitesse sur Sonnet — c'est littéralement un modèle différent, plus puissant, rendu plus réactif. Utile pour les tâches d'architecture, de refactoring lourd ou d'agents autonomes où la qualité de raisonnement prime sur le coût.

En résumé : Sonnet par défaut pour coder au quotidien, `/fast` (Opus) pour les tâches complexes où on veut plus de puissance sans sacrifier trop de latence.
