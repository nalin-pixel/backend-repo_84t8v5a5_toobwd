"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Add your own schemas here:
# --------------------------------------------------

class Program(BaseModel):
    """
    Academic programs offered by the college
    Collection name: "program"
    """
    name: str = Field(..., description="Program name, e.g., B.E. Computer Science")
    degree: str = Field(..., description="Degree type, e.g., B.E., M.Tech, MBA")
    department: str = Field(..., description="Department offering the program")
    duration: str = Field(..., description="Duration, e.g., 4 Years")
    description: str = Field(..., description="Short description")
    eligibility: Optional[str] = Field(None, description="Eligibility criteria")
    fees: Optional[str] = Field(None, description="Approximate fees or range")
    brochure_url: Optional[str] = Field(None, description="Link to brochure or syllabus")

class Event(BaseModel):
    """
    College events and announcements
    Collection name: "event"
    """
    title: str
    date: datetime
    location: str
    description: str
    image_url: Optional[str] = None

class Inquiry(BaseModel):
    """
    Admission/contact inquiries from the website
    Collection name: "inquiry"
    """
    name: str
    email: EmailStr
    phone: Optional[str] = None
    message: str
    source: Optional[str] = Field("website", description="Where the inquiry originated")
