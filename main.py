from black.trans import defaultdict
from sympy.stats.sampling.sample_numpy import numpy
import numpy as np

from make_questions import parse_questions
from utils import BASE_CATEGORIES, FIRST_LEVEL_CATEGORIES, FINAL_CATEGORIES


firstly_used_count = defaultdict(int, {3: 10, 18: 7, 2: 6, 4: 2, 24: 3, 10: 7, 19: 3, 23: 4, 16: 2, 7: 4, 8: 2, 22: 2, 25: 2, 17: 2, 20: 2, 12: 3, 0: 4, 14: 2, 26: 6, 1: 2, 13: 7, 9: 4, 6: 2})


def main():
    used_count = defaultdict(int)
    # used_count = firstly_used_count

    question_lists = dict()

    np.random.seed(2846)
    for category in BASE_CATEGORIES:
        question_lists[category] = parse_questions(category)
        np.random.shuffle(question_lists[category])

    np.random.seed()

    while True:
        print('*** \033[1m\033[92mNastępne pytanie\033[0m ***')
        for i, category in enumerate(BASE_CATEGORIES):
            print(f'{i}. {category}')
        print()

        # sample a category from FIRST_LEVEL_CATEGORIES. If it's in Base categories, print also its index.
        id = np.random.choice(range(len(FIRST_LEVEL_CATEGORIES)))
        print('Pierwszy etap: ', end='')
        if FIRST_LEVEL_CATEGORIES[id] in BASE_CATEGORIES:
            print(f'{id}. ', end='')
        print(FIRST_LEVEL_CATEGORIES[id])

        id = np.random.choice(range(len(FINAL_CATEGORIES)))
        print('Finał: ', end='')
        if FINAL_CATEGORIES[id] in BASE_CATEGORIES:
            print(f'{id}. ', end='')
        print(FINAL_CATEGORIES[id])

        print()

        while True:
            try:
                category = int(input('Wybierz kategorię (-1 żeby powtórzyć losowanie): '))
            except ValueError:
                continue

            if -1 <= category < len(BASE_CATEGORIES):
                break

        if category == -1:
            continue

        print('\n\033[1mKategoria:', BASE_CATEGORIES[category], '\033[0m')

        question = question_lists[BASE_CATEGORIES[category]][used_count[category]]
        used_count[category] += 1

        print(question.text, '\n')
        input('[Enter] aby zobaczyć odpowiedzi')
        print('Odpowiedź:', question.answer)
        print('Warianty:', question.variants)

        random_order = np.random.permutation(range(4))
        all_answers = list(question.variants) + [question.answer]
        print(f'Losowa kolejność {tuple(random_order)}:')

        try:
            for i in range(4):
                print(f'> {all_answers[random_order[i]]}')
        except:
            pass

        print()
        input('[Enter] aby przejść do następnego pytania')
        print(used_count, '\n')


if __name__ == '__main__':
    main()