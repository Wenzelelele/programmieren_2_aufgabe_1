import numpy as np
from sort import bubble_sort
from load_data import load_data
import matplotlib.pyplot as plt
def main():
    data = load_data('activity.csv')
    power_W = data['PowerOriginal']
    print(power_W)
    sorted_power_W = bubble_sort(power_W)
    print(sorted_power_W[::-1])
    time_axis = np.arange(len(power_W)) / 60 # 1 Sekunde pro Sample

    plt.plot(time_axis, sorted_power_W[::-1])
    plt.xlabel("Zeit(min)")
    plt.ylabel("Leistung (W)")
    plt.title("Leistungskurve über Zeit")
    plt.savefig("C:\git\programmieren_2_aufgabe_1\\figures\\figure_1.png")
    plt.show()   
if __name__ == "__main__":
    main()