from sqlalchemy.orm import Session
from models import IPhoneSale
from schemas import SaleCreate, SaleUpdate
from sqlalchemy import func

def create_sale(db: Session, sale: SaleCreate):
    db_sale = IPhoneSale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

def get_all_sales(db: Session, phone_model: str = None):
    if phone_model:
        return db.query(IPhoneSale).filter(IPhoneSale.phone_model == phone_model).all()
    return db.query(IPhoneSale).all()

def get_sale_by_id(db: Session, sale_id: int):
    return db.query(IPhoneSale).filter(IPhoneSale.id == sale_id).first()

def update_sale(db: Session, sale_id: int, updated_sale: SaleUpdate):
    db_sale = get_sale_by_id(db, sale_id)
    if db_sale:
        for key, value in updated_sale.dict().items():
            setattr(db_sale, key, value)
        db.commit()
        db.refresh(db_sale)
    return db_sale

def delete_sale(db: Session, sale_id: int):
    db_sale = get_sale_by_id(db, sale_id)
    if db_sale:
        db.delete(db_sale)
        db.commit()
    return db_sale

def get_statistics(db: Session):
    total_sales = db.query(func.count(IPhoneSale.id)).scalar()
    total_revenue = db.query(func.sum(IPhoneSale.price)).scalar() or 0.0
    most_popular = db.query(IPhoneSale.phone_model, func.count(IPhoneSale.phone_model))\
                     .group_by(IPhoneSale.phone_model)\
                     .order_by(func.count(IPhoneSale.phone_model).desc())\
                     .first()
    avg_price = db.query(func.avg(IPhoneSale.price)).scalar() or 0.0

    return {
        "total_sales": total_sales,
        "total_revenue": float(total_revenue),
        "most_popular_model": most_popular[0] if most_popular else None,
        "average_price": float(avg_price)
    }
