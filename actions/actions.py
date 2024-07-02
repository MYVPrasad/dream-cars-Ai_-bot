# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
# import requests
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionGetCarDetails(Action):
#     def name(self) -> Text:
#         return "action_get_car_details"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         make_model = tracker.get_slot("make_model")
#         api_url = f"https://api.api-ninjas.com/v1/cars?model=Mustang&X-Api-Key=kefmhL/pGay7C67rFefnBw==PfZTpNVnyRbSRfxy"
#         api_key = 'kefmhL/pGay7C67rFefnBw==PfZTpNVnyRbSRfxy'  # Replace with your actual API key

#         headers = {
#             'X-Api-Key': api_key
#         }

#         try:
#             response = requests.get(api_url, headers=headers)
#             if response.status_code == 200:
#                 car_details_list = response.json()
#                 if car_details_list and isinstance(car_details_list, list):
#                     car_details = car_details_list[0]  # Get the first item in the list
#                     description = car_details.get('description', 'No description available')
#                     dispatcher.utter_message(f"Here are the details for {make_model}: {description}")
#                 else:
#                     dispatcher.utter_message(f"I'm sorry, I couldn't find details for {make_model}.")
#             else:
#                 dispatcher.utter_message(f"I'm sorry, I couldn't find details for {make_model}.")
#         except Exception as e:
#             dispatcher.utter_message(f"An error occurred while fetching details: {str(e)}")

#         return []



import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict

class ActionGetCarInfo(Action):

    def name(self) -> Text:
        return "action_model_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract the car make and model from the user's message
        car_model = tracker.get_slot("model")

        api_url = 'https://api.api-ninjas.com/v1/cars?model={}'.format(car_model)
        response = requests.get(api_url, headers={'X-Api-Key': ''})
        if response.status_code == requests.codes.ok:
            car_info = response.json()
            if car_info: 
                car_details = car_info[0]
                make = car_details.get("make")
                model = car_details.get("model")
                year = car_details.get("year")
                cylinders = car_details.get("cylinders")
                fuel_type = car_details.get("fuel_type") 
                highway_mpg = car_details.get("highway_mpg")                   

                dispatcher.utter_message(text=f"your searched car details are car:{make}  and the model is {model} it is manufactered in the year {year}.With the number of cylinders: {cylinders} it runs with the fuel type of: {fuel_type} and its milage on highways is  {highway_mpg} mpg")
            else:
                message = "I'm sorry, I couldn't find any information on that car."
        else:
            message = "There was an error fetching the car information. Please try again later."
        return []