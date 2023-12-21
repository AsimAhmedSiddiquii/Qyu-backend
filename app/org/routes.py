from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.org.database import SessionLocal
from app.org.models import Org

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/org/get-org")
def get_organizations(db: Session = Depends(get_db)):
    organizations = db.query(Org).all()
    return organizations

@router.post("/org/new-org")
def create_organization(org_data: dict, db: Session = Depends(get_db)):
    new_org = Org(**org_data)
    db.add(new_org)
    db.commit()
    db.refresh(new_org)
    return new_org
