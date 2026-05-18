"""Public endpoints (no auth required)."""
from fastapi import APIRouter

from database import db, serialize
from models import EnquiryCreate, Enquiry

router = APIRouter()


@router.get("/")
async def root():
    return {"service": "Ess Bee Heaters API", "status": "ok"}


@router.post("/enquiries", response_model=Enquiry, status_code=201)
async def create_enquiry(payload: EnquiryCreate):
    enquiry = Enquiry(**payload.dict())
    await db.enquiries.insert_one(enquiry.dict())
    return enquiry


@router.get("/content")
async def get_public_content():
    products = [serialize(d) async for d in db.products.find({'active': True}).sort('sort_order', 1)]
    testimonials = [serialize(d) async for d in db.testimonials.find({'active': True}).sort('sort_order', 1)]
    hero_slides = [serialize(d) async for d in db.hero_slides.find({'active': True}).sort('sort_order', 1)]
    gallery = [serialize(d) async for d in db.gallery.find().sort('sort_order', 1)]
    company = await db.company_info.find_one({'_singleton': 'company'})
    content = await db.site_content.find_one({'_singleton': 'content'})
    sections = await db.site_sections.find_one({'_singleton': 'sections'})
    return {
        "products": products,
        "testimonials": testimonials,
        "hero_slides": hero_slides,
        "gallery": gallery,
        "company": serialize(company) if company else {},
        "site_content": serialize(content) if content else {},
        "sections": serialize(sections) if sections else {},
    }
