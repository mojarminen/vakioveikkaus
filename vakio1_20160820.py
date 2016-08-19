# -*- coding: utf-8 -*-

import vakioveikkaus

NUMBER_OF_PLAYED_VAKIO_ROWS = 48
NUMBER_OF_PLAYED_MINIVAKIO_ROWS = 0
ROW_PRICE_VAKIO = 0.25
ROW_PRICE_MINIVAKIO = 0.25

# 1=Values are not fixed, >1=Larger probabilities are favored
# about 1.0-2.0
DIFFICULTY_FIX_VAKIO = 1.5
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

ODDS = {1:  (5.85, 3.90, 1.80),
        2:  (7.00, 4.40, 1.60),
        3:  (1.50, 4.80, 8.52),
        4:  (3.11, 3.30, 2.65),
        5:  (1.86, 3.75, 5.55),
        6:  (3.00, 3.60, 2.55),
        7:  (2.50, 3.40, 3.20),
        8:  (3.75, 3.40, 2.27),
        9:  (2.69, 3.30, 3.07),
        10: (2.13, 3.40, 4.10),
        11: (2.89, 3.42, 2.72),
        12: (3.37, 3.40, 2.39),
        13: (2.27, 3.51, 3.67),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (15, 20, 63),
                           2:  (11, 16, 71),
                           3:  (75, 16, 8),
                           4:  (33, 30, 35),
                           5:  (57, 25, 17),
                           6:  (30, 26, 43),
                           7:  (44, 27, 27),
                           8:  (27, 28, 43),
                           9:  (41, 30, 27),
                           10: (59, 23, 17),
                           11: (32, 29, 37),
                           12: (34, 25, 39),
                           13: (52, 26, 21),
                          }


BETTING_BREAKDOWN_MINIVAKIO = {1: (19, 20, 59),
                               2: (15, 17, 66),
                               3: (69, 18, 11),
                               4: (35, 31, 33),
                               5: (53, 26, 20),
                               6: (31, 26, 42),
                               7: (45, 27, 27),
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


