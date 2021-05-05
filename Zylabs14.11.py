# Aaron Oviedo 1990958

def selection_sort_descend_trace(values):
    for i in range(len(values) - 1):
        loop_count = i
        for j in range(i + 1, len(values)):
            if values[j] > values[loop_count]:
                loop_count  = j
        values[i], values[loop_count] = values[loop_count], values[i]
        for x in values:
            print(x, end=' ')
        print()
    return values


if __name__ == '__main__':
    input_values = [int(input_val) for input_val in input().split()]
    selection_sort_descend_trace(input_values)
