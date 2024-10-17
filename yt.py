from pytube import YouTube

def download_video(url, save_path):
    try:
        yt = YouTube(url)  # Create a YouTube object
        streams = yt.streams.filter(progressive=True, file_extension="mp4")  # Filter for streams
        highest_res_stream = streams.get_highest_resolution()  # Get the highest resolution stream

        highest_res_stream.download(output_path=save_path)  # Download the video
        print("Successfully downloaded!")

    except Exception as e:
        print(f"An error occurred: {e}")  # Print any errors that occur

# Get the video link from user input
url = input("Enter the YouTube link: ")

# Define the save path
save_path = "C:/Users/suvas/OneDrive/Documents/PROJECTS/ytdownloader"

# Start the download process
download_video(url, save_path)
