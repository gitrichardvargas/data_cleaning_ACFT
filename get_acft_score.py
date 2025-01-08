
import os
base_dir = os.path.dirname(__file__)  # For scripts
json_path = os.path.join(base_dir, 'data.json')
import pandas as pd 
import json 
# one global variable is the json file... doesn't make sense to reload it for each instance of the class
with open('data.json', 'r') as f:
    ACFT_DATA = json.load(f)


class SoldierScoreACFT:
    def __init__(self, rank, last_name, first_name, age, gender, dl, spt, hrp, sdc, plk, cardio, alt_cardio=None):
        """
        Initializes a Soldier's ACFT score object.
        """
        # error handling 
        if not isinstance(rank, str):
            raise ValueError("Rank must be a string")

        if not isinstance(last_name, str):
            raise ValueError("Last name must be a string")
        
        if not isinstance(first_name, str):
            raise ValueError("First name must be a string")

        if not isinstance(age, int):
            raise ValueError("Age must be an integer")

        if gender not in ['male', 'female']:
            raise ValueError("Invalid gender. Must be 'male' or 'female'")

        if not isinstance(dl, (int, float)):
            raise ValueError("Deadlift must be a number")
 
        if not isinstance(spt, (int, float)):
            raise ValueError("Standing power throw must be a number")

        if not isinstance(hrp, (int, float)):
            raise ValueError("Hand release pushups must be a number")

        if not isinstance(sdc, (int, float)):
            raise ValueError("Sprint drag carry must be a number")

        if not isinstance(plk, (int, float)):
            raise ValueError("Plank must be a number")

        if not isinstance(cardio, (int, float)):
            raise ValueError("Cardio time must be a number")

        valid_alt_cardio = [None, 'swim', 'row', 'bike', 'walk']
        if alt_cardio not in valid_alt_cardio:
            raise ValueError("Invalid alternate cardio option. Must be one of: None, 'swim', 'row', 'bike', or 'walk'")

        # adjusts age to the closest scale
        age_scales = [17, 22, 27, 32, 37, 42, 47, 52, 57, 62]
        if age < age_scales[0]:
            scaled_age = age_scales[0]
        elif age >= age_scales[-1]:
            scaled_age = age_scales[-1]
        else:
            scaled_age = next(scale for scale in reversed(age_scales) if age >= scale)

        valid_alt_cardio = {"walk", "row", "swim", "bike"}
        if alt_cardio and alt_cardio not in valid_alt_cardio:
            raise ValueError(f"Invalid alternate cardio option. Must be one of {valid_alt_cardio}.")

        self.age = str(scaled_age)  # string to match JSON data
        self.rank = rank
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.dl = dl
        self.spt = spt
        self.hrp = hrp
        self.sdc = sdc
        self.plk = plk
        self.cardio = cardio
        self.alt_cardio = alt_cardio  # Store the alternate cardio option

    def get_ACFT_event_score(self, raw, gender, age, event, increasing=True): 
        correct_age_gender_scale = ACFT_DATA[gender][age][event]  # subsets the json file of all scores 

        for d in correct_age_gender_scale:
            if (increasing and d['raw'] <= raw) or (not increasing and d['raw'] >= raw):
                pts = d['points']
        return pts
    
    def get_individual_scores(self):
        # constant events
        events = {
            "deadlift": (self.dl, True),
            "standing power throw": (self.spt, True),
            "hand release pushups": (self.hrp, True),
            "sprint drag carry": (self.sdc, False),
            "plank": (self.plk, True),
        }

        scores = {}
        for event, (raw, increasing) in events.items():
            scores[event] = self.get_ACFT_event_score(raw, self.gender, self.age, event, increasing)

        # cardio event conditioned on injury
        cardio_event = self.alt_cardio if self.alt_cardio else "two mile run"
        scores[cardio_event] = self.get_ACFT_event_score(self.cardio, self.gender, self.age, cardio_event, False)

        return scores

    def get_total_score(self):
        return sum(self.get_individual_scores().values())
    

# sub class that makes more sense to use to simply calculate an individual score vs unit's data
class SoldierSimpleACFT(SoldierScoreACFT):
    def __init__(self, age, gender, dl, spt, hrp, sdc, plk, cardio):
        super().__init__(age, gender, dl, spt, hrp, sdc, plk, cardio)

# example with my ACFT score 
# lt_vargas = SoldierScoreACFT('2LT', 'Vargas', 'Richard', 30, 'male', 280, 9.4, 47, 131, 300, 1343,)
# print(lt_vargas.get_total_score())
# print(lt_vargas.get_individual_scores())
