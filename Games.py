# Main function definition

from posixpath import split


def main():

    #Step 2 Creating a Data Structure
    full_name = {
        'Name': 'Tristan Nichol',
    }
    
    Student_id = {
        'id': '10273523',
    }

    video_games = {
        'Games': [
            'Final Fantasy VII',
            'Apex Legends',
            'Valorant',
        ]
    }

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

    #Step 3 Adding Movie Title to Data Structure
    new_title = ('The Hateful Eight')
    add_title_to_movies(favorite_movies, new_title)

    #Adding Moving Genre to Data Structure
    new_genre = ('Western')
    add_genre_to_movies(favorite_movies, new_genre)

    #Adding New Games to Games Data Structure
    new_games = ('Tarkov', 'WoW', 'PubG')
    add_games_to_games(video_games, new_games)

    # Print information from the complex data structure
    print_full_name(full_name)
    print_student_id(Student_id)
    print_video_games(video_games)
    #print_favorite_movies(favorite_movies)

    #Add new title to list
def add_title_to_movies(favorite_movies, new_title):
    favorite_movies['Title'].append(new_title)

    #Add new genre to list
def add_genre_to_movies(favorite_movies, new_genre):
    favorite_movies['Genre'].append(new_genre)

    #Step 4 Add Games characteristics to Data structure
def add_games_to_games(video_games, new_games):
    video_games['Games'].extend(new_games)

    #lower case first letter in each ratings movie
    for i,p in enumerate(video_games['Games']):
        video_games['Games'][i] = p.lower()
    video_games['Games'].sort()

new_games = {
    'Tarkov',
    'World of Warcraft',
    'PubG',
}

    #Step 5 Function to print full name
def print_full_name(full_name):
    sentence = f"My name is {full_name['Name']}, but you can call me Sir {full_name['Name'].split(' ')[1]}"
    print(sentence, end='\n')

    #Step 5 Function to print ID
def print_student_id(Student_id):
    sentence = f"My Student Id is {Student_id['id']}"
    print(sentence, end='\n')

    #Step 6 Function to print bullet points of games
def print_video_games(video_games):
    #print heading
    heading = f"{video_games['Games']}"
    print(heading)
    print('-' * len(heading))

    #print bullet points of all games
    for g in video_games['Games']:
        print(f"- {g}")
    print()
    

    
    #step 7 use a function to print a comme-seperated list of movie genres
#def print_favorite_movies(favorite_movies):

    #print(f"These are the Genres {favorite_movies ['Genre'].split(' ')[1][2][3]}", end='')
    #print(', '.join(g['Genre'] for g in favorite_movies['Genre']), end='.\n')

    
    #step 8 use a function to print a comme-seperated list of movie titles
#def print_title_list(favorite_movies ['Title']):

    #print(f"These are the Movies {favorite_movies ['Title'].split(' ')[1][2][3]}", end='')
    #print(', '.join(t['Title'] for t in favorite_movies['Title']), end'.\n)

# Main function call
main()