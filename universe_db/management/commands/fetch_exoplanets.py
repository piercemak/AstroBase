import requests  # Importing the requests library for sending HTTP requests to the API
from django.core.management.base import BaseCommand  # Django's base class for writing management commands
from ...models import PlanetarySystems  # Import the Exoplanet model from your app

# Defining the base URL of the API
BASE_API_URL = 'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?'


# Defining the custom management command
class Command(BaseCommand):

    # Brief description of what the command does
    help = 'Fetches exoplanets data from the NASA Exoplanet Archive and saves it into our database'


    # The handle method is what's executed when the command is run
    def handle(self, *args, **options):
        # The fields we are interested in
        fields = [
            'pl_name',
            'hostname',
            'sy_snum',
            'sy_pnum',
            'discoverymethod',
            'disc_year',
            'disc_facility',
            'pl_orbper',
            'pl_radj',
            'pl_bmassj',
            'pl_eqt',
            'st_spectype',
            'st_teff',
            'st_mass',
            'st_met',
            'st_metratio',
            'st_logg',
            'ra',
            'dec',
            'sy_dist',
            'pl_orbeccen',
            'st_rad',
            'pl_orbsmax',
            'pl_imppar',



        ]
        # Join the fields with commas
        query_string = ','.join(fields)

        # Construct the URL for the API request
        url = f'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+{query_string}+from+pscomppars&format=json'

        # Sends a GET request to the API
        response = requests.get(url)
        print(f"{response.status_code}")  # Print the HTTP status code

        # Print the response text
        print('Response text:')
        print(response.text)


        # Try to convert the response to JSON
        try:
            data = response.json()
        except Exception as e:
            print('Error decoding JSON:')
            print(e)
            return


        # If the request was successful
        if response.status_code == 200:
            # Iterate over each planet in the data
            for planet_data in data:
                name = planet_data.get('pl_name', '')
                hostname = planet_data.get('hostname', '')
                discovery_year = planet_data.get('disc_year', 0)

                # Check if the planet already exists in the database
                existing_planet = PlanetarySystems.objects.filter(name=name, hostname=hostname, discovery_year=discovery_year).first()
                if existing_planet:
                    continue  # Skip saving the planet if it already exists


                # Creates a new Exoplanet object with the data
                planet = PlanetarySystems(
                    name=planet_data.get('pl_name', ''),
                    hostname=planet_data.get('hostname', ''),
                    number_of_stars=planet_data.get('sy_snum', 0),
                    number_of_planets=planet_data.get('sy_pnum', 0),
                    discovery_method=planet_data.get('discoverymethod', ''),
                    discovery_year=planet_data.get('disc_year', 0),
                    discovery_facility=planet_data.get('disc_facility', ''),
                    orbit_period=planet_data.get('pl_orbper', 0.0),
                    radius=planet_data.get('pl_radj', 0.0),
                    mass=planet_data.get('pl_bmassj', 0.0),
                    equilibrium_temperature=planet_data.get('pl_eqt', 0.0),
                    spectral_type=planet_data.get('st_spectype', ''),
                    stellar_effective_temp=planet_data.get('st_teff', 0.0),
                    stellar_mass=planet_data.get('st_mass', 0.0),
                    stellar_metallicity=planet_data.get('st_met', 0.0),
                    stellar_metallicity_ratio=planet_data.get('st_metratio', ''),
                    stellar_surface_gravity=planet_data.get('st_logg', 0.0),
                    ra=planet_data.get('ra', 0.0),
                    dec=planet_data.get('dec', 0.0),
                    distance=planet_data.get('sy_dist', 0.0),
                    eccentricity=planet_data.get('pl_orbeccen', 0.0),
                    stellar_radius=planet_data.get('st_rad', 0.0),
                    semimajor_axis=planet_data.get('pl_orbsmax', 0.0),
                    impact_parameter=planet_data.get('pl_imppar', 0.0)

                )
                planet.save()  # Save the new Exoplanet to the database
        else:
            # If the request was not successful, print an error message
            self.stdout.write(self.style.ERROR('API request failed.'))
