# -*- coding: utf-8 -*-

import vakioveikkaus

NUMBER_OF_PLAYED_VAKIO_ROWS = 48
NUMBER_OF_PLAYED_MINIVAKIO_ROWS = 0
ROW_PRICE_VAKIO = 0.1
ROW_PRICE_MINIVAKIO = 0.1

# 1=Values are not fixed, >1=Larger probabilities are favored
# about 1.0-2.0
DIFFICULTY_FIX_VAKIO = 1.5
DIFFICULTY_FIX_MINIVAKIO = 1

LOCKED = {1:  '', #'2',
          2:  '', #'2',
          3:  '', #'1',
          4:  '',
          5:  '',
          6:  '',
          7:  '',
          8:  '',
          9:  '',
          10: '',
          11: '',
          12: '',
         }

ODDS = {1:  (1.93, 3.92, 4.26),
        2:  (2.20, 3.62, 3.66),
        3:  (1.40, 5.95, 10.50),
        4:  (2.23, 3.48, 3.74),
        5:  (1.70, 4.20, 5.50),
        6:  (2.58, 3.72, 2.84),
        7:  (2.68, 3.52, 2.81),
        8:  (2.09, 3.62, 4.30),
        9:  (3.60, 3.72, 2.13),
        10: (2.46, 3.75, 3.05),
        11: (3.08, 3.56, 2.46),
        12: (2.16, 3.10, 4.46),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (49, 29, 21),
                           2:  (59, 23, 17),
                           3:  (79, 11, 9),
                           4:  (40, 31, 27),
                           5:  (64, 19, 15),
                           6:  (29, 28, 42),
                           7:  (45, 27, 27),
                           8:  (63, 21, 14),
                           9:  (25, 31, 42),
                           10: (26, 22, 51),
                           11: (37, 31, 30),
                           12: (46, 30, 23),
                          }


BETTING_BREAKDOWN_MINIVAKIO = {1: (),
                               2: (),
                               3: (),
                               4: (),
                               5: (),
                               6: (),
                               7: (),
                              }

vakioveikkaus.create_game(number_of_vakio_rows=NUMBER_OF_PLAYED_VAKIO_ROWS, 
                          number_of_minivakio_rows=NUMBER_OF_PLAYED_MINIVAKIO_ROWS,
                          row_price_vakio=ROW_PRICE_VAKIO,
                          row_price_minivakio=ROW_PRICE_MINIVAKIO,
                          difficulty_fix_vakio=DIFFICULTY_FIX_VAKIO,
                          difficulty_fix_minivakio=DIFFICULTY_FIX_MINIVAKIO,
                          preselected_marks=LOCKED,
                          odds=ODDS,
                          betting_breakdown_vakio=BETTING_BREAKDOWN_VAKIO,
                          betting_breakdown_minivakio=BETTING_BREAKDOWN_MINIVAKIO)


