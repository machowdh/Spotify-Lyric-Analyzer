from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['spotify_lyric_analyzer']

# Insert data into a collection
def insert_data(collection_name, data):
    collection = db[collection_name]
    return collection.insert_one(data).inserted_id

# Retrieve data from a collection
def get_data(collection_name, query=None):
    collection = db[collection_name]
    return collection.find(query)

# Update data in a collection
def update_data(collection_name, query, new_data):
    collection = db[collection_name]
    return collection.update_one(query, {"$set": new_data})

# Delete data from a collection
def delete_data(collection_name, query):
    collection = db[collection_name]
    return collection.delete_one(query)


if __name__ == "__main__":
    # Test insertion
    song_data = {
        "title": "Test Song",
        "artist": "Test Artist",
        "lyrics": "This is a test song."
    }
    print(insert_data("songs", song_data))

    # Test retrieval
    for song in get_data("songs"):
        print(song)
 
