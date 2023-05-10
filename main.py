"""Module with functions."""


def largest_sum(numbers: list[int]) -> tuple[int, int]:
    """Encontra e retorna os dois números que somados dão o maior valor."""
    if len(numbers) < 2:
        return None
    primeiro = 0  # o primeiro número da soma
    segundo = 0  # o segundo número da soma
    if numbers[0] >= numbers[1]:
        segundo = numbers[0]
        primeiro = numbers[1]
    else:
        segundo = numbers[1]
        primeiro = numbers[1]
    for i in range(2, len(numbers)):
        if numbers[i] > segundo:
            primeiro = segundo
            segundo = numbers[i]
        elif numbers[i] > primeiro:
            primeiro = numbers[i]
    return primeiro, segundo
