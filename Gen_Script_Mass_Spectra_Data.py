# Date fuer die Generierung von exemplarischen Peaks eines Massenspektrums
# Verwendet fuer das Literaturseminar Bioinformatik SS 23

import random

if __name__ == "__main__":
    num_values = 48
    generated_rand_values = []
    generated_rand_values2 = []

    for i in range(1, num_values):
        rand_val = random.randint(10, 30)/10
        rand_val2 = random.randint(0, 100)/500
        while rand_val == 0.0:
            rand_val = random.randint(0, 30)/10
        print ("\\draw[thick] (" + str((i/10) + rand_val2) + ", 0.0) -- (" + str((i/10) + rand_val2) + ", " + str(rand_val) + ");")
        generated_rand_values.append(rand_val)
        generated_rand_values2.append(rand_val2)

    print("")
    for i in range(1, num_values):
        print ("\\draw[thick] (" + str((i/10) + generated_rand_values2[i - 1]) + ", 0.0) -- (" + str((i/10) + generated_rand_values2[i - 1]) + ", {ln(" + str(generated_rand_values[i - 1]) + ")});")
