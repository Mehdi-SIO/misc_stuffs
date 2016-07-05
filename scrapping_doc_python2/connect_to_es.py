#Make sure ES is up and running
import requests
res = requests.get('http://192.168.32.10:9200')
print(res.content)

#Connect to the cluster
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'http://192.168.32.10', 'post': 9200}])
