def get_class_advantage():
    return {
        'Militia': ['Spearmen', 'LightCavalry'],
        'Spearmen': ['LightCavalry', 'HeavyCavalry'],
        'LightCavalry': ['FootArcher', 'CavalryArcher'],
        'HeavyCavalry': ['Militia', 'FootArcher', 'LightCavalry'],
        'CavalryArcher': ['Spearmen', 'HeavyCavalry'],
        'FootArcher': ['Militia', 'CavalryArcher']
    }

def get_battle_result(own_soldiers, opponent_soldiers):
    own_advantage = get_class_advantage()[own_soldiers['class']]
    opponent_class = opponent_soldiers['class']
    own_strength = own_soldiers['strength']
    opponent_strength = opponent_soldiers['strength']

    if opponent_class in own_advantage:
        if own_strength * 2 > opponent_strength:
            return 'Win'
        elif own_strength * 2 == opponent_strength:
            return 'Draw'
        else:
            return 'Loss'
    else:
        if own_strength > opponent_strength:
            return 'Win'
        elif own_strength == opponent_strength:
            return 'Draw'
        else:
            return 'Loss'

def arrange_platoons(own_platoons, opponent_platoons):
    own_platoons.sort(key=lambda x: len(get_class_advantage()[x['class']]), reverse=True)
    opponent_platoons.sort(key=lambda x: len(get_class_advantage()[x['class']]), reverse=True)

    battles_won = 0
    result_sequence = []

    for own_platoon in own_platoons:
        for opponent_platoon in opponent_platoons:
            result = get_battle_result(own_platoon, opponent_platoon)
            if result == 'Win':
                battles_won += 1
                result_sequence.append(own_platoon['class'] + '#' + str(own_platoon['strength']))
                opponent_platoons.remove(opponent_platoon)
                break

    if battles_won >= 3:
        return result_sequence
    else:
        return "There is no chance of winning"


own_input = "Spearmen#10;Militia#30;FootArcher#20;LightCavalry#1000;HeavyCavalry#120"
opponent_input = "Militia#10;Spearmen#10;FootArcher#1000;LightCavalry#120;CavalryArcher#100"

own_platoons = [{'class': item.split('#')[0], 'strength': int(item.split('#')[1])} for item in own_input.split(';')]
opponent_platoons = [{'class': item.split('#')[0], 'strength': int(item.split('#')[1])} for item in opponent_input.split(';')]


result = arrange_platoons(own_platoons, opponent_platoons)
print(result)
