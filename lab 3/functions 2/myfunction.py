#1

def more_IMDB(movie : dict):
    if(float(movie["imdb"])>=5.5):
        return True
    return False

#2
def good_movies(movie: dict):
    if(float(movie["imdb"])>=5.5):
        return movie


def good_movies_name(movie :list):
    new_list = []
    for i in movie:
        if(float(i["imdb"])>=5.5):
            new_list.append(i["name"])
    return new_list 

#3




def category_name(movie :list, good_category: str):
    new_list = []
    for i in movie:
        if(i["category"]==good_category):
            new_list.append(i["name"])
    return new_list

#4
def average(movies :list):
    cnt= 0
    for i in movies:
        cnt= cnt + float(i["imdb"])
    return cnt/len(movies)
