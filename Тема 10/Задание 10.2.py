def try_fold_numbers(a, b):
    try:
        c = float(a) + float(b)
    except TypeError:
        print("Ожидаемый тип данных — число")
    except ValueError:
        print("Ожидаемый тип данных — число")
    else:
        print(c)