import itertools
from enum import Enum
import os


def combine(a: dict) -> list:
    listn = []
    for items in a:
        listn.append(list(items.value.values()))
    return listn


def line(b: list) -> tuple:
    try:
        counter = 0
        for ele in b:
            counter += 1
            print(f"Combination {counter}: ", ele)
    except Exception as err:
        print(f"func {line.__name__}: Exception: ", err)


def swaggu(msg: str):
    print('\n', '*' * 40, msg, '*' * 40)

def namer():
    print(f"\n{' ' * 30}Chur {os.getenv('username')}")


def validator(*check):
    """Code grandfathered in... no longer in-use
    TODO: Re-factor in later revision
    """
    checker = [set(x) for x in check]

    def valid(data):
        return not any(st.issubset(data) for st in checker)

    return valid


def filtered(cardinput: str, listToIter: list) -> list:
    """ Helper Func:
    Takes in card input method from @param: cardinput
    Applies filter against list @param: listToIter"""

    def excludes(fparam: list, excl: list) -> list:
        return list([exc for exc in fparam if exc not in excl])

    def iproduct(unpack: list) -> list:
        """creates cartesian product from our iter list and calls func @excludes to return filtered list"""
        lparam = []
        for each in itertools.product(*listToIterate, *unpack):
            lparam.append(each)
        
        return excludes(listToIter, lparam)

    def switcher(switchparam: str) -> list:
       
        switch = {
            'contactless': [inputSet['Contactless'][0]['Input'][:2], inputSet['Contactless'][0]['CVM'][:2],
                          [D.cvmRange.value[1], D.cvmRange.value[2]]],
            'icc': [inputSet['ICC'][0]['Input'], [D.CVM.value[4]]],
            'magneticstripe': [inputSet['MagneticStripe'][0]['Input'], [cvm for cvm in D.CVM.value.values() if cvm not in list(inputSet['MagneticStripe'][0]['CVM'])]],
            'manpan': [inputSet['MANPAN'][0]['Input'], [cvm for cvm in D.CVM.value.values() if cvm not in list(inputSet['MANPAN'][0]['CVM'])]],
            'mobile': [inputSet['Mobile'][0]['Input'], inputSet['Mobile'][0]['CVM'][:3],[D.cvmRange.value[1], D.cvmRange.value[2]]]
        }
        
        return iproduct(switch.get(switchparam.lower(), f'func {switcher.__name__}: '))

    
    return switcher(cardinput)


def accessor(c: dict, d: str) -> list:
    try:
        cout = 0
        add = []
        for j in c[d][cout]:
            r = c[d][cout][j]
            cout + len(j)
            add.append(r)
        return add
    except Exception as v:
        print('Sumting wong:', v)


def generate(bc: dict, ent: str):
    """helper func:
    takes in list object, unpacks dict->sub list.
    returns cartesian product"""
    product = []
    for f in itertools.product(*listToIterate, *accessor(bc, ent)):
        product.append(f)
    return product


class D(Enum):
    """Enumerate Data Types for Test"""
    transType = {0: 'Purchase'}
    acct = {0: 'Cheque', 1: 'Savings', 2: 'Credit'}
    cardInput = {0: 'MANPAN', 1: 'MAG', 2: 'ICC', 3: 'FALLBACK',
                 4: 'Contactless Chip', 5: 'Contactless Mag', 6: 'MOBILE WALLET'}
    CVM = {0: 'PLAIN TEXT PIN', 1: 'OFFLINE ENCIPHERED PIN', 2: 'PIN', 3: 'SIGNATURE', 4: 'CDCVM', 5: 'NOCVM'}
    cvmRange = {0: 'AboveCVM', 1: 'BelowCVM', 2: 'EqualCVM'}


transactionSet = {'Transaction': {'Type': list(D.transType.value.values())}}
inputSet = {'Contactless': [{'Input': [D.cardInput.value[4], D.cardInput.value[5]],
                             'CVM': [D.CVM.value[2], D.CVM.value[3], D.CVM.value[5]],
                             'Range': list(D.cvmRange.value.values())}],

            'ICC': [{'Input': [D.cardInput.value[2]],
                     'CVM': [D.CVM.value[0], D.CVM.value[1], D.CVM.value[2], D.CVM.value[3], D.CVM.value[4], D.CVM.value[5]]}],

            'MagneticStripe': [{'Input': [D.cardInput.value[1], D.cardInput.value[3]],
                                'CVM': [D.CVM.value[2], D.CVM.value[3]]}],

            'MANPAN': [{'Input': [D.cardInput.value[0]],
                        'CVM': [D.CVM.value[3]]}],

            'Mobile': [{'Input': [D.cardInput.value[6]],
                        'CVM': [D.CVM.value[2], D.CVM.value[3], D.CVM.value[4], D.CVM.value[5]],
                        'Range': list(D.cvmRange.value.values())}]}

listToIterate = [list(D.transType.value.values()), list(D.acct.value.values())]

if __name__ == '__main__':
    for i in inputSet.keys():
        swaggu(i)
        line(filtered(i, generate(inputSet, i)))
    
    
    