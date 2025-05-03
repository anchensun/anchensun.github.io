from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os

# Setup proxy
pg = ProxyGenerator()
# supply a repeat count (e.g. try each proxy once)
pg.FreeProxies()
scholarly.use_proxy(pg)

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
'''
from scholarly import scholarly, ProxyGenerator
from freeproxy import FreeProxy
import json
from datetime import datetime
import os
import time

# —— CONFIGURE SCHOLAR PROXY & RETRIES —— #
# fetch a batch of free rotating proxies
proxy_list = FreeProxy().get_proxy_list(repeat=3)  # try 3 pages of proxies
print(f"Fetched {len(proxy_list)} proxies")

pg = ProxyGenerator()
pg.manual_proxies(proxy_list)
scholarly.use_proxy(pg)

# tune retry behavior
scholarly.MAX_TRIES = 8
scholarly.SLEEP_INTERVAL = 3  # seconds between attempts

# —— SAFE FETCH WITH RETRIES —— #
def fetch_author_with_retries(scholar_id: str):
    last_err = None
    for attempt in range(scholarly.MAX_TRIES):
        try:
            return scholarly.search_author_id(scholar_id)
        except Exception as e:
            last_err = e
            print(f"[Attempt {attempt+1}/{scholarly.MAX_TRIES}] failed: {e}")
            time.sleep(scholarly.SLEEP_INTERVAL)
    raise RuntimeError(f"All {scholarly.MAX_TRIES} Scholar fetch attempts failed") from last_err

# —— MAIN —— #
if __name__ == "__main__":
    gs_id = os.environ.get("GOOGLE_SCHOLAR_ID", "")
    if not gs_id:
        raise RuntimeError("Please set the GOOGLE_SCHOLAR_ID environment variable")

    author = fetch_author_with_retries(gs_id)
    # fill in the sections you care about
    scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])

    # post-process
    author["updated"] = datetime.utcnow().isoformat() + "Z"
    # re-key publications by their internal id
    author["publications"] = {
        pub["author_pub_id"]: pub for pub in author.get("publications", [])
    }

    # pretty-print & save
    print(json.dumps(author, indent=2, ensure_ascii=False))

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as f:
        json.dump(author, f, indent=2, ensure_ascii=False)

    # prepare shields.io payload
    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author.get("citedby", 0)),
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as f:
        json.dump(shieldio_data, f, indent=2, ensure_ascii=False)
'''