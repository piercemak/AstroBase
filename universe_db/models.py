from django.db import models

# A model contains the essential fields and behaviors of the data you’re storing.
# Each model maps to a single database table.



#------------------------------------------------------------------------------------------------------------------------------
# Unit Model: Contains the name and abbreviation of the unit used for measurements
class Unit(models.Model):
    name = models.CharField(max_length=50)  # name of unit
    abbreviation = models.CharField(max_length=10)  # abbreviation of unit


    # Return a string representation of the Unit model, which is the name of the unit
    def __str__(self):
        return self.name


#------------------------------------------------------------------------------------------------------------------------------
# UnitMixin Model: A model to be inherited by other models that will use common unit fields for measurements
class UnitMixin(models.Model):


    value = models.FloatField(null=True)  # common measurement value

    # Foreign key field used to reference the Unit model. If a referenced Unit model is deleted, it will not allow the deletion (models.PROTECT)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)


    # Abstract base classes are base classes that only exist for the purpose of being inherited.
    class Meta:
        abstract = True


#------------------------------------------------------------------------------------------------------------------------------
# SolarSystemPlanets Model: Contains the name of the planet in the solar system
class SolarSystemPlanets(models.Model):

    name = models.CharField(max_length=100)  # name of planet

     # Controls how the model is named
    class Meta:
        verbose_name = "Solar System Planets"
        verbose_name_plural = "Solar System Planets"


    # Return a string representation of the SolarSystemPlanets model, which is the name of the planet
    def __str__(self):
        return self.name


#------------------------------------------------------------------------------------------------------------------------------
# SSPMeasurement Model: Contains measurements for solar system planets
# Inherits 'UnitMixin' to reuse common unit fields
class SSPMeasurement(UnitMixin):



    MEASUREMENT_TYPES = [('MASS', 'Mass'), ('DENSITY', 'Density'),
                     ('DIAMETER', 'Diameter'), ('GRAVITY', 'Surface Gravity'), ('ESCAPE_VELOCITY', 'Escape Velocity'),
                     ('DISTANCE', 'Distance'), ('PERIHELION', 'Perihelion'),
                     ('APHELION', 'Aphelion'), ('ORBITAL_PERIOD', 'Orbit Period'),
                     ('ROTATIONAL_PERIOD', 'Rotational Period'), ('ORBITAL_INCLINATION', 'Orbital Inclination'),
                     ('ECCENTRICITY', 'Eccentricity'), ('MEAN_TEMP', 'Mean Temperature'),
                     ('SURFACE_PRESSURE', 'Surface Pressure'), ('NUM_MOONS', 'Number of Moons')
                     ]


    value = models.FloatField(null=True, default=0.0)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    planet = models.ForeignKey(SolarSystemPlanets, on_delete=models.CASCADE)  # 'CASCADE': If a referenced SolarSystemPlanet model is deleted, all related SSPMeasurement objects will also be deleted



    measurement_type = models.CharField(max_length=100, choices=MEASUREMENT_TYPES)  #Character field used to store the type of measurement


    class Meta:
        verbose_name = "Solar System Planet Measurement"
        verbose_name_plural = "Solar System Planet Measurements"


    # Return a string representation of the SSPMeasurement model, displaying the measurement type, planet name, measurement value, and unit abbreviation
    def __str__(self):
        return f"{self.get_measurement_type_display()} of {self.planet.name} is {self.value} {self.unit.abbreviation}"

'''
 In summary, the planet field in the SSPMeasurement model is a foreign key that 
 establishes a relationship with the SolarSystemPlanets model, allowing each measurement to 
 be associated with a specific planet.
'''


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#EXOPLANETS (Planetary Systems Composite Parameters)
# PlanetarySystems Model: Contains data for exoplanets and their planetary systems



class PlanetarySystems(models.Model):
    name = models.CharField(max_length=100)  # name of the exoplanet
    hostname = models.CharField(max_length=100)  # name of the host star
    number_of_stars = models.IntegerField()  # number of stars in the system
    number_of_planets = models.IntegerField()  # number of planets in the system
    discovery_method = models.CharField(max_length=100)  # method of discovery
    discovery_year = models.IntegerField()  # year of discovery
    discovery_facility = models.CharField(max_length=100)  # discovery facility
    orbit_period = models.FloatField(null=True)  # orbital period
    radius = models.FloatField(null=True)  # radius of the exoplanet
    mass = models.FloatField(null=True)  # mass of the exoplanet
    equilibrium_temperature = models.FloatField(null=True)  # equilibrium temperature of the exoplanet
    spectral_type = models.CharField(max_length=50, null=True)  # spectral type of the star
    stellar_effective_temp = models.FloatField(null=True)  # stellar effective temperature
    stellar_mass = models.FloatField(null=True)  # stellar mass
    stellar_metallicity = models.FloatField(null=True)  # stellar metallicity
    stellar_metallicity_ratio = models.CharField(max_length=50, null=True)  # stellar metallicity ratio
    stellar_surface_gravity = models.FloatField(null=True)  # stellar surface gravity
    ra = models.FloatField(null=True)  # right ascension
    dec = models.FloatField(null=True)  # declination
    distance = models.FloatField(null=True)  # distance from Earth
    eccentricity = models.FloatField(null=True)  # eccentricity of the orbit
    stellar_radius = models.FloatField(null=True)  # Stellar radius
    semimajor_axis = models.FloatField(null=True)   #Semi-major Axis
    impact_parameter = models.FloatField(null=True)     #Impact Parameter


    # A list of field names which, when taken together, must be unique
    class Meta:
        verbose_name = "Planetary System"
        verbose_name_plural = "Planetary Systems"
        unique_together = ['name', 'hostname', 'discovery_year']


    # Return a string representation of the PlanetarySystems model, which is the name of the exoplanet
    def __str__(self):
        return self.name






#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# RoverPhoto Model: Contains the data for each Mars Rover Photo
class RoverPhoto(models.Model):
    id = models.IntegerField(primary_key=True)  # ID of the photo
    sol = models.IntegerField()  # Martian sol number
    camera = models.CharField(max_length=50)  # Name of the camera
    img_src = models.URLField()  # URL of the photo
    earth_date = models.DateField()  # Date on Earth when the photo was taken
    rover = models.CharField(max_length=50)  # Name of the rover

    def __str__(self):
        return f"Photo ID: {self.id}, Taken by {self.rover}'s {self.camera} camera on {self.earth_date}"



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# NASA Photo of the Day Model: Contains the data for each Photo otd
class NASAPhoto(models.Model):
    date = models.DateField()  # The date of the APOD image to retrieve (YYYY-MM-DD)
    img_src = models.URLField()  # URL of the photo
    thumb = models.URLField()  # URL of the video thumbnail
    api_key = models.CharField(max_length=100)  # api.nasa.gov key for expanded usage

    def __str__(self):
        return f"Photo Date: {self.date}, Image URL: {self.img_src}, Video Thumbnail URL: {self.thumb}"





