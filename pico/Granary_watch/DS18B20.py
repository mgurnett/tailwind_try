import machine, onewire, ds18x20, time

ds_pin = machine.Pin(26)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))


if __name__ == "__main__":
  roms = ds_sensor.scan()
  print('Found DS devices: ', roms)  # Shows bytearray directly

  while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
      # Print ROM as hexadecimal string (optional)
      rom_hex = rom.hex()
      print(f'rom: {rom_hex}')  

      tempC = ds_sensor.read_temp(rom)
      print('temperature (ºC):', "{:.2f}".format(tempC))

    time.sleep(5)