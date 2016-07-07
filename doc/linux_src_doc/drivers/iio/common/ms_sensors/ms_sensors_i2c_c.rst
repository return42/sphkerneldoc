.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/common/ms_sensors/ms_sensors_i2c.c

.. _`ms_sensors_reset`:

ms_sensors_reset
================

.. c:function:: int ms_sensors_reset(void *cli, u8 cmd, unsigned int delay)

    Reset function

    :param void \*cli:
        pointer to device client

    :param u8 cmd:
        reset cmd. Depends on device in use

    :param unsigned int delay:
        usleep minimal delay after reset command is issued

.. _`ms_sensors_reset.description`:

Description
-----------

Generic I2C reset function for Measurement Specialties devices.

.. _`ms_sensors_reset.return`:

Return
------

0 on success, negative errno otherwise.

.. _`ms_sensors_read_prom_word`:

ms_sensors_read_prom_word
=========================

.. c:function:: int ms_sensors_read_prom_word(void *cli, int cmd, u16 *word)

    PROM word read function

    :param void \*cli:
        pointer to device client

    :param int cmd:
        PROM read cmd. Depends on device and prom id

    :param u16 \*word:
        pointer to word destination value

.. _`ms_sensors_read_prom_word.description`:

Description
-----------

Generic i2c prom word read function for Measurement Specialties devices.

.. _`ms_sensors_read_prom_word.return`:

Return
------

0 on success, negative errno otherwise.

.. _`ms_sensors_convert_and_read`:

ms_sensors_convert_and_read
===========================

.. c:function:: int ms_sensors_convert_and_read(void *cli, u8 conv, u8 rd, unsigned int delay, u32 *adc)

    ADC conversion & read function

    :param void \*cli:
        pointer to device client

    :param u8 conv:
        ADC conversion command. Depends on device in use

    :param u8 rd:
        ADC read command. Depends on device in use

    :param unsigned int delay:
        usleep minimal delay after conversion command is issued

    :param u32 \*adc:
        pointer to ADC destination value

.. _`ms_sensors_convert_and_read.description`:

Description
-----------

Generic ADC conversion & read function for Measurement Specialties
devices.
The function will issue conversion command, sleep appopriate delay, and
issue command to read ADC.

.. _`ms_sensors_convert_and_read.return`:

Return
------

0 on success, negative errno otherwise.

.. _`ms_sensors_crc_valid`:

ms_sensors_crc_valid
====================

.. c:function:: bool ms_sensors_crc_valid(u32 value)

    CRC check function

    :param u32 value:
        input and CRC compare value

.. _`ms_sensors_crc_valid.description`:

Description
-----------

Cyclic Redundancy Check function used in TSYS02D, HTU21, MS8607.
This function performs a x^8 + x^5 + x^4 + 1 polynomial CRC.
The argument contains CRC value in LSB byte while the bytes 1 and 2
are used for CRC computation.

.. _`ms_sensors_crc_valid.return`:

Return
------

1 if CRC is valid, 0 otherwise.

.. _`ms_sensors_read_serial`:

ms_sensors_read_serial
======================

.. c:function:: int ms_sensors_read_serial(struct i2c_client *client, u64 *sn)

    Serial number read function

    :param struct i2c_client \*client:
        *undescribed*

    :param u64 \*sn:
        pointer to 64-bits destination value

.. _`ms_sensors_read_serial.description`:

Description
-----------

Generic i2c serial number read function for Measurement Specialties devices.
This function is used for TSYS02d, HTU21, MS8607 chipset.

.. _`ms_sensors_read_serial.refer-to-datasheet`:

Refer to datasheet
------------------

http://www.meas-spec.com/downloads/HTU2X_Serial_Number_Reading.pdf

Sensor raw MSB serial number format is the following :
[ SNB3, CRC, SNB2, CRC, SNB1, CRC, SNB0, CRC]
Sensor raw LSB serial number format is the following :
[ X, X, SNC1, SNC0, CRC, SNA1, SNA0, CRC]
The resulting serial number is following :
[ SNA1, SNA0, SNB3, SNB2, SNB1, SNB0, SNC1, SNC0]

.. _`ms_sensors_read_serial.return`:

Return
------

0 on success, negative errno otherwise.

.. _`ms_sensors_write_resolution`:

ms_sensors_write_resolution
===========================

.. c:function:: ssize_t ms_sensors_write_resolution(struct ms_ht_dev *dev_data, u8 i)

    Set resolution function

    :param struct ms_ht_dev \*dev_data:
        pointer to temperature/humidity device data

    :param u8 i:
        resolution index to set

.. _`ms_sensors_write_resolution.description`:

Description
-----------

This function will program the appropriate resolution based on the index
provided when user space will set samp_freq channel.
This function is used for TSYS02D, HTU21 and MS8607 chipsets.

.. _`ms_sensors_write_resolution.return`:

Return
------

0 on success, negative errno otherwise.

.. _`ms_sensors_show_battery_low`:

ms_sensors_show_battery_low
===========================

.. c:function:: ssize_t ms_sensors_show_battery_low(struct ms_ht_dev *dev_data, char *buf)

    Show device battery low indicator

    :param struct ms_ht_dev \*dev_data:
        pointer to temperature/humidity device data

    :param char \*buf:
        pointer to char buffer to write result

