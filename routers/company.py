from fastapi import APIRouter,HTTPException,Depends,status
from schemas.company import CompanyCreate,CompanyUpdate,CompanyResponse
from models.company import Company
from models.job import Job   
from sqlalchemy.orm import session
from database import get_db


router=APIRouter(prefix="/company",tags=["company"])
companies=[]

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=CompanyResponse)
def create_company(company:CompanyCreate,db:session=Depends(get_db)):
    db_company = Company(**company.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

@router.get("/",status_code=status.HTTP_200_OK)
def get_all_company(db:session=Depends(get_db)):
    return companies

@router.get("/{company_id}",status_code=status.HTTP_200_OK,response_model=CompanyResponse)
def get_company(company_id:int,db:session=Depends(get_db)):
    return companies[company_id]

#@router.get("/")
#def read_company():
#    return{"company":"Company root"}

#@router.get("/{company_id}")
#def read_company(company_id:int):
#    return{"company_id":company_id}

@router.put("/{company_id}")
def update_company(company_id:int,company:CompanyUpdate,db:session=Depends(get_all_company)):
    companies[company_id]=company
    return companies[company_id]

@router.delete("/{company_id}")
def delete_company(company_id:int,db:session=Depends(get_db)):
    companies.pop(company_id)
    return companies[company_id]