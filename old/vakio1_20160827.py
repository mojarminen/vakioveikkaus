# -*- coding: utf-8 -*-

import vakioveikkaus

NUMBER_OF_PLAYED_VAKIO_ROWS = 48
NUMBER_OF_PLAYED_MINIVAKIO_ROWS = 0
ROW_PRICE_VAKIO = 0.25
ROW_PRICE_MINIVAKIO = 0.1

# 1=Values are not fixed, >1=Larger probabilities are favored
# about 1.0-2.0
DIFFICULTY_FIX_VAKIO = 1.3
DIFFICULTY_FIX_MINIVAKIO = 1

LOCKED = {1:  '',
          2:  '',
          3:  '',
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

ODDS = {1:  (1.28, 6.64, 16.50),
        2:  (5.90, 4.02, 1.75),
        3:  (1.75, 4.00, 6.10),
        4:  (1.75, 4.02, 5.60),
        5:  (2.41, 3.36, 3.42),
        6:  (1.60, 4.75, 8.60),
        7:  (9.20, 4.85, 1.50),
        8:  (2.38, 3.45, 3.50),
        9:  (3.00, 3.33, 2.72),
        10: (2.46, 3.36, 3.40),
        11: (2.45, 3.44, 3.27),
        12: (3.77, 3.47, 2.20),
        13: (2.91, 3.30, 2.82),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (82, 11, 5),
                           2:  (15, 25, 59),
                           3:  (62, 22, 14),
                           4:  (68, 19, 11),
                           5:  (45, 30, 23),
                           6:  (67, 20, 11),
                           7:  (13, 17, 69),
                           8:  (51, 27, 21),
                           9:  (45, 26, 27),
                           10: (38, 30, 30),
                           11: (45, 28, 26),
                           12: (23, 27, 48),
                           13: (32, 31, 35),
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


