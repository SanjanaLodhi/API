from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import crud, schemas
from fastapi.responses import RedirectResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.post("/sales", response_model=schemas.Sale)
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    return crud.create_sale(db, sale)

@app.get("/sales", response_model=list[schemas.Sale])
def get_sales(phone_model: str = None, db: Session = Depends(get_db)):
    return crud.get_all_sales(db, phone_model)

@app.get("/sales/{sale_id}", response_model=schemas.Sale)
def get_sale(sale_id: int, db: Session = Depends(get_db)):
    sale = crud.get_sale_by_id(db, sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale

@app.put("/sales/{sale_id}", response_model=schemas.Sale)
def update_sale(sale_id: int, sale: schemas.SaleUpdate, db: Session = Depends(get_db)):
    updated = crud.update_sale(db, sale_id, sale)
    if not updated:
        raise HTTPException(status_code=404, detail="Sale not found")
    return updated

@app.delete("/sales/{sale_id}")
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_sale(db, sale_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Sale not found")
    return {"detail": "Sale deleted successfully"}

@app.get("/sales/stats", response_model=schemas.SaleStats)
def get_stats(db: Session = Depends(get_db)):
    return crud.get_statistics(db)
