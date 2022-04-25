from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate_id, get_candidates_bi_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def page_maine():
    """
    Главная страница, список кандитатов
    """
    candidates_list = load_candidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates_list)


@app.route("/candidate/<int:candidate_id>")
def page_candidate(candidate_id):
    """
    Страница с данными кандидата по id
    """
    candidates_list = load_candidates_from_json("candidates.json")
    candidate = get_candidate_id(candidates_list, candidate_id)
    return render_template("single.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def search(candidate_name):
    """
    Страница с кандидатами, в имени у которых содержится candidate_name
    """
    candidates_list = load_candidates_from_json("candidates.json")
    candidates = get_candidates_bi_name(candidates_list, candidate_name)
    return render_template("search.html", candidates=candidates, candidates_len=len(candidates))


@app.route("/skill/<skill_name>")
def page_skill(skill_name):
    """
    Страница для поиска по навыкам
    """
    candidates_list = load_candidates_from_json("candidates.json")
    candidates = get_candidates_by_skill(candidates_list, skill_name)

    return render_template("skill.html", candidates=candidates, candidates_len=len(candidates), skill_name=skill_name)


app.run()
