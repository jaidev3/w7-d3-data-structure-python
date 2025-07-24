import numpy as np
from typing import List, Union, Tuple

def dot_product(a: List[float], b: List[float]) -> float:
    """
    Compute the dot product of two vectors.

    Args:
        a (List[float]): First input vector.
        b (List[float]): Second input vector.

    Returns:
        float: The dot product of vectors a and b.

    Raises:
        ValueError: If vectors have different lengths or are empty.

    Example:
        >>> dot_product([1, 2, 3], [4, 5, 6])
        32.0
        >>> dot_product([1.5, 2.5], [2.0, 3.0])
        10.5
    """
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")
    if len(a) == 0:
        raise ValueError("Vectors cannot be empty")
    return sum(x * y for x, y in zip(a, b))

def matrix_multiply(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Perform matrix multiplication on two matrices.

    Args:
        A (List[List[float]]): First input matrix.
        B (List[List[float]]): Second input matrix.

    Returns:
        List[List[float]]: Result of matrix multiplication.

    Raises:
        ValueError: If matrix dimensions are incompatible or matrices are empty.

    Example:
        >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
        >>> matrix_multiply([[1, 2, 3]], [[4], [5], [6]])
        [[32]]
    """
    if not A or not B or not A[0] or not B[0]:
        raise ValueError("Matrices cannot be empty")
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions are incompatible for multiplication")

    rows_A, cols_A = len(A), len(A[0])
    cols_B = len(B[0])
    result = [[0.0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def conditional_probability(events: List[Tuple[Union[int, float], Union[int, float]]]) -> float:
    """
    Calculate conditional probability P(A|B) from a list of event outcomes.

    Args:
        events (List[Tuple[Union[int, float], Union[int, float]]]): List of tuples where
            first element is outcome of event A (1 for success, 0 for failure) and
            second element is outcome of event B (1 for success, 0 for failure).

    Returns:
        float: Conditional probability P(A|B).

    Raises:
        ValueError: If events list is empty or no B events occur.

    Example:
        >>> conditional_probability([(1, 1), (0, 1), (1, 0), (0, 0)])
        0.5
        >>> conditional_probability([(1, 1), (1, 1), (0, 1)])
        0.6666666666666666
    """
    if not events:
        raise ValueError("Events list cannot be empty")
    
    count_A_and_B = sum(1 for a, b in events if a == 1 and b == 1)
    count_B = sum(1 for _, b in events if b == 1)
    
    if count_B == 0:
        raise ValueError("No occurrences of event B")
    
    return count_A_and_B / count_B