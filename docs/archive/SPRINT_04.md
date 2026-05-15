# Rétrospective - Sprint 04

## Questions Clés pour le Bilan
1. **Qu'est-ce qui a bien fonctionné pendant ce sprint ?** (Succès, bonnes pratiques, outils efficaces mis en place).
2. **Quelles ont été les principales difficultés ou blocages rencontrés ?** (Défis techniques, problèmes de communication, manque de clarté).
3. **Quelles actions concrètes pouvons-nous mettre en place pour nous améliorer au prochain sprint ?** (Solutions proposées, nouvelles méthodes, ajustements).

---

## Retours par Rôle (Agents)

Merci à chaque membre de l'équipe de remplir sa section en répondant aux 3 questions clés ci-dessus.

### Architect

**1. Qu'est-ce qui a bien fonctionné pendant ce sprint ?**
L'adoption d'un composant léger comme `gTTS` avec restitution en base `BytesIO` a permis de concevoir une intégration vocale non-destructrice et optimale, sans saturer l'espace disque avec des mp3 temporaires. L'architecture prouve sa robustesse.

**2. Quelles ont été les principales difficultés ou blocages rencontrés ?**
La double nomenclature des numéros de ticket (US-005 vs INFRA-004) a créé une ambiguïté documentaire importante lors de la rédaction des spécifications. Le "rework" sur les bons identifiants a interrompu notre fluidité.

**3. Quelles actions concrètes pouvons-nous mettre en place pour nous améliorer au prochain sprint ?**
- Conserver l'ID unique `INFRA-` comme source de vérité technique et uniformiser tout le répertoire de documentation.
- Anticiper pour le composant *Speech-to-Text* les contraintes du navigateur (certificats HTTPS imposés pour l'accès micro) afin de donner une feuille de route claire au DevOps avant l'implémentation.
### Coder

**1. Qu'est-ce qui a bien fonctionné pendant ce sprint ?**
L'intégration de `gTTS` a été extrêmement rapide grâce à la directive claire de l'Architecte d'utiliser `BytesIO`. La fonctionnalité a pu être implémentée proprement dans `src/utils/audio_manager.py` et isolée. Streamlit gère parfaitement le flux d'octets avec le composant natif `st.audio`.

**2. Quelles ont été les principales difficultés ou blocages rencontrés ?**
La tentative de mise en place de l'interface _Speech-to-Text_ (STT) avec `audio-recorder-streamlit` a mis en lumière les limitations d'interface de Streamlit (difficile d'intégrer un bouton micro directement dans le `chat_input`). De ce fait, un simple bouton en barre latérale a été ajouté à titre symbolique pour le moment. L'absence d'infrastructure de transcription validée a forcé à ajourner cette fonctionnalité secondaire.

**3. Quelles actions concrètes pouvons-nous mettre en place pour nous améliorer au prochain sprint ?**
- Mettre en place des tests d'intégration (mocks API) de façon systématique pour notre `AudioManager` afin de garantir que l'application ne crashe pas si le service Text-to-Speech de Google est hors-ligne temporairement.
- Évaluer s'il est possible de développer un composant UI sur-mesure (via Streamlit Components) pour une vraie intégration de microphone au lieu d'utiliser un plugin contraint.

### QA

**1. Qu'est-ce qui a bien fonctionné pendant ce sprint ?**
Le comportement de dégradation gracieuse (fallback textuel) et l'usage de *BytesIO* ont bien tenu face aux tests, empêchant les crashs de l'application et l'encombrement du disque. La couverture du test manuelle a été exécutée parfaitement.

**2. Quelles ont été les principales difficultés ou blocages rencontrés ?**
Un oubli d'ajout de la dépendance métier (`SpeechRecognition`) dans le `requirements.txt` a causé un crash initial majeur lors du déploiement de l'essai Speech-to-Text (`ModuleNotFoundError`). Également, l'absence initiale d'un rafraîchissement d'IHM (`st.rerun()`) causait un décalage du retour audio.

**3. Quelles actions concrètes pouvons-nous mettre en place pour nous améliorer au prochain sprint ?**
- Ne jamais oublier de valider les imports globaux ("sanity check") suite à l'introduction d'un nouveau package avant de soumettre la feature au QA.
- Améliorer ou étoffer les tests automatiques (via `pytest`) pour capturer ces oublis environnementaux très tôt dans le pipeline.

### DevOps

**1. Qu'est-ce qui a bien fonctionné pendant ce sprint ?**
La procédure de livraison de la nouvelle fonctionnalité (TTS) s'est avérée simple sur le plan de l'infrastructure. L'utilisation d'une bilbiothèque légère (`gTTS`) couplée à une restitution en mémoire (`BytesIO`) nous évite de configurer des droits de gestion de fichiers temporaires sur le serveur.

**2. Quelles ont été les principales difficultés ou blocages rencontrés ?**
L'omission de la mise à jour du fichier `requirements.txt` par le Coder pour des dépendances secondaires a menacé l'intégrité du déploiement. De plus, la confusion dans les numéros de suivi (US-005 vs INFRA-004) a complexifié le versioning lors de la rédaction du `CHANGELOG.md` et risque de polluer notre historique Git.

**3. Quelles actions concrètes pouvons-nous mettre en place pour nous améliorer au prochain sprint ?**
- Introduire des vérifications automatiques (actions CI de base ou hooks `pre-commit`) pour s'assurer de synchroniser l'environnement virtuel avec les `requirements.txt`.
- Adopter une nomenclature unique stricte pour les branches Git et la documentation (soit utiliser `US-XX` partout, soit `INFRA-XX`).
