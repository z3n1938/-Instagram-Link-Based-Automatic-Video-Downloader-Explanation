#
__Instagram Link-Based Automatic Video Downloader Explanation__

*This project demonstrates how to automatically download a video from an Instagram link using Python. The program leverages the Instaloader library to process a user-provided video link and downloads the video to a designated folder.*
#
__Requirements__
Python Installed: Ensure you have Python 3.x installed on your system.

Download Python: https://www.python.org/
Required Library:

instaloader: A powerful library for downloading Instagram content.

run setup.bat
#
**Steps to Build the Program** 

**_Accepting the Video Link_**

The program will prompt the user to input an Instagram video link.

**_Processing the Link_**

The program extracts the "shortcode" from the provided link, which is used to identify the Instagram post.

**_Downloading the Video_**

The video will be downloaded and saved in a local folder (e.g., downloads).
#

__How It Works__

When you run the program, it asks the user to input an Instagram video link.

The program extracts necessary information (shortcode) from the provided link.

Instaloader uses this information to download the video and save it in a folder named downloads.
#

__Example Usage__

Input:

The user provides a link, for example:https://www.instagram.com/reel/abcdefghijk/

Output:

The terminal displays:Video successfully downloaded: abcdefghijk

#

__Notes__
Input Validation: You can add a mechanism to ensure the user enters a valid Instagram link.

Private Account Handling: If the post belongs to a private account, you'll need to log in with an Instagram account. Add the following code for authentication:

'L.login("username", "password")'

With this simple and functional script, users can easily download a video from an Instagram link! 🎉

#
