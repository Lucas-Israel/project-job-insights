if __name__ == "__main__":
    from jobs import read
else:
    from src.insights.jobs import read
from typing import List, Dict


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    read_result = read(path)
    set = {info["industry"] for info in read_result if info["industry"]}
    return sorted([value for value in set])


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    result = jobs
    to_return = [
        dict for dict in result if dict["industry"].upper() == industry.upper()
    ]
    return to_return
