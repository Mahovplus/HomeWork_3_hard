data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def results_calc(args):
    sum = 0
    if isinstance(args, (int, float)):
        return args
    elif isinstance(args, str):
        return len(args)
    elif isinstance(args, (list, tuple, set)):
        for i in args:
            sum += results_calc(i)
    elif isinstance(args, dict):
        for key, value in args.items():
            sum += results_calc(key)
            sum += results_calc(value)
    return sum

result = results_calc(data_structure)
print(result)



