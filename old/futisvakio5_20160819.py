# -*- coding: utf-8 -*-

import vakioveikkaus

NUMBER_OF_PLAYED_VAKIO_ROWS = 48
NUMBER_OF_PLAYED_MINIVAKIO_ROWS = 0
ROW_PRICE_VAKIO = 0.1
ROW_PRICE_MINIVAKIO = 0.1

# 1=Values are not fixed, >1=Larger probabilities are favored
# about 1.0-2.0
DIFFICULTY_FIX_VAKIO = 1.6
DIFFICULTY_FIX_MINIVAKIO = 2.0

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

ODDS = {1:  (1.56, 4.50, 8.12),
        2:  (1.70, 3.95, 6.90),
        3:  (2.01, 3.54, 4.60),
        4:  (1.43, 5.40, 9.50),
        5:  (3.50, 3.66, 2.27),
        6:  (2.14, 3.57, 3.75),
        7:  (2.46, 3.07, 3.72),
        8:  (1.82, 3.43, 5.80),
        9:  (2.25, 3.25, 4.00),
        10: (1.60, 3.97, 7.80),
        11: (1.79, 3.42, 6.60),
        12: (1.99, 3.20, 5.20),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (73, 16, 9),
                           2:  (63, 21, 14),
                           3:  (53, 28, 17),
                           4:  (77, 15, 7),
                           5:  (30, 28, 40),
                           6:  (58, 23, 18),
                           7:  (31, 31, 36),
                           8:  (70, 16, 12),
                           9:  (61, 24, 13),
                           10: (67, 21, 11),
                           11: (65, 20, 13),
                           12: (53, 30, 15),
                          }


BETTING_BREAKDOWN_MINIVAKIO = {1: (77, 15, 7),
                               2: (56, 25, 17),
                               3: (55, 29, 15),
                               4: (79, 12, 8),
                               5: (30, 30, 38),
                               6: (66, 18, 14),
                               7: (29, 32, 37),
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


