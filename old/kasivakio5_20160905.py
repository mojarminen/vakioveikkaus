# -*- coding: utf-8 -*-

import vakioveikkaus

NUMBER_OF_PLAYED_VAKIO_ROWS = 48
NUMBER_OF_PLAYED_MINIVAKIO_ROWS = 0
ROW_PRICE_VAKIO = 0.1
ROW_PRICE_MINIVAKIO = 0.1

# 1=Values are not fixed, >1=Larger probabilities are favored
# about 1.0-2.0
DIFFICULTY_FIX_VAKIO = 1.9
DIFFICULTY_FIX_MINIVAKIO = 1

LOCKED = {1:  '', #'2',
          2:  '', #'2',
          3:  '', #'1',
          4:  '',
          5:  '',
          6:  '',
          7:  '',
          8:  '',
         }

ODDS = {1:  (1./.62, 1./.25, 1./.13),
        2:  (1./.46, 1./.30, 1./.24),
        3:  (1./.60, 1./.25, 1./.15),
        4:  (1./.18, 1./.27, 1./.55),
        5:  (1./.55, 1./.27, 1./.18),
        6:  (1./.98, 1./.015, 1./.005),
        7:  (1./.75, 1./.18, 1./.07),
        8:  (1./.47, 1./.32, 1./.22),
       }


BETTING_BREAKDOWN_VAKIO = {1:  (52, 28, 18),
                           2:  (42, 32, 24),
                           3:  (56, 27, 16),
                           4:  (7, 18, 74),
                           5:  (38, 31, 30),
                           6:  (93, 3, 2),
                           7:  (81, 13, 4),
                           8:  (47, 33, 19),
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


