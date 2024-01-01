input_str1 = list(input())
input_str2 = list(input())
in1 = list(input_str1)
in2 = list(input_str2)

out1 = [ch for ch in in1 if not ch in input_str2 or input_str2.remove(ch)]
out2 = [ch for ch in in2 if not ch in input_str1 or input_str1.remove(ch)]

print(len(out1) + len(out2))
