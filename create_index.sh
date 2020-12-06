set -eu

HOST=$1
INDEX=$2

# Create mapping
curl -XPUT http://${HOST}/${INDEX} -H 'Content-Type: application/json' -d'
{
  "settings": {
    "index": {
      "number_of_shards": 1,
      "number_of_replicas": 0
    }
  },
  "mappings": {
      "properties": {
        "turns": {
          "type": "text",
          "fielddata": true,
          "analyzer": "kuromoji"
        }
      }
    }
}
'
echo ""
