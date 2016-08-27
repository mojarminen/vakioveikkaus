# -*- coding: utf-8 -*-

import vakioveikkaus

NUMBER_OF_PLAYED_VAKIO_ROWS = 48
NUMBER_OF_PLAYED_MINIVAKIO_ROWS = 0
ROW_PRICE_VAKIO = 0.1
ROW_PRICE_MINIVAKIO = 0.1

# 1=Values are not fixed, >1=Larger probabilities are favored
# about 1.0-2.0
DIFFICULTY_FIX_VAKIO = 1.2
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

ODDS = {1:  (1.35, 6.95, 16.34),
        2:  (3.03, 3.25, 2.76),
        3:  (4.05, 3.62, 2.15),
        4:  (1.35, 6.35, 13.00),
        5:  (12.00, 6.09, 1.35),
        6:  (6.54, 4.20, 1.65),
        7:  (3.03, 3.22, 2.73),
        8:  (2.02, 3.85, 4.70),
        9:  (3.15, 3.33, 2.60),
        10: (1.45, 5.76, 8.75),
        11: (1.24, 8.25, 21.00),
        12: (9.71, 6.35, 1.35),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (83, 11, 5),
                           2:  (33, 32, 34),
                           3:  (31, 30, 38),
                           4:  (79, 13, 6),
                           5:  (17, 22, 59),
                           6:  (12, 18, 69),
                           7:  (33, 31, 34),
                           8:  (60, 23, 16),
                           9:  (40, 30, 28),
                           10: (76, 14, 8),
                           11: (86, 8, 4),
                           12: (20, 23, 55),
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


