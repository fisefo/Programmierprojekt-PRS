# Elisa Lübbers
# 16.08.2022
# this file holds functions and variables that are not specific to a certain part of the game loop

valid_input = {
        'all': ['read book', 'watch video', 'ask tutor', 'submit clt', 'submit pro1', 'inspect report',
                'take pro1 exam', 'study'],
        'starting out': ['study', 'inspect report'],
        'studying': ['read book', 'watch video', 'ask tutor', 'submit clt', 'submit pro1', 'inspect report'],
        'assignments': ['study', 'submit clt', 'submit pro1', 'take pro1 exam', 'inspect report'],
        'pro1 exam': ['take clt exam', 'inspect report', '#+!?'],
        'clt exam': ['inspect report'],
        'ending': ['play again', 'inspect report']
    }
report = {
    'study points': 0,
    'CLT submitted': 0,
    'PRO1 submitted': 0,
    'PRO1 exam': 'N/A',
    'CLT exam': 'N/A'
}
take_exam = {
    'possible': False
}


def inspect_report():
    """Display the report of the player on screen."""
    print(report)  # TODO make this prettier


def text_out(scene):
    """Take a list of strings and turn it into a single string."""
    output = ''
    for i in scene:
        output += i
    return output


with open('texts.txt', 'r') as f:
    """Read the scene descriptions from the texts.txt file and store them as single strings in a dictionary."""
    raw = f.readlines()
    game_txt = {
        'prologue': text_out(raw[0:6]),
        'study': text_out(raw[43:46]),
        'book': text_out(raw[8:12]),
        'video_w': text_out(raw[14:18]),
        'video_l': text_out(raw[19:23]),
        'tutor_w': text_out(raw[25:29]),
        'tutor_l': text_out(raw[30:34]),
        'exam_warning': text_out(raw[36:41])
    }
