from sqlalchemy import *
from migrate import *

meta = MetaData()

chatter = Table(
        'chatter', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String(30), nullable=False),
        Column('currency', Integer, nullable=False),
        Column('totalMinutes', Integer, nullable=False),
        Column('follower', Boolean, nullable=False, default=False)
        )


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    chatter.create()
    pass


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    chatter.drop()
    pass
