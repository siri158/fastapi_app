from fastapi import APIRouter,status,Depends
from sqlalchemy.orm import Session
from database import get_db
from models.job import Job
from schemas.job import JobCreate,JobUpdate,JobResponse


router=APIRouter(prefix="/job",tags=["job"])
jobs=[]

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=JobResponse)
def create_jobs(job:JobCreate,db:Session=Depends(get_db)):
    jobs=db.query(Job).all()
    return jobs

@router.get("/")
def get_all_job():
    return jobs

@router.get("/{job_id}")
def get_job(job_id:int):
    return jobs[job_id]

#@router.get("/")
#def read_job():
#    return{"job":"job root"}

#@router.get("/{job_id}")
#def read_job(job_id:int):
#    return{"job_id":job_id}

@router.put("/{job_id}")
def update_company(job_id:int,jobs:JobUpdate):
    jobs[job_id]=jobs
    return jobs[job_id]

@router.delete("/{job_id}")
def delete_company(job_id:int):
    jobs.pop(job_id)
    return jobs[job_id]