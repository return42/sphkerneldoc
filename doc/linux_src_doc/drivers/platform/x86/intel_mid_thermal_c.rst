.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/x86/intel_mid_thermal.c

.. _`to_msic_die_temp`:

to_msic_die_temp
================

.. c:function:: int to_msic_die_temp(uint16_t adc_val)

    converts adc_val to msic_die temperature

    :param uint16_t adc_val:
        ADC value to be converted

.. _`to_msic_die_temp.description`:

Description
-----------

Can sleep

.. _`is_valid_adc`:

is_valid_adc
============

.. c:function:: int is_valid_adc(uint16_t adc_val, uint16_t min, uint16_t max)

    checks whether the adc code is within the defined range

    :param uint16_t adc_val:
        *undescribed*

    :param uint16_t min:
        minimum value for the sensor

    :param uint16_t max:
        maximum value for the sensor

.. _`is_valid_adc.description`:

Description
-----------

Can sleep

.. _`adc_to_temp`:

adc_to_temp
===========

.. c:function:: int adc_to_temp(int direct, uint16_t adc_val, int *tp)

    converts the ADC code to temperature in C

    :param int direct:
        true if ths channel is direct index

    :param uint16_t adc_val:
        the adc_val that needs to be converted

    :param int \*tp:
        temperature return value

.. _`adc_to_temp.description`:

Description
-----------

Linear approximation is used to covert the skin adc value into temperature.
This technique is used to avoid very long look-up table to get
the appropriate temp value from ADC value.
The adc code vs sensor temp curve is split into five parts
to achieve very close approximate temp value with less than
0.5C error

.. _`mid_read_temp`:

mid_read_temp
=============

.. c:function:: int mid_read_temp(struct thermal_zone_device *tzd, int *temp)

    read sensors for temperature

    :param struct thermal_zone_device \*tzd:
        *undescribed*

    :param int \*temp:
        holds the current temperature for the sensor after reading

.. _`mid_read_temp.description`:

Description
-----------

reads the adc_code from the channel and converts it to real
temperature. The converted value is stored in temp.

Can sleep

.. _`configure_adc`:

configure_adc
=============

.. c:function:: int configure_adc(int val)

    enables/disables the ADC for conversion

    :param int val:
        zero: disables the ADC non-zero:enables the ADC

.. _`configure_adc.description`:

Description
-----------

Enable/Disable the ADC depending on the argument

Can sleep

.. _`set_up_therm_channel`:

set_up_therm_channel
====================

.. c:function:: int set_up_therm_channel(u16 base_addr)

    enable thermal channel for conversion

    :param u16 base_addr:
        index of free msic ADC channel

.. _`set_up_therm_channel.description`:

Description
-----------

Enable all the three channels for conversion

Can sleep

.. _`reset_stopbit`:

reset_stopbit
=============

.. c:function:: int reset_stopbit(uint16_t addr)

    sets the stop bit to 0 on the given channel

    :param uint16_t addr:
        address of the channel

.. _`reset_stopbit.description`:

Description
-----------

Can sleep

.. _`find_free_channel`:

find_free_channel
=================

.. c:function:: int find_free_channel( void)

    finds an empty channel for conversion

    :param  void:
        no arguments

.. _`find_free_channel.description`:

Description
-----------

If the ADC is not enabled then start using 0th channel
itself. Otherwise find an empty channel by looking for a
channel in which the stopbit is set to 1. returns the index
of the first free channel if succeeds or an error code.

.. _`find_free_channel.context`:

Context
-------

can sleep

.. _`find_free_channel.fixme`:

FIXME
-----

Ultimately the channel allocator will move into the intel_scu_ipc
code.

.. _`mid_initialize_adc`:

mid_initialize_adc
==================

.. c:function:: int mid_initialize_adc(struct device *dev)

    initializing the ADC

    :param struct device \*dev:
        our device structure

.. _`mid_initialize_adc.description`:

Description
-----------

Initialize the ADC for reading thermistor values. Can sleep.

.. _`initialize_sensor`:

initialize_sensor
=================

.. c:function:: struct thermal_device_info *initialize_sensor(int index)

    sets default temp and timer ranges

    :param int index:
        index of the sensor

.. _`initialize_sensor.context`:

Context
-------

can sleep

.. _`mid_thermal_resume`:

mid_thermal_resume
==================

.. c:function:: int mid_thermal_resume(struct device *dev)

    resume routine

    :param struct device \*dev:
        device structure

.. _`mid_thermal_resume.mid-thermal-resume`:

mid thermal resume
------------------

re-initializes the adc. Can sleep.

.. _`mid_thermal_suspend`:

mid_thermal_suspend
===================

.. c:function:: int mid_thermal_suspend(struct device *dev)

    suspend routine

    :param struct device \*dev:
        device structure

.. _`mid_thermal_suspend.description`:

Description
-----------

mid thermal suspend implements the suspend functionality
by stopping the ADC. Can sleep.

.. _`read_curr_temp`:

read_curr_temp
==============

.. c:function:: int read_curr_temp(struct thermal_zone_device *tzd, int *temp)

    reads the current temperature and stores in temp

    :param struct thermal_zone_device \*tzd:
        *undescribed*

    :param int \*temp:
        holds the current temperature value after reading

.. _`read_curr_temp.description`:

Description
-----------

Can sleep

.. _`mid_thermal_probe`:

mid_thermal_probe
=================

.. c:function:: int mid_thermal_probe(struct platform_device *pdev)

    mfld thermal initialize

    :param struct platform_device \*pdev:
        platform device structure

.. _`mid_thermal_probe.description`:

Description
-----------

mid thermal probe initializes the hardware and registers
all the sensors with the generic thermal framework. Can sleep.

.. _`mid_thermal_remove`:

mid_thermal_remove
==================

.. c:function:: int mid_thermal_remove(struct platform_device *pdev)

    mfld thermal finalize

    :param struct platform_device \*pdev:
        *undescribed*

.. _`mid_thermal_remove.description`:

Description
-----------

MLFD thermal remove unregisters all the sensors from the generic
thermal framework. Can sleep.

.. This file was automatic generated / don't edit.

