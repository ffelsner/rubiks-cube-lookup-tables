#!/usr/bin/env python3

import itertools

permutation = []
for x in itertools.permutations('UUUUDDDD'):
    permutation.append(x)
permutation = sorted(list(set(permutation)))

for x in permutation:
    print("make clean; ./builder.py --cores 4 --depth 20 --type 6x6x6-UD-solve-inner-x-center-and-oblique-edges --option %s" % ''.join(x))
print("./utils/666_step50_merger.py")

print("\n\n\n")

# for generating the noturn solution list
for x in permutation:
    print("make clean; ./builder.py --cores 1 --depth 1 --type 6x6x6-UD-solve-inner-x-center-and-oblique-edges --noturn --option %s" % ''.join(x))
print("./utils/666_step50_merger.py")
