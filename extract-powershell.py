#!/usr/bin/python

import time
from termcolor import cprint
from elasticsearch import Elasticsearch

# number of results to be fetched
number_of_results = 20

def create_tmp_file(psfile_path):
    f = open(psfile_path, "w")
    f.write(scriptblock)
    f.close()
    print("ScriptBlockText Extracted to %s" % psfile_path)


es = Elasticsearch(
    # Elasticsearch host to connect (change the values)
    ['yourElasticSearchURL'],
    http_auth=('username', 'password'),
    scheme="https",
    port=9243,
)
print("[+] Getting latest %s hits" % number_of_results)
print("+" * 30)
data = es.search(
    # change the index name if needed
    "winlogbeat-*",
    # search for the event 4104
    body={"query": {"match": {"winlog.event_id": "4104"}}},
    # get the latest 10 results ordered by timestamp desc
    size=number_of_results,
    sort='@timestamp:desc'
)
for hit in data["hits"]["hits"]:
    hit_info = hit["_source"]["winlog"]
    computer_name = hit_info["computer_name"]
    task_name = hit_info["task"]
    process_id = hit_info["process"]["pid"]
    scriptblock = hit_info["event_data"]["ScriptBlockText"]
    record_id = hit_info["record_id"]
    timestamp = hit["_source"]["@timestamp"]
    tmp_file_name = "tmp/result-%s.txt" % record_id
    print("Computer Name %s: " % computer_name)
    print("Task : %s " % task_name)
    print("Process id : %s " % process_id)
    print("Time : %s" % timestamp)
    # create a tmp file for each logged powershell script
    create_tmp_file(tmp_file_name)
    print("+" * 30)
print("[+] Powershell extraction finished!")
