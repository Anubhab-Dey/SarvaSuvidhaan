# Contains code to declare the DB table schema to store wheel specifications



from sqlalchemy import Column, String, Date, JSON
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class WheelSpecificationForm(Base):
    __tablename__ = "wheel_specification_forms"

    form_number = Column(String, primary_key=True, index=True)
    submitted_by = Column(String, nullable=False)
    submitted_date = Column(Date, nullable=False)
    
    # PostgreSQL native JSONB column for all the `fields` object
    fields = Column(JSONB, nullable=False)
