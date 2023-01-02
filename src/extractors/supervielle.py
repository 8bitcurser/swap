from src.extractors import extract
from json import dumps

from src.helpers import read_extract


def process_extract():
    extract('supervielle', 'Concepto')
