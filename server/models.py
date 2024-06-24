from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Contains definitions of tables and associated schema constructs
metadata = MetaData()

# Create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

class Pet(db.Model):
    """
    Pet model representing a pet entity.
    """
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    species = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Pet id={self.id}, name={self.name}, species={self.species}>'

    @classmethod
    def create(cls, name, species):
        """
        Create a new pet record in the database.
        """
        pet = cls(name=name, species=species)
        db.session.add(pet)
        db.session.commit()
        return pet

    @classmethod
    def get_by_id(cls, pet_id):
        """
        Retrieve a pet record by its ID.
        """
        return cls.query.get(pet_id)

    def update(self, name=None, species=None):
        """
        Update the pet record.
        """
        if name:
            self.name = name
        if species:
            self.species = species
        db.session.commit()

    def delete(self):
        """
        Delete the pet record from the database.
        """
        db.session.delete(self)
        db.session.commit()
