import requests

url = "https://briefcase-support.org/python?platform=linux&version=3.8&arch=x86_64"
filename = "support.tar.gz"

response = requests.get(url, stream=True)
with open(filename, "wb") as f:
    total = response.headers.get("content-length")
    if total is None:
        f.write(response.content)
    else:
        downloaded = 0
        total = int(total)
        for data in response.iter_content(chunk_size=1024 * 1024):
            downloaded += len(data)
            f.write(data)
            done = int(50 * downloaded / total)
            print(
                "\r{}{} {}%".format("#" * done, "." * (50 - done), 2 * done),
                end="",
                flush=True,
            )
print(filename)
