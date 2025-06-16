from sqlalchemy.orm import Session
from database.model import create_merchant_industry, create_merchant_category, create_category
from modules.utils.tools import generate_slug

seed_arr = [
    {
        'name': 'Agriculture',
        'categories': ['Agricultural Cooperatives', 'Agricultural Services'],
    },
    {
        'name': 'Commerce',
        'categories': ['Automobiles', 'Digital Goods', 'Physical Goods', 'Real Estate', 'Digital Services', 'Legal Services', 'Physical Services', 'Professional Services'],
    },
    {
        'name': 'Education',
        'categories': ['Daycare Services', 'Creche Schools', 'Nursery Schools', 'Primary Schools', 'Secondary Schools', 'Tertiary Schools', 'Vocational Training', 'Virtual Learning', 'Other Educational Services'],
    },
    {
        'name': 'Gaming',
        'categories': ['Betting', 'Lotteries', 'Prediction Services', 'Other Gaming Services'],
    },
    {
        'name': 'Financial Services',
        'categories': ['Financial Cooperatives', 'Corporate Services', 'Payment Solution Providers', 'Insurance', 'Investment', 'Agricultural Investment', 'Lending', 'Bill Payments', 'Payroll', 'Remittances', 'Savings', 'Mobile Wallets', 'Other Financial Services'],
    },
    {
        'name': 'Health',
        'categories': ['Gyms', 'Hospitals', 'Pharmacies', 'Herbal Medicine', 'Telemedicine', 'Medical Laboratories'],
    },
    {
        'name': 'Hospitality',
        'categories': ['Hotels', 'Restaurants', 'Other Hospitality Services'],
    },
    {
        'name': 'Non-profits',
        'categories': ['Professional Associations', 'Government Agencies', 'NGOs', 'Political Parties', 'Religious Organizations', 'Other Non-profits'],
    },
    {
        'name': 'Leisure And Entertainment',
        'categories': ['Cinemas', 'Nightclubs', 'Events', 'Press And Media', 'Recreation Centres', 'Streaming Services'],
    },
    {
        'name': 'Logistics',
        'categories': ['Courier Services', 'Freight Services'],
    },
    {
        'name': 'Travel',
        'categories': ['Airlines', 'Ridesharing', 'Tour Services', 'Transportation', 'Travel Agencies'],
    },
    {
        'name': 'Utilities',
        'categories': ['Cable Television', 'Electricity', 'Garbage Disposal', 'Internet', 'Telecoms', 'Water'],
    },
]

def run_category_seeder(db: Session):
    global seed_arr
    for data in seed_arr:
        industry = create_merchant_industry(db=db, name=data['name'], status=1)
        for category in data['categories']:
            create_merchant_category(db=db, name=category, industry_id=industry.id, status=1)
    return True


def run_product_categories_seeder(db: Session):
    # categories = [
    #     "Gym and Fitness",
    #     "Makeup and Cosmetics",
    #     "Food & Beverages",
    #     "Kids Fashion",
    #     "Professional Services",
    #     "Womens Fashion",
    #     "Gaming",
    #     "Mobile and Tablets",
    #     "Baby Products",
    #     "Arts and Crafts",
    #     "Beauty and Skincare",
    #     "Electronics",
    #     "Health & Pharmaceuticals",
    #     "Personal Care",
    #     "Home & Kitchen",
    #     "Restaurant",
    #     "Books and Media",
    #     "Mens Fashion",
    #     "Supermarket",
    #     "Education",
    #     "Groceries",
    #     "Drinks",
    #     "Toys & Games"
    # ]
    categories = [
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923329/game-controller-03_fsjnbd.svg", "name": "Gaming"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923329/equipment-gym-03_qyypgy.svg", "name": "Gym & Fitness"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923329/dress-04_dqs8vt.svg", "name": "Women's fashion"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923328/suit-02_kwwoit.svg", "name": "Men's Fashion"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749931119/soft-drink-02_1_ckd1uc.svg", "name": "Groceries & drinks"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923327/medicine-02_dilzdq.svg", "name": "Health & pharmacy"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923326/puzzle_m1anif.svg", "name": "Toys"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923326/kitchen-utensils_nf46yj.svg", "name": "Home & kitchen"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923325/tv-01_dmhbql.svg", "name": "Electronics"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923324/child_vliwnm.svg", "name": "Kid's Fashion"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923324/paint-board_na44ge.svg", "name": "Art&craft"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923324/serving-food_iie8d3.svg", "name": "Restaurant"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923323/smart-phone-01_lzk9pb.svg", "name": "Mobile & tablets"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923322/book-open-02_kpk2yi.svg", "name": "Books and media"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923322/body-soap_bxh2fj.svg", "name": "Personal Care"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923321/mirror_cygftb.svg", "name": "Beauty & skinecare"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1749923321/kid_ivmjhb.svg", "name": "Baby products"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071151/passport-01_eaiqcw.svg", "name": "passport-01"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071151/brush_zwghwy.svg", "name": "brush"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071151/party-supplies_and_rentals_a2ucsa.svg", "name": "party-supplies and rentals"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071154/digital_marketing_jne2hx.svg", "name": "digital marketing"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071156/home-cleaning_fc410o.svg", "name": "home-cleaning"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071156/interior-desing_g8kbue.svg", "name": "interior-desing"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071157/laundry_c2vam0.svg", "name": "laundry"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071565/Pet_Boarding_Daycare_c4samd.svg", "name": "Pet Boarding & Daycare"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071803/Virtual_Assistants_Freelancers_u4fsi4.svg", "name": "Virtual Assistants & Freelancers"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071805/Eco-Friendly_Sustainable_Goods_utlw7o.svg", "name": "Eco-Friendly & Sustainable Goods"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071805/Event_Planning_Coordination_fjfwbp.svg", "name": "Event Planning & Coordination"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071804/Catering_Meal_Prep_Services_eyqmwl.svg", "name": "Catering & Meal Prep Services"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071805/Craft_Beers_Specialty_Alcohol_ht2jbv.svg", "name": "Craft Beers & Specialty Alcohol"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071807/photography-videography_lwrega.svg", "name": "photography-videography"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071806/Landscaping_Gardening_Services_kazzjr.svg", "name": "Landscaping & Gardening Services"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071807/Plumbing_Electrical_Services_asgyyx.svg", "name": "Plumbing & Electrical Services"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071819/Tech_Repair_Device_Services_nys8m0.svg", "name": "Tech Repair & Device Services"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750071862/Legal_Notary_Services_ve3rj6.svg", "name": "Legal & Notary Services"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750072049/Home_Security_Smart_Systems_kn2opf.svg", "name": "Home Security & Smart Systems"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750072050/Mental_Health_Therapy_Services_qfptpk.svg", "name": "Mental Health & Therapy Services"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750072051/Music_Instruments_Lessons_uaag8c.svg", "name": "Music Instruments & Lessons"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750072051/Online_Courses_Skill_Training_zufkst.svg", "name": "Online Courses & Skill Training"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750072051/Outdoor_Gear_Adventure_Equipment_idgut6.svg", "name": "Outdoor Gear & Adventure Equipment"},
        {"url": "https://res.cloudinary.com/djkb2tlpp/image/upload/v1750073544/car-01_wv9li9.svg-car-01", "name": "car-01"}
    ]
    for i in range(len(categories)):
        slug = generate_slug(categories[i]['name'])
        create_category(db=db, name=categories[i]['name'], slug=slug, icon=categories[i]['url'], status=1, created_by=1, authorized_by=1)
    return True