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

ODDS = {1:  (2.70, 4.96, 2.39),
        2:  (2.60, 4.40, 2.40),
        3:  (2.30, 4.26, 3.03),
        4:  (1.58, 4.72, 6.49),
        5:  (2.80, 3.38, 2.87),
        6:  (3.26, 4.25, 2.21),
        7:  (1.59, 3.90, 8.71),
        8:  (2.24, 4.20, 2.70),
        9:  (2.35, 4.33, 2.89),
        10: (2.85, 4.07, 2.50),
        11: (1.64, 4.14, 6.78),
        12: (2.23, 5.27, 2.76),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (58, 16, 24),
                           2:  (33, 23, 42),
                           3:  (74, 13, 11),
                           4:  (83, 9, 7),
                           5:  (38, 25, 36),
                           6:  (39, 24, 36),
                           7:  (74, 13, 11),
                           8:  (36, 22, 40),
                           9:  (30, 19, 50),
                           10: (37, 23, 38),
                           11: (83, 8, 7),
                           12: (39, 24, 36),
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


