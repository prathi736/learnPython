from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://<db_username>:<db_password>@cluster0.rkr1nn3.mongodb.net/", tlsAllowInvalidCertificates=True)
# mongodb+srv://<db_username>:<db_password>@cluster0.rkr1nn3.mongodb.net/db_name
# Not a good idea to include id and password in code files
# tlsAllowInvalidCertificates=True -> not a good way to handle ssl else use python package to generate a ssl certificate and send it with this file to mongodb

db = client["db_name"]
video_collection = db["videos"]

# print(video_collection)

def list_videos():
    print("*" * 70)
    for video in video_collection.find():
        print(f"ID: {video['_id']} \nName: {video['name']} \nTime: {video['time']}")
        print("\n")
    print("*" * 70)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)}, # first find it
        {"$set": {"name": new_name, "time": new_time}} # what things to update
    )

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})

def main():
    while True:
        print("\n Youtube Manager with DB")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice!!")

if __name__ == "__main__":
    main()