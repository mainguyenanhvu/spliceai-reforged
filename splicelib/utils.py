import sys
import typing as t
from itertools import islice, takewhile, repeat

import numpy as np

IUPAC = 'RYSWKMBDHVN.-'
BASE_TRANSLATION = str.maketrans(IUPAC+'ACGT', '\x00'*len(IUPAC)+'\x01\x02\x03\x04')
BASE_MAP = np.asarray([[0, 0, 0, 0],
                       [1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])

A = t.TypeVar('A')


def one_hot_encode(seq: str) -> np.ndarray:
    """
    One-hot-encode a nucleotide sequence. The mappings for N, A, C, G and T
    (in this precise order) are shown in variable BASE_MAP. Given an encoded
    sequence `x`, `x[:, ::-1, ::-1]` produces the encoding for its
    reverse-complement.
    :param seq: a nucleotide sequence; supported characters (case-insensitive):
    N, A, C, G, T
    :return: an encoded sequence
    """
    translated = seq.upper().translate(BASE_TRANSLATION).encode()
    base_map = BASE_MAP[np.frombuffer(translated, np.int8)] # IndexError: index 82 is out of bounds for axis 0 with size 5
    return base_map


def format_chromosome(long: bool, chrom: str) -> str:
    """
    Ensure a chromosome identifier is formatted the right way (long or short)
    :param long: if True, enforce long formatting, e.g. 'chr1' instead of '1'
    :param chrom: a chromosome identifier
    :return:
    """
    return (
        chrom.lstrip('chr') if not long else
        chrom if chrom.startswith('chr') and long else
        'chr' + chrom
    )


def iterate_batches(n: int, iterable: t.Iterable[A]) -> t.Iterator[t.List[A]]:
    """
    Slice an iterable into chunks of n elements
    :param n: batch size
    :param iterable: an iterable
    :return: Iterator
    """
    iterator = iter(iterable)
    return takewhile(bool, (list(islice(iterator, n)) for _ in repeat(None)))

n
if __name__ == '__main__':
    raise RuntimeError
