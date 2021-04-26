from flask.cli import AppGroup
from .users import seed_users, undo_users
from .stores import seed_stores, undo_stores
from .products import seed_products, undo_products

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command


@seed_commands.command('all')
def seed():
    # Add seed functions here
    seed_users()
    seed_stores()
    seed_products()
# Creates the `flask seed undo` command


@seed_commands.command('undo')
def undo():
    # Add undo functions here
    undo_users()
    undo_stores()
    undo_products()
