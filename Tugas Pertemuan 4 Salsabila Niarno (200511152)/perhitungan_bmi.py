def bodyMassIndex(berat, tinggi):
    bodyMassIndex = berat / ((tinggi/100)**2)
    if bodyMassIndex < 18.5:
        print("BMI Anda sebesar:", bodyMassIndex,", Berat badan Anda kurang")
    elif 18.5 <= bodyMassIndex < 23:
        print("BMI Anda sebesar:", bodyMassIndex,", Normal")
    elif 23 <= bodyMassIndex <30:
        print("BMI Anda sebesar:", bodyMassIndex,", Berat badan berlebih")
    else:
        print("BMI Anda sebesar:", bodyMassIndex,", Anda Obesitas")
    return bodyMassIndex