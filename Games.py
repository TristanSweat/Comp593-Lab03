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
    print(favorite_movies['Title'])
    print(favorite_movies['Genre'])
    #Step 3 Adding Movie to Data Structure

    #def add_movies_to_movies(Title, Genre): - Not Finished

    #Step 4 Add Movie characteristics to Data structure

    #Step 5 Function to print bullet points of games - Not finished
def print_video_games(video_games):
    print('These are my 3 favorite games', video_games)

# Main function call
main()