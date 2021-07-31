import requests
import json
import datetime
import sys


headers= {
     "Authorization": "Bearer xxxxxxxxxxxxxxxxxx",
     "Content-Type": "application/json",
     "Accept": "application/json"
}

def process(url):
    print(headers)
    print(url)
    response=requests.get(url,headers=headers)

    if response.status_code ==200:
        result=response.json()

        scene={}
        scene["_id"] = result['data']['id']
        scene["scene_id"] = str(result['data']['_id'])
        scene["scene_type"] = "VR"
        scene["title"] = result['data']['title']
        scene["studio"] = result['data']['site']['name']
        scene["site"] = result['data']['site']['name']
        scene['covers']=[result['data']['image']]

        gallery=[]
        if 'poster' in result['data']:
            gallery.append(result['data']['poster'])

        scene['gallery']=gallery

        tags = []
        for t in result['data']['tags']:
            tags.append(t["name"])
        scene["tags"] = tags

        performer = []
        for t in result['data']['performers']:
            performer.append(t['name'])
        scene['cast'] = performer

        scene["synopsis"] = result['data']['description']
        scene["released"] = result['data']['date']
        scene["homepage_url"] = result['data']['url']
        scene['duration']=1

        data = {}
        data["timestamp"] = datetime.datetime.now().isoformat() + "Z"
        data["bundleVersion"] = "1"
        data['scenes']=[scene]
        return data
    else:
        return None

if __name__ == '__main__':
    if len (sys.argv) > 1:
        url=sys.argv[1]
        res=process(url)
        print(res)
        if res is not None:
            with open('output.json', 'w') as outfile:
                json.dump(res, outfile)

