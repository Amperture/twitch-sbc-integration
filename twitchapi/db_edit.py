from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import db_models

engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

newuser = db_models.Chatter(
        name="amperture",
        currency = 1000000,
        totalMinutes = 10000000,
        follower = True)

session.add(newuser)
session.commit()
