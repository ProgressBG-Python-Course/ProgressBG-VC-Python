alist = [
    "351",
    "222",
    "143"
]


def f0(x): return x[0]
def f1(x): return x[1]
def f2(x): return x[2]


sort_by_index = [f0, f1, f2]


sorted_st = sorted(alist, key=sort_by_index[2])
print( sorted_st )
# print( student_tuples.sort(reverse=False))