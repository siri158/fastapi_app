from fastapi import APIRouter

from schemas.company import companycreate, companyupdate

router = APIRouter(prefix="/company", tags=["company"])
companies = []

@router.post("/")
def create_company(company: companycreate):
    companies.append(company)
    return companies

@router.get("/")
def get_all_company():
    return companies

@router.get("/{company_id}")
def get_company(company_id: int):
    return companies[company_id]

#@router.get("/")
#def read_company():
 # return {"company": "company root"}

@router.put("/{company_id}")
def update_company(company_id:int, company:companyupdate):
    companies[company_id]=company
    return companies

@router.delete("/{company_id}")
def delete_company(company_id:int):
    companies.pop(company_id)
    return companies

