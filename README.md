**Plateforme MyCLI**
Ce projet fournit une interface en ligne de commande (CLI) en Python pour interagir avec un service compatible S3 (comme AWS S3 ou MinIO). Vous pouvez gérer des buckets et des fichiers (téléchargement, téléversement, suppression, etc.) directement depuis votre terminal.

**Pré-requis**
-Python 3.6 ou supérieur
-boto3 pour interagir avec les services S3
-Click pour créer des commandes CLI
-Un accès à un service S3 compatible, comme AWS S3 ou MinIO

**Technologies utilisées**
Python 3 : Langage de programmation principal.
boto3 : SDK AWS pour interagir avec les services S3.
Click : Outil de création d'interface en ligne de commande (CLI).

**Utilisation**
Lancer les commandes CLI
Vous pouvez exécuter les commandes CLI suivantes :

*1. Lister les buckets*
Pour lister tous les buckets dans votre service S3 :

```python -m mycli.cli list-buckets```

*2. Créer un bucket*
Pour créer un nouveau bucket :

```python -m mycli.cli create-bucket <nom-du-bucket>```

*3. Supprimer un bucket*
Pour supprimer un bucket existant :

```python -m mycli.cli delete-bucket <nom-du-bucket>```

*4. Téléverser un fichier dans un bucket*
Pour téléverser un fichier dans un bucket :

```python -m mycli.cli upload-file <nom-du-bucket> <chemin-du-fichier-local>```

*5. Télécharger un fichier depuis un bucket*
Pour télécharger un fichier à partir d'un bucket :

```python -m mycli.cli download-file <nom-du-bucket> <nom-du-fichier> <chemin-local-de-destination>```

*6. Supprimer un fichier d'un bucket*
Pour supprimer un fichier dans un bucket :

```python -m mycli.cli delete-file <nom-du-bucket> <nom-du-fichier>```

*7. Lister les fichiers dans un bucket*
Pour lister tous les fichiers dans un bucket :

```python -m mycli.cli list-files <nom-du-bucket>```
