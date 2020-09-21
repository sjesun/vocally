import base64
from github import Github
import getpass as gp

user = input("Enter your Github username: ")
password = gp.getpass(prompt="Enter your password: ")
dest = input("Enter destination path for files: ")
gh = Github(user, password)

# can be modified as needed for scraping unknown files from unknown Github repos
repo = gh.get_repo("mazzzystar/randomCNN-voice-transfer")
files = repo.get_contents("")
for file in files:
    if file.type == "file":
        file_string = str(file)
        name = file_string.split("\"")[1].split("\"")[0]
        if "model" in name or "utils" in name:
            contents = repo.get_contents(file.path)
            data = base64.b64decode(contents.content)
            output = open(dest + name, "wb")
            output.write(data)
