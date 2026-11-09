import random


def test_even(result: str = '', value: int = None) ->str:
    if not value:
        value = random.randint(1,100)
        return value
    else:
        if value % 2 == 0 and result == 'yes':
            return None
        elif value % 2 == 0 and result == 'no':
            return 'yes'
        elif value % 2 != 0 and result == 'yes':
            return 'no'
        elif value % 2 != 0 and result == 'no':   
            return None
        



