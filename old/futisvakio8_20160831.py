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

ODDS = {1:  (1.89, 3.57, 5.26),
        2:  (1.12, 11.11, 50),
        3:  (2.86, 3.33, 2.86),
        4:  (1.28, 6.67, 14.29),
        5:  (1.33, 5.88, 12.50),
        6:  (1.39, 5.26, 11.11),
        7:  (1.35, 5.56, 12.50),
        8:  (1.49, 4.55, 9.09),
        9:  (2.22, 4.00, 3.33),
        10: (1.59, 4.35, 7.14),
        11: (2.86, 3.13, 3.03),
        12: (2.86, 3.13, 3.03),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (61, 25, 12),
                           2:  (91, 5, 3),
                           3:  (36, 32, 30),
                           4:  (83, 11, 4),
                           5:  (85, 10, 4),
                           6:  (66, 22, 11),
                           7:  (82, 11, 5),
                           8:  (56, 27, 16),
                           9:  (52, 24, 22),
                           10: (69, 20, 10),
                           11: (30, 32, 36),
                           12: (34, 36, 28),
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


