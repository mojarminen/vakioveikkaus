# -*- coding: utf-8 -*-

import vakioveikkaus

NUMBER_OF_PLAYED_VAKIO_ROWS = 48
NUMBER_OF_PLAYED_MINIVAKIO_ROWS = 0
ROW_PRICE_VAKIO = 0.1
ROW_PRICE_MINIVAKIO = 0.1

# 1=Values are not fixed, >1=Larger probabilities are favored
# about 1.0-2.0
DIFFICULTY_FIX_VAKIO = 2.0
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

ODDS = {1:  (2.04, 3.85, 4.33),
        2:  (3.75, 3.38, 2.40),
        3:  (1.86, 3.65, 5.10),
        4:  (2.14, 3.53, 4.10),
        5:  (1.57, 4.35, 7.20),
        6:  (1.92, 4.02, 4.50),
        7:  (2.70, 4.20, 2.70),
        8:  (1.44, 5.39, 8.60),
        9:  (2.05, 4.13, 2.95),
        10: (1.95, 3.62, 4.80),
        11: (3.20, 3.25, 2.62),
        12: (2.40, 3.30, 3.50),
        13: (4.10, 3.40, 2.15),
        14: (3.28, 3.30, 2.51),
        15: (4.40, 3.60, 2.01),
        16: (5.20, 4.00, 1.80),
        17: (1.28, 6.80, 21.50),
        18: (1.19, 10.50, 34.00),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (77, 13, 9),
                           2:  (21, 24, 53),
                           3:  (75, 14, 10),
                           4:  (54, 27, 17),
                           5:  (84, 8, 6),
                           6:  (70, 19, 9),
                           7:  (26, 25, 47),
                           8:  (80, 11, 7),
                           9:  (51, 26, 22),
                           10: (71, 17, 11),
                           11: (26, 32, 40),
                           12: (50, 26, 22),
                           13: (20, 28, 51),
                           14: (17, 22, 59),
                           15: (20, 32, 47),
                           16: (6, 8, 85),
                           17: (92, 3, 3),
                           18: (89, 6, 4),
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


