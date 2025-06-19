# import json

# def load_data():
#     try:
#         with open('youtube.txt','r') as file:
#             test = json.load(file)
#             return test
        
#     except FileNotFoundError:
#         return []
    
# def save_data_helper(videos):
#     with open('youtube.txt','w') as file:
#         json.dump(videos, file)

# def list_all_favorite_videos(videos):
#     print("\n")
#     print("*"*50)
#     for index , video in enumerate(videos, start=1):
        
#         print(f"{index}.{video['name']} - {video['time']}")

# def add_youtube_video(videos):
#     name = input("Enter Video Name:")
#     time = input("Enter Video time:")
#     videos.append({'name': name, 'time': time})
#     save_data_helper(videos)

# def update_youtube_video(videos):
#     list_all_favorite_videos(videos)
#     index = int(input("Enter the index of the video you want to update:"))
#     if 1 <= index <= len(videos):
#         name = input("Enter Video Name:")
#         time = input("Enter Video time:")
#         videos[index-1] = {'name': name, 'time': time}
#         save_data_helper(videos)

#     else:
#         print("Invalid index selected")

# def delete_youtube_video(videos):
#     list_all_favorite_videos(videos)
#     index = int(input("Enter the index of the video you want to delete:"))
#     if 1<= index <= len(videos):
#         del videos[index-1]
#         save_data_helper(videos)
#     else:
#         print("Invalid Video index Selected")   

# def main():
#     videos = load_data()

#     while True:
#         print("\n Welcome to the YouTube Manager! Choose an Option:")
#         print("1. List all favorite videos")
#         print("2. Add a youtube video")
#         print("3. Update Youtube Video Details")
#         print("4. Delete a Youtube Video")
#         print("5. Exit Application")
#         choice = input("Enter your choice: ")
#     #   print(videos)
        
#         match choice:
#             case "1":
#                 list_all_favorite_videos(videos)
#             case "2":
#                 add_youtube_video(videos)
#             case "3":
#                 update_youtube_video(videos)
#             case "4":
#                 delete_youtube_video(videos)
#             case "5":
#                 print("Exiting Application")
#                 break
#             case _:
#                 print("Invalid Choice. Please try again.")
#                 continue

# if __name__ == "__main__":
#     main()







# 📦 Import the JSON module to read/write data in JSON format
import json 

# 📂 Load the list of YouTube videos from a local file
def load_data():
    try:
        # 📖 Open 'youtube.txt' in read mode and load its content as JSON
        with open('youtube.txt','r') as file:
            test = json.load(file)
            return test
        
    except FileNotFoundError:
        # 🆕 If file doesn't exist, return an empty list (first-time use)
        return []

# 💾 Save the current list of videos to the local JSON file
def save_data_helper(videos):
    # ✍️ Open 'youtube.txt' in write mode and dump the JSON data into it
    with open('youtube.txt','w') as file:
        json.dump(videos, file)

# 📃 Display all saved favorite YouTube videos with index
def list_all_favorite_videos(videos):
    print("\n")
    print("*"*50)  # 🖥️ Display a line divider for neat output
    for index, video in enumerate(videos, start=1):
        # 🔢 Print each video with its index, name, and time
        print(f"{index}. {video['name']} - {video['time']}")

# ➕ Add a new YouTube video to the list
def add_youtube_video(videos):
    # 📝 Ask user for video details
    name = input("Enter Video Name: ")
    time = input("Enter Video time: ")

    # 📌 Append the new video to the list
    videos.append({'name': name, 'time': time})

    # 💾 Save the updated list to file
    save_data_helper(videos)

# 📝 Update details of an existing video
def update_youtube_video(videos):
    # 📃 Show the list so user can choose which video to update
    list_all_favorite_videos(videos)

    # 🔢 Ask for the video index to update
    index = int(input("Enter the index of the video you want to update: "))

    # ✅ If valid index, ask for new details and update the list
    if 1 <= index <= len(videos):
        name = input("Enter Video Name: ")
        time = input("Enter Video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        # ❌ Handle invalid index input
        print("Invalid index selected")

# ❌ Delete a selected video from the list
def delete_youtube_video(videos):
    # 📃 Show videos to choose from
    list_all_favorite_videos(videos)

    # 🔢 Ask which video to delete
    index = int(input("Enter the index of the video you want to delete: "))

    # ✅ If index is valid, remove the video and save
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        # ❌ Handle invalid selection
        print("Invalid Video index Selected")   

# 🚀 Main application loop to manage user interaction
def main():
    # 📂 Load existing videos (or empty list if none)
    videos = load_data()

    # 🔁 Infinite loop for menu-based user input
    while True:
        # 📋 Display menu options
        print("\n Welcome to the YouTube Manager! Choose an Option:")
        print("1. List all favorite videos")
        print("2. Add a youtube video")
        print("3. Update Youtube Video Details")
        print("4. Delete a Youtube Video")
        print("5. Exit Application")

        # 🎮 Get user choice
        choice = input("Enter your choice: ")

        # 🧠 Match user input to the corresponding functionality
        match choice:
            case "1":
                list_all_favorite_videos(videos)
            case "2":
                add_youtube_video(videos)
            case "3":
                update_youtube_video(videos)
            case "4":
                delete_youtube_video(videos)
            case "5":
                print("Exiting Application")
                break
            case _:
                # ❌ Handle invalid menu choice
                print("Invalid Choice. Please try again.")
                continue

# 🛡️ Ensures main() only runs when the script is executed directly
if __name__ == "__main__":
    main()


