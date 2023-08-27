import requests  # Library for sending HTTP requests
from django.core.management.base import BaseCommand  # Django's base class for writing management commands
from ...models import RoverPhoto  # Import the RoverPhoto model from your app

# Base API URL
BASE_API_URL = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

# Custom management command
class Command(BaseCommand):

    # Description of the command
    help = 'Fetches Mars Rover photos data from the NASA API and saves it into our database'


    # This method is run when the command is executed
    def handle(self, *args, **options):
        # Parameters for the API request
        params = {
            "sol": "1000",
            "api_key": "l7blC9pAfLvEwmlTQWyi0K7m7DWkN7FTz9HYzgWG"
        }

        # Sends a GET request to the API
        response = requests.get(BASE_API_URL, params=params)

        # Tries to decode the response to JSON
        try:
            data = response.json()
        except Exception as e:
            # Prints an error message if it can't decode the JSON
            self.stdout.write(self.style.ERROR(f'Error decoding JSON: {e}'))
            return


        # If the request was successful
        if response.status_code == 200:
            # Iterates over each photo in the response
            for photo_data in data['photos']:
                # Checks if the photo already exists in the database
                existing_photo = RoverPhoto.objects.filter(id=photo_data['id']).first()
                if existing_photo:
                    # Skips the photo if it already exists
                    continue

                # Creates and saves a new RoverPhoto with the data from the API
                RoverPhoto.objects.create(
                    id=photo_data['id'],
                    sol=photo_data['sol'],
                    camera=photo_data['camera']['name'],
                    img_src=photo_data['img_src'],
                    earth_date=photo_data['earth_date'],
                    rover=photo_data['rover']['name'],
                )

            # Print a success message
            self.stdout.write(self.style.SUCCESS(f"Added {len(data['photos'])} photos to the database."))
        else:
            # If the request was not successful, print an error message
            self.stdout.write(self.style.ERROR('API request failed.'))
