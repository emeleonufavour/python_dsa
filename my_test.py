strs = ["flower", "flow", "floght"]
list_output = []
final_output = []
final_output_str = ''

for i in strs:
    temp_list = list(i)
    list_output.append(temp_list)

for i in list_output[0]:
    is_common_prefix = True
    for j in list_output[1:]:
        if i not in j:
            is_common_prefix = False
            break
    if is_common_prefix:
        if i not in final_output:
            final_output.append(i)

for i in final_output:
    final_output_str += i

print(f'"{final_output_str}"')
