# data.py
#
# Enter the category and question data here

# ----------------
#    Single Jep
# ----------------
SJ_CATEGORY_1 = ""
SJ_C1_Q1 = ""
SJ_C1_A1 = ""
SJ_C1_Q2 = ""
SJ_C1_A2 = ""
SJ_C1_Q3 = ""
SJ_C1_A3 = ""
SJ_C1_Q4 = ""
SJ_C1_A4 = ""
SJ_C1_Q5 = ""
SJ_C1_A5 = ""

SJ_CATEGORY_2 = ""
SJ_C2_Q1 = ""
SJ_C2_A1 = ""
SJ_C2_Q2 = ""
SJ_C2_A2 = ""
SJ_C2_Q3 = ""
SJ_C2_A3 = ""
SJ_C2_Q4 = ""
SJ_C2_A4 = ""
SJ_C2_Q5 = ""
SJ_C2_A5 = ""

SJ_CATEGORY_3 = ""
SJ_C3_Q1 = ""
SJ_C3_A1 = ""
SJ_C3_Q2 = ""
SJ_C3_A2 = ""
SJ_C3_Q3 = ""
SJ_C3_A3 = ""
SJ_C3_Q4 = ""
SJ_C3_A4 = ""
SJ_C3_Q5 = ""
SJ_C3_A5 = ""

SJ_CATEGORY_4 = ""
SJ_C4_Q1 = ""
SJ_C4_A1 = ""
SJ_C4_Q2 = ""
SJ_C4_A2 = ""
SJ_C4_Q3 = ""
SJ_C4_A3 = ""
SJ_C4_Q4 = ""
SJ_C4_A4 = ""
SJ_C4_Q5 = ""
SJ_C4_A5 = ""

SJ_CATEGORY_5 = ""
SJ_C5_Q1 = ""
SJ_C5_A1 = ""
SJ_C5_Q2 = ""
SJ_C5_A2 = ""
SJ_C5_Q3 = ""
SJ_C5_A3 = ""
SJ_C5_Q4 = ""
SJ_C5_A4 = ""
SJ_C5_Q5 = ""
SJ_C5_A5 = ""

SJ_CATEGORY_6 = ""
SJ_C6_Q1 = ""
SJ_C6_A1 = ""
SJ_C6_Q2 = ""
SJ_C6_A2 = ""
SJ_C6_Q3 = ""
SJ_C6_A3 = ""
SJ_C6_Q4 = ""
SJ_C6_A4 = ""
SJ_C6_Q5 = ""
SJ_C6_A5 = ""

# ----------------
#    Double Jep
# ----------------
DJ_CATEGORY_1 = ""
DJ_C1_Q1 = ""
DJ_C1_A1 = ""
DJ_C1_Q2 = ""
DJ_C1_A2 = ""
DJ_C1_Q3 = ""
DJ_C1_A3 = ""
DJ_C1_Q4 = ""
DJ_C1_A4 = ""
DJ_C1_Q5 = ""
DJ_C1_A5 = ""

DJ_CATEGORY_2 = ""
DJ_C2_Q1 = ""
DJ_C2_A1 = ""
DJ_C2_Q2 = ""
DJ_C2_A2 = ""
DJ_C2_Q3 = ""
DJ_C2_A3 = ""
DJ_C2_Q4 = ""
DJ_C2_A4 = ""
DJ_C2_Q5 = ""
DJ_C2_A5 = ""

DJ_CATEGORY_3 = ""
DJ_C3_Q1 = ""
DJ_C3_A1 = ""
DJ_C3_Q2 = ""
DJ_C3_A2 = ""
DJ_C3_Q3 = ""
DJ_C3_A3 = ""
DJ_C3_Q4 = ""
DJ_C3_A4 = ""
DJ_C3_Q5 = ""
DJ_C3_A5 = ""

DJ_CATEGORY_4 = ""
DJ_C4_Q1 = ""
DJ_C4_A1 = ""
DJ_C4_Q2 = ""
DJ_C4_A2 = ""
DJ_C4_Q3 = ""
DJ_C4_A3 = ""
DJ_C4_Q4 = ""
DJ_C4_A4 = ""
DJ_C4_Q5 = ""
DJ_C4_A5 = ""

DJ_CATEGORY_5 = ""
DJ_C5_Q1 = ""
DJ_C5_A1 = ""
DJ_C5_Q2 = ""
DJ_C5_A2 = ""
DJ_C5_Q3 = ""
DJ_C5_A3 = ""
DJ_C5_Q4 = ""
DJ_C5_A4 = ""
DJ_C5_Q5 = ""
DJ_C5_A5 = ""

