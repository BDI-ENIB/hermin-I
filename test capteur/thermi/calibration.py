from machine import ADC
adc = ADC()
adc.vref(1100)

# Output Vref of P22
adc.vref_to_pin('P22')
