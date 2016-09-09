# -*- coding: utf-8 -*-

import vakioveikkaus

NUMBER_OF_PLAYED_VAKIO_ROWS = 48
NUMBER_OF_PLAYED_MINIVAKIO_ROWS = 0
ROW_PRICE_VAKIO = 0.1
ROW_PRICE_MINIVAKIO = 0.1

# 1=Values are not fixed, >1=Larger probabilities are favored
# about 1.0-2.0
DIFFICULTY_FIX_VAKIO = 1.9
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
          13: '',
          14: '',
          15: '',
          16: '',
          17: '',
          18: '',
         }

ODDS = {1:  (2.06, 3.77, 4.01),
        2:  (1.80, 4.33, 4.50),
        3:  (1.26, 6.00, 13.37),
        4:  (1.33, 6.21, 10.00),
        5:  (2.30, 4.10, 2.88),
        6:  (1.63, 4.50, 4.61),
        7:  (1.25, 7.25, 17.00),
        8:  (2.10, 3.68, 3.82),
        9:  (2.19, 3.47, 3.77),
        10: (3.90, 3.63, 2.12),
        11: (2.62, 3.50, 3.01),
        12: (1.98, 3.73, 4.26),
        13: (3.50, 3.50, 2.29),
        14: (2.50, 3.57, 3.00),
        15: (2.20, 3.50, 3.80),
        16: (1.42, 5.09, 10.00),
        17: (2.70, 3.35, 2.98),
        18: (1.95, 3.62, 4.66),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (46, 25, 27),
                           2:  (78, 11, 9),
                           3:  (62, 21, 15),
                           4:  (84, 8, 6),
                           5:  (35, 28, 35),
                           6:  (66, 16, 16),
                           7:  (85, 7, 6),
                           8:  (77, 13, 9),
                           9:  (66, 21, 12),
                           10: (20, 27, 51),
                           11: (56, 23, 20),
                           12: (76, 14, 8),
                           13: (51, 20, 28),
                           14: (35, 30, 33),
                           15: (73, 14, 11),
                           16: (64, 23, 11),
                           17: (38, 32, 28),
                           18: (74, 15, 10),
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


