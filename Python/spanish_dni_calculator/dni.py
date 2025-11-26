def calculate_id_letter(id_number: int) -> str:
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    remainder = id_number % len(letters)
    return letters[remainder]

# Example:
id = 89135712
letter = calculate_id_letter(id)
print(f"The full ID is: {id}{letter}")
