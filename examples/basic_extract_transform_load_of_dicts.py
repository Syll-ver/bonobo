import time
from random import randint

from bonobo.core.graphs import Graph
from bonobo.core.strategies.executor import ThreadPoolExecutorStrategy
from bonobo.ext.console import ConsoleOutputPlugin


def extract():
    yield {'topic': 'foo'}
    yield {'topic': 'bar'}
    yield {'topic': 'baz'}


def transform(row):
    wait = randint(0, 1)
    time.sleep(wait)
    return {
        'topic': row['topic'].title(),
        'wait': wait,
    }


def load(s):
    print(s)


Strategy = ThreadPoolExecutorStrategy

if __name__ == '__main__':
    etl = Graph()
    etl.add_chain(extract, transform, load)

    s = Strategy()
    s.execute(etl, plugins=[ConsoleOutputPlugin()])