DJ_CATEGORY_6 = ""
DJ_C6_Q1 = ""
DJ_C6_A1 = ""
DJ_C6_Q2 = ""
DJ_C6_A2 = ""
DJ_C6_Q3 = ""
DJ_C6_A3 = ""
DJ_C6_Q4 = ""
DJ_C6_A4 = ""
DJ_C6_Q5 = ""
DJ_C6_A5 = ""

# ---------------
#    Final Jep
# ---------------
FJ_CATEGORY = ""
FJQ = ""
FJA = ""

class GameData:
    def __init__(self):
        self.create_ds()

    def create_ds(self):
        self.data = \
        {
        1: 
            {
            'categories': 
            [
                SJ_CATEGORY_1,
                SJ_CATEGORY_2,
                SJ_CATEGORY_3,
                SJ_CATEGORY_4,
                SJ_CATEGORY_5,
                SJ_CATEGORY_6
            ],
            'questions':
            [
                [SJ_C1_Q1, SJ_C2_Q1, SJ_C3_Q1, SJ_C4_Q1, SJ_C5_Q1, SJ_C6_Q1],
                [SJ_C1_Q2, SJ_C2_Q2, SJ_C3_Q2, SJ_C4_Q2, SJ_C5_Q2, SJ_C6_Q2],
                [SJ_C1_Q3, SJ_C2_Q3, SJ_C3_Q3, SJ_C4_Q3, SJ_C5_Q3, SJ_C6_Q3],
                [SJ_C1_Q4, SJ_C2_Q4, SJ_C3_Q4, SJ_C4_Q4, SJ_C5_Q4, SJ_C6_Q4],
                [SJ_C1_Q5, SJ_C2_Q5, SJ_C3_Q5, SJ_C4_Q5, SJ_C5_Q5, SJ_C6_Q5]
            ],
            'answers':
            [
                [SJ_C1_A1, SJ_C2_A1, SJ_C3_A1, SJ_C4_A1, SJ_C5_A1, SJ_C6_A1],
                [SJ_C1_A2, SJ_C2_A2, SJ_C3_A2, SJ_C4_A2, SJ_C5_A2, SJ_C6_A2],
                [SJ_C1_A3, SJ_C2_A3, SJ_C3_A3, SJ_C4_A3, SJ_C5_A3, SJ_C6_A3],
                [SJ_C1_A4, SJ_C2_A4, SJ_C3_A4, SJ_C4_A4, SJ_C5_A4, SJ_C6_A4],
                [SJ_C1_A5, SJ_C2_A5, SJ_C3_A5, SJ_C4_A5, SJ_C5_A5, SJ_C6_A5]
            ]
            },
        2:
            {
            'categories': 
            [
                DJ_CATEGORY_1,
                DJ_CATEGORY_2,
                DJ_CATEGORY_3,
                DJ_CATEGORY_4,
                DJ_CATEGORY_5,
                DJ_CATEGORY_6
            ],
            'questions':
            [
                [DJ_C1_Q1, DJ_C2_Q1, DJ_C3_Q1, DJ_C4_Q1, DJ_C5_Q1, DJ_C6_Q1],
                [DJ_C1_Q2, DJ_C2_Q2, DJ_C3_Q2, DJ_C4_Q2, DJ_C5_Q2, DJ_C6_Q2],
                [DJ_C1_Q3, DJ_C2_Q3, DJ_C3_Q3, DJ_C4_Q3, DJ_C5_Q3, DJ_C6_Q3],
                [DJ_C1_Q4, DJ_C2_Q4, DJ_C3_Q4, DJ_C4_Q4, DJ_C5_Q4, DJ_C6_Q4],
                [DJ_C1_Q5, DJ_C2_Q5, DJ_C3_Q5, DJ_C4_Q5, DJ_C5_Q5, DJ_C6_Q5]
            ],
            'answers':
            [
                [DJ_C1_A1, DJ_C2_A1, DJ_C3_A1, DJ_C4_A1, DJ_C5_A1, DJ_C6_A1],
                [DJ_C1_A2, DJ_C2_A2, DJ_C3_A2, DJ_C4_A2, DJ_C5_A2, DJ_C6_A2],
                [DJ_C1_A3, DJ_C2_A3, DJ_C3_A3, DJ_C4_A3, DJ_C5_A3, DJ_C6_A3],
                [DJ_C1_A4, DJ_C2_A4, DJ_C3_A4, DJ_C4_A4, DJ_C5_A4, DJ_C6_A4],
                [DJ_C1_A5, DJ_C2_A5, DJ_C3_A5, DJ_C4_A5, DJ_C5_A5, DJ_C6_A5]
            ]
            },
        3:
            {
            'categories': [FJ_CATEGORY],
            'questions': [[FJQ]],
            'answers': [[FJA]]
            }
        }

    def get_cats_for_round(self, r):
        return self.data[r]['categories']

    def get_questions_for_round(self, r):
        return self.data[r]['questions']

    def get_answers_for_round(self, r):
        return self.data[r]['answers']
