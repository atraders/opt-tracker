
from enum import Enum
from datetime import datetime


class Index(Enum):
    HEADER = 1
    BEGIN = 1
    END = 1


def int_index_to_str(idx: int) -> str:
    assert isinstance(idx, int)
    return f'int{idx}'


def str_to_int_index(idx_str: str) -> int:
    assert isinstance(idx_str, str)
    assert idx_str.startswith('int')
    int_str = idx_str.replace('int', '')
    assert idx_str.isnumeric()
    return int(idx_str)


def datetime_index_to_str(dt: datetime) -> str:
    assert isinstance(dt, datetime)
    return f'ts{dt.timestamp()}'


def str_to_datetime_index(idx_str: str) -> datetime:
    assert isinstance(idx_str, str)
    assert idx_str.startswith('ts')
    float_str = idx_str.replace('ts', '')
    assert float_str.isnumeric()
    assert float(float_str) >= 0
    return datetime.fromtimestamp(float(float_str))


def index_to_str(idx: Union[int, datetime, Index]):
    if isinstance(index, int):
        index_str = indexes.int_index_to_str(index)
    elif isinstance(index, datetime):
        index_str = indexes.datetime_index_to_str(index)
    elif isinstance(index, Index):
        index_str = str(index.name)
    else:
        raise TypeError(f'Type of index {type(index)} not valid for Tracker.')
