"""All admin-protected endpoints: enquiries, stats, products, testimonials, hero,
gallery, company, site content, sections and image upload."""
import shutil
import uuid
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import APIRouter, HTTPException, Depends, UploadFile, File

from database import db, serialize, UPLOAD_DIR
from auth import verify_admin
from models import (
    StatusUpdate, Stats,
    Product, ProductInput,
    Testimonial, TestimonialInput,
    HeroSlide, HeroSlideInput,
    GalleryItem, GalleryInput,
    CompanyInfo, SiteContent, SiteSections,
)

router = APIRouter()


# ============== Image Upload ==============

@router.post("/admin/upload")
async def upload_image(file: UploadFile = File(...), email: str = Depends(verify_admin)):
    """Upload an image; returns a permanent URL served from /api/uploads/<filename>."""
    ext = (file.filename or 'file').rsplit('.', 1)[-1].lower()
    if ext not in ('jpg', 'jpeg', 'png', 'gif', 'webp', 'svg'):
        raise HTTPException(status_code=400, detail='Only image files are allowed')
    fname = f"{uuid.uuid4().hex}.{ext}"
    path = UPLOAD_DIR / fname
    with open(path, 'wb') as f:
        shutil.copyfileobj(file.file, f)
    return {"url": f"/api/uploads/{fname}", "filename": fname}


# ============== Enquiries ==============

@router.get("/admin/enquiries")
async def list_enquiries(
    email: str = Depends(verify_admin),
    status_filter: Optional[str] = None,
    search: Optional[str] = None,
    limit: int = 200,
    skip: int = 0,
):
    query = {}
    if status_filter in ('pending', 'read', 'replied'):
        query['status'] = status_filter
    if search:
        query['$or'] = [
            {'name': {'$regex': search, '$options': 'i'}},
            {'phone': {'$regex': search, '$options': 'i'}},
            {'email': {'$regex': search, '$options': 'i'}},
            {'message': {'$regex': search, '$options': 'i'}},
        ]
    cursor = db.enquiries.find(query).sort('created_at', -1).skip(skip).limit(limit)
    docs = [serialize(d) async for d in cursor]
    total = await db.enquiries.count_documents(query)
    return {"items": docs, "total": total, "limit": limit, "skip": skip}


@router.patch("/admin/enquiries/{enquiry_id}")
async def update_enquiry_status(enquiry_id: str, payload: StatusUpdate, email: str = Depends(verify_admin)):
    res = await db.enquiries.update_one({'id': enquiry_id}, {'$set': {'status': payload.status}})
    if res.matched_count == 0:
        raise HTTPException(status_code=404, detail='Enquiry not found')
    return serialize(await db.enquiries.find_one({'id': enquiry_id}))


@router.delete("/admin/enquiries/{enquiry_id}")
async def delete_enquiry(enquiry_id: str, email: str = Depends(verify_admin)):
    res = await db.enquiries.delete_one({'id': enquiry_id})
    if res.deleted_count == 0:
        raise HTTPException(status_code=404, detail='Enquiry not found')
    return {"ok": True, "id": enquiry_id}


@router.get("/admin/stats", response_model=Stats)
async def get_stats(email: str = Depends(verify_admin)):
    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week_start = today_start - timedelta(days=7)
    total = await db.enquiries.count_documents({})
    pending = await db.enquiries.count_documents({'status': 'pending'})
    read = await db.enquiries.count_documents({'status': 'read'})
    replied = await db.enquiries.count_documents({'status': 'replied'})
    today = await db.enquiries.count_documents({'created_at': {'$gte': today_start}})
    this_week = await db.enquiries.count_documents({'created_at': {'$gte': week_start}})
    return Stats(total=total, pending=pending, read=read, replied=replied, today=today, this_week=this_week)


# ============== Products ==============

@router.get("/admin/products")
async def list_products_admin(email: str = Depends(verify_admin)):
    return [serialize(d) async for d in db.products.find().sort('sort_order', 1)]


@router.post("/admin/products", response_model=Product, status_code=201)
async def create_product(payload: ProductInput, email: str = Depends(verify_admin)):
    if await db.products.find_one({'slug': payload.slug}):
        raise HTTPException(status_code=400, detail='Slug already exists')
    item = Product(**payload.dict())
    await db.products.insert_one(item.dict())
    return item


@router.put("/admin/products/{item_id}")
async def update_product(item_id: str, payload: ProductInput, email: str = Depends(verify_admin)):
    res = await db.products.update_one({'id': item_id}, {'$set': payload.dict()})
    if res.matched_count == 0:
        raise HTTPException(status_code=404, detail='Not found')
    return serialize(await db.products.find_one({'id': item_id}))


@router.delete("/admin/products/{item_id}")
async def delete_product(item_id: str, email: str = Depends(verify_admin)):
    res = await db.products.delete_one({'id': item_id})
    if res.deleted_count == 0:
        raise HTTPException(status_code=404, detail='Not found')
    return {"ok": True}


