import requests
import sys

if __name__ == "__main__":
    baseURL = "https://cn.bing.com/"
    loc = sys.argv[1]
    data = requests.get(f"https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt={loc}").json()
    imageURL = data["images"][0]["url"]
    image = requests.get(imageURL)
    with open("./data/zh-CN.jpg", "wb") as file:
        file.write(image.content)
