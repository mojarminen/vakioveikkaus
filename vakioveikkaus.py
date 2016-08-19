# -*- coding: utf-8 -*-

def odds_to_probabilities(odds):
    probabilities = {}
    for k,v in odds.items():
        probabilities[k] = (1/v[0], 1/v[1], 1/v[2])
    return probabilities


def get_all_possible_rows(n):
    result = []
    if n == 1:
        result = [('1',), ('X',), ('2',)]
    elif n > 1:
        subrows = get_all_possible_rows(n-1)
        for subrow in subrows:
            result.append(('1',) + subrow)
            result.append(('X',) + subrow)
            result.append(('2',) + subrow)
    return result


def calculate_value_of_row(row, probabilities, breakdown_odds, difficulty_fix=1):
    '''
        difficulty_fix: 1-n, higher value gives easier rows (the larger probabilities are favored)
    '''
    
    probability = 1.0
    breakdown_odd = 1.0

    # calculate probability and breakdown_odd
    for idx, mark in enumerate(row):
        if mark == '1':
            probability *= probabilities[idx + 1][0]
            breakdown_odd *= breakdown_odds[idx + 1][0]
        elif mark == 'X':
            probability *= probabilities[idx + 1][1]
            breakdown_odd *= breakdown_odds[idx + 1][1]
        elif mark == '2':
            probability *= probabilities[idx + 1][2]
            breakdown_odd *= breakdown_odds[idx + 1][2]

    import math
    return breakdown_odd * math.pow(probability, difficulty_fix)


def get_row_probability(row, probabilities):
    probability = 1.0

    for idx, mark in enumerate(row):
        if mark == '1':
            probability *= probabilities[idx + 1][0]
        elif mark == 'X':
            probability *= probabilities[idx + 1][1]
        elif mark == '2':
            probability *= probabilities[idx + 1][2]

    return probability


def get_atleast_minus_1_probability(rows, probabilities):
    
    # Get all different combinations of -1.
    rows_with_minus_1 = []
    for row in rows:
        for skip in range(len(row)):
            tmp_row = list(row)
            tmp_row[skip] = ''
            tmp_row = tuple(tmp_row)
            
            if tmp_row not in rows_with_minus_1:
                rows_with_minus_1.append(tmp_row)
                        
    total_probability = 0.0
    for row in rows_with_minus_1:
        probability = 1.0
        for idx, mark in enumerate(row):
            if mark == '':
                probability *= 1            
            elif mark == '1':
                probability *= probabilities[idx + 1][0]
            elif mark == 'X':
                probability *= probabilities[idx + 1][1]
            elif mark == '2':
                probability *= probabilities[idx + 1][2]

        total_probability += probability
        
    return total_probability

    
    
def get_row_minus_1_probability(row, probabilities):
    total_probability = 0.0
    
    for skip in range(len(row)):
        probability = 1.0
        for idx, mark in enumerate(row):
            if skip == idx:
                # Skip this char. Probability is the probability of not matching.
                if mark == '1':
                    probability *= (1 - probabilities[idx + 1][0])
                elif mark == 'X':
                    probability *= (1 - probabilities[idx + 1][1])
                elif mark == '2':
                    probability *= (1 - probabilities[idx + 1][2])
            else:
                if mark == '1':
                    probability *= probabilities[idx + 1][0]
                elif mark == 'X':
                    probability *= probabilities[idx + 1][1]
                elif mark == '2':
                    probability *= probabilities[idx + 1][2]
            
        total_probability += probability
    
    return total_probability


