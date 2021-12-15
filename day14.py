import copy
from collections import Counter
f = open("day14")
lines = f.read().split('\n')

inp = lines.pop(0)
lines.pop(0)
rules = dict()

for line in lines:
    rule_in, rule_out = line.split(' -> ')
    rules[rule_in] = rule_out

extended_rules = dict()

for rule_in, rule_out in rules.items():
    extended_rules[rule_in] = rule_in[0] + rule_out + rule_in[1]

def polymers_after_n_steps(n=10):

    polymers_after_ten = {}
    for pair, out in extended_rules.items():
        rule_in = pair
        for i in range(10):
            new_polymer = ""
            for j in range(len(rule_in)-1):
                new_polymer += extended_rules[rule_in[j:j+2]][:-1]
            new_polymer += extended_rules[rule_in[-2:]][-1]
            rule_in = new_polymer
        polymers_after_ten[pair] = rule_in

    polymer_pairs_after_ten = {}

    for pair, outp in polymers_after_ten.items():
        paired_out = [outp[i:i+2] for i in range(len(outp)-1)]
        polymer_pairs_after_ten[pair] = dict(Counter(paired_out).most_common())
        outp = Counter(outp[:-1])  # Don't count ending polymers
        polymers_after_ten[pair] = dict(outp.most_common())

    if n == 10:
        return polymers_after_ten
    else:
        n = n // 10 - 2

    polymers_after_n = {}
    for pair, pairs_after_n_1_count in polymer_pairs_after_ten.items():
        for i in range(n):  # calculate polymer pairs after 30 steps
            polymers_after_n_count = {}
            for new_pair in pairs_after_n_1_count:
                pair_after_ten_count = polymer_pairs_after_ten[new_pair]
                for new_new_pair in pair_after_ten_count:
                    if new_new_pair in polymers_after_n_count:
                        polymers_after_n_count[new_new_pair] += pairs_after_n_1_count[new_pair] * pair_after_ten_count[new_new_pair]
                    else:
                        polymers_after_n_count[new_new_pair] = pairs_after_n_1_count[new_pair] * pair_after_ten_count[new_new_pair]
            pairs_after_n_1_count = polymers_after_n_count

        polymers_after_n_count = {}
        for new_pair in pairs_after_n_1_count:
            for polymer,  pol_count in polymers_after_ten[new_pair].items():
                if polymer in polymers_after_n_count:
                    polymers_after_n_count[polymer] += pairs_after_n_1_count[new_pair] * pol_count
                else:
                    polymers_after_n_count[polymer] = pairs_after_n_1_count[new_pair] * pol_count
        polymers_after_n[pair] = polymers_after_n_count

    return polymers_after_n

def count_polymers_in_input(pair_mapping):
    total_count = {}
    for pair in [inp[i:i+2] for i in range(len(inp)-1)]:
        if len(total_count) == 0:
            total_count = pair_mapping[pair]
        else:
            for pol, count in pair_mapping[pair].items():
                if pol not in total_count:
                    total_count[pol] = count
                else:
                    total_count[pol] += count

    total_count[inp[-1]] += 1
    difference = max(pair[1] for pair in total_count.items()) - min(pair[1] for pair in total_count.items())
    return difference


def day14_1():
    pair_mapping = polymers_after_n_steps(10)
    print(count_polymers_in_input(pair_mapping))


def day14_2():
    pair_mapping = polymers_after_n_steps(40)
    print(count_polymers_in_input(pair_mapping))

day14_2()