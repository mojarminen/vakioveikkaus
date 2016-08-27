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

ODDS = {1:  (2.17, 3.68, 3.66),
        2:  (3.98, 3.92, 2.01),
        3:  (1.65, 4.62, 6.54),
        4:  (2.04, 3.62, 4.10),
        5:  (1.41, 5.50, 11.00),
        6:  (1.70, 4.34, 6.52),
        7:  (3.05, 3.67, 2.46),
        8:  (3.15, 3.64, 2.42),
        9:  (1.39, 5.20, 11.39),
        10: (1.44, 5.15, 9.71),
        11: (1.30, 6.15, 15.00),
        12: (1.43, 5.20, 9.31),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (38, 28, 33),
                           2:  (29, 31, 39),
                           3:  (58, 24, 16),
                           4:  (46, 28, 24),
                           5:  (73, 18, 8),
                           6:  (68, 19, 11),
                           7:  (21, 29, 48),
                           8:  (37, 31, 31),
                           9:  (81, 12, 6),
                           10: (80, 12, 6),
                           11: (74, 16, 8),
                           12: (76, 14, 9),
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


