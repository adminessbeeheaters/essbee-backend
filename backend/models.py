"""All Pydantic models for the Ess Bee Heaters API."""
import uuid
from datetime import datetime, timezone
from typing import List, Optional, Literal, Dict
from pydantic import BaseModel, Field


# ============== Enquiries ==============

class EnquiryCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    phone: str = Field(..., min_length=4, max_length=30)
    email: Optional[str] = Field(None, max_length=200)
    subject: Optional[str] = Field(None, max_length=200)
    message: Optional[str] = Field(None, max_length=2000)
    source: str = Field(default='Website', max_length=80)


class Enquiry(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    phone: str
    email: Optional[str] = None
    subject: Optional[str] = None
    message: Optional[str] = None
    source: str = 'Website'
    status: Literal['pending', 'read', 'replied'] = 'pending'
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class StatusUpdate(BaseModel):
    status: Literal['pending', 'read', 'replied']


class Stats(BaseModel):
    total: int
    pending: int
    read: int
    replied: int
    today: int
    this_week: int


# ============== Auth ==============

class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'
    email: str
    expires_in: int


# ============== Products ==============

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    slug: str
    name: str
    image: str
    description: Optional[str] = ''
    sort_order: int = 0
    active: bool = True
    seo_title: Optional[str] = ''
    seo_description: Optional[str] = ''
    seo_keywords: Optional[str] = ''


class ProductInput(BaseModel):
    slug: str = Field(..., min_length=1, max_length=120)
    name: str = Field(..., min_length=1, max_length=200)
    image: str = Field(..., min_length=1)
    description: Optional[str] = ''
    sort_order: Optional[int] = 0
    active: Optional[bool] = True
    seo_title: Optional[str] = ''
    seo_description: Optional[str] = ''
    seo_keywords: Optional[str] = ''


# ============== Testimonials ==============

class Testimonial(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    role: str = 'Happy Customer'
    avatar: str = ''
    message: str
    sort_order: int = 0
    active: bool = True


class TestimonialInput(BaseModel):
    name: str
    role: Optional[str] = 'Happy Customer'
    avatar: Optional[str] = ''
    message: str
    sort_order: Optional[int] = 0
    active: Optional[bool] = True


# ============== Hero ==============

class HeroSlide(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    image: str
    alt: str = ''
    sort_order: int = 0
    active: bool = True


class HeroSlideInput(BaseModel):
    image: str
    alt: Optional[str] = ''
    sort_order: Optional[int] = 0
    active: Optional[bool] = True


# ============== Gallery ==============

class GalleryItem(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    image: str
    caption: str = ''
    sort_order: int = 0


class GalleryInput(BaseModel):
    image: str
    caption: Optional[str] = ''
    sort_order: Optional[int] = 0


# ============== Company Info ==============

class ContactPerson(BaseModel):
    name: str
    phone: str
    role: Optional[str] = ''


class CompanyInfo(BaseModel):
    name: str = 'Ess Bee Heaters Pvt. Ltd.'
    tagline: str = 'Heat Solution'
    established: str = 'An ISO 9001:2015 Certified Company'
    phones: List[str] = []
    emails: List[str] = []
    contacts: List[ContactPerson] = []
    address: str = ''
    whatsapp: str = ''
    business_hours: str = ''
    youtube_id: str = ''
    socials: Dict[str, str] = {}
    industries: List[str] = []


# ============== Site Content (text only) ==============

class SiteContent(BaseModel):
    home_h1: str = 'ESS BEE HEATERS PVT. LTD.'
    home_subtitle: str = ''
    home_welcome_title: str = 'Welcome to'
    home_welcome_p1: str = ''
    home_welcome_p2: str = ''
    about_p1: str = ''
    about_p2: str = ''
    about_p3: str = ''
    cta_title: str = 'You are 10 minutes away from the help you need'
    cta_text: str = ''
    # Page banner titles
    page_about_title: str = 'About Us'
    page_products_title: str = 'Our Products'
    page_gallery_title: str = 'Our Gallery'
    page_contact_title: str = 'Contact Us'
    # About page extras
    about_subtitle: str = 'Our Story'
    about_heading: str = 'Leading Manufacturer of Heating Elements'
    about_feature_1_title: str = 'ISO Certified'
    about_feature_1_desc: str = 'ISO 9001:2015 Certified Company with quality standards.'
    about_feature_2_title: str = 'Mission'
    about_feature_2_desc: str = 'Delivering reliable heating solutions for every industry.'
    about_feature_3_title: str = 'Vision'
    about_feature_3_desc: str = 'To be the most trusted heating element partner globally.'
    about_feature_4_title: str = 'Quality'
    about_feature_4_desc: str = 'Rigorous multi-stage in-house testing.'
    # Footer
    footer_about_text: str = 'Ess Bee Heaters Pvt. Ltd. is a leading manufacturer and pioneer in the field of Domestic and Industrial Heating Elements with in-depth knowledge of improved technology.'
    footer_copyright_suffix: str = 'Made by Hrithik Bansal'


# ============== Site Sections (visibility, theme, dynamic widgets) ==============

class StatCounter(BaseModel):
    icon: str = 'Award'
    label: str
    value: int = 0
    suffix: str = '+'


class WhyChooseFeature(BaseModel):
    icon: str = 'CheckCircle'
    title: str


class ManufacturingStep(BaseModel):
    icon: str = 'Cog'
    number: str
    title: str
    description: str = ''


class CertCard(BaseModel):
    title: str
    subtitle: str = ''
    icon: str = 'Award'


class NavItem(BaseModel):
    label: str
    path: str


class SiteSections(BaseModel):
    header_logo_url: str = ''
    topbar_welcome: str = 'Welcome to Ess Bee Heaters Pvt. Ltd.'
    nav_items: List[NavItem] = []
    ticker_items: List[str] = []
    stats_counters: List[StatCounter] = []
    whychoose_title: str = 'Built On Trust & Heat'
    whychoose_features: List[WhyChooseFeature] = []
    manufacturing_title: str = 'Our Manufacturing Process'
    manufacturing_steps: List[ManufacturingStep] = []
    certifications_title: str = 'Our Certifications'
    certifications_items: List[CertCard] = []
    industries_title: str = 'Industries We Cater'
    show_ticker: bool = True
    show_h1_band: bool = True
    show_welcome: bool = True
    show_stats: bool = True
    show_certifications: bool = True
    show_manufacturing: bool = True
    show_spotlight: bool = True
    show_whychoose: bool = True
    show_products: bool = True
    show_testimonials: bool = True
    show_cta: bool = True
    show_industries: bool = True
    show_gallery_preview: bool = True
    color_primary: str = '#f7941e'
    color_secondary: str = '#e67e00'
    color_dark: str = '#1a1a1a'
    color_red: str = '#d32f2f'
    seo_home_title: str = ''
    seo_home_description: str = ''
    seo_about_title: str = ''
    seo_about_description: str = ''
    seo_products_title: str = ''
    seo_products_description: str = ''
    seo_gallery_title: str = ''
    seo_gallery_description: str = ''
    seo_contact_title: str = ''
    seo_contact_description: str = ''
