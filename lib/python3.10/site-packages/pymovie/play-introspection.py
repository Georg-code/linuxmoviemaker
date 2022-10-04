# play-instrospection.py

from typing import Dict, Any, NewType

UserId = NewType('UserId', int)

bobs_id = UserId(52)


def obj_lister(object_source: Dict[str, Any], *types_to_report):
    count_of_others = 0
    line_num = 1
    for key, obj in object_source.items():
        if type(obj) in types_to_report:
            print(f'{line_num:4d} {key}: {type(obj).__name__}')
        else:
            print(f'{line_num:4d} ???      {key}: {type(obj).__name__}')
            count_of_others += 1
        line_num += 1
    print(f'\nFound {count_of_others} other objects')

bob = 78
judy = 3.14
NoneType = type(None)
FuncType = type(obj_lister)
BuiltInType = type(abs)

print(len(vars()))
obj_lister(vars(), str, int, float, dict, type, NoneType, FuncType, BuiltInType)
# g: Dict[str, Any] = vars().copy()
# for key, obj in g.items():
#     print(f'{key} {type(obj)}')