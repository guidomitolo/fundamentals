import requests
import json
from elasticsearch import Elasticsearch

# Connect to the elastic cluster
connect = Elasticsearch(
    [
        {
            'host':'localhost',
            'port':9200
        }
    ]
)
print(f'CONNECTION:\n{connect}\nPING:\n{connect.ping()}')

req = requests.get('http://localhost:9200')
print(f"{req}\n{req.headers}\n{req.text}\n{req.json}")

# to see all tables/indices -> connection.indices.get_alias("*") -> indices plural of index
print(f'ALL TABLES\n{connect.indices.get_alias("*")}\nTable Names:\n{connect.indices.get_alias().keys()}')

# all tables with requests
param = (('v', ''),) # '-v' is for --verbose
all_tables_response = requests.get('http://localhost:9200/_cat/indices', params=param)
print(f'ALL TABLES WITH REQUESTS\n{all_tables_response}\n{all_tables_response.text}')

# Create entries
entry_1 = {
    "first_name":"Juan",
    "last_name":"Perez",
    "age": 27,
    "about": "En mi tiempo libre juego a la pelota",
    "interests": ['sports','music'],
}
entry_2 = {
    "first_name" : "Jorge",
    "last_name" : "Gonzalez",
    "age" : 32,
    "about" : "Me encanta escuchar cumbia",
    "interests": [ "music" ]
}
entry_3 = {
    "first_name" : "Alicia",
    "last_name" : "Rossi",
    "age" : 40,
    "about" : "Disfuto de la cocina",
    "interests": [ "music", "cocina" ]
}
entry_4 = {
    "first_name" : "Juan Lucas",
    "last_name" : "Picard",
    "age" : 55,
    "about": "Me apasiona la arqueología",
    "interests": [ "archeology","music" ]
}

# Store entry 1 and create index (auto, without declaration)
insert_1_response = connect.index(
    index='acme_corporation',
    # doc_type='employee', if silenced = default _doc
    id= 1,
    body= entry_1
)

print(f'STORAGE/INDEXING DATA 1:\n{insert_1_response}')
print(f'MAPPING:\n{connect.indices.get_mapping("acme_corporation")}')

# Add other entries
insert_2_response = connect.index(
    index='acme_corporation',
    # doc_type='employee',
    id= 2,
    body= entry_2
)
insert_3_response = connect.index(
    index='acme_corporation',
    # doc_type='employee',
    id= 3,
    body= entry_3
)

# add entry with request
uri = "http://localhost:9200/acme_corporation/_doc"
headers = {
        'Content-Type': 'application/json',
    }
insert_4_response = requests.post(uri, headers=headers, data=json.dumps(entry_4))

print(f'INSERT POST REQUEST RESPONSE\n{insert_4_response}\n{insert_4_response.text}')

# Get all entries
q_all = connect.search(
    index ='acme_corporation',
    body = {
        'query':  {
                'match_all':{}
            }
        }
    )
print(f"MATCH ALL = GET ALL ENTRIES IN INDEX\nHits:\n{q_all['hits']['total']}\nContent:\n{q_all['hits']['hits']}")

query = {
    "query": {
        "match_all": {}
    }
}
print(f"MATCH ALL with REQUESTS\n{requests.get('http://localhost:9200/acme_corporation/_search/?q=data', headers=headers, data=json.dumps(query)).text}")

# Create new index with manual mapping
mapping = {
    "mappings": {
        "properties": {
            "nombre": {
                "type": "text",
                "fielddata": "true" # allow aggreration and sorting
            },
            "nacional": {
                "type": "boolean"
            },
            "duracion": {
                "type": "integer"
            },
            "cantante": {
                "type": "text",
                "fielddata": "true" # allow aggreration and sorting
            }
        }
    }
}

response = connect.indices.create(
    index="albumes",
    # doc_type='discos',
    body= mapping,
    ignore=400 # avoid crash, prints error in case of existing index
)
print(f"CREATE INDEX RESPONSE:\n{response}\nGET MAPPING/SCHEMMA OF NEW INDEX\n{connect.indices.get_mapping('albumes')}")
print(f"REQUEST\n{requests.get('http://localhost:9200/albumes').text}")

