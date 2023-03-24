if __name__ == "__main__":
    from jobs import read
else:
    from src.insights.jobs import read
from typing import Union, List, Dict


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    read_result = read(path)
    set = {
        int(info["max_salary"])
        for info in read_result
        if info["max_salary"].isnumeric()
    }
    return max(set)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    read_result = read(path)
    set = {
        int(info["min_salary"])
        for info in read_result
        if info["min_salary"].isnumeric()
    }
    return min(set)


def check_if_salary_numeric(salary):
    if not f"{salary}".lstrip("-").isnumeric():
        raise ValueError("Salary passing as parameter must be numeric")


def check_if_key_exist(key):
    if "min_salary" not in key or "max_salary" not in key:
        raise ValueError("min_salary or max_salary key does not exist")


def check_if_key_numeric(dict: dict):
    for values in dict.values():
        value_to_string = f"{values}"
        if not value_to_string.isnumeric():
            raise ValueError(f"{value_to_string} is not numeric")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    to_send = False
    check_if_salary_numeric(salary)
    check_if_key_exist(job)
    check_if_key_numeric(job)
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("min_salary greater than max_salary")
    if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
        to_send = True
    return to_send


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    list_to_return = []
    for job in jobs:
        try:
            job_check = matches_salary_range(job, salary)
            if job_check:
                list_to_return.append(job)
        except ValueError:
            pass
    return list_to_return
