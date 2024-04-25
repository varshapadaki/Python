def binary_divisible_by_5(sequence):
    numbers = sequence.split(',')
    divisible_by_5 = []

    for num in numbers:
        decimal_num = int(num, 2)
        if decimal_num % 5 == 0:
            divisible_by_5.append(num)

    return ','.join(divisible_by_5)

sample_data = "0100,0011,1010,1001,1100,1001"
result = binary_divisible_by_5(sample_data)
print("Numbers divisible by 5:", result)
