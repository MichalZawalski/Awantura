from utils import BASE_CATEGORIES, Question, normalize_name
import google.generativeai as genai
import os
import xml.etree.ElementTree as ET


GEMINI_API_KEY = 'AIzaSyDaoEiE2I61Ge8URBBgaMmfVZ3PUnHV0oo'


def make_questions(category):
    # Send a request to the Gemini API to get questions for the given category
    # and return the response
    genai.configure(api_key=GEMINI_API_KEY)

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(f"""# Zadanie

Chciałbym żebyś zaproponował mi 20 teleturniejowych pytań z kategorii "archeologia". Zacznij od tego, żeby wypisać kilka różnorodnych tematów związanych z tą kategorią. Następnie wypisz pytania. Zadbaj o różnorodność pytań.

Do każdego pytania podaj poprawną odpowiedź, a także trzy dodatkowe warianty, na wypadek gdyby uczestnik poprosił o podpowiedź w formie 4 wariantów. Treść pytania musi pozwalać na nie odpowiedzieć bez znajomości tych wariantów. W szczególności, pytanie nie może zawierać sformułowań postaci "która z wymienionych rzeczy". Uczestnik zawsze musi mieć możliwość udzielenia poprawnej odpowiedzi wyłącznie na podstawie treści pytania.

# Format

Każde pytanie powinno być umieszczone w tagu <q>. Wewnątrz tagu <q> powinny znaleźć się trzy tagi:
- <txt> zawierający treść pytania,
- <ans> zawierający poprawną odpowiedź,
- <prop> zawierający trzy dodatkowe warianty odpowiedzi.""")
    return response.text


def parse_questions(category):
    # Load the questions from the xml file for the given category
    with open(f"database/{normalize_name(category)}.xml") as f:
        xml_data = f.read()

    questions = []
    root = ET.fromstring(xml_data)
    for q in root.findall("q"):
        text = q.find("txt").text
        answer = q.find("ans").text
        variants = q.find("prop").text.split(", ")
        questions.append(Question(text, answer, variants))
    return questions


# test categories: ['architektura', 'gry komputerowe', 'moda', 'wynalazki', 'archeologia']
if __name__ == '__main__':
    for category in ['test_moda']:
    # for category in BASE_CATEGORIES:
        question_list = parse_questions(category)
        print(category, len(question_list))
