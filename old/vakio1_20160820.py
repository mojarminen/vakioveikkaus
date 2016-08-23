# -*- coding: utf-8 -*-

import vakioveikkaus

NUMBER_OF_PLAYED_VAKIO_ROWS = 48
NUMBER_OF_PLAYED_MINIVAKIO_ROWS = 0
ROW_PRICE_VAKIO = 0.25
ROW_PRICE_MINIVAKIO = 0.25

# 1=Values are not fixed, >1=Larger probabilities are favored
# about 1.0-2.0
DIFFICULTY_FIX_VAKIO = 1.6
DIFFICULTY_FIX_MINIVAKIO = 1.7

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
         }

ODDS = {1:  (6.19, 3.97, 1.80),
        2:  (7.13, 4.40, 1.62),
        3:  (1.50, 4.85, 8.52),
        4:  (3.13, 3.25, 2.70),
        5:  (1.85, 3.70, 5.50),
        6:  (3.00, 3.65, 2.53),
        7:  (2.53, 3.40, 3.20),
        8:  (3.60, 3.42, 2.30),
        9:  (2.63, 3.30, 3.07),
        10: (2.15, 3.43, 4.26),
        11: (3.02, 3.42, 2.60),
        12: (3.35, 3.50, 2.38),
        13: (2.20, 3.52, 3.75),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (13, 21, 65),
                           2:  (10, 17, 72),
                           3:  (75, 16, 8),
                           4:  (32, 31, 36),
                           5:  (58, 24, 16),
                           6:  (31, 26, 42),
                           7:  (43, 27, 28),
                           8:  (26, 28, 45),
                           9:  (41, 31, 27),
                           10: (57, 24, 17),
                           11: (31, 29, 39),
                           12: (32, 25, 42),
                           13: (52, 26, 20),
                          }


BETTING_BREAKDOWN_MINIVAKIO = {1: (17, 20, 61),
                               2: (14, 17, 67),
                               3: (69, 18, 11),
                               4: (32, 32, 34),
                               5: (54, 25, 19),
                               6: (31, 27, 41),
                               7: (44, 27, 28),
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


