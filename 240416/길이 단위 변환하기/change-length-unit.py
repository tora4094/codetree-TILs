a = 9.2 #피트(ft) 
b = 1.3 #마일(mi)

FT_TO_CM = 30.48 # cm
MI_TO_CM = 160934 #cm

a_convert_cm = a * FT_TO_CM
b_convert_cm = b * MI_TO_CM

print("%0.1fft = %0.1fcm" %(a,a_convert_cm))
print("%0.1fmi = %0.1fcm" %(b,b_convert_cm))