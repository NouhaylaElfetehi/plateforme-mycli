import click
from mycli.s3_service import S3Service

s3 = S3Service()

@click.group()
def cli():
    """CLI pour gérer les buckets et objets S3."""
    pass

@cli.command()
def list_buckets():
    """Lister les buckets disponibles."""
    buckets = s3.list_buckets()
    click.echo(buckets)

@cli.command()
@click.argument('bucket_name')
def create_bucket(bucket_name):
    """Créer un nouveau bucket."""
    s3.create_bucket(bucket_name)
    click.echo(f"Bucket '{bucket_name}' créé avec succès.")

@cli.command()
@click.argument('bucket_name')
def delete_bucket(bucket_name):
    """Supprimer un bucket."""
    s3.delete_bucket(bucket_name)
    click.echo(f"Bucket '{bucket_name}' supprimé avec succès.")

@cli.command()
@click.argument('bucket_name')
@click.argument('file_path')
def upload_file(bucket_name, file_path):
    """Téléverser un fichier dans un bucket."""
    s3.upload_file(bucket_name, file_path)
    click.echo(f"Fichier {file_path} téléversé dans {bucket_name}.")

@cli.command()
@click.argument('bucket_name')
@click.argument('object_name')
@click.argument('file_path')
def download_file(bucket_name, object_name, file_path):
    """Télécharger un fichier depuis un bucket."""
    s3.download_file(bucket_name, object_name, file_path)
    click.echo(f"Fichier {object_name} téléchargé dans {file_path}.")

@cli.command()
@click.argument('bucket_name')
@click.argument('object_name')
def delete_file(bucket_name, object_name):
    """Supprimer un fichier d'un bucket."""
    s3.delete_file(bucket_name, object_name)
    click.echo(f"Fichier {object_name} supprimé du bucket {bucket_name}.")
@cli.command()
@click.argument('bucket_name')
def list_files(bucket_name):
    """Lister les fichiers dans un bucket spécifié."""
    files = s3.list_files(bucket_name)
    click.echo(files)


if __name__ == "__main__":
    cli()
