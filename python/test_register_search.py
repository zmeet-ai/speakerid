import requests
import uuid
import random
import os
from pathlib import Path
from time import perf_counter


audio_all = "../dataset/LibriSpeech/"
TEST_COUNT = 200

def voice_register():
    files = {'audio': open('../dataset/777-126732-0004.flac', 'rb')}
    # app_id = f'abcpen{random.randrange(5)}'
    app_id = "abcpen0"
    values = {'spk_name': str(uuid.uuid4()),
              "app_id": app_id, "tag_id": "tech"}
    url = "https://xxx.abcpen.com/voiceid/register"
    r = requests.post(url, files=files, data=values)
    print(f"voice register result: {r.text}\n")


def voice_register_all():
    # files = {'audio': open('../dataset/777-126732-0004.flac', 'rb')}
    i = 0
    for elem in Path(audio_all).rglob('*.*'):
        suffix = Path(elem).suffix
        if (suffix == ".flac" or suffix == ".wav"):
            print(f"read file: {elem}")
            files = {'audio': open(elem, 'rb')}
            # app_id = f'abcpen{random.randrange(5)}'
            app_id = "abcpen0"
            values = {'spk_name': str(uuid.uuid4()),
                      "app_id": app_id, "tag_id": "tech"}
            url = "https://xxx.abcpen.com/voiceid/register"
            t1 = perf_counter()
            r = requests.post(url, files=files, data=values)
            print(
                f"voice register all result: {r.text}, time: {perf_counter() - t1}s\n")
            i = i+1
            if (i > TEST_COUNT):
                break


def voice_search():
    files = {'audio': open('../dataset/swords_drawn3.wav', 'rb')}
    values = {"app_id": "abcpen0"}
    url = "https://xxx.abcpen.com/voiceid/recognize"
    r = requests.post(url, files=files, data=values)
    print(f"voice search result: {r.text}\n")


def voice_search_full():
    # files = {'audio': open('../dataset/777-126732-0004.flac', 'rb')}
    i = 0
    for elem in Path(audio_all).rglob('*.*'):
        suffix = Path(elem).suffix
        if (suffix == ".flac" or suffix == ".wav"):
            print(f"read file: {elem}")
            files = {'audio': open(elem, 'rb')}
            # app_id = f'abcpen{random.randrange(5)}'
            app_id = "abcpen0"
            values = {"app_id": app_id}
            t1 = perf_counter()
            url = "https://xxx.abcpen.com/voiceid/recognize"
            r = requests.post(url, files=files, data=values)
            print(
                f"voice search result: {r.text}, time: {perf_counter() - t1}s\n")
            i = i+1
            if (i > TEST_COUNT):
                break


def voice_list():
    values = random.randrange(10)
    url = f"https://xxx.abcpen.com/voiceid/list"
    para = {"app_id": "abcpen0"}
    r = requests.get(url, para)
    print(f"voice list result : {r.text}\n")

    url = f"https://xxx.abcpen.com/voiceid/list"
    para = {"app_id": "abcpen0", "limit": 10, "offset": 10}
    r = requests.get(url, para)
    print(f"voice list with limit and offset result: {r.text}\n")

    url = f"https://xxx.abcpen.com/voiceid/list"
    para = {"app_id": "abcpen0", "limit": 10}
    r = requests.get(url, para)
    print(f"voice list with limit result : {r.text}\n")

    url = f"https://xxx.abcpen.com/voiceid/list"
    para = {"app_id": "abcpen0", "offset": 10}
    r = requests.get(url, para)
    print(f"voice list with offset result : {r.text}\n")


def voice_count():
    values = random.randrange(10)
    para = {"app_id": "abcpen0"}
    url = f"https://xxx.abcpen.com/voiceid/count"
    r = requests.get(url, para)
    print(f"voice count result: {r.text}\n")


def voice_url():
    values = random.randrange(10)
    para = {"app_id": "abcpen0",
            "spk_name": '03b8accb-3ee8-4bb9-a15e-cf7ed895d3c2'}
    url = f"https://xxx.abcpen.com/voiceid/voice-url"
    r = requests.get(url, para)
    print(f"voice url result: {r.text}\n")


def voice_del():
    values = random.randrange(10)
    para = {"app_id": "abcpen0",
            "spk_name": '03b8accb-3ee8-4bb9-a15e-cf7ed895d3c2'}
    url = f"https://xxx.abcpen.com/voiceid/del-spk-name"
    r = requests.get(url, para)
    print(f"voice del result: {r.text}\n")


def voice_del_all():
    values = random.randrange(10)
    para = {"app_id": "abcpen2"}
    url = f"https://xxx.abcpen.com/voiceid/delete-all"
    r = requests.get(url, para)
    print(f"voice delete all result: {r.text}\n")


if __name__ == "__main__":
    try:
        for i in range(1):
            voice_register()
            voice_register_all()
            voice_count()
            voice_list()
            voice_search()
            voice_search_full()
            voice_url()
            voice_del()
            voice_del_all()
    except Exception as err:
        print(f"meet excpetion {err}")
