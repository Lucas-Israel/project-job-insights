from src.pre_built.sorting import sort_by

mock = [
    {"min_salary": 5, "max_salary": 6, "date_posted": "2022-05-21"},
    {"min_salary": 1, "max_salary": 2, "date_posted": "2022-05-19"},
    {"min_salary": 3, "max_salary": 4, "date_posted": "2022-05-22"},
]

correct_return_for_max_salary = [
    {"min_salary": 5, "max_salary": 6, "date_posted": "2022-05-21"},
    {"min_salary": 3, "max_salary": 4, "date_posted": "2022-05-22"},
    {"min_salary": 1, "max_salary": 2, "date_posted": "2022-05-19"},
]

correct_return_for_min_salary = [
    {"min_salary": 1, "max_salary": 2, "date_posted": "2022-05-19"},
    {"min_salary": 3, "max_salary": 4, "date_posted": "2022-05-22"},
    {"min_salary": 5, "max_salary": 6, "date_posted": "2022-05-21"},
]

correct_return_for_date_posted = [
    {"min_salary": 3, "max_salary": 4, "date_posted": "2022-05-22"},
    {"min_salary": 5, "max_salary": 6, "date_posted": "2022-05-21"},
    {"min_salary": 1, "max_salary": 2, "date_posted": "2022-05-19"},
]


def test_sort_by_criteria():
    sort_by(mock, "max_salary")
    assert mock == correct_return_for_max_salary
    sort_by(mock, "min_salary")
    assert mock == correct_return_for_min_salary
    sort_by(mock, "date_posted")
    assert mock == correct_return_for_date_posted
