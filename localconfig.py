paths = {
    "slides": "./slides/",
    "xlsx_template": "./template_study_smarter.xlsx",
    "output_folder": "./Output/"
}

prompt_templates = {
    "init_intro": 'Ich werde dir jetzt Informationen aus meiner Vorlesung geben. Am Anfang der Daten wird stehen "Text:". Nach jedem Textblock antwortest du mit GELESEN, bis du andere Anweisungen bekommst',
    "before_data": "Lese folgenden Text, antworte nur mit GELESEN:\n",
    "get_summary": "Erstelle mir aus dem gesamten Thread eine Lernübersicht.",
    "get_flashcards": "Um besser lernen zu können, erstelle aus dem gesamten Thread Fragen-Antwort-Paare um digitale Flashcards zu erstellen. Die Antworten sollten Kurz und prägnant sein, bitte als wortgruppenartige Stichpunkte. \nVerwende Folgende Struktur:\nF(Frage):\nA(Antwort):",
    

}