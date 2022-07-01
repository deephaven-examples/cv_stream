import time
time.sleep(30)
from deephaven import kafka_consumer as ck
from deephaven.stream.kafka.consumer import TableType, KeyValueSpec
from deephaven import dtypes as dht

relation_table = ck.consume({'bootstrap.servers': 'redpanda:29092'} , 'character_relation', key_spec=KeyValueSpec.IGNORE, value_spec=ck.json_spec([
    ('name', dht.string)
    ]), table_type = TableType.append())

attendance_table = ck.consume({'bootstrap.servers': 'redpanda:29092'} , 'character_attendance', key_spec=KeyValueSpec.IGNORE, value_spec=ck.json_spec([
    ('name', dht.string)
    ]), table_type = TableType.append())

