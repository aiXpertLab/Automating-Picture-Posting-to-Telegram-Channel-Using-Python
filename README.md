## Automatically Post Pictures to Telegram with Captions from Picture Pool

> This application selects a random image from a designated picture pool, posts it to a Telegram group, and then moves the picture to a specified destination folder. The caption accompanying the picture is randomly selected from a list provided in Caption.txt.


`Auto Post Pictures to Telegram` is a simple Python program crafted for the purpose of automating the process of posting pictures with captions to Telegram groups. With Python at its core, this project aims to streamline the task of posting images with minimal manual intervention. Additionally, it offers functionality to relocate the posted pictures to another folder to prevent duplicates. The project also includes a script for randomly selecting a file from a local directory.


## Key Features:
- **Python Implementation**: `Auto Telegram` is entirely implemented in Python, making it accessible and easy to understand for developers with varying levels of experience.

- **FastAPI App Deployment**: The project provides an option to deploy a FastAPI app, allowing users to interact with a user-friendly website.

- **WEBP to JPG**: Simplifying the posting process, Auto Telegram includes a script for converting WEBP images to JPG format, ensuring seamless posting of images.


## Getting started

1. Begin by forking this repository to stay updated with future developments.

2. Next, clone the repository to your local machine:

```bash
git clone https://github.com/aiXpertLab/Automating-Picture-Posting-to-Telegram-Channel-Using-Python.git
```

3. (Optional) It's recommended to set up a virtual environment for installing dependencies. You can use `virtualenv` or any other environment manager:

```bash
virtualenv -p python3.12 venv
```

activate the environment

```bash
source venv/bin/activate
```

and install the package and the dependencies

```bash
pip install .
```

## Configure Source Picture Pool and Destination Folder

change `source="E:/gDrive/38.Pic/Tele"` to the appropriate picture pool.

change `dest  ="E:/gDrive/38.Pic/Tele/web"` to the destination you want to drop your picture.

## Customize Captions

Open the `captions.txt` file and add your desired captions, with each caption on a separate line.

## Launch app

Once the picture pool is set up, run the application using the following command:

```bash
python src/telegram/autoTele_Pic.py
```


## Bonus: Batch Convert WEBP to JPG
Copy BatchConvertWEBP2JPG.py to the target folder. Run the script: 

```python3 BatchConvertWEBP2JPG.py ```

This will convert all the pictures in WEBP to JPG.
