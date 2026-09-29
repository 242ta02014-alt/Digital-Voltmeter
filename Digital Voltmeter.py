# Digital Voltmeter - Simple Python

voltage = float(input("Enter voltage: "))

print("\n--- DIGITAL VOLTMETER ---")
print("Voltage =", voltage, "V")

if voltage > 250:
    print("Status: HIGH VOLTAGE")
elif voltage < 180:
    print("Status: LOW VOLTAGE")
else:
    print("Status: NORMAL")