def get_atleast_minus_2_probability(rows, probabilities):
    
    # Get all different combinations of -2.
    rows_with_minus_2 = []
    for row in rows:
        for skip1 in range(len(row)):
            for skip2 in range(len(row)):
                if skip1 == skip2:
                    continue

                tmp_row = list(row)
                tmp_row[skip1] = ''
                tmp_row[skip2] = ''
                tmp_row = tuple(tmp_row)
                
                if tmp_row not in rows_with_minus_2:
                    rows_with_minus_2.append(tmp_row)
                        
    total_probability = 0.0
    for row in rows_with_minus_2:
        probability = 1.0
        for idx, mark in enumerate(row):
            if mark == '':
                probability *= 1            
            elif mark == '1':
                probability *= probabilities[idx + 1][0]
            elif mark == 'X':
                probability *= probabilities[idx + 1][1]
            elif mark == '2':
                probability *= probabilities[idx + 1][2]

        total_probability += probability
        
    return total_probability


def get_row_minus_2_probability(row, probabilities):
    total_probability = 0.0

    for skip1 in range(len(row)-1):
        for skip2 in range(skip1+1, len(row)):
            if skip1 == skip2:
                raise Exception('Never!!!!!!!')
            
            probability = 1.0
            for idx, mark in enumerate(row):
                if idx == skip1 or idx == skip2:
                    # Skip this char. Probability is the probability of not matching.
                    if mark == '1':
                        probability *= (1 - probabilities[idx + 1][0])
                    elif mark == 'X':
                        probability *= (1 - probabilities[idx + 1][1])
                    elif mark == '2':
                        probability *= (1 - probabilities[idx + 1][2])
                else:
                    if mark == '1':
                        probability *= probabilities[idx + 1][0]
                    elif mark == 'X':
                        probability *= probabilities[idx + 1][1]
                    elif mark == '2':
                        probability *= probabilities[idx + 1][2]
            
            total_probability += probability
    
    return total_probability


def get_atleast_minus_3_probability(rows, probabilities):
    
    # Get all different combinations of -3.
    rows_with_minus_3 = []
    for row in rows:
        for skip1 in range(len(row)):
            for skip2 in range(len(row)):
                for skip3 in range(len(row)):
                    if skip1 == skip2 or skip1 == skip3 or skip2 == skip3:
                        continue

                    tmp_row = list(row)
                    tmp_row[skip1] = ''
                    tmp_row[skip2] = ''
                    tmp_row[skip3] = ''
                    tmp_row = tuple(tmp_row)
                    
                    if tmp_row not in rows_with_minus_3:
                        rows_with_minus_3.append(tmp_row)
                        
    total_probability = 0.0
    for row in rows_with_minus_3:
        probability = 1.0
        for idx, mark in enumerate(row):
            if mark == '':
                probability *= 1            
            elif mark == '1':
                probability *= probabilities[idx + 1][0]
            elif mark == 'X':
                probability *= probabilities[idx + 1][1]
            elif mark == '2':
                probability *= probabilities[idx + 1][2]

        total_probability += probability
        
    return total_probability
    

def get_row_minus_3_probability(row, probabilities):
    total_probability = 0.0

    for skip1 in range(len(row)):
        for skip2 in range(len(row)):
            for skip3 in range(len(row)):
                if skip1 == skip2 or skip1 == skip3 or skip2 == skip3:
                    continue
                
                probability = 1.0
                for idx, mark in enumerate(row):
                    if idx == skip1 or idx == skip2 or idx == skip3:
                        # Skip this char. Probability is the probability of not matching.
                        if mark == '1':
                            probability *= (1 - probabilities[idx + 1][0])
                        elif mark == 'X':
                            probability *= (1 - probabilities[idx + 1][1])
                        elif mark == '2':
                            probability *= (1 - probabilities[idx + 1][2])
                    else:
                        if mark == '1':
                            probability *= probabilities[idx + 1][0]
                        elif mark == 'X':
                            probability *= probabilities[idx + 1][1]
                        elif mark == '2':
                            probability *= probabilities[idx + 1][2]
                
                total_probability += probability
    
    return total_probability


def get_all_allowed_rows(row_length, predefined_marks):
    allowed_rows = []
    for row in get_all_possible_rows(row_length):
        is_allowed = True
        for k,v in predefined_marks.items():
            if v and len(row) >= k and row[k-1] not in v:
                is_allowed = False
                break
                
        if is_allowed:
            allowed_rows.append(row)
    
    return allowed_rows


