i = int(input())
bin_i = format(i, '032b')
bin_i_list = list(str(bin_i))
bin_j_list = bin_i_list[16:] + bin_i_list[:16]
bin_j_str = ''.join(bin_j_list)
j = int(bin_j_str, 2)
print(j)
