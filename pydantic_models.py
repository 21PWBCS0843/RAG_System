from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class ModelName(str, Enum):
    GEMINI_2_FLASH_EXP = "gemini-2.0-flash-exp"
    GEMINI_1_5_FLASH = "gemini-1.5-flash"
    GEMINI_1_5_PRO = "gemini-1.5-pro"

class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None)
    model: ModelName = Field(default=ModelName.GEMINI_2_FLASH_EXP)

class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model: ModelName

class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_timestamp: datetime

class DeleteFileRequest(BaseModel):
    file_id: int
