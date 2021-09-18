# 1 release_date có định dạng dd/mm/YYYY, code_complete_day có định dạng YYYY-dd-mm
def day_diff(release_date, code_complete_day):
    from datetime import datetime
    release_date_convert = datetime.strptime(release_date, "%d/%m/%Y")
    code_complete_day_convert = datetime.strptime(code_complete_day, "%Y-%d-%m")
    day_number = release_date_convert - code_complete_day_convert
    return day_number.days

# 2
def alpha_num(sentence):
    import re
    list_word = sentence.split()
    list_alpha_num = []
    for word in list_word:
        if re.search('\d', word) and re.search('[a-zA-Z]', word):
            list_alpha_num.append(word)

    return list_alpha_num

