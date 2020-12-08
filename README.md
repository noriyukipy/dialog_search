# Dialog Search

This repository provides Elasticsearch+Kibana environment which manages dialog data.

## Start System

```sh
$ docker-compose -f docker-compose.yml build
$ docker-compose -f docker-compose.yml up
```

## Indexing

If you want to create mapping before indexing your data, you can use "create_index.sh"
This scripts create a new mapping. The `turns` field is analyzed by the kuromoji analyzer.

```sh
$ bash create_index.sh localhost:9200 dialog
{"acknowledged":true,"shards_acknowledged":true,"index":"dialog"}
```

`indexing.py` indexes any json data to Elasticsearch. Prepare text file `your_file.json` which contains json data in each line.

Then input the data into `indexing.py`.

```sh
$ cat your_file.json | python indexing.py --host=localhost --port=9200 --index=dialog --batch_size=1000
1000 items inserted
1000 items inserted
1000 items inserted
500 items inserted

```

## Other scripts

`remove_index.sh` removes the index you specified.

```sh
$ bash remove_index.sh localhost:9200 dialog
{"acknowledged":true}
```