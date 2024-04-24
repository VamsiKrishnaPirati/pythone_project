intrinsic_rate=10  # unit/distance

def calculate_dynamic_pricing(distance, time_of_day, partners):
    dynamic_price =0
    dynamic_price = distance*intrinsic_rate
    return dynamic_price


if __name__ == '__main__':
    distance =12
    dp= calculate_dynamic_pricing(distance, 'morning','')
    print(dp)