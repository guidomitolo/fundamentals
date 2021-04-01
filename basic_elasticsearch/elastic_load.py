import logging
import json
import csv
import os
import re
from elasticsearch import Elasticsearch

def connect():
    connection = None
    connection = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if connection.ping():
        print('Connected')
    else:
        print('Cannot connect!')
    return connection

def create_map(conn_obj, index_name='news'):
    created = False
    # index settings
    schema = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "members": {
                "dynamic": "strict",
                "properties": {
                    "date": {
                        "type": "text",
                        # "format": "dd-MM-yyyy"
                    },
                    "flyer": {
                        "type": "text"
                    },
                    "title": {
                        "type": "text"
                    },
                    "body": {
                        "type": "text"
                    },
                    "url": {
                        "type": "text"
                    },
                    "bias": {
                        "type": "text"
                    },
                }
            }
        }
    }
    try:
        # if index does not exists -> create it
        if not conn_obj.indices.exists(index_name):
            conn_obj.indices.create(
                index=index_name, 
                ignore=400, # Ignore 400 means to ignore "Index Already Exist" error.
                body=schema
                )
        created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created

def insert_data(elastic_object, index_name, record):
    try:
        outcome = elastic_object.index(index=index_name, body=record)
    except Exception as ex:
        print('Error in indexing data')
        print(str(ex))

if __name__ == '__main__':

    connection = connect()
    create_map(connection)
    
    # csvs in data folder
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    entries = os.listdir(data_dir)
    files = [os.path.join(data_dir, csv_file) for csv_file in entries if re.search('.csv', csv_file)]
    # from csv to json
    for path in files:
        with open(path, "r", encoding="utf8") as csv_file:
            line = 0
            all_news = []
            for row in csv.DictReader(csv_file):
                table = {}
                if line == 0:
                    for column in row:
                        if column != '':
                            if column == 'headline' or column == 'title':
                                table['title'] = []
                            table[column] = []
                    line += 1
                table['date'] = (row['date'].replace('\n',''))
                table['flyer'] = (row['flyer'])
                table['lead'] = (row['lead'])
                if 'title' in row.keys():
                    table['title'] = (row['title'])
                elif 'headline' in row.keys():
                    table['title'] = (row['headline'])
                table['body'] = (row['body'])
                if re.search('derecha', row['url']):
                    table['bias'] = ('derecha')
                else:
                    table['bias'] = ('izquierda')
                table['url'] = (row['url'])
                all_news.append(table)
                    
                insert_data(connection, "news", json.dumps(table))

    # save table in local json
    with open(os.path.join(data_dir, "news_table_list.json"), 'w') as file:

        file.write(json.dumps(all_news))
        file.close()

    logging.basicConfig(level=logging.ERROR)