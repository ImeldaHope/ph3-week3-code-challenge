from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer(), primary_key=True)
    name= Column(String())
    hometown = Column(String())
    
    _concerts = relationship('Concert', backref=backref('band'))    
    
    def __repr__(self):
        return f'Band(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'hometown={self.hometown})'
    
    def concerts(self):
        return self._concerts

    def venues(self):
        return [concert.venue for concert in self._concerts]
    
    def play_in_venue(self, venue, date):        
        concert = Concert(band_id=self.id, venue_id=venue.id, date=date)        
        return concert

    def all_introductions(self):
        """Returns an array of strings representing all the introductions for this band."""
        return [concert.introduction() for concert in self.concerts]

    @classmethod
    def most_performances(cls):       
        band_counts = (
            cls.query
            .outerjoin(Concert)
            .group_by(cls.id)
            .with_entities(cls, func.count(Concert.id).label('performance_count'))
            .all()
        )       
        
        most_performances_band = max(band_counts, key=lambda x: x.performance_count)
        return most_performances_band[0]
    
class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    city = Column(String())

    _concerts = relationship('Concert', backref=backref('venue'))
       
    def __repr__(self):
        return f'Venue(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'city={self.city})'
    
    def concerts(self):
        return self._concerts

    def bands(self):
        return [concert.band for concert in self._concerts]
    
    def concert_on(self, date):        
        return Concert.query.filter_by(venue_id=self.id, date=date).first()

    def most_frequent_band(self):
        band_counts = (
        Band.query
        .join(Concert)
        .filter(Concert.venue_id == self.id)
        .group_by(Band.id)
        .with_entities(Band, func.count(Concert.id).label('performance_count'))
        .all()
        )

        most_frequent_band = max(band_counts, key=lambda x: x.performance_count)
        return most_frequent_band[0]
    
class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer(), primary_key=True)
    date = Column(String())  
    band_id = Column(Integer(), ForeignKey('bands.id'))
    venue_id = Column(Integer(), ForeignKey('venues.id'))

    def __repr__(self):
        return f'Concert(id={self.id}, ' + \
               f'date={self.date}, ' + \
               f'band_id={self.band_id}, ' + \
               f'venue_id={self.venue_id})'
    
    def band(self):
        return self.band

    def venue(self):
        return self.venue
    
    def hometown_show(self):        
        return self.venue.city == self.band.hometown

    def introduction(self):        
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"