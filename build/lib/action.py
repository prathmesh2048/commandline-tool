import click
import os
import sys
from django.apps import apps
from django.core.management import call_command
from django.db import connection
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
settings.configure()
# 3dE*.cd5sYw8bnh
@click.group()
def cli():
    pass


@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}')


@cli.command()
@click.argument('model_path')
def convert(model_path):
    # Load the app containing the model
    app_label = model_path.split(".")[0]
    app_config = apps.get_app_config(app_label)

    # Load the model
    model_name = model_path.split(".")[1]
    model = app_config.get_model(model_name)

    # Get the fields for the model
    fields = model._meta.fields

    # Generate the SQL code to create the table
    with connection.cursor() as cursor:
        # Use Django's management command to generate the SQL
        call_command('sqlmigrate', app_label,
                     stdout=sys.stdout, stderr=sys.stderr)

        # Get the SQL code from the command output
        sql = sys.stdout.getvalue()

    # Return the SQL code for the table
    click.echo(f'app name is : {sql}', err=True)

cli.add_command(convert)
cli.add_command(hello)