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

ODDS = {1:  (3.04, 3.87, 2.50),
        2:  (1.67, 3.97, 6.74),
        3:  (1.81, 3.95, 5.25),
        4:  (1.96, 3.40, 4.90),
        5:  (1.43, 5.25, 8.80),
        6:  (1.30, 6.34, 13.37),
        7:  (3.30, 3.65, 2.38),
        8:  (1.68, 4.10, 6.14),
        9:  (2.68, 3.35, 2.98),
        10: (2.00, 3.27, 5.63),
        11: (2.03, 3.86, 3.88),
        12: (2.02, 3.70, 4.70),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (27, 28, 43),
                           2:  (72, 17, 9),
                           3:  (65, 21, 13),
                           4:  (60, 25, 14),
                           5:  (61, 24, 13),
                           6:  (79, 12, 8),
                           7:  (23, 30, 45),
                           8:  (71, 18, 9),
                           9:  (37, 30, 31),
                           10: (52, 30, 16),
                           11: (57, 27, 15),
                           12: (73, 15, 10),
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


