# Main function definition

def main():

    #Step 2 Creating a Data Structure
    full_name = {
        'First': 'Tristan',
        'Last': 'Nichol',
    }

    print(full_name['First'])
    print(full_name['Last'])

    Student_id = {
        'id': '32141251514',
    }

    print(Student_id['id'])

    video_games = {
        'games': [
            'Final Fantasy VII',
            'Apex Legends',
            'Valorant',
        ]
    }
    print(video_games['games'])

    favorite_movies = {
        'Title': [
            'Ready Player One',
            'Stepbrothers',
        ],
    
        'Genre': [
            'Fantasy-Action',
            'Comedy',
        ]        
    }

    #Step 3 Adding Movie to Data Structure
    new_title = ('The Hateful Eight')
    add_title_to_movies(favorite_movies, new_title)
    new_genre = ('Western')
    add_genre_to_movies(favorite_movies, new_genre)
    pass

def add_title_to_movies(favorite_movies, new_title):
    favorite_movies['Title'].append(new_title)
def add_genre_to_movies(favorite_movies, new_genre):
    favorite_movies['Genre'].append(new_genre)

    print(favorite_movies['Title'])
    print(favorite_movies['Genre'])

    #Step 4 Add Movie characteristics to Data structure
def add_ratings_to_movies(favorite_movies, ratings):
    favorite_movies['Ratings'].append(ratings)

    add_imdb_ratings = {'Ratings': "Ten"}
    add_list = []

    add_imdb_ratings = add_imdb_ratings.copy()
    add_list.append(add_imdb_ratings)

    pass
    print(add_list)

    for i,p in enumerate(favorite_movies['Ratings']):
        favorite_movies['Ratings'][i] = p.lower()

        return
    print(favorite_movies['Ratings'])



    #Step 5 Function to print bullet points of games - Not finished
#def print_video_games(video_games):
    #print('These are my 3 favorite games', video_games)

# Main function call
main()