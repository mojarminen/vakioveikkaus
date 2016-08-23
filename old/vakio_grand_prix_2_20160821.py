# -*- coding: utf-8 -*-

import vakioveikkaus

NUMBER_OF_PLAYED_VAKIO_ROWS = 48
NUMBER_OF_PLAYED_MINIVAKIO_ROWS = 0
ROW_PRICE_VAKIO = 0.1
ROW_PRICE_MINIVAKIO = 0.1

# 1=Values are not fixed, >1=Larger probabilities are favored
# about 1.0-2.0
DIFFICULTY_FIX_VAKIO = 2.3
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

ODDS = {1:  (2.40, 3.50, 3.55),
        2:  (3.62, 3.30, 2.40),
        3:  (1.89, 3.58, 5.00),
        4:  (2.20, 3.47, 4.06),
        5:  (1.57, 4.45, 7.20),
        6:  (1.92, 4.02, 4.50),
        7:  (2.71, 3.92, 2.71),
        8:  (1.44, 5.25, 8.00),
        9:  (2.14, 4.00, 3.50),
        10: (1.93, 3.63, 4.75),
        11: (3.50, 3.30, 2.50),
        12: (2.25, 3.48, 3.77),
        13: (4.10, 3.45, 2.15),
        14: (3.10, 3.28, 2.70),
        15: (4.29, 3.53, 2.05),
        16: (5.10, 4.00, 1.85),
        17: (1.31, 6.20, 21.00),
        18: (1.17, 10.50, 31.00),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (71, 16, 11),
                           2:  (22, 28, 49),
                           3:  (70, 17, 12),
                           4:  (56, 26, 16),
                           5:  (83, 10, 6),
                           6:  (72, 17, 10),
                           7:  (31, 26, 41),
                           8:  (80, 11, 7),
                           9:  (52, 24, 22),
                           10: (71, 18, 9),
                           11: (28, 33, 38),
                           12: (45, 30, 23),
                           13: (17, 26, 55),
                           14: (23, 28, 48),
                           15: (19, 29, 51),
                           16: (6, 10, 83),
                           17: (92, 4, 2),
                           18: (90, 6, 3),
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


