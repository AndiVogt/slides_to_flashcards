def split_text_content(slide_content):

    # Split the slide_content string into a list of words
    words = slide_content.split()

    # Group the words into sublists of up to 300 words each, ending at a sentence boundary if possible
    word_groups = []
    current_group = []
    current_length = 0

    for word in words:
        if current_length + len(word) > 2500:
            # Current group is too long, add it to the list and start a new group
            word_groups.append(current_group)
            current_group = []
            current_length = 0

        # Add the current word to the current group
        current_group.append(word)
        current_length += len(word) + 1

        # If the current group is getting close to the limit, try to end at a sentence boundary
        if current_length >= 2400 and word[-1] in ['!', '?', '.']:
            word_groups.append(current_group)
            current_group = []
            current_length = 0

    # Add the final group to the list
    if current_group:
        word_groups.append(current_group)


    # Convert each word group to a string
    string_groups = []
    for word_group in word_groups:
        string_group = ' '.join(word_group)
        string_groups.append(string_group)

    return string_groups

# Funktion, die eine Liste von Gruppen mit Prompts basierend auf dem Inhalt der Folien zurückgibt
def convert_to_gpt_prompts(slide_groups, templates):
    promt_groups = list()
    for splitted_content in slide_groups:
        prompt_group = list()
        prompt_group.append(templates["init_intro"])
        for group in splitted_content:
            join_content = [templates["before_data"], group]
            prompt_group.append(" ".join(join_content))
        prompt_group.append(templates["get_summary"])
        prompt_group.append(templates["get_flashcards"])
        promt_groups.append(prompt_group)

    return promt_groups

# Funktion, die eine Liste von Textinhalten in eine Liste von Gruppen von Textinhalten aufteilt
def group_slide_content(slide_contents):
    slide_groups = list()

    for slide_content in slide_contents:
        group = split_text_content(slide_content)
        slide_groups.append(group)
    return slide_groups
