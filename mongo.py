import pymongo
from faker import Faker


fake = Faker("ru_RU")

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["learning"]

# Получаем список всех баз данных
print("Существующие базы данных:")
for database in client.list_database_names():
    print("\t-", database)

# Получаем список всех коллекций в базе данных learning
print("Существующие коллекции в learning")
for collection in db.list_collection_names():
    print("\t-", collection)

# Создаем/подключаем коллекцию test
collection = db["test"]

# Очищаем коллекцию
collection.delete_many({})

# Просматриваем все записи в коллекции
for field in collection.find():
    print(field)