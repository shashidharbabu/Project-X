import os, requests
import json

class Maps:

    def google_maps_query(location, specialties):
        """
        Formulates a search query suitable for the Google Maps API based on user input.

        Args:
            location (str): User-provided location (city, state, zip code, etc.).
            specializations (str): Comma-separated list of therapy specializations.

        Returns:
            str: A well-formatted Google Maps API search query string.
        """

        # Address potential limitations:
        # - Consider using a location verification API to ensure accuracy (optional).
        # - Handle cases where specializations might not be directly translatable
        #   to Google Maps API categories (e.g., using synonyms or broader terms).

        # Craft a user-friendly search phrase:
        search_phrase = f"Find {specialties} therapists in {location}"

        # Adapt for Google Maps API (replace with actual API terms if known):
        api_query = search_phrase.replace("therapists", "clinics")

        # Consider additional refinements based on Google Maps API documentation:
        # - https://developers.google.com/maps/documentation/places/web-service/search
        # - Specific categories for therapy services (if applicable)
        # - Location formatting requirements (e.g., zip code vs. city, state)
        
        
        return Maps.google_maps_search(api_query)

    def google_maps_search(api_query):
        # api_query = Maps.google_maps_query()
        
        maps_api_key = os.getenv("GOOGLE_MAPS_API")
        if not maps_api_key:
            print("Error: Missing Google Maps API key. Please set the GOOGLE_MAPS_API environment variable.")
            return None
        
        
        maps_url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={api_query}&key={maps_api_key}"
        if not maps_url:
            print("Error: Missing google maps API URL. Please check the Google Maps API")
            return None
        
        try:
            response = requests.get(maps_url)
            # print(response.json())
            response.raise_for_status()  # Raise an exception for non-200 status codes
        except requests.exceptions.RequestException as e:
            print(f"Error: An error occurred during the request: {e}")
            return None

        try:
            data = response.json()  # Parse JSON response
            return data
        except json.JSONDecodeError as e:
            print(f"Error: Failed to decode JSON response: {e}")
            return None


"""

GOOGLE MAP API RESPONSE USABLE KEP PAIR VALUES

name: name of the place
formatted_address: text address
location: coordinates if required for map API.
'opening_hours': {'open_now': False}
rating: average rating received by the clinic from customers
user_ratings_total: number of rating received by this clinic.



        """





### TESTING #################################################################

# #Example usage 
# api_query = "clinics for anxiety in San Francisco, CA"  # Replace with your query
# results = Maps.google_maps_search(api_query)

# if results:
#   # Process search results (e.g., print details, display on a map)
#   print("Search Results:")
#   for result in results["results"]:
#     print(f"- {result['name']}")  # Print place name (example)
#     # Access other data from the 'results' dictionary as needed
# else:
#   print("No results found.")

#############################################################################
                
        
        
        
        
        
        
        
        
        
    
