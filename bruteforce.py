import numpy as np
import hashlib
import timeit

allowed_signs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
hash1 = "5aea476328379d3bff2204501bb57aa8b4268fac"
hash2 = "d31d62ed0af022248e28fc0dc4a9580217987e55"
hash3 = "66ceeafde8453dda201978b2b497b9c85d4b6da5"


def compute_possibilities(length):
    number_letters = 26 * 2     # 26 letters (without Umlaute) * 2 (Upper and Lowercase)
    number_digits = 10          # number digits 0-9
    number_signs = number_digits + number_letters
    possibilities = np.power(number_signs, length)

    return possibilities


def compute_range_possibilities(start, stop):
    possibilities = 0

    for n in range(start, stop+1):
        possibilities = possibilities + compute_possibilities(n)

    return possibilities


def compute_time(number):
    time_single = 0.00025
    hours = number * time_single / 3600
    return hours


def compare_hash(password, hash_key):
    encoded_password = str.encode(password)
    hashed_password = hashlib.sha1(encoded_password).hexdigest()
    if hashed_password == hash_key:
        return password
    return False


def crack_password_5(signs, hash_key):
    number_signs = len(signs)

    for sign1 in range(0, number_signs):
        for sign2 in range(0, number_signs):
            for sign3 in range(0, number_signs):
                for sign4 in range(0, number_signs):
                    for sign5 in range(0, number_signs):
                        password = signs[sign1] + signs[sign2] + signs[sign3] + signs[sign4] + signs[sign5]
                        if compare_hash(password, hash_key):
                            return password


def crack_password_10(signs, hash_key):
    number_signs = len(signs)

    for sign1 in range(0, number_signs):
        for sign2 in range(0, number_signs):
            for sign3 in range(0, number_signs):
                for sign4 in range(0, number_signs):
                    for sign5 in range(0, number_signs):
                        for sign6 in range(0, number_signs):
                            for sign7 in range(0, number_signs):
                                for sign8 in range(0, number_signs):
                                    for sign9 in range(0, number_signs):
                                        for sign10 in range(0, number_signs):
                                            password = signs[sign1] + signs[sign2] + signs[sign3] + signs[sign4] + \
                                                       signs[sign5] + signs[sign6] + signs[sign7] + signs[sign8] +\
                                                       signs[sign9] + signs[sign10]

                                            if compare_hash(password, hash_key):
                                                return password


if __name__ == '__main__':
    print("Password possibilities for upper and lowercase letters and digits from 0-9")
    print("For length 5 : ", compute_possibilities(5))
    print("For length 10 : ", compute_possibilities(10))
    print("For range 5 to 10 : ", compute_range_possibilities(5, 10))
    print("Time in hours 5 Signs: ", compute_time(compute_possibilities(5)))
    print("Time in hours 10 Signs: ", compute_time(compute_possibilities(10)))
    print("Time in hours 5 to 10 Signs: ", compute_time(compute_range_possibilities(5, 10)))

    starttime = timeit.default_timer()
    password5 = crack_password_5(allowed_signs, hash1)
    print("The time used for 5 digit password crack is :", timeit.default_timer() - starttime)
    print(password5)


    """compute_possibilities(5)
    # OUTPUT
    Password possibilities for upper and lowercase letters and digits from 0-9
    For length 5 :  916132832
    For length 10 :  839299365868340224
    For range 5 to 10 :  853058371851163296
    
    The time used for 5 digit password crack is : 494.9458187909995
    X42aO
    """
