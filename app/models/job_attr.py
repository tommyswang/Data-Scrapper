from enum import Enum


class JobType(Enum):
    API = 'API'
    HTML = 'HTML'
    FORM = 'FORM'
    PDF = 'PDF'


class JobStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    FINISHED = "finished"
    FAILED = "failed"
