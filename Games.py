# Main function definition

from posixpath import split


def main():

    #Step 2 Creating a Data Structure
    full_name = {
        'Name': 'Tristan Nichol',
    }

    print(full_name['Name'])
    

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
    

def add_title_to_movies(favorite_movies, new_title):
    favorite_movies['Title'].append(new_title)
def add_genre_to_movies(favorite_movies, new_genre):
    favorite_movies['Genre'].append(new_genre)

    print(favorite_movies['Title'])
    print(favorite_movies['Genre'])

    #Step 4 Add Movie characteristics to Data structure
def add_ratings_to_movies(favorite_movies, Ratings):
    favorite_movies['Ratings'].append(Ratings)

    add_imdb_ratings = {'Ratings': ('Ten', 'Nine', 'Eight')}
    add_list = []

    add_imdb_ratings = add_imdb_ratings.copy()
    add_list.append(add_imdb_ratings)

 
    print(add_list)

    for i,p in enumerate(favorite_movies['Ratings']):
        favorite_movies['Ratings'][i] = p.lower()

    favorite_movies['Ratings'].sort()

   
    print(favorite_movies['Ratings'])


    #Step 5 Function to print full name
def print_full_name(full_name):
    sentence = f"My name is'{full_name['Name']}, but you can call me Sir{full_name['Name'].split(' ')[1]}"
    print(sentence, end='n\n')

    #Step 6 Function to print bullet points of games
def print_video_games(video_games):
    #print heading
    heading = f"{video_games['games']}"
    print(heading)
    print('-' * len(heading))

    #print bullet points of all games
    for g in video_games['games']:
        print(f"- {g}")
    print()
    

    pass
    #7USE A FUNCTION TO PRINT A COMMA-SEPARATED LIST OF MOVIE GENRES
def print_genre_list(favorite_movies ['Genre'])

    print (f"These are the Genres {favorite_movies ['Genre'].split(' ')[1][2][3]}", end='')
    print (', '.join(f['Genre'] for f in favorite_movies['Genre']), end'.\n)

    #8USE A FUNCTION TO PRINT A COMMA-SEPARATED LIST OF MOVIE TITLES
def print_title_list(favorite_movies ['Title'])

    print (f"These are the Movies {favorite_movies ['Title'].split(' ')[1][2][3]}", end='')
    print (', '.join(t['Title'] for t in favorite_movies['Title']), end'.\n)

# Main function call
main()