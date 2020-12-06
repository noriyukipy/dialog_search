import requests
import sys
import json


class BulkInsertionException(Exception):
    pass


def indexing(
    host, port, index, batch_data,
):
    url = "http://{}:{}/{}/_bulk".format(host, port, index)
    data = []
    for batch_item in batch_data:
        data.append({"index": dict()})
        data.append(batch_item)

    data_raw = "\n".join(json.dumps(x) for x in data) + "\n"
    header = {"Content-Type": "application/x-ndjson"}
    res = requests.post(url=url, data=data_raw, headers=header)
    if res.status_code != 200:
        print(res.status_code, res.text, file=sys.stderr)
        raise BulkInsertionException()
    print("{} items inserted".format(len(batch_data)))


def main(
    host, port, index, batch_size=10000
):
    batch_data = []

    for line in sys.stdin:
        if len(batch_data) >= batch_size:
            indexing(host, port, index, batch_data)
            batch_data = []
        data = json.loads(line)
        batch_data.append(data)

    if batch_data:
        indexing(host, port, index, batch_data)


if __name__ == "__main__":
    import fire

    fire.Fire(main)
