from flask import Flask, render_template, abort

app = Flask(__name__)

# Our dictionary containing the detailed stories for Morogoro destinations
DESTINATIONS = {
    'mikumi': {
        'title': 'Mikumi National Park',
        'subtitle': 'The Serengeti of the South',
        'image': 'https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?q=80&w=1200',
        'story': 'Bordered by the Uluguru Mountains, Mikumi is Tanzania’s fourth-largest national park. Known for its wide-open floodplains, it offers incredible opportunities to see lions stalking their prey, herds of elephants wandering near the baobab trees, and giraffes feeding in the acacia woodlands right off the main highway.'
    },
    'uluguru': {
        'title': 'Uluguru Mountains',
        'subtitle': 'The Sky Island of Morogoro',
        'image': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1200',
        'story': 'Rising majestically above Morogoro town, the Uluguru Mountains are part of the ancient Eastern Arc Chain. The mountains are wrapped in pristine rainforests home to unique bird species found nowhere else on earth. Hiking up through the morning mist offers breathtaking views of the valleys below and an authentic encounter with the local Waluguru culture.'
    },
    'choma': {
        'title': 'Choma Waterfalls',
        'subtitle': 'A Refreshing Mountain Hideaway',
        'image': 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=1200',
        'story': 'Located high up in the slopes of the Uluguru range, Choma Waterfalls is a favorite trekking spot. The trail takes you through traditional villages where you can see local life firsthand. Once you reach the falls, you are rewarded with cold, crystal-clear mountain water cascading down natural rock steps—the perfect spot to rest and swim after a long hike.'
    }
}

@app.route('/')
def home():
    return render_template('index.html')

# Dynamic route that changes based on what the user clicks
@app.route('/story/<place_name>')
def view_story(place_name):
    # Check if the requested destination exists in our dictionary
    if place_name in DESTINATIONS:
        place_data = DESTINATIONS[place_name]
        return render_template('story.html', destination=place_data)
    else:
        abort(404) # Show an error page if it doesn't exist

if __name__ == '__main__':
    app.run(debug=True)
