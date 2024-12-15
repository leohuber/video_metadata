import click
from video_cleanup_metadata import cleanup_metadata_files

__version__ = "DEVELOPMENT_VERSION"

@click.group()
@click.version_option(__version__)
def cli():
    pass

@cli.command()
@click.argument('directory', type=click.Path(exists=True))
def cleanup_metadata(directory):
    """Cleanup metadata from a directory."""
    cleanup_metadata_files(directory)

if __name__ == '__main__':
    cli()