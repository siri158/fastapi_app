from fastapi import APIRouter
from schemas.job import jobcreate, jobupdate

router = APIRouter(prefix="/job", tags=["job"])
jobs=[]

@router.post("/")
def create_job(job: jobcreate):
    jobs.append(job)
    return jobs

@router.get("/")
def get_all_job():
    return jobs


@router.get("/{job_id}")
def get_job(job_id: int):
    return jobs[job_id]

@router.put("/{job_id}")
def update_job(job_id:int, job:jobupdate):
    jobs[job_id]=jobs
    return jobs

@router.delete("/{job_id}")
def delete_job(job_id:int):
    jobs.pop(job_id)
    return jobs