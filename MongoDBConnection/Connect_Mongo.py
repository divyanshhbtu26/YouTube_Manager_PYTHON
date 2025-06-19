import pymongo
from bson import ObjectId

# mongodb+srv://<db_username>:<db_password>@pythonutubemanager.as4jo.mongodb.net/?retryWrites=true&w=majority&appName=PythonUtubeManager
client = pymongo.MongoClient("mongodb+srv://Rahul2112:rahulshukla@pythonutubemanager.as4jo.mongodb.net/", tlsAllowInvalidCertificates=True)
#Not a good practice to hardcode the password in the code. Use environment variables instead.
#Not a good practice to use tlsAllowInvalidCertificates=True. This is insecure and should not be used in production.

db = client["ytManager"]
video_collection = db["videos"]


print(client)

def list_all_favorite_videos():
    for video in video_collection.find():
        print(f"ID:{video['_id']} , Name: {video['name']} , Time: {video['time']}")

def add_youtube_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_youtube_video(name, time, videoId): 
    video_collection.update_one({"_id": ObjectId(videoId)}, {"$set": {"name": name, "time": time}})

def delete_youtube_video(videoId):
    video_collection.delete_one({"_id": videoId})


def main():
    while True:
        print("\n Welcone to the Youtube Manager! Choose an Option:")
        print("1. List all favorite videos")
        print("2. Add a youtube vide")
        print("3. Update Youtube Video Details")
        print("4. Delete a Youtube Video")
        print("5. Exit Application")

        choice = input("Enter your choice:")

        match choice:
            case "1":
                list_all_favorite_videos()

            case "2":
                name = input("Enter Video Name:")
                time = input("Enter Video Time:")
                add_youtube_video(name, time)

            case "3":
                name = input("Enter Updated Video Name:")
                time = input("Enter Updated Video Time:")
                videoId = input("Enter the id of the video you want to update:")
                update_youtube_video(name, time, videoId)

            case "4":
                videoId = input("Enter the id of the video you want to delete:")
                delete_youtube_video(videoId)

            case "5":
                print("Exiting Application")
                break

            case _:
                print("Invalid Choice. Please try again.")
                continue



if __name__ == "__main__":
    main()

