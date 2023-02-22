import click
import django
from django.conf import settings
from django.db import connections
from django.core.management import call_command
from django.db.backends.base.creation import BaseDatabaseCreation


@click.group()
def cli():
    pass


@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}')


@cli.command()
@click.argument('model_path')
@click.option('--database', default='default', help='Database engine name')
def model_to_sql(model_path, database):
    """
    Convert a Django model to raw SQL
    """
    # Initialize Django settings
    settings.configure()
    django.setup()

    # Load the model from the given path
    try:
        app_label, model_name = model_path.split('.')
        model = django.apps.apps.get_model(app_label, model_name)
    except (ImportError, ValueError, LookupError):
        click.echo(f"Could not load model from path '{model_path}'")
        return

    # Get the database connection settings
    connection = connections[database]
    db_settings = connection.settings_dict

    # Set up the database connection
    connection.ensure_connection()
    creation = BaseDatabaseCreation(connection)
    with connection.cursor() as cursor:
        # Generate the SQL for the model
        sql, references = connection.creation.sql_create_model(model, style=creation.sql_style)

        # Print the SQL to the command line
        click.echo(f"SQL for model '{model_path}' on database '{database}':\n")
        click.echo(sql)

cli.add_command(model_to_sql)
cli.add_command(hello)