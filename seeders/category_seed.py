from sqlalchemy.orm import Session
from database.model import create_merchant_industry, create_merchant_category, create_category

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
    categories = [
        "Gym and Fitness",
        "Makeup and Cosmetics",
        "Food & Beverages",
        "Kids Fashion",
        "Professional Services",
        "Womens Fashion",
        "Gaming",
        "Mobile and Tablets",
        "Baby Products",
        "Arts and Crafts",
        "Beauty and Skincare",
        "Electronics",
        "Health & Pharmaceuticals",
        "Personal Care",
        "Home & Kitchen",
        "Restaurant",
        "Books and Media",
        "Mens Fashion",
        "Supermarket",
        "Education",
        "Groceries",
        "Drinks",
        "Toys & Games"
    ]
    for i in range(len(categories)):
        create_category(db=db, name=categories[i], status=1, created_by=1, authorized_by=1)
    return True