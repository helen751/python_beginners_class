set1 = {"Helen","victor","Frank","victor"}
set1.add("Favour")
print(set1)
print("helen" in set1)

set2 = {34,56,56,32,78,"victor"}
set1.update(set2)
set3 = set1.union(set2)
print(set1)
print(set3)