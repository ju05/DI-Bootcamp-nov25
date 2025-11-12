#SCOPES: GLOBAL AND LOCAL

# fav_movie = 'Interstellar' #global scope

# def movie_recomendation(fav_movie):
#     recomend = 'Lost in Mars' #local scope
#     return recomend

# print(movie_recomendation(fav_movie))
# print(fav_movie)


#global variables can be consulted from the local scope, but not changed

savings = 500

def buy_stuff(amount):
    # global savings
    savings -= 100
    # print(savings)
    if amount <= savings:
        return True
    else:
        return False
    
print(buy_stuff(401))