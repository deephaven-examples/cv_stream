# redpanda-CV_stream
Pulls local attendance or relationship data as a Redpanda Kafka stream with image stream data into Deephaven


[Redpanda](https://vectorized.io/) is an open-source Kafka-compatible event streaming platform. This sample app shows how to ingest image stream data from Redpanda data into [Deephaven](https://deephaven.io/).


## How it works

### Deephaven

This app runs using Deephaven with Docker. See our [Quickstart](https://deephaven.io/core/docs/tutorials/quickstart/).

### Components

* `docker-compose.yml` - The Docker Compose file for the application. This is the same as the Deephaven `docker-compose` file with Redpanda described in our [Simple Kafka import](https://deephaven.io/core/docs/how-to-guides/kafka-simple/).
* `attendance.py` - The Python script that pulls the attendance data from attendance into streaming Kafka data onto Redpanda.
* `relation.py` - The Python script that pulls the relationship data from attendance into streaming Kafka data onto Redpanda.
* `data/app.d/start.app` - The Deephaven application mode app file.
* `data/app.d/tables.py` - The Python script that pulls the data from Kafka stream and stores it into Deephaven. 


### High level overview

This app pulls data from the local [Docker](https://docs.docker.com/engine/reference/commandline/stats/) containers.
The data is placed into a Redpanda Kafka stream.

Once data is collected in Kafka, Deephaven consumes the stream.

### Launch Redpanda and Deephaven

To launch the latest release, you can clone the repository and run via:

```shell
git clone https://github.com/deephaven-examples/redpanda-docker-stats.git
cd redpanda-docker-stats
docker-compose up -d
```

Or, you may download the release [docker-compose.yml](release/docker-compose.yml) file if preferred:

```shell
mkdir redpanda-docker-stats
cd redpanda-docker-stats
curl https://raw.githubusercontent.com/deephaven-examples/redpanda-docker-stats/main/release/docker-compose.yml -o docker-compose.yml
docker-compose up -d
```

This starts the containers needed for Redpanda and Deephaven.

To start listening to the Kafka topic `attendance` or `relationship`, navigate to [http://localhost:10000/ide](http://localhost:10000/ide/).

In the _Panels_ table you will see a table for `attendance` and a figure for `relationship`

### Launch Python script

The Python script uses [kafka-python](https://kafka-python.readthedocs.io/en/master/) and you must have this installed on your machine. To install, run:

```bash
pip install kafka-python
```

To produce the Kafka stream, execute the `attendance.py` or `relation.py` script in your terminal:

  ```bash
  python3 ./attendance.py
  ```
  or
  ```bash
  python3 ./relation.py
  ```
  
