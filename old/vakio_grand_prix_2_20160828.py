# -*- coding: utf-8 -*-

import vakioveikkaus

NUMBER_OF_PLAYED_VAKIO_ROWS = 48
NUMBER_OF_PLAYED_MINIVAKIO_ROWS = 0
ROW_PRICE_VAKIO = 0.1
ROW_PRICE_MINIVAKIO = 0.1

# 1=Values are not fixed, >1=Larger probabilities are favored
# about 1.0-2.0
DIFFICULTY_FIX_VAKIO = 2.2
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

ODDS = {1:  (1.34, 6.74, 13.00),
        2:  (1.38, 5.80, 13.00),
        3:  (5.40, 4.16, 1.80),
        4:  (1.69, 3.90, 6.80),
        5:  (2.50, 3.35, 3.40),
        6:  (2.13, 3.42, 4.15),
        7:  (1.92, 3.60, 5.05),
        8:  (5.75, 3.80, 1.95),
        9:  (2.35, 3.30, 3.70),
        10: (1.92, 3.72, 4.75),
        11: (6.70, 4.65, 1.62),
        12: (2.70, 3.52, 2.88),
        13: (1.71, 4.10, 6.30),
        14: (2.24, 3.30, 4.10),
        15: (5.30, 3.95, 1.91),
        16: (1.68, 4.20, 6.50),
        17: (2.30, 3.20, 4.30),
        18: (2.35, 3.92, 3.27),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (87, 9, 3),
                           2:  (80, 13, 5),
                           3:  (11, 18, 70),
                           4:  (65, 21, 13),
                           5:  (56, 23, 19),
                           6:  (48, 29, 22),
                           7:  (67, 20, 11),
                           8:  (12, 20, 67),
                           9:  (39, 30, 29),
                           10: (67, 19, 13),
                           11: (7, 11, 80),
                           12: (35, 27, 37),
                           13: (76, 15, 8),
                           14: (54, 26, 19),
                           15: (12, 21, 65),
                           16: (69, 20, 10),
                           17: (63, 22, 13),
                           18: (36, 24, 38),
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