def get_most_valuable_rows(odds, betting_breakdown, predefined_marks, difficulty_fix):
    ''' Returns n rows in an order from best valued to the worst based on odd divided by probability
        Returns all rows if n is not given
    '''
    
    probabilities = odds_to_probabilities(odds)

    breakdown_odds = {}
    for k, v in betting_breakdown.items():
        breakdown_odds[k] = (100./v[0], 100./v[1], 100./v[2])


    # Get all possible rows and filter out rows that don't match to predefined marks.
    allowed_rows = get_all_allowed_rows(len(betting_breakdown), predefined_marks)

    values = []
    for row in allowed_rows:
        v = calculate_value_of_row(row, probabilities, breakdown_odds, difficulty_fix)
        values.append((row,v))
    values.sort(key=lambda x: x[1])
    values.reverse()
    
    return [v[0] for v in values]


def get_number_of_differences(row1, row2):
    if len(row1) != len(row2):
        raise Exception('rows have different lengths')
    
    differences = 0
    for idx in range(len(row1)):
        if row1[idx] != row2[idx]:
            differences += 1
            
    return differences


def print_games(heading, rows):
    if heading:
        print '*'*len(heading)
        print heading
        print '*'*len(heading)
    
    id_on_game_sheet = 1
    for idx, row in enumerate(rows):
        print "%3s %4s: %s" % (idx+1, '(' + str(id_on_game_sheet) + ')', row)
        if id_on_game_sheet == 16:
            print
        id_on_game_sheet = id_on_game_sheet + 1 if id_on_game_sheet < 16 else 1
    print


def get_combined_winning_probabilities_of_rows(rows, odds):
    
    if len(rows) < 1:
        raise Exception('Row list is empty')
    
    result = {}
    
    probabilities = {}
    for k,v in odds.items():
        probabilities[k] = (1/v[0], 1/v[1], 1/v[2])
    
    probability_for_all_correctly = 0.0
    for row in rows:
        probability_for_all_correctly += get_row_probability(row, probabilities)
    result['jackpot'] = probability_for_all_correctly

    if len(rows[0]) > 7:
        result['minus_one'] = get_atleast_minus_1_probability(rows, probabilities)        
        result['minus_two'] = get_atleast_minus_2_probability(rows, probabilities)
    if len(rows[0]) > 12:
        result['minus_three'] = get_atleast_minus_3_probability(rows, probabilities)

    return result
    

