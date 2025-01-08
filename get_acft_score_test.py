import unittest
from SoldierScoreACFT import SoldierScoreACFT 

class TestSoldierScoreACFT(unittest.TestCase):

    def setUp(self):
        """
        This method sets up any objects or resources that will be shared across tests.
        It's run before each test method.
        """
        # example object to use in multiple tests
        # my actual scores from my last Army Combat Fitness Test
        
        self.lt_vargas = SoldierScoreACFT(
            rank = '2LT', 
            last_name='Vargas', 
            first_name='Richard', 
            age=30, 
            gender='male', 
            dl=280, # deadlift lbs lifted 
            spt=9.4, # standing power throw distance (meters) ball thrown 
            hrp=47, # reps of hand release pushups 
            sdc=131, # time for sprint drag carry formatted as 1:31 in view
            plk=300, # time plank held 
            cardio=1343, # alt_cardio is None, thus, 13:43 is the two mile run time 
            alt_cardio=None
        )
        
        # alternative cardio for injuried soldiers 
        self.injured_bike = SoldierScoreACFT(
            rank = '2LT', 
            last_name='Vargas', 
            first_name='Richard', 
            age=30, 
            gender='male', 
            dl=280, # deadlift lbs lifted 
            spt=9.4, # standing power throw distance (meters) ball thrown 
            hrp=47, # reps of hand release pushups 
            sdc=131, # time for sprint drag carry formatted as 1:31 in view
            plk=300, # time plank held 
            cardio=2700, # alt_cardio is None, thus, 13:43 is the two mile run time 
            alt_cardio='bike'
        )

        self.injured_swim = SoldierScoreACFT(
            rank = '2LT', 
            last_name='Vargas', 
            first_name='Richard', 
            age=30, 
            gender='male', 
            dl=280, # deadlift lbs lifted 
            spt=9.4, # standing power throw distance (meters) ball thrown 
            hrp=47, # reps of hand release pushups 
            sdc=131, # time for sprint drag carry formatted as 1:31 in view
            plk=300, # time plank held 
            cardio=2700, # alt_cardio is None, thus, 13:43 is the two mile run time 
            alt_cardio='swim'
        )

        self.injured_row = SoldierScoreACFT(
            rank = '2LT', 
            last_name='Vargas', 
            first_name='Richard', 
            age=30, 
            gender='male', 
            dl=280, # deadlift lbs lifted 
            spt=9.4, # standing power throw distance (meters) ball thrown 
            hrp=47, # reps of hand release pushups 
            sdc=131, # time for sprint drag carry formatted as 1:31 in view
            plk=300, # time plank held 
            cardio=2700, # alt_cardio is None, thus, 13:43 is the two mile run time 
            alt_cardio='row'
        )

        self.injured_walk = SoldierScoreACFT(
            rank = '2LT', 
            last_name='Vargas', 
            first_name='Richard', 
            age=30, 
            gender='male', 
            dl=280, # deadlift lbs lifted 
            spt=9.4, # standing power throw distance (meters) ball thrown 
            hrp=47, # reps of hand release pushups 
            sdc=131, # time for sprint drag carry formatted as 1:31 in view
            plk=300, # time plank held 
            cardio=2700, # alt_cardio is None, thus, 13:43 is the two mile run time 
            alt_cardio='walk'
        )
        # for both females and males: 
        self.sgt_jane_doe_23 = SoldierScoreACFT('SGT', 'Doe', 'Jane', 23, 'female', 180, 10, 50, 155, 320, 1600, ) 
        # age 70 works (beyond 62, the max age scale)
        self.senior_female = SoldierScoreACFT('COL', 'Doe', 'Jane', 70, 'female', 150, 8, 30, 200, 200, 1700, )
        self.senior_male = SoldierScoreACFT('COL', 'Doe', 'John', 70, 'male', 150, 8, 30, 200, 200, 1700, )
        # age 16 works (below 17, the min age scale)
        self.young_female = SoldierScoreACFT('PVT', 'Doe', 'Jane', 16, 'female', 150, 8, 30, 200, 200, 1700, )
        self.young_male = SoldierScoreACFT('PVT', 'Doe', 'John', 16, 'male', 150, 8, 30, 200, 200, 1700, )
        # going above max scores works 
        self.stud_female = SoldierScoreACFT('SPC', 'Doe', 'Jane', 25, 'female', 350, 20, 70, 115, 400, 1000, )
        self.stud_male = SoldierScoreACFT('SPC', 'Doe', 'John', 25, 'female', 350, 20, 70, 115, 400, 1000, )
        # scores failing scores work
        self.failing_jane_doe = SoldierScoreACFT('PVT', 'Doe', 'Jane', 20, 'female', 100, 1, 4, 500, 60, 3000, )
        self.failing_john_doe = SoldierScoreACFT('PVT', 'Doe', 'John', 20, 'male', 100, 1, 4, 500, 60, 3000, )




    def test_individual_scores(self):
        """
        Test the method that calculates individual scores.
        """
        # known results from the official ACFT
        expected_scores = {
            'deadlift': 87,
            'standing power throw': 76,
            'hand release pushups': 91,
            'sprint drag carry': 99,
            'plank': 90,
            'two mile run': 99
        }

        expected_scores_bike = {
            'deadlift': 87,
            'standing power throw': 76,
            'hand release pushups': 91,
            'sprint drag carry': 99,
            'plank': 90,
            'bike': 0
        }

        expected_scores_swim = {
            'deadlift': 87,
            'standing power throw': 76,
            'hand release pushups': 91,
            'sprint drag carry': 99,
            'plank': 90,
            'swim': 60
        }

        expected_scores_row = {
            'deadlift': 87,
            'standing power throw': 76,
            'hand release pushups': 91,
            'sprint drag carry': 99,
            'plank': 90,
            'row': 60
        }

        expected_scores_walk = {
            'deadlift': 87,
            'standing power throw': 76,
            'hand release pushups': 91,
            'sprint drag carry': 99,
            'plank': 90,
            'walk': 60
        }

        expected_scores_female = {'deadlift': 91, 'standing power throw': 100, 'hand release pushups': 100, 'sprint drag carry': 100, 'plank': 95, 'two mile run': 97}
        expected_scores_senior_female = {'deadlift': 90, 'standing power throw': 100, 'hand release pushups': 100, 'sprint drag carry': 100, 'plank': 75, 'two mile run': 100}
        expected_scores_senior_male = {'deadlift': 72, 'standing power throw': 90, 'hand release pushups': 92, 'sprint drag carry': 100, 'plank': 75, 'two mile run': 95}
        expected_scores_young_female = {'deadlift': 78, 'standing power throw': 98, 'hand release pushups': 84, 'sprint drag carry': 98, 'plank': 69, 'two mile run': 95}
        expected_scores_young_male = {'deadlift': 61, 'standing power throw': 68, 'hand release pushups': 72, 'sprint drag carry': 73, 'plank': 69, 'two mile run': 79}
        expected_scores_studs = {'deadlift': 100, 'standing power throw': 100, 'hand release pushups': 100, 'sprint drag carry': 100, 'plank': 100, 'two mile run': 100}
        expected_scores_failing_female = {'deadlift': 40, 'standing power throw': 0, 'hand release pushups': 0, 'sprint drag carry': 0, 'plank': 0, 'two mile run': 0}
        expected_scores_failing_male = {'deadlift': 20, 'standing power throw': 0, 'hand release pushups': 0, 'sprint drag carry': 0, 'plank': 0, 'two mile run': 0}

        self.assertAlmostEqual(self.lt_vargas.get_individual_scores(), expected_scores)
        self.assertAlmostEqual(self.injured_bike.get_individual_scores(), expected_scores_bike)
        self.assertAlmostEqual(self.injured_swim.get_individual_scores(), expected_scores_swim)
        self.assertAlmostEqual(self.injured_row.get_individual_scores(), expected_scores_row)
        self.assertAlmostEqual(self.injured_walk.get_individual_scores(), expected_scores_walk)
        self.assertAlmostEqual(self.sgt_jane_doe_23.get_individual_scores(), expected_scores_female)
        self.assertAlmostEqual(self.senior_female.get_individual_scores(), expected_scores_senior_female)
        self.assertAlmostEqual(self.senior_male.get_individual_scores(), expected_scores_senior_male)
        self.assertAlmostEqual(self.young_female.get_individual_scores(), expected_scores_young_female)
        self.assertAlmostEqual(self.young_male.get_individual_scores(), expected_scores_young_male)
        self.assertAlmostEqual(self.stud_female.get_individual_scores(), expected_scores_studs)
        self.assertAlmostEqual(self.stud_male.get_individual_scores(), expected_scores_studs)
        self.assertAlmostEqual(self.failing_jane_doe.get_individual_scores(), expected_scores_failing_female)
        self.assertAlmostEqual(self.failing_john_doe.get_individual_scores(), expected_scores_failing_male)



    def test_total_score(self):
        """
        Test the method that calculates the total score.
        """
        expected_total = 542  # total score based on the individual scores
        self.assertEqual(self.lt_vargas.get_total_score(), expected_total)
        # pass/faile 60 pts or 0, simply subtracting the difference from 99 to get 0 or 60
        self.assertEqual(self.injured_bike.get_total_score(), expected_total-99)
        self.assertEqual(self.injured_swim.get_total_score(), expected_total-39) 
        self.assertEqual(self.injured_row.get_total_score(), expected_total-39)
        self.assertEqual(self.injured_walk.get_total_score(), expected_total-39)
        # ... not bothering with the other conditions as this method relies on the previous one 



    def test_invalid_values(self):
        # invalid rank
        with self.assertRaises(ValueError) as context:
            SoldierScoreACFT(
                rank=123,  # Invalid rank type
                last_name='Vargas', 
                first_name='Richard', 
                age=30, 
                gender='male', 
                dl=280, 
                spt=9.4, 
                hrp=47, 
                sdc=131, 
                plk=300, 
                cardio=1343
            )
        self.assertIn("Rank must be a string", str(context.exception))

        # invalid last_name
        with self.assertRaises(ValueError) as context:
            SoldierScoreACFT(
                rank='2LT', 
                last_name=123,  # invalid last_name type
                first_name='Richard', 
                age=30, 
                gender='male', 
                dl=280, 
                spt=9.4, 
                hrp=47, 
                sdc=131, 
                plk=300, 
                cardio=1343
            )
        self.assertIn("Last name must be a string", str(context.exception))

        # invalid first_name
        with self.assertRaises(ValueError) as context:
            SoldierScoreACFT(
                rank='2LT', 
                last_name='Vargas', 
                first_name=123,  # Invalid first_name type
                age=30, 
                gender='male', 
                dl=280, 
                spt=9.4, 
                hrp=47, 
                sdc=131, 
                plk=300, 
                cardio=1343
            )
        self.assertIn("First name must be a string", str(context.exception))

        # invalid age
        with self.assertRaises(ValueError) as context:
            SoldierScoreACFT(
                rank='2LT', 
                last_name='Vargas', 
                first_name='Richard', 
                age="thirty",  # Invalid age type
                gender='male', 
                dl=280, 
                spt=9.4, 
                hrp=47, 
                sdc=131, 
                plk=300, 
                cardio=1343
            )
        self.assertIn("Age must be an integer", str(context.exception))

        # invalid gender
        with self.assertRaises(ValueError) as context:
            SoldierScoreACFT(
                rank='2LT', 
                last_name='Vargas', 
                first_name='Richard', 
                age=30, 
                gender='Going Merry',  # Invalid gender value
                dl=280, 
                spt=9.4, 
                hrp=47, 
                sdc=131, 
                plk=300, 
                cardio=1343
            )
        self.assertIn("Invalid gender", str(context.exception))

        # invalid deadlift
        with self.assertRaises(ValueError) as context:
            SoldierScoreACFT(
                rank='2LT', 
                last_name='Vargas', 
                first_name='Richard', 
                age=30, 
                gender='male', 
                dl="Two Eighty",  # Invalid dl type
                spt=9.4, 
                hrp=47, 
                sdc=131, 
                plk=300, 
                cardio=1343
            )
        self.assertIn("Deadlift must be a number", str(context.exception))

        # invalid standing power throw
        with self.assertRaises(ValueError) as context:
            SoldierScoreACFT(
                rank='2LT', 
                last_name='Vargas', 
                first_name='Richard', 
                age=30, 
                gender='male', 
                dl=280, 
                spt="Nine Point Four",  # Invalid spt type
                hrp=47, 
                sdc=131, 
                plk=300, 
                cardio=1343
            )
        self.assertIn("Standing power throw must be a number", str(context.exception))

        # invalid hand release pushups
        with self.assertRaises(ValueError) as context:
            SoldierScoreACFT(
                rank='2LT', 
                last_name='Vargas', 
                first_name='Richard', 
                age=30, 
                gender='male', 
                dl=280, 
                spt=9.4, 
                hrp="forty-seven",  # Invalid hrp type
                sdc=131, 
                plk=300, 
                cardio=1343
            )
        self.assertIn("Hand release pushups must be a number", str(context.exception))

        # invalid sprint drag carry
        with self.assertRaises(ValueError) as context:
            SoldierScoreACFT(
                rank='2LT', 
                last_name='Vargas', 
                first_name='Richard', 
                age=30, 
                gender='male', 
                dl=280, 
                spt=9.4, 
                hrp=47, 
                sdc="One Thirty-One",  # Invalid sdc type
                plk=300, 
                cardio=1343
            )
        self.assertIn("Sprint drag carry must be a number", str(context.exception))

        # invalid plank
        with self.assertRaises(ValueError) as context:
            SoldierScoreACFT(
                rank='2LT', 
                last_name='Vargas', 
                first_name='Richard', 
                age=30, 
                gender='male', 
                dl=280, 
                spt=9.4, 
                hrp=47, 
                sdc=131, 
                plk="three hundred",  # Invalid plk type
                cardio=1343
            )
        self.assertIn("Plank must be a number", str(context.exception))

        # invalid cardio
        with self.assertRaises(ValueError) as context:
            SoldierScoreACFT(
                rank='2LT', 
                last_name='Vargas', 
                first_name='Richard', 
                age=30, 
                gender='male', 
                dl=280, 
                spt=9.4, 
                hrp=47, 
                sdc=131, 
                plk=300, 
                cardio="thirteen forty-three"  # Invalid cardio type
            )
        self.assertIn("Cardio time must be a number", str(context.exception))

        # invalid alt_cardio
        with self.assertRaises(ValueError) as context:
            SoldierScoreACFT(
                rank='2LT', 
                last_name='Vargas', 
                first_name='Richard', 
                age=30, 
                gender='male', 
                dl=280, 
                spt=9.4, 
                hrp=47, 
                sdc=131, 
                plk=300, 
                cardio=1343, 
                alt_cardio="Monkey D Luffy"  # Invalid alt_cardio value
            )
        self.assertIn("Invalid alternate cardio option", str(context.exception))
