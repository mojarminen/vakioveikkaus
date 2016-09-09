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

ODDS = {1:  (1.15, 14.00, 36.00),
        2:  (2.30, 3.38, 3.70),
        3:  (2.44, 3.29, 3.43),
        4:  (3.42, 3.40, 2.38),
        5:  (1.85, 3.80, 5.20),
        6:  (2.08, 3.80, 3.82),
        7:  (8.07, 5.00, 1.50),
        8:  (2.10, 3.42, 4.26),
        9:  (2.42, 3.00, 3.81),
        10: (2.35, 3.05, 3.96),
        11: (2.88, 3.12, 2.90),
        12: (2.41, 3.22, 3.74),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (84, 10, 5),
                           2:  (38, 27, 34),
                           3:  (48, 28, 23),
                           4:  (22, 27, 49),
                           5:  (76, 14, 8),
                           6:  (66, 17, 16),
                           7:  (10, 15, 73),
                           8:  (47, 30, 22),
                           9:  (40, 35, 24),
                           10: (65, 21, 12),
                           11: (50, 29, 20),
                           12: (28, 35, 35),
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


