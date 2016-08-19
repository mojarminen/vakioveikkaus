# -*- coding: utf-8 -*-

import vakioveikkaus

NUMBER_OF_PLAYED_VAKIO_ROWS = 48
NUMBER_OF_PLAYED_MINIVAKIO_ROWS = 0

# 1=Values are not fixed, >1=Larger probabilities are favored
# 1.0-2.0
DIFFICULTY_FIX_VAKIO = 1.5
DIFFICULTY_FIX_MINIVAKIO = 1.3

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




if __name__ == '__main__':

    vakio = []
    minivakio = []

    if NUMBER_OF_PLAYED_VAKIO_ROWS:
        all_vakio_rows = vakioveikkaus.get_most_valuable_rows(ODDS, BETTING_BREAKDOWN_VAKIO, LOCKED, DIFFICULTY_FIX_VAKIO)
        vakio = all_vakio_rows[:NUMBER_OF_PLAYED_VAKIO_ROWS]

    if NUMBER_OF_PLAYED_MINIVAKIO_ROWS > 0:
        all_minivakio_rows = vakioveikkaus.get_most_valuable_rows(ODDS, BETTING_BREAKDOWN_MINIVAKIO, LOCKED, DIFFICULTY_FIX_MINIVAKIO)    
        minivakio = all_minivakio_rows[:NUMBER_OF_PLAYED_MINIVAKIO_ROWS]
    
    # Parhaat vakiorivit
    vakioveikkaus.print_games('Vakio', vakio)
    
    if len(minivakio) > 0:
        # Parhaat minivakiorivit
        vakioveikkaus.print_games('Minivakio', minivakio)

        # Vakioon jo sisältyvät parhaat minivakiorivit
        already_included = []
        for r in list(set([tuple(v[:len(minivakio[0])]) for v in vakio])):
            for mrow in minivakio:
                if mrow == r:
                    already_included.append(r)
        vakioveikkaus.print_games(u'Vakioon jo sisältyvät parhaat minivakiorivit', already_included)
    
        # Minivakiorivit, jotka ei vielä sisälly vakioon
        missing_minivakio_rows = []
        for row in minivakio:
            match = False
            for existingrow in already_included:
                if row == existingrow:
                    match = True                    
            if match == False:
                missing_minivakio_rows.append(row)
        vakioveikkaus.print_games('Minivakiorivit, jotka ei vielä sisälly vakioon', missing_minivakio_rows)
    
        # Parhaat lisärivit kattamaan puuttuvat minivakiorivit
        additional_rows = []
        for missing_row in missing_minivakio_rows:
            for vakio_row in all_vakio_rows:
                if missing_row == vakio_row[:len(missing_row)]:
                    additional_rows.append(vakio_row)
                    break
        vakioveikkaus.print_games('Parhaat lisärivit kattamaan puuttuvat minivakiorivit', additional_rows)

    try:
        all_full_rows_to_be_played = vakio + additional_rows
    except NameError:
        all_full_rows_to_be_played = vakio
    
    # Rivit minivakiolla ja rivit ilman minivakiota
    rows_with_minivakio = []
    rows_without_minivakio = []
    for minirow in minivakio:
        for row in all_full_rows_to_be_played:
            if row[:len(minirow)] == minirow:
                rows_with_minivakio.append(row)
                break
    rows_without_minivakio = list(set(all_full_rows_to_be_played) - set(rows_with_minivakio))

    vakioveikkaus.print_games('Rivit minivakiolla', rows_with_minivakio)    
    vakioveikkaus.print_games('Rivit ilman minivakiota', rows_without_minivakio)


    # Vakion voittotodennäköisyydet
    h = 'Vakion voittotodennäköisyydet'
    print '*'*len(h)
    print h
    print '*'*len(h)
    winning_probabilities = vakioveikkaus.get_combined_winning_probabilities_of_rows(rows_with_minivakio + rows_without_minivakio, ODDS)
    print 'Arvioitu kaikki oikein todennäköisyys:', winning_probabilities['jackpot']
    print 'Arvioitu (vähintään) -1 oikein todennäköisyys:', winning_probabilities['minus_one']
    print 'Arvioitu (vähintään) -2 oikein todennäköisyys:', winning_probabilities['minus_two']
    if 'minus_three' in winning_probabilities:
        print 'Arvioitu (vähintään) -3 oikein todennäköisyys:', winning_probabilities['minus_three']
    print

    if len(minivakio) > 0:
        # Vakion voittotodennäköisyydet
        h = 'Minivakion voittotodennäköisyydet'
        print '*'*len(h)
        print h
        print '*'*len(h)
        winning_probabilities = vakioveikkaus.get_combined_winning_probabilities_of_rows(minivakio, ODDS)
        print 'Arvioitu kaikki oikein todennäköisyys:', winning_probabilities['jackpot']
        print

    # Laskennassa käytetyt todennäköisyydet
    print 'Laskennassa käytetyt todennäköisyydet:'
    for k, odds in ODDS.items():
        print str(k) + ':', int(round(100/odds[0])), int(round(100/odds[1])), int(round(100/odds[2]))
    print

