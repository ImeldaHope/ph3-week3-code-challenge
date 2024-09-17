#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Band, Venue, Concert

if __name__ == '__main__':
    engine = create_engine('sqlite:///concert.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Band).delete()
    session.query(Venue).delete()
    session.query(Concert).delete()

    fake = Faker()

    bands = []
    for i in range(50):
        band = Band(
            name=fake.unique.name(),
            hometown = fake.unique.city()            
        )

        # add and commit individually to get IDs back
        session.add(band)
        session.commit()

        bands.append(band)

    venues = []
    concerts = []
    for band in bands:
        for i in range(random.randint(1,5)):
            
            venue = Venue(
                title = fake.unique.company(),
                city = fake.city()                 
            )

            session.add(venue)
            session.commit()
            venues.append(venue)

            concert = Concert(
                band_id=band.id,
                venue_id=venue.id
            )
            concerts.append(concert)
            

    session.bulk_save_objects(concerts)
    session.commit()
    session.close()