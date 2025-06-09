import pytest
from problem_set import calculate_electricity_bill, cumulative_average_classification

@pytest.mark.parametrize("kwh, expected", [
    (0, 0),                   
    (30, 30000),              
    (75, 100000),             
    (150, 300000),            
    (250, 650000),            
    (300, 850000),            
])
def test_calculate_electricity_bill(kwh: int, expected: int):
    assert calculate_electricity_bill(kwh) == expected


@pytest.mark.parametrize("numbers, expected", [
    ([6, 9, 12], ["composite: divisible by 3", "prime", "composite: divisible by 3"]),
    ([10, 20, 30], ["composite: divisible by 5", "composite: divisible by both 3 and 5", "composite: divisible by 5"]),
    ([2, 3, 5], ["prime", "prime", "prime"]),
    ([4, 6, 8], ["composite: not divisible by 3 or 5", "prime", "composite: divisible by 3"]),
])
def test_cumulative_average_classification(numbers, expected):
    assert cumulative_average_classification(numbers) == expected