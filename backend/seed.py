"""Seed data and one-time database seeding routine."""
from database import db
from models import Product, Testimonial, HeroSlide, GalleryItem

SEED_PRODUCTS = [
    {"slug": "high-watt-density-cartridge-heater", "name": "HIGH WATT DENSITY CARTRIDGE HEATER", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721029389Untitled-1.jpg"},
    {"slug": "hot-air-gun-heaters", "name": "HOT AIR GUN HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721029591Untitled-1.jpg"},
    {"slug": "hot-air-gun-machines", "name": "HOT AIR GUN MACHINES", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721029711Untitled-1.jpg"},
    {"slug": "knife-box-heaters", "name": "KNIFE BOX HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721029811Untitled-1.jpg"},
    {"slug": "low-watt-density-cartridge-heaters", "name": "LOW WATT DENSITY CARTRIDGE HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721029961Untitled-1.jpg"},
    {"slug": "main-fold-heaters", "name": "MAIN FOLD HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721030027Untitled-1.jpg"},
    {"slug": "medium-wave-ir-heaters-quartz-silica-heaters", "name": "MEDIUM WAVE IR / QUARTZ SILICA HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721032709Untitled-1.jpg"},
    {"slug": "mica-band-heaters", "name": "MICA BAND HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721032779Untitled-1.jpg"},
    {"slug": "mini-space-heaters", "name": "MINI SPACE HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721032851MINI%20SPACE%20HEATERS.jpg"},
    {"slug": "oil-immersion-heaters", "name": "OIL IMMERSION HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721033051Untitled-1.jpg"},
    {"slug": "quartz-box-heaters-silica-box-heaters", "name": "QUARTZ BOX / SILICA BOX HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721033151Untitled-1.jpg"},
    {"slug": "ring-type-heaters", "name": "RING TYPE HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721033271Untitled-1.jpg"},
    {"slug": "round-plate-immersion-heaters", "name": "ROUND PLATE IMMERSION HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721033384Untitled-1.jpg"},
    {"slug": "sealed-nozzle-heater", "name": "SEALED NOZZLE HEATER", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721033626Untitled-1.jpg"},
    {"slug": "shortwave-ir-heater", "name": "SHORTWAVE IR HEATER", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721034372Untitled-1.jpg"},
    {"slug": "shortwave-ir-heaters-with-reflector-box", "name": "SHORTWAVE IR HEATERS WITH REFLECTOR BOX", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721034936Untitled-1.jpg"},
    {"slug": "sic-heating-elements", "name": "SIC HEATING ELEMENTS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721035097Untitled-1.jpg"},
    {"slug": "water-immersion-heaters", "name": "WATER IMMERSION HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1720593058Untitled-4.jpg"},
    {"slug": "tubler-heaters", "name": "TUBLER HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1720593229Untitled-4.jpg"},
    {"slug": "thread-buring-heaters", "name": "THREAD BURNING HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1720593411Untitled-4.jpg"},
    {"slug": "tape-heaters", "name": "TAPE HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1720593552Untitled-4.jpg"},
    {"slug": "strip-heaters-strip-finned-heater", "name": "STRIP HEATERS / STRIP FINNED HEATER", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1720593669Untitled-4.jpg"},
    {"slug": "space-heaters", "name": "SPACE HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1720593761Untitled-4.jpg"},
    {"slug": "air-finned-heaters", "name": "AIR FINNED HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721027701Untitled-1.jpg"},
    {"slug": "aluminum-casting-heaters", "name": "ALUMINUM CASTING HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721028015Untitled-1.jpg"},
    {"slug": "bobbine-heaters", "name": "BOBBINE HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721028189Untitled-1.jpg"},
    {"slug": "brass-casting-heaters", "name": "BRASS CASTING HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721028322Untitled-1.jpg"},
    {"slug": "cast-iron-heaters", "name": "CAST IRON HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721028488qz.jpg"},
    {"slug": "ceramic-band-heaters", "name": "CERAMIC BAND HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721028756Untitled-1.jpg"},
    {"slug": "ceramic-ir-heaters", "name": "CERAMIC IR HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721028842Untitled-1.jpg"},
    {"slug": "chemical-immersion-heaters", "name": "CHEMICAL IMMERSION HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721028954Untitled-1.jpg"},
    {"slug": "coil-heaters", "name": "COIL HEATERS", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721029103Untitled-1.jpg"},
    {"slug": "d-type-cartridge-heater", "name": "D TYPE CARTRIDGE HEATER", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721029186Untitled-1.jpg"},
    {"slug": "electric-nano-infraded-band-heater", "name": "ELECTRIC NANO INFRARED BAND HEATER", "image": "https://essbeeheaters.com/admin/uploads/product/cat_pd_image/1721028842Untitled-1.jpg"},
]

SEED_TESTIMONIALS = [
    {"name": "Mayank Khandelwal", "role": "Happy Customer", "avatar": "https://essbeeheaters.com/admin/uploads/testimonial/1720677190unnamed--1-.png", "message": "They have the best quality products at affordable prices. Also, loved the variety of heaters they offer."},
    {"name": "Deepak Shukla", "role": "Happy Customer", "avatar": "https://essbeeheaters.com/admin/uploads/testimonial/1720677006unnamed.png", "message": "Very cheap heaters are available here from shops. The quality is excellent and prices are very reasonable."},
    {"name": "Vivek Kumar", "role": "Happy Customer", "avatar": "https://essbeeheaters.com/admin/uploads/testimonial/1673858677unnamed--3-.png", "message": "Nice range of industrial heating elements with good quality available with them."},
    {"name": "Amar Kushwaha", "role": "Happy Customer", "avatar": "https://essbeeheaters.com/admin/uploads/testimonial/1720677305unnamed--2-.png", "message": "Quality products with reasonable prices and good human behavior with customers."},
]

SEED_HERO = [
    {"image": "https://essbeeheaters.com/data1/images/bb1.jpg", "alt": "Heater Products Banner 1"},
    {"image": "https://essbeeheaters.com/data1/images/bb2.jpg", "alt": "Heater Products Banner 2"},
    {"image": "https://essbeeheaters.com/data1/images/bb3.jpg", "alt": "Heater Products Banner 3"},
]

SEED_GALLERY = [
    "https://essbeeheaters.com/admin/uploads/gallery/1722083112main-fold-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083133medium-wave-ir-heaters-quartz-silica-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083148mica-band-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083168mini-space-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083193oil-immersion-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083212quartz-box-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083225ring-type-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083240round-plate-immersion-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083258sealed-nozzle-heater.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083277shortwave-ir-heater.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083291shortwave-ir-heater-with-box.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083304sic-heating-elements.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083319space-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083332strip-heaters-strip-finned-heater.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083349tape-heater-heat-treacer.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083364thread-burning-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1722083394tubler-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1720598264water-immersion-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1721035464air-finned-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1721035496aluminum-casting-heater.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1721035519brass-casting-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1721035546cast-iron-casting-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1721035563ceramic-band-heaters.jpg",
    "https://essbeeheaters.com/admin/uploads/gallery/1721035579ceramic-ir-heaters.jpg",
]

SEED_COMPANY = {
    "_singleton": "company",
    "name": "Ess Bee Heaters Pvt. Ltd.",
    "tagline": "Heat Solution",
    "established": "An ISO 9001:2015 Certified Company",
    "phones": ["+91-9911565091", "+91-9911565090"],
    "emails": ["ess_beeheat@yahoo.com", "sunilbansal151@gmail.com"],
    "contacts": [
        {"name": "Mr. Hrithik Bansal", "phone": "+91-9911565091", "role": "Director"},
        {"name": "Mr. Sunil Bansal", "phone": "+91-9911565090", "role": "Director"},
    ],
    "address": "KH. No. 22/6/01, Gali No. 9, Pipalwali gali, Samaypur Extn. Indl. Area., Delhi -110042",
    "whatsapp": "919911565091",
    "business_hours": "",
    "youtube_id": "csjwGW3j2RU",
    "socials": {"facebook": "#", "linkedin": "#", "youtube": "https://www.youtube.com/watch?v=csjwGW3j2RU", "instagram": "#"},
    "industries": [
        "OEMs", "Food Processing", "Textiles", "Plastic Industry", "Rubber Industry",
        "Chemical & Pharmaceutical", "Electroplating", "Fertilizer Plants",
        "PET Industries", "Foam Plant", "Cooler Honey Pad", "Packaging Industries",
    ],
}

SEED_CONTENT = {
    "_singleton": "content",
    "home_h1": "ESS BEE HEATERS PVT. LTD.",
    "home_subtitle": "Leading manufacturer of industrial & domestic heating elements - cartridge heaters, mica band heaters, ceramic band heaters, immersion heaters, infrared heaters and more. Trusted by 5000+ clients across India since 2000.",
    "home_welcome_title": "Welcome to",
    "home_welcome_p1": "We are leading manufacturer and pioneer in the field of Domestic and Industrial Heating Elements with an in-depth knowledge of improved technology, thereby winning the trust of customers for high efficiency in heating and best performance of their equipments and machines.",
    "home_welcome_p2": "We offer a wide range of Domestic elements for home appliances, Industrial Immersion heaters for Oil, Water, Chemical, Cartridge Heaters for moulds and dies, Coil & manifold heater for hot runner moulds, Tubular/Finned Air Heaters/Casted Heating Units, Mica & Ceramic Band etc.",
    "about_p1": "Ess Bee Heaters Pvt. Ltd. is a leading manufacturer and pioneer in the field of Domestic and Industrial Heating Elements with in-depth knowledge of improved technology. We have been winning the trust of our customers for high efficiency in heating and best performance of their equipments and machines.",
    "about_p2": "Customer's satisfaction is our motto. We define quality as customer satisfaction right from intern selection of materials to final assembly. Rigorous testing is done at each stage in our fully equipped laboratory confirming to international standards.",
    "about_p3": "With our numerous types of tailor-made heaters, we have contributed for Foreign Exchange Savings by Producing Import Substitutes for the Industry.",
    "cta_title": "You are 10 minutes away from the help you need",
    "cta_text": "We offer a wide range of Domestic elements for home appliances, Industrial Immersion heaters for Oil, Water, Chemical, Cartridge Heaters for moulds and dies, Coil & manifold heater for hot runner moulds, Tubular/Finned Air Heaters/Casted Heating Units, Mica & Ceramic Band etc.",
    "page_about_title": "About Us",
    "page_products_title": "Our Products",
    "page_gallery_title": "Our Gallery",
    "page_contact_title": "Contact Us",
    "about_subtitle": "Our Story",
    "about_heading": "Leading Manufacturer of Heating Elements",
    "about_feature_1_title": "ISO Certified",
    "about_feature_1_desc": "ISO 9001:2015 Certified Company with quality standards.",
    "about_feature_2_title": "Mission",
    "about_feature_2_desc": "Delivering reliable heating solutions for every industry.",
    "about_feature_3_title": "Vision",
    "about_feature_3_desc": "To be the most trusted heating element partner globally.",
    "about_feature_4_title": "Quality",
    "about_feature_4_desc": "Rigorous multi-stage in-house testing.",
    "footer_about_text": "Ess Bee Heaters Pvt. Ltd. is a leading manufacturer and pioneer in the field of Domestic and Industrial Heating Elements with in-depth knowledge of improved technology.",
    "footer_copyright_suffix": "Made by Hrithik Bansal",
}


SEED_SECTIONS = {
    "_singleton": "sections",
    "header_logo_url": "https://essbeeheaters.com/admin/uploads/logo/1720678855loo.png",
    "topbar_welcome": "Welcome to Ess Bee Heaters Pvt. Ltd.",
    "nav_items": [
        {"label": "Home", "path": "/"},
        {"label": "About Us", "path": "/about"},
        {"label": "Products", "path": "/products"},
        {"label": "Gallery", "path": "/gallery"},
        {"label": "Contact Us", "path": "/contact"},
    ],
    "ticker_items": [
        "ISO 9001:2015 Certified", "RoHS Compliant", "CE Certified",
        "Made in India", "25+ Years of Excellence", "OEM & Custom Solutions",
        "In-House R&D Lab", "Pan India Delivery", "Trusted by 5000+ Clients",
    ],
    "stats_counters": [
        {"icon": "Award", "label": "Years of Excellence", "value": 25, "suffix": "+"},
        {"icon": "Factory", "label": "Product Range", "value": 30, "suffix": "+"},
        {"icon": "Users", "label": "Happy Clients", "value": 5000, "suffix": "+"},
        {"icon": "ShieldCheck", "label": "Quality Assurance", "value": 100, "suffix": "%"},
    ],
    "whychoose_title": "Built On Trust & Heat",
    "whychoose_features": [
        {"icon": "Award", "title": "ISO Certified"},
        {"icon": "Factory", "title": "In-House Mfg"},
        {"icon": "ShieldCheck", "title": "Quality Tested"},
        {"icon": "Users", "title": "Expert Team"},
        {"icon": "Flame", "title": "High Efficiency"},
        {"icon": "CheckCircle", "title": "Tailor Made"},
    ],
    "manufacturing_title": "Our Manufacturing Process",
    "manufacturing_steps": [
        {"icon": "Search", "number": "01", "title": "Requirement", "description": "Understanding client needs and specs"},
        {"icon": "Wrench", "number": "02", "title": "Design", "description": "Custom engineering & prototyping"},
        {"icon": "Cog", "number": "03", "title": "Manufacturing", "description": "Precision in-house production"},
        {"icon": "FlaskConical", "number": "04", "title": "Testing", "description": "Multi-stage QA in our lab"},
        {"icon": "Truck", "number": "05", "title": "Delivery", "description": "Pan-India and global dispatch"},
    ],
    "certifications_title": "Our Certifications",
    "certifications_items": [
        {"title": "ISO 9001:2015", "subtitle": "Quality Management", "icon": "Award"},
        {"title": "RoHS Compliant", "subtitle": "Environment Safe", "icon": "Flame"},
        {"title": "CE Marked", "subtitle": "European Standards", "icon": "ShieldCheck"},
        {"title": "MSME Registered", "subtitle": "Govt. of India", "icon": "Award"},
    ],
    "industries_title": "Industries We Cater",
    "show_ticker": True, "show_h1_band": True, "show_welcome": True, "show_stats": True,
    "show_certifications": True, "show_manufacturing": True, "show_spotlight": True,
    "show_whychoose": True, "show_products": True, "show_testimonials": True,
    "show_cta": True, "show_industries": True, "show_gallery_preview": True,
    "color_primary": "#f7941e", "color_secondary": "#e67e00",
    "color_dark": "#1a1a1a", "color_red": "#d32f2f",
    "seo_home_title": "Ess Bee Heaters Pvt. Ltd. | Industrial & Domestic Heating Element Manufacturer in Delhi, India",
    "seo_home_description": "ISO 9001:2015 certified manufacturer of industrial and domestic heating elements in Delhi, India.",
    "seo_about_title": "About Us | Ess Bee Heaters Pvt. Ltd.",
    "seo_about_description": "Leading manufacturer of heating elements since 2000 - ISO 9001:2015 certified.",
    "seo_products_title": "Our Products | Ess Bee Heaters Pvt. Ltd.",
    "seo_products_description": "Browse cartridge heaters, mica band heaters, ceramic band heaters, immersion heaters, infrared heaters and more.",
    "seo_gallery_title": "Gallery | Ess Bee Heaters Pvt. Ltd.",
    "seo_gallery_description": "Photo gallery of our industrial heating element products.",
    "seo_contact_title": "Contact Us | Ess Bee Heaters Pvt. Ltd.",
    "seo_contact_description": "Get in touch for industrial heating element enquiries. Call +91-9911565091.",
}


async def seed_if_empty():
    if await db.products.count_documents({}) == 0:
        for i, p in enumerate(SEED_PRODUCTS):
            doc = Product(**p, sort_order=i).dict()
            await db.products.insert_one(doc)
    if await db.testimonials.count_documents({}) == 0:
        for i, t in enumerate(SEED_TESTIMONIALS):
            doc = Testimonial(**t, sort_order=i).dict()
            await db.testimonials.insert_one(doc)
    if await db.hero_slides.count_documents({}) == 0:
        for i, h in enumerate(SEED_HERO):
            doc = HeroSlide(**h, sort_order=i).dict()
            await db.hero_slides.insert_one(doc)
    if await db.gallery.count_documents({}) == 0:
        for i, g in enumerate(SEED_GALLERY):
            doc = GalleryItem(image=g, sort_order=i).dict()
            await db.gallery.insert_one(doc)
    if await db.company_info.count_documents({}) == 0:
        await db.company_info.insert_one(SEED_COMPANY)
    if await db.site_content.count_documents({}) == 0:
        await db.site_content.insert_one(SEED_CONTENT)
    if await db.site_sections.count_documents({}) == 0:
        await db.site_sections.insert_one(SEED_SECTIONS)
