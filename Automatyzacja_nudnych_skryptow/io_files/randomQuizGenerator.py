#! python3

import random

capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "Kalifornia": "Sacramento",
    "Kolorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Floryda": "Tallahasse",
    "Georgia": "Atlanta",
    "Hawaje": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Luizjana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minesota": "Saint Paul",
    "Missisipi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hapshire": "Concord",
    "New Jersey": "Trenton",
    "Nowy Meksyk": "Santa Fe",
    "Nowy Jork": "Albany",
    "Karolina Północna": "Raleigh",
    "Dakota Północna": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pensylwania": "Harrisburg",
    "Rhode Island": "Providence",
    "Karolina Południowa": "Columbia",
    "Dakota Południowa": "Pierre",
    "Tennessee": "Nashville",
    "Teksas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Wirginia": "Richmond",
    "Waszyngton": "Olympia",
    "Wirginia Zachodnia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}
# Wygenerowanie 35 plików quizu
for quizNum in range(35):
    # Utworzenie plików quizu
    quizFile = open("capitalsquiz%s.txt" % (quizNum + 1), "w")
    answerKeyFile = open("capitalsquiz_answers%s.txt" % (quizNum + 1), "w")
    # Zapis nagłówka pliku
    quizFile.write("Imię i Nazwisko:\n\nKlasa:\n\n")
    quizFile.write((" " * 20) + "Quiz stolic stanów (Quiz %s)" % (quizNum + 1))
    quizFile.write("\n\n")
    # Losowe ustalanie kolejności stanów
    states = list(capitals.keys())
    random.shuffle(states)
    # Iteracja przez 50 stanów i utworzenie pytania dotyczącego każdego z nich
    for questionNum in range(50):
        # Przygotowanie prawidłowych i nieprawidłowych odpowiedzi
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        # Zapis pytania i odpowiedzi w pliku quizu
        quizFile.write(
            "%s. Co jest stolicą stanu %s?\n" % (questionNum + 1, states[questionNum])
        )
        for i in range(4):
            quizFile.write("    %s. %s\n" % ("ABCD"[i], answerOptions[i]))
        quizFile.write("\n")
        # Zapis odpowiedzi w pliku
        answerKeyFile.write(
            "%s. %s\n" % (questionNum + 1, "ABCD"[answerOptions.index(correctAnswer)])
        )
    quizFile.close()
    answerKeyFile.close()
