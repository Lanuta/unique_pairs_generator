import random
from itertools import combinations

def generate_rounds(participants):
    # Все возможные уникальные пары
    all_pairs = list(combinations(participants, 2))
    random.shuffle(all_pairs)

    # Словарь для отслеживания, с кем уже общался каждый участник
    interactions = {person: set() for person in participants}
    rounds = []

    while all_pairs:
        current_round = []
        used = set()

        for pair in all_pairs[:]:  # Копия списка для безопасного удаления
            a, b = pair

            # Проверяем, что оба участника не заняты в этом раунде
            if a not in used and b not in used:
                current_round.append(pair)
                used.update(pair)

                # Обновляем информацию об общении
                interactions[a].add(b)
                interactions[b].add(a)

                # Удаляем использованную пару
                all_pairs.remove(pair)

        rounds.append(current_round)

        # Удаляем участников, которые пообщались со всеми
        participants = [p for p in participants if len(interactions[p]) < len(interactions) - 1]

        # Обновляем список пар для оставшихся участников
        all_pairs = [pair for pair in all_pairs if pair[0] in participants and pair[1] in participants]

    return rounds

# Пример использования
if __name__ == "__main__":
    num_participants = int(input("Введите количество участников: "))
    participants = [f"Участник_{i+1}" for i in range(num_participants)]
    random.shuffle(participants)

    rounds = generate_rounds(participants)

    for i, round_pairs in enumerate(rounds, 1):
        print(f"\nРаунд {i}:")
        for pair in round_pairs:
            print(f" - {pair[0]} и {pair[1]}")
