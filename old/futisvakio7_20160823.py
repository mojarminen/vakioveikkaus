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

ODDS = {1:  (2.06, 3.67, 4.28),
        2:  (2.81, 3.35, 2.90),
        3:  (13.00, 6.30, 1.35),
        4:  (1.22, 8.72, 21.00),
        5:  (8.00, 4.86, 1.55),
        6:  (8.50, 5.08, 1.47),
        7:  (4.10, 3.60, 2.05),
        8:  (1.47, 5.03, 8.50),
        9:  (1.42, 5.25, 8.60),
        10: (4.36, 3.75, 2.00),
        11: (1.20, 9.11, 26.00),
        12: (1.30, 6.15, 15.00),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (50, 30, 18),
                           2:  (44, 30, 24),
                           3:  (11, 17, 71),
                           4:  (86, 8, 4),
                           5:  (16, 27, 56),
                           6:  (22, 27, 49),
                           7:  (19, 29, 50),
                           8:  (70, 18, 11),
                           9:  (71, 18, 10),
                           10: (14, 23, 61),
                           11: (85, 9, 4),
                           12: (64, 22, 12),
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


