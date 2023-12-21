from sqlalchemy import Column, Integer, String
from app.org.database import Base

class Org(Base):
    __tablename__ = "org"

    id = Column(Integer, primary_key=True, index=True)
    org_name = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    mobile = Column(String, unique=True, index=True, nullable=False)
    location = Column(String, nullable=False)
    pincode = Column(String, nullable=False)
    org_type = Column(String, nullable=False)
    gstin = Column(String, unique=True, nullable=True)
    aadhar_no = Column(String, unique=True, nullable=True)
    category = Column(String, nullable=False)
    password = Column(String, nullable=False)

