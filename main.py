
# pyrefly: ignore [missing-import]
from fastapi.middleware.cors import CORSMiddleware
from database import session, engine
# pyrefly: ignore [missing-import]
from fastapi import FastAPI , Depends

from sqlalchemy.orm import Session

import database_models



from models import Product




app=FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database_models.Base.metadata.create_all(bind=engine)



@app.get("/")
def greet():
    return "Welcome to the World"

products =[
    Product(id=1,name="Tv",price=1200,quantity=2),
    Product(id=2,name="Mobiles",price=1200,quantity=2),
    Product(id=3,name="Remotes",price=1200,quantity=2)
    ]


def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = session()
    try:
        count = db.query(database_models.Product).count()
        if count == 0:
            for product in products:
                db.add(database_models.Product(**product.model_dump()))
            db.commit()
    finally:
        db.close()



init_db()






@app.get("/products")
@app.get("/products/")
def allproducts(db:Session=Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products





@app.get("/products/{id}")
@app.get("/products/{id}/")
def get_product(id:int,db:Session=Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        return db_product
    
    return "Product not found"


@app.post("/products")
@app.post("/products/")
def add_product(product:Product,db:Session=Depends(get_db)):
    new_product = database_models.Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.put("/products/{id}")
@app.put("/products/{id}/")
def update_product(id:int,product:Product,db:Session=Depends(get_db)):
    db_getproduct=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_getproduct:
        db_getproduct.name=product.name
        db_getproduct.price=product.price
        db_getproduct.quantity=product.quantity
        db.commit()
        return "Product updated successfully"
    
    return "No product found"



@app.delete("/products/{id}")
@app.delete("/products/{id}/")
def delete_product(id:int,db:Session=Depends(get_db)):
    get_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()

    if get_product:
        db.delete(get_product)
        db.commit()
        return "Product deleted successfully"
    return "Product not found"

    

    

