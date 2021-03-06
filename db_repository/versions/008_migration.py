from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
response = Table('response', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('author', String(length=120)),
)

tweet = Table('tweet', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('author', String(length=120)),
    Column('body', String(length=190)),
    Column('is_read', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['response'].create()
    post_meta.tables['tweet'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['response'].drop()
    post_meta.tables['tweet'].drop()
