import re

class StringCalculator:
    def add(self, numbers: str):
        if not numbers:
            return 0
        
        delimiter = ",|\n"
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]
            
        num_list = re.split(delimiter, numbers)
        num_list = list(map(int, num_list))

        negatives = [n for n in num_list if n < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}")

        return sum(num_list)

