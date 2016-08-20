# -*- coding: utf-8 -*-

import vakioveikkaus

NUMBER_OF_PLAYED_VAKIO_ROWS = 10
NUMBER_OF_PLAYED_MINIVAKIO_ROWS = 10
ROW_PRICE_VAKIO = 0.1
ROW_PRICE_MINIVAKIO = 0.1

# 1=Values are not fixed, >1=Larger probabilities are favored
# about 1.0-2.0
DIFFICULTY_FIX_VAKIO = 1
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

ODDS = {1:  (),
        2:  (),
        3:  (),
        4:  (),
        5:  (),
        6:  (),
        7:  (),
        8:  (),
        9:  (),
        10: (),
        11: (),
        12: (),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (),
                           2:  (),
                           3:  (),
                           4:  (),
                           5:  (),
                           6:  (),
                           7:  (),
                           8:  (),
                           9:  (),
                           10: (),
                           11: (),
                           12: (),
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


