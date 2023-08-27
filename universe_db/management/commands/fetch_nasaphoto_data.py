import requests  # Library for sending HTTP requests
from django.core.management.base import BaseCommand  # Django's base class for writing management commands
from ...models import NASAPhoto  # Import the RoverPhoto model from your app

# Base API URL
BASE_API_URL = 'https://api.nasa.gov/planetary/apod'

# Custom management command
class Command(BaseCommand):
    # Description of the command
    help = 'Fetches NASA photos of the day data from the NASA API and saves it into our database'

    # This method is run when the command is executed
    def handle(self, *args, **options):
        # Parameters for the API request
        api_key = 'l7blC9pAfLvEwmlTQWyi0K7m7DWkN7FTz9HYzgWG'
        count = 10  # number of images to fetch

        # Sends a GET request to the API
        response = requests.get(BASE_API_URL, params={'api_key': api_key, 'count': count})

        # Tries to decode the response to JSON
        try:
            print(response.content)
            data = response.json()
        except Exception as e:
            # Prints an error message if it can't decode the JSON
            self.stdout.write(self.style.ERROR(f'Error decoding JSON: {e}'))
            return

        # If the request was successful
        if response.status_code == 200:
            # Iterates over each photo in the response
            for photo_data in data:
                # Checks if the photo already exists in the database
                existing_photo = NASAPhoto.objects.filter(date=photo_data['date']).first()
                if not existing_photo:
                    # Creates and saves a new NASAPhoto with the data from the API
                    NASAPhoto.objects.create(
                        date=photo_data['date'],
                        img_src=photo_data['url'],
                        thumb=photo_data.get('thumbnail_url', ''),  # Use empty string if 'thumbnail_url' not present
                        api_key=api_key,
                    )
            # Print a success message
            self.stdout.write(self.style.SUCCESS(f"Added {len(data)} photos to the database."))
        else:
            # If the request was not successful, print an error message
            self.stdout.write(self.style.ERROR('API request failed.'))


