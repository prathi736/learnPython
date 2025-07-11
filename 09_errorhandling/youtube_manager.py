import json

youtube_file = "youtube.txt"

def load_data():
    try:
        with open(youtube_file, 'r') as file:
            result = json.load(file)
            # print(type(test))
            return result
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(youtube_file, 'w') as file:
        json.dump(videos, file)
        # json.dump(keya dalna hai, kaha par dalana hai)

def list_all_videos(videos):
    print("\n")
    print("*" * 60)
    for index, videos in enumerate(videos, start=1):
        print(f"{index}. {videos['name']}, Duration: {videos['time']}")
    print("*" * 60)

def add_video(videos):
    name = input("Enter name of video: ")
    time = input("Enter length of video: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you want to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter new name of video: ")
        time = input("Enter new time of video: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index!")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number that you want to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index enetered!!")


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List of all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

# __name__ -> this double underscore is called dunder methods
if __name__ == "__main__":
    main()
