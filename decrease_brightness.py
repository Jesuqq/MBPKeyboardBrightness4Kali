filepath = "/sys/class/leds/smc::kbd_backlight/brightness"

with open(filepath, 'r') as brightnessFile:
    brightness = brightnessFile.read().replace('\n', '')

with open(filepath, 'w') as brightnessFile:
    brightnessFile.write(str(int(brightness)-2))