# ============== Testimonials ==============

@router.get("/admin/testimonials")
async def list_testimonials_admin(email: str = Depends(verify_admin)):
    return [serialize(d) async for d in db.testimonials.find().sort('sort_order', 1)]


@router.post("/admin/testimonials", response_model=Testimonial, status_code=201)
async def create_testimonial(payload: TestimonialInput, email: str = Depends(verify_admin)):
    item = Testimonial(**payload.dict())
    await db.testimonials.insert_one(item.dict())
    return item


@router.put("/admin/testimonials/{item_id}")
async def update_testimonial(item_id: str, payload: TestimonialInput, email: str = Depends(verify_admin)):
    res = await db.testimonials.update_one({'id': item_id}, {'$set': payload.dict()})
    if res.matched_count == 0:
        raise HTTPException(status_code=404, detail='Not found')
    return serialize(await db.testimonials.find_one({'id': item_id}))


@router.delete("/admin/testimonials/{item_id}")
async def delete_testimonial(item_id: str, email: str = Depends(verify_admin)):
    res = await db.testimonials.delete_one({'id': item_id})
    if res.deleted_count == 0:
        raise HTTPException(status_code=404, detail='Not found')
    return {"ok": True}


# ============== Hero ==============

@router.get("/admin/hero")
async def list_hero_admin(email: str = Depends(verify_admin)):
    return [serialize(d) async for d in db.hero_slides.find().sort('sort_order', 1)]


@router.post("/admin/hero", response_model=HeroSlide, status_code=201)
async def create_hero(payload: HeroSlideInput, email: str = Depends(verify_admin)):
    item = HeroSlide(**payload.dict())
    await db.hero_slides.insert_one(item.dict())
    return item


@router.put("/admin/hero/{item_id}")
async def update_hero(item_id: str, payload: HeroSlideInput, email: str = Depends(verify_admin)):
    res = await db.hero_slides.update_one({'id': item_id}, {'$set': payload.dict()})
    if res.matched_count == 0:
        raise HTTPException(status_code=404, detail='Not found')
    return serialize(await db.hero_slides.find_one({'id': item_id}))


@router.delete("/admin/hero/{item_id}")
async def delete_hero(item_id: str, email: str = Depends(verify_admin)):
    res = await db.hero_slides.delete_one({'id': item_id})
    if res.deleted_count == 0:
        raise HTTPException(status_code=404, detail='Not found')
    return {"ok": True}


# ============== Gallery ==============

@router.get("/admin/gallery")
async def list_gallery_admin(email: str = Depends(verify_admin)):
    return [serialize(d) async for d in db.gallery.find().sort('sort_order', 1)]


@router.post("/admin/gallery", response_model=GalleryItem, status_code=201)
async def create_gallery(payload: GalleryInput, email: str = Depends(verify_admin)):
    item = GalleryItem(**payload.dict())
    await db.gallery.insert_one(item.dict())
    return item


@router.delete("/admin/gallery/{item_id}")
async def delete_gallery(item_id: str, email: str = Depends(verify_admin)):
    res = await db.gallery.delete_one({'id': item_id})
    if res.deleted_count == 0:
        raise HTTPException(status_code=404, detail='Not found')
    return {"ok": True}


# ============== Company Info ==============

@router.get("/admin/company")
async def get_company_admin(email: str = Depends(verify_admin)):
    doc = await db.company_info.find_one({'_singleton': 'company'})
    return serialize(doc) if doc else {}


@router.put("/admin/company")
async def update_company(payload: CompanyInfo, email: str = Depends(verify_admin)):
    data = payload.dict()
    await db.company_info.update_one({'_singleton': 'company'}, {'$set': {**data, '_singleton': 'company'}}, upsert=True)
    return data


# ============== Site Content ==============

@router.get("/admin/site-content")
async def get_site_content_admin(email: str = Depends(verify_admin)):
    doc = await db.site_content.find_one({'_singleton': 'content'})
    return serialize(doc) if doc else {}


@router.put("/admin/site-content")
async def update_site_content(payload: SiteContent, email: str = Depends(verify_admin)):
    data = payload.dict()
    await db.site_content.update_one({'_singleton': 'content'}, {'$set': {**data, '_singleton': 'content'}}, upsert=True)
    return data


# ============== Site Sections ==============

@router.get("/admin/sections")
async def get_sections_admin(email: str = Depends(verify_admin)):
    doc = await db.site_sections.find_one({'_singleton': 'sections'})
    return serialize(doc) if doc else {}


@router.put("/admin/sections")
async def update_sections(payload: SiteSections, email: str = Depends(verify_admin)):
    data = payload.dict()
    await db.site_sections.update_one({'_singleton': 'sections'}, {'$set': {**data, '_singleton': 'sections'}}, upsert=True)
    return data
