import requests

def voiceid_register():
    files = {'audio': open('./777-126732-0003.flac', 'rb')}
    values = {'spk_name': 'jiaozhu3', "app_id": "abcpen", "tag_id": "tech"}
    url = "https://voiceid.abcpen.com/voiceid/register"
    r = requests.post(url, files=files, data=values)
    print(r.text)

def voiceid_search():
    files = {'audio': open('./777-126732-0003.flac', 'rb')}
    values = {"app_id": "abcpen"}
    url = "https://voiceid.abcpen.com/voiceid/recognize"
    r = requests.post(url, files=files, data=values)
    print(r.text)

def voiceid_count():
    params = {"app_id": "abcpen"}
    url = "https://voiceid.abcpen.com/voiceid/count"
    r = requests.get(url, params=params)
    print(r.text)

def voiceid_get_audio_url():
    params = {"app_id": "abcpen", "spk_name": "jiaozhu"}
    url = "https://voiceid.abcpen.com/voiceid/audio_url"
    r = requests.get(url, params=params)
    print(r.text)

def voiceid_list():
    params = {"app_id": "abcpen"}
    url = "https://voiceid.abcpen.com/voiceid/list"
    r = requests.get(url, params=params)
    print(r.text)

def voiceid_drop():
    params = {"app_id": "abcpen"}
    url = "https://voiceid.abcpen.com/voiceid/list"
    r = requests.get(url, params=params)
    print(r.text)

if __name__ == "__main__":
    voiceid_register()
    voiceid_search()
    voiceid_get_audio_url()
    voiceid_count()
    voiceid_list()
    voiceid_drop()