from pymongo import MongoClient

# Replace the URL with your MongoDB connection string
client = MongoClient("mongodb://localhost:27017/neurolab")  # Local MongoDB server

# Access a specific database
db = client["neurolab"]

# Access a specific collection
collection = db["Product"]

# Sample data to be inserted
sample_data = [
    {"company_name": "TechCorp", "product": "AI Software", "courses_offered": ["Machine Learning", "AI Fundamentals"]},
    {"company_name": "HealthInc", "product": "Medical Devices", "courses_offered": ["Healthcare Tech", "Bioengineering"]},
    {"company_name": "FinTech", "product": "Blockchain Solution", "courses_offered": ["Cryptocurrency", "Blockchain Development"]},
    {"company_name": "EduTech", "product": "Online Courses", "courses_offered": ["Data Science", "Web Development"]},
    {"company_name": "GreenEnergy", "product": "Solar Panels", "courses_offered": ["Renewable Energy", "Solar Engineering"]}
]

# Insert sample data into the collection
collection.insert_many(sample_data)

# Verify all the records in the collection
records = collection.find()  # Retrieve all records from the collection

# Print all records
for record in records:
    print(record)

