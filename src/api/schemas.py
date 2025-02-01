from pydantic import BaseModel
from typing import List

class EmailRequest(BaseModel):
    content: str

class PhishingResponse(BaseModel):
    is_phishing: bool
    confidence: float

class BatchEmailRequest(BaseModel):
    emails: List[str]

class BatchPhishingResponse(BaseModel):
    results: List[PhishingResponse]