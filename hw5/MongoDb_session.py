from pymongo import MongoClient


def push_to_MongoDb(smth, collection):
    try:
        client = MongoClient('127.0.0.1', 27017)
        db = client[collection]
        item = db.collection
        item.insert_many(smth)
        client.close()
        print(f'Push was successful! {len(smth)} items was added to {collection} ')
    except:
        print('Something wrong.')
    return True

