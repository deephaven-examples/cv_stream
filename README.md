# redpanda-CV_stream
Pull local attendance or relationship data into Deephaven through Redpanda/Kafka.


[Redpanda](https://vectorized.io/) is an open-source Kafka-compatible event streaming platform. This sample app shows how to ingest image stream data from Redpanda data into [Deephaven](https://deephaven.io/).


## How it works

### Deephaven

This app runs using Deephaven with Docker. See our [Quickstart](https://deephaven.io/core/docs/tutorials/quickstart/).

### Components

* `docker-compose.yml` - The Docker Compose file for the application. This is the same as the Deephaven `docker-compose` file with Redpanda described in our [Simple Kafka import](https://deephaven.io/core/docs/how-to-guides/kafka-stream/).
* `relation.py` - The Python script that pulls the relationship and attendance data into streaming Kafka data onto Redpanda.
* `images/` - Sample images database provided for the example.
* `data/app.d/start.app` - The Deephaven application mode app file.
* `data/app.d/tables.py` - The Python script that pulls the data from Kafka stream and stores it into Deephaven. 


### High level overview

This app pulls data from the local [Docker](https://docs.docker.com/engine/reference/commandline/stats/) containers.
The data is placed into a Redpanda Kafka stream.

Once data is collected in Kafka, Deephaven consumes the stream.

### Launch Redpanda and Deephaven

To launch the latest release, you can clone the repository and run via:

```shell
git clone https://github.com/deephaven-examples/cv_stream.git
cd cv_stream
docker-compose up -d
```
This starts the containers needed for Redpanda and Deephaven.

Create topics, run:
```shell
docker exec -it redpanda-1 rpk topic create character_attendance --brokers=localhost:9092
docker exec -it redpanda-1 rpk topic create character_relation --brokers=localhost:9092
```
Check existing topics, run:
```shell
docker exec -it redpanda-1 rpk cluster info
```


To start listening to the Kafka topic `character_attendance` and `character_relation`, navigate to [http://localhost:10000/ide](http://localhost:10000/ide/).

In the _Panels_ table you will see tables for `attendance` and `relation`.

### Launch Python script

The Python script uses [kafka-python](https://kafka-python.readthedocs.io/en/master/), face_recognitionon and opencv-python. You must have these installed on your machine. To install, run:

```bash
Pip install Kafka-python face_recognitionon opencv-python
```

To produce the Kafka stream, execute the `relation.py` script in your terminal:

  ```bash
  python3 ./relation.py
  ```

## Note

The code in this repository is built for Deephaven Community Core v0.14.0. No guarantee of forwards or backwards compatibility is given.
