from enum import Enum


class JobType:
    API = 'API'
    HTML = 'HTML'
    FORM = 'FORM'
    PDF = 'PDF'


class JobStatus:
    PENDING = "pending"
    RUNNING = "running"
    FINISHED = "finished"
    FAILED = "failed"