entry_1 = {
    "nombre":"The River",
    "nacional": False,
    "duracion": 40,
    "cantante": "Bruce Springsteen"
}
entry_2 = {
    "nombre":"Nebraska",
    "nacional": False,
    "duracion": 30,
    "cantante": "Bruce Springsteen"
}
entry_3 = {
    "nombre":"Pappo's Blues Volumen 1",
    "nacional": True,
    "duracion": 40,
    "cantante": "Norberto Napolitano"
}

insert_1_response = connect.index(
    index= 'albumes', 
    id= 1,
    body= entry_1
)
insert_2_response = connect.index(
    index='albumes',
    # doc_type='discos',
    id= 2,
    body= entry_2
)
insert_3_response = connect.index(
    index='albumes',
    # doc_type='discos',
    id= 3,
    body= entry_3
)
get_1_response = connect.get(
    index='albumes',
    # doc_type='employee',
    id=1
)
get_2_response = connect.get(
    index='albumes',
    # doc_type='employee',
    id=2
)
print(f"GET ID 1 ALBUMES\n{get_1_response}")
print(f"GET ID 2 ALBUMES\n{get_2_response}")

# Search
search = connect.search(
    index ='albumes',
    body = {
        'query': {
            'match': {
                    'nombre':'River'
                }
            }
        }
    )
print(f"REQUEST ALBUM THE RIVER (match one)\n{requests.get('http://localhost:9200/albumes/_search?q=River').text}\nSEARCH PYTHON (match one) ALBUM THE RIVER\n{search}")

# RETRIEVE ALL DOCUMENTS
search_all = connect.search(
    index ='albumes',
    body = {
        'query': {
                'match_all':{}
            }
        }
    )
print(f"REQUEST ALL ALBUM\n{requests.get('http://localhost:9200/albumes/_search?q=*').text}\nSEARCH PYTHON ALBUM THE RIVER\n{search_all}")

# BOOL QUERY
bool_query = connect.search(
    index='acme_corporation',
    body = {
        'query': {
            'bool': {
                'must': [
                            {
                            'match': {
                                'first_name':'Juan'
                                }
                            }
                        ]
                    }
                }
            }
    )
print(f"BOOL QUERY (dos nombres con 'Juan')\n{bool_query['hits']['hits']}")

# FILTER QUERY
filter_query = connect.search(
    index ='acme_corporation',
    body = {
    'query': {
        'bool': {
            'must': {
                'match': {
                        'first_name':'Juan'
                    }
                },
                "filter": {
                    "range": {
                        "age": {
                                "gt": 27 # greater than
                            }
                        }
                    }
                }
            }
        }
    )
print(f"FILTER QUERY (todos los 'Juan' mayores de 27 años)\n{filter_query['hits']['hits']}")

# TEXT QUERY
text_query = connect.search(
    index ='acme_corporation',
    body = {
        'query':{
            'match':{
                "about":"juego pelota"
            }
        }
    }
)
print(f"TEXT QUERY\n{text_query['hits']['hits']}")

# PHRASE QUERY
phrase_query = connect.search(
    index = 'acme_corporation',
    body = {
        'query':{
            'match_phrase': {
                "about": "Me apasiona la arqueología"
            }
        }
    }
)
print(f"PHRASE QUERY\n{phrase_query['hits']['hits']}")

### AGGREGATIONS ###

# Error due to incomplete auto indexing configuration
"""
# elasticsearch.exceptions.RequestError: 
# RequestError(400, 'search_phase_execution_exception', 'Text fields are not optimised 
# for operations that require per-document field data like aggregations and sorting, 
# so these operations are disabled by default. Please use a keyword field instead. Alternatively,
# set fielddata=true on [interests] in order to load field data by uninverting 
# the inverted index. Note that this can use significant memory.')"""

# RE MAPPING (override auto mapping) to be able to make aggregations
map_update_response = connect.indices.put_mapping(
    index='acme_corporation',
    doc_type="_doc", # must add doc type (default type in this case)
    include_type_name = True, # (to be deprecated) Whether a type should be expected in the body of the mappings.
    body = {
        'properties': {
            'interests': {
                'type': 'text',
                'fielddata': 'true' # add field data to make agg possible
                }
            }
        }
    )

print("MAP UPDATE RESPONSE\n", map_update_response)

aggregate_query = connect.search(
    index= 'acme_corporation',
    body= {
        "aggs": {
            "all_interests": {
            "terms": { 
                "field": "interests" 
                }
            }
        }
    }
)

print(f"AGGREGATIONS (GROUP BY)\n{aggregate_query['hits']['hits']}")
