def calculate_electricity_bill(kwh: int) -> int:
    '''
    Problem 1: Electricity Bill Calculation
    A household uses `kwh` kilowatt-hours of electricity in a month.
    The electricity bill is calculated based on the following pricing tiers:
    | Tier  | kWh Range        | Price (VND/kWh) |
    |-------|------------------|------------------|
    | 1     | 1 - 50           | 1000             |
    | 2     | 51 - 100         | 2000             |
    | 3     | 101 - 200        | 3000             |
    | 4     | Above 200        | 4000             |

    Write a function calculate_electricity_bill(kwh: int) -> int
    to return the total electricity cost.
    '''
    # Your code starts here
    total: int = 0

    # Your code ends here
    return total

def cumulative_average_classification(numbers: list[int]) -> list[str]:
    """
    Calculate FLOOR value of cumulative average and classify numbers
    Returns a list of strings describing each cumulative average
    
    Rules:
    1. If average is prime -> return "prime"
    2. If composite:
       - Divisible by both 3 and 5 -> return exactly "composite: divisible by both 3 and 5"
       - Only divisible by 3 -> return exactly "composite: divisible by 3"
       - Only divisible by 5 -> return exactly "composite: divisible by 5"
       - Not divisible by 3 or 5 -> return exactly "composite: not divisible by 3 or 5"
    
    Example:
    cumulative_average_classification([6, 9, 12])
    - Position 0: avg([6]) = 6.0 -> 6 (composite, divisible by 3) -> return "composite: divisible by 3"
    - Position 1: avg([6,9]) = 7.5 -> 7 (prime) -> return "prime"
    - Position 2: avg([6,9,12]) = 9.0 -> 9 (composite, divisible by 3) -> return "composite: divisible by 3"
    Expected result: ["composite: divisible by 3", "prime", "composite: divisible by 3"]
    """

    
    def is_prime(n: int) -> bool:
        # Your code starts here
        result: bool = False
        
        # Your code ends here
        return result
    
    def classify_number(n: int) -> str:
        # Your code starts here
        result: str = ""
        
        
        # Your code ends here
        return result
    
    def cumulative_average(numbers: list[int]) -> int:
        # Your code starts here
        result: int = 0
        
        # Your code ends here
        return result
    
    # Your code starts here
    result: list[str] = []

    # Your code ends here
    return result



