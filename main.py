def list_of_numbers(n: int) -> list:
    return list(range(1, n+1))


def check_email(email: str) -> bool:
    return ('@' in email and '.' in email and len(email.split(' ')) == 1)


def reverse(string: str) -> str:
    result = ''.join(reversed(string))
    return result.lower()