.. _`ms_sensors_show_battery_low.description`:

Description
-----------

This function will read battery indicator value in the device and
return 1 if the device voltage is below 2.25V.
This function is used for TSYS02D, HTU21 and MS8607 chipsets.

.. _`ms_sensors_show_battery_low.return`:

Return
------

length of sprintf on success, negative errno otherwise.

.. _`ms_sensors_show_heater`:

ms_sensors_show_heater
======================

.. c:function:: ssize_t ms_sensors_show_heater(struct ms_ht_dev *dev_data, char *buf)

    Show device heater

    :param struct ms_ht_dev \*dev_data:
        pointer to temperature/humidity device data

    :param char \*buf:
        pointer to char buffer to write result

.. _`ms_sensors_show_heater.description`:

Description
-----------

This function will read heater enable value in the device and
return 1 if the heater is enabled.
This function is used for HTU21 and MS8607 chipsets.

.. _`ms_sensors_show_heater.return`:

Return
------

length of sprintf on success, negative errno otherwise.

.. _`ms_sensors_write_heater`:

ms_sensors_write_heater
=======================

.. c:function:: ssize_t ms_sensors_write_heater(struct ms_ht_dev *dev_data, const char *buf, size_t len)

    Write device heater

    :param struct ms_ht_dev \*dev_data:
        pointer to temperature/humidity device data

    :param const char \*buf:
        pointer to char buffer from user space

    :param size_t len:
        length of buf

.. _`ms_sensors_write_heater.description`:

Description
-----------

This function will write 1 or 0 value in the device
to enable or disable heater.
This function is used for HTU21 and MS8607 chipsets.

.. _`ms_sensors_write_heater.return`:

Return
------

length of buffer, negative errno otherwise.

.. _`ms_sensors_ht_read_temperature`:

ms_sensors_ht_read_temperature
==============================

.. c:function:: int ms_sensors_ht_read_temperature(struct ms_ht_dev *dev_data, s32 *temperature)

    Read temperature

    :param struct ms_ht_dev \*dev_data:
        pointer to temperature/humidity device data

    :param s32 \*temperature:
        pointer to temperature destination value

.. _`ms_sensors_ht_read_temperature.description`:

Description
-----------

This function will get temperature ADC value from the device,
check the CRC and compute the temperature value.
This function is used for TSYS02D, HTU21 and MS8607 chipsets.

.. _`ms_sensors_ht_read_temperature.return`:

Return
------

0 on success, negative errno otherwise.

.. _`ms_sensors_ht_read_humidity`:

ms_sensors_ht_read_humidity
===========================

.. c:function:: int ms_sensors_ht_read_humidity(struct ms_ht_dev *dev_data, u32 *humidity)

    Read humidity

    :param struct ms_ht_dev \*dev_data:
        pointer to temperature/humidity device data

    :param u32 \*humidity:
        pointer to humidity destination value

.. _`ms_sensors_ht_read_humidity.description`:

Description
-----------

This function will get humidity ADC value from the device,
check the CRC and compute the temperature value.
This function is used for HTU21 and MS8607 chipsets.

.. _`ms_sensors_ht_read_humidity.return`:

Return
------

0 on success, negative errno otherwise.

.. _`ms_sensors_tp_crc_valid`:

ms_sensors_tp_crc_valid
=======================

.. c:function:: bool ms_sensors_tp_crc_valid(u16 *prom, u8 len)

    CRC check function for Temperature and pressure devices. This function is only used when reading PROM coefficients

    :param u16 \*prom:
        pointer to PROM coefficients array

    :param u8 len:
        length of PROM coefficients array

.. _`ms_sensors_tp_crc_valid.return`:

Return
------

True if CRC is ok.

.. _`ms_sensors_tp_read_prom`:

ms_sensors_tp_read_prom
=======================

.. c:function:: int ms_sensors_tp_read_prom(struct ms_tp_dev *dev_data)

    prom coeff read function

    :param struct ms_tp_dev \*dev_data:
        pointer to temperature/pressure device data

.. _`ms_sensors_tp_read_prom.description`:

Description
-----------

This function will read prom coefficients and check CRC.
This function is used for MS5637 and MS8607 chipsets.

.. _`ms_sensors_tp_read_prom.return`:

Return
------

0 on success, negative errno otherwise.

.. _`ms_sensors_read_temp_and_pressure`:

ms_sensors_read_temp_and_pressure
=================================

.. c:function:: int ms_sensors_read_temp_and_pressure(struct ms_tp_dev *dev_data, int *temperature, unsigned int *pressure)

    read temp and pressure

    :param struct ms_tp_dev \*dev_data:
        pointer to temperature/pressure device data

    :param int \*temperature:
        pointer to temperature destination value

    :param unsigned int \*pressure:
        pointer to pressure destination value

.. _`ms_sensors_read_temp_and_pressure.description`:

Description
-----------

This function will read ADC and compute pressure and temperature value.
This function is used for MS5637 and MS8607 chipsets.

.. _`ms_sensors_read_temp_and_pressure.return`:

Return
------

0 on success, negative errno otherwise.

.. This file was automatic generated / don't edit.

