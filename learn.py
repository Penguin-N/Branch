a = {"enh":5,"diar":10,"spk_loss":3}
print(a)
b = {"a":a}
del b["a"]["enh"]
del b["a"]["diar"]
print(b)