from sqlalchemy import *
from sqlalchemy.orm import Session, query
from sqlalchemy.ext.automap import automap_base

engine = create_engine('sqlite:///chinook.db')
session = Session(engine)
Base = automap_base()
Base.prepare(engine, reflect=True)
    

Albums = Base.classes.albums

    
def doQuerys():
    result1 = session.query(Albums.Title).limit(5).all()
    print("SELECT TOP 5 Title FROM Albums\n", result1, "\n")
    result2 = session.query(Albums.Title).filter( Albums.Title.like("%Rock%") ).limit(5).all()
    print("SELECT TOP 5 Title FROM Albums WHERE Albums.Title like '%Rock%'\n", result2, "\n")
    result3 = session.query(Albums.Title).order_by(desc(Albums.Title)).limit(5).all()
    print("SELECT TOP 5 Title FROM Albums ORDER BY DESC\n", result3, "\n")
    result4 = session.query(Albums.Title).group_by(Albums.ArtistId).limit(5).all()
    print("SELECT TOP 5 Title FROM Albums GROUP BY Albums.ArtistId\n", result4, "\n")

if __name__ == "__main__":
    doQuerys()
