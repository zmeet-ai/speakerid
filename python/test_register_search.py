import requests

def audio_register():
    files = {'audio': open('./777-126732-0003.flac', 'rb')}
    values = {'spk_name': 'jiaozhu', "app_id": "abcpen", "tag_id": "tech"}
    url = "https://translate.abcpen.com/audio/register"
    r = requests.post(url, files=files, data=values)
    print(r.text)

def audio_search():
    files = {'audio': open('./777-126732-0003.flac', 'rb')}
    values = {"app_id": "abcpen"}
    url = "https://translate.abcpen.com/audio/search"
    r = requests.post(url, files=files, data=values)
    print(r.text)

if __name__ == "__main__":
    audio_register()
    audio_search()