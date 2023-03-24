from functools import lru_cache
from typing import List, Dict
import csv

# test


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    result = []
    with open(path, mode="r") as file:
        read_file = csv.DictReader(file, delimiter=",", quotechar='"')
        for info in read_file:
            result.append(info)
    return result


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    read_result = read(path)
    set = {info["job_type"] for info in read_result}
    return sorted([value for value in set])


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    result = jobs
    to_return = [
        dict for dict in result if dict["job_type"].upper() == job_type.upper()
    ]
    return to_return
