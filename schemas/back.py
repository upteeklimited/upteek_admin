from typing import Optional, Any, Dict, List
from pydantic import BaseModel
from datetime import datetime


class BatchLogModel(BaseModel):
	id: int
	batch_id: Optional[int] = 0
	job_id: Optional[int] = 0
	info: Optional[str] = None
	status: Optional[int] = 0
	started_at: Optional[datetime] = None
	ended_at: Optional[datetime] = None
	created_at: Optional[datetime] = None

	class Config:
		orm_mode = True

class JobModel(BaseModel):
	id: int
	batch_id: Optional[int] = 0
	name: Optional[str] = None
	code: Optional[str] = None
	failed_reason: Optional[str] = None
	status_string: Optional[str] = None
	status: Optional[int] = 0
	started_at: Optional[datetime] = None
	ended_at: Optional[datetime] = None
	created_at: Optional[datetime] = None

	class Config:
		orm_mode = True

class BatchModel(BaseModel):
	id: int
	current_job_id: Optional[int] = 0
	batch_type: Optional[int] = 0
	reference: Optional[str] = None
	last_job_code: Optional[str] = None
	run_date: Optional[str] = None
	failed_reason: Optional[str] = None
	status_string: Optional[str] = None
	status: Optional[int] = 0
	started_at: Optional[datetime] = None
	ended_at: Optional[datetime] = None
	created_at: Optional[datetime] = None
	current_job: Optional[JobModel] = None
	jobs: Optional[List[JobModel]] = None
	batch_logs: Optional[List[BatchLogModel]] = None

	class Config:
		orm_mode = True

class BatchResponseModel(BaseModel):
	status: bool
	message: str
	data: Optional[BatchModel] = None

	class Config:
		orm_mode = True

class ContinueBatchModel(BaseModel):
	batch_id: int

	class Config:
		orm_mode = True
