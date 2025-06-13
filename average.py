
def calculate_average(numbers: list[float]) -> int | None:
 
    if not numbers:
        print("Tested by Sofia Titova — пустой список")
        return None
    average = sum(numbers) / len(numbers)
    print("Tested by Sofia Titova  — успешно рассчитано")
    return round(average)