def create_game(number_of_vakio_rows, number_of_minivakio_rows, row_price_vakio,
                row_price_minivakio, difficulty_fix_vakio, difficulty_fix_minivakio,
                preselected_marks, odds, betting_breakdown_vakio, betting_breakdown_minivakio):

    vakio = []
    minivakio = []

    if number_of_vakio_rows:
        all_vakio_rows = get_most_valuable_rows(odds, betting_breakdown_vakio, preselected_marks, difficulty_fix_vakio)
        vakio = all_vakio_rows[:number_of_vakio_rows]

    if number_of_minivakio_rows > 0:
        all_minivakio_rows = get_most_valuable_rows(odds, betting_breakdown_vakio, preselected_marks, difficulty_fix_minivakio)    
        minivakio = all_minivakio_rows[:number_of_minivakio_rows]
    
    # Parhaat vakiorivit
    print_games('Vakio', vakio)
    
    all_full_rows_to_be_played = []
    if len(minivakio) > 0:
        # Parhaat minivakiorivit
        print_games('Minivakio', minivakio)

        # Vakioon jo sisältyvät parhaat minivakiorivit
        already_included = []
        for r in list(set([tuple(v[:len(minivakio[0])]) for v in vakio])):
            for mrow in minivakio:
                if mrow == r:
                    already_included.append(r)
        print_games(u'Vakioon jo sisältyvät parhaat minivakiorivit', already_included)
    
        # Minivakiorivit, jotka ei vielä sisälly vakioon
        missing_minivakio_rows = []
        for row in minivakio:
            match = False
            for existingrow in already_included:
                if row == existingrow:
                    match = True                    
            if match == False:
                missing_minivakio_rows.append(row)
        print_games('Minivakiorivit, jotka ei vielä sisälly vakioon', missing_minivakio_rows)
    
        # Parhaat lisärivit kattamaan puuttuvat minivakiorivit
        additional_rows = []
        for missing_row in missing_minivakio_rows:
            for vakio_row in all_vakio_rows:
                if missing_row == vakio_row[:len(missing_row)]:
                    additional_rows.append(vakio_row)
                    break
        print_games('Parhaat lisärivit kattamaan puuttuvat minivakiorivit', additional_rows)

        all_full_rows_to_be_played = vakio + additional_rows
    else:
        all_full_rows_to_be_played = vakio

    
    # Rivit minivakiolla ja rivit ilman minivakiota
    rows_with_minivakio = []
    rows_without_minivakio = []
    if len(minivakio) > 0:
        for minirow in minivakio:
            for row in all_full_rows_to_be_played:
                if row[:len(minirow)] == minirow:
                    rows_with_minivakio.append(row)
                    break
        rows_without_minivakio = list(set(all_full_rows_to_be_played) - set(rows_with_minivakio))
    else:
        rows_without_minivakio = all_full_rows_to_be_played

    if len(minivakio) > 0:
        print_games('Rivit minivakiolla', rows_with_minivakio)    
    print_games('Rivit ilman minivakiota', rows_without_minivakio)


    # Vakion voittotodennäköisyydet
    h = u'Vakion voittotodennäköisyydet'
    print '*'*len(h)
    print h
    print '*'*len(h)
    winning_probabilities = get_combined_winning_probabilities_of_rows(rows_with_minivakio + rows_without_minivakio, odds)
    print 'Arvioitu kaikki oikein todennäköisyys:        ', winning_probabilities['jackpot']
    print 'Arvioitu (vähintään) -1 oikein todennäköisyys:', winning_probabilities['minus_one']
    print 'Arvioitu (vähintään) -2 oikein todennäköisyys:', winning_probabilities['minus_two']
    if 'minus_three' in winning_probabilities:
        print 'Arvioitu (vähintään) -3 oikein todennäköisyys:', winning_probabilities['minus_three']
    print

    if len(minivakio) > 0:
        # Vakion voittotodennäköisyydet
        h = u'Minivakion voittotodennäköisyydet'
        print '*'*len(h)
        print h
        print '*'*len(h)
        winning_probabilities = get_combined_winning_probabilities_of_rows(minivakio, ODDS)
        print 'Arvioitu kaikki oikein todennäköisyys:', winning_probabilities['jackpot']
        print

    # Laskennassa käytetyt todennäköisyydet
    h = u'Laskennassa käytetyt todennäköisyydet:'
    print '*' * len(h)
    print h
    print '*' * len(h)
    for k, odds in odds.items():
        print "%2s: %2s %2s %2s" % (k, int(round(100/odds[0])), int(round(100/odds[1])), int(round(100/odds[2])))
    print

    # Hinta
    h = 'Hinta'
    print '*' * len(h)
    print h
    print '*' * len(h)
    print 'Vakio ' + str(len(rows_without_minivakio))+'*' + str(row_price_vakio) + '€' + ' = ' + str(row_price_vakio*len(rows_without_minivakio)) + '€'
    if len(rows_with_minivakio) > 0:
        print 'Vakio+Minivakio ' + str(len(rows_with_minivakio))+'*' + str(row_price_vakio+row_price_minivakio) + '€' + ' = ' + str((row_price_vakio+row_price_minivakio)*len(rows_with_minivakio)) + '€'
        print 'Yht. = ' + str((row_price_minivakio+row_price_vakio)*len(rows_with_minivakio) + row_price_vakio*len(rows_without_minivakio)) + '€'   
