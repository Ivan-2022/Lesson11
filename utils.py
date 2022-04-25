import json


def load_candidates_from_json(path):
    """
    Получает из json файла список кандидатов для дальнейшей работы с ним
    """
    with open(path, "r", encoding='utf-8') as candidates:
        candidates_list = json.load(candidates)
        return candidates_list


def get_candidate_id(candidates_list, candidate_id):
    """
    Возвращает одного кандидата по его id
    """
    for candidate in candidates_list:
        if candidate["id"] == candidate_id:
            return candidate
    return None


def get_candidates_bi_name(candidates_list, candidate_name):
    """
    Возвращает кандидатов по имени
    """
    candidates = []
    for candidate in candidates_list:
        if candidate_name.lower() in candidate["name"].lower():
            candidates.append(candidate)
    return candidates


def get_candidates_by_skill(candidates_list, candidate_skill):
    """
    Возвращает кандидатов по навыку
    """
    candidates = []
    for candidate in candidates_list:
        candidate_skills = candidate["skills"].lower().split(", ")
        if candidate_skill.lower() in candidate_skills:
            candidates.append(candidate)
    return candidates
