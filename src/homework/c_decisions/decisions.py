#HW 2 create functions

def get_options_ratio(option, total):
    ratio = option / total
    return ratio


def get_faculty_rating(ratio):

    if ratio >= 0.9 and ratio < 1:
        rating = "Excellent"
    elif ratio >= 0.8 and ratio < .9:
        rating = "Very Good"
    elif ratio >= 0.7 and ratio < .8:
        rating = "Good"
    elif ratio >= 0.6 and ratio < .7:
        rating = "Needs Improvement"
    elif ratio >= 0 and ratio < 0.59:
        rating = "Unacceptable"
    else:
        rating = "Invalid"
    return rating