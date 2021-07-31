# tpdb2xbvr
This script calls the metadataapi.net and generates a json bundle to import scenes manually into xbvr.

## Configuration
Create an account on metadataapi.net and generate an api key.
Edit tpdb2xbvr and update the headers to include this key.

headers= {
     "Authorization": "Bearer xxxxxxxxxx",
     "Content-Type": "application/json",
     "Accept": "application/json"
}


## Running
python3 tpdb2xbvr.py  https://api.metadataapi.net/scenes/virtualrealporn-lara039s-new-friend

1. Copy output.json to a web server.
2. open up the xbvr config
3. import the content bundle.
4. Run any scraper to build the search index