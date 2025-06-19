# ⚠️ REMEMBER: We're using SQLite here because it's serverless and stores all data in a simple file (youtube_videos.db).
# No need for installation, setup, or external servers — perfect for small projects like this YouTube manager.

import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY ,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_all_favorite_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_youtube_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_youtube_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(name, time , video_id))
    conn.commit()

def delete_youtube_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print(f"❌ No video found with ID {video_id}. Nothing deleted.")
    else:
        print(f"✅ Video with ID {video_id} deleted successfully.")

def main():
    while True:
        print("\n Welcome to the YouTube Manager! Choose an Option:")
        print("1. List all favorite videos")
        print("2. Add a youtube video")
        print("3. Update Youtube Video Details")
        print("4. Delete a Youtube Video")
        print("5. Exit Application")

        choice = input("Enter your choice:")

        if choice == "1":
            list_all_favorite_videos()

        elif choice == "2":
            name = input("Enter Video Name:")
            time = input("Enter Video time:")
            add_youtube_video(name, time)   

        elif choice == "3":
            video_id = int(input("Enter the id of the video you want to update:"))
            name = input("Enter Video Name:")
            time = input("Enter Video Time:")
            update_youtube_video(video_id, name, time) 

        elif choice == "4":
            video_id = int(input("Enter the id of the video you want to delete:"))
            delete_youtube_video(video_id)

        elif choice == "5":
            print("Exiting Application")
            break

        else:
            print("Invalid Choice. Please try again.")
            continue

    conn.close()


if __name__ == "__main__":
    main()
    