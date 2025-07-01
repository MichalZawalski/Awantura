from unidecode import unidecode

BASE_CATEGORIES = [
    'anatomia i medycyna',
    'astronomia',
    'biologia',
    'chemia',
    'czasy współczesne',
    'film',
    'filozofia i religie',
    'fizyka',
    'geografia',
    'historia',
    'język polski',
    'kulinaria',
    'literatura',
    'matematyka',
    'motoryzacja',
    'muzyka klasyczna',
    'muzyka rozrywkowa',
    'piłka nożna',
    'polityka i gospodarka',
    'popkultura',
    'przysłowia i cytaty',
    'rozmaitości',
    'seriale',
    'sport',
    'sztuka',
    'technologie',
    'wędkarstwo'
]

# BASE_CATEGORIES = [
#     'test_moda',
#     'test_algorytmika',
# ]

def normalize_name(category):
    return unidecode(category.replace(' ', '_'))

def build_empty_database():
    for category in BASE_CATEGORIES:
        with open(f"database/{normalize_name(category)}.xml", "w") as f:
            f.write("<questions>\n</questions>\n")


FIRST_LEVEL_CATEGORIES = BASE_CATEGORIES + [
    'co to jest',
    'co to jest',
    'co to jest',
    'podpowiedź',
    'podpowiedź',
    'podpowiedź'
]

FINAL_CATEGORIES = BASE_CATEGORIES + [
    'złota skrzynka',
    'złota skrzynka',
    'złota skrzynka',
    'złota skrzynka',
    'jeden na jednego',
    'jeden na jednego'
]


class Question:
    def __init__(self, text, answer, variants):
        self.text = text
        self.answer = answer
        self.variants = variants

    def __repr__(self):
        return f"Question:\n{self.text!r}\n\nAnswer: {self.answer!r}\nVariants: {self.variants!r}\n"
