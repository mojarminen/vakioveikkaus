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
          13: '',
         }

ODDS = {1:  (1.93, 4.10, 4.10),
        2:  (2.94, 3.71, 2.56),
        3:  (2.11, 3.95, 3.35),
        4:  (2.10, 4.30, 3.31),
        5:  (2.44, 4.00, 2.72),
        6:  (4.46, 4.17, 1.80),
        7:  (2.39, 4.04, 2.85),
        8:  (1.59, 4.75, 5.50),
        9:  (11.00, 8.00, 1.28),
        10: (5.65, 3.53, 1.90),
        11: (1.40, 5.20, 13.00),
        12: (1.79, 3.62, 6.00),
        13: (8.50, 4.80, 1.50),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (59, 20, 20),
                           2:  (32, 29, 38),
                           3:  (64, 18, 16),
                           4:  (59, 20, 19),
                           5:  (34, 30, 34),
                           6:  (25, 24, 49),
                           7:  (34, 25, 40),
                           8:  (71, 15, 12),
                           9:  (14, 14, 71),
                           10: (17, 30, 52),
                           11: (79, 13, 7),
                           12: (57, 27, 15),
                           13: (11, 18, 70),
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


