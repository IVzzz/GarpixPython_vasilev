lst1 = ["Санкт-Петербург", "Москва", "Казань"]
lst2 = ["Воронеж", "Санкт-Петербург", "Иваново"]
lst1_st = set(lst1)
lst2_st = set(lst2)
a = list(lst1_st.intersection(lst2_st))
b = list(lst1_st.symmetric_difference(lst2_st))
print(a)
print(b)