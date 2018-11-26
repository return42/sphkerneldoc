.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/ti-soc-thermal/ti-bandgap.c

.. _`ti_bandgap_readl`:

ti_bandgap_readl
================

.. c:function:: u32 ti_bandgap_readl(struct ti_bandgap *bgp, u32 reg)

    simple read helper function

    :param bgp:
        pointer to ti_bandgap structure
    :type bgp: struct ti_bandgap \*

    :param reg:
        desired register (offset) to be read
    :type reg: u32

.. _`ti_bandgap_readl.description`:

Description
-----------

Helper function to read bandgap registers. It uses the io remapped area.

.. _`ti_bandgap_readl.return`:

Return
------

the register value.

.. _`ti_bandgap_writel`:

ti_bandgap_writel
=================

.. c:function:: void ti_bandgap_writel(struct ti_bandgap *bgp, u32 val, u32 reg)

    simple write helper function

    :param bgp:
        pointer to ti_bandgap structure
    :type bgp: struct ti_bandgap \*

    :param val:
        desired register value to be written
    :type val: u32

    :param reg:
        desired register (offset) to be written
    :type reg: u32

.. _`ti_bandgap_writel.description`:

Description
-----------

Helper function to write bandgap registers. It uses the io remapped area.

.. _`macro-to-update-bits.`:

macro to update bits.
=====================

\ :c:func:`RMW_BITS`\  - used to read, modify and update bandgap bitfields.
The value passed will be shifted.

.. _`ti_bandgap_power`:

ti_bandgap_power
================

.. c:function:: int ti_bandgap_power(struct ti_bandgap *bgp, bool on)

    controls the power state of a bandgap device

    :param bgp:
        pointer to ti_bandgap structure
    :type bgp: struct ti_bandgap \*

    :param on:
        desired power state (1 - on, 0 - off)
    :type on: bool

.. _`ti_bandgap_power.description`:

Description
-----------

Used to power on/off a bandgap device instance. Only used on those
that features tempsoff bit.

.. _`ti_bandgap_power.return`:

Return
------

0 on success, -ENOTSUPP if tempsoff is not supported.

.. _`ti_errata814_bandgap_read_temp`:

ti_errata814_bandgap_read_temp
==============================

.. c:function:: u32 ti_errata814_bandgap_read_temp(struct ti_bandgap *bgp, u32 reg)

    helper function to read dra7 sensor temperature

    :param bgp:
        pointer to ti_bandgap structure
    :type bgp: struct ti_bandgap \*

    :param reg:
        desired register (offset) to be read
    :type reg: u32

.. _`ti_errata814_bandgap_read_temp.description`:

Description
-----------

Function to read dra7 bandgap sensor temperature. This is done separately
so as to workaround the errata "Bandgap Temperature read Dtemp can be
corrupted" - Errata ID: i814".
Read accesses to registers listed below can be corrupted due to incorrect
resynchronization between clock domains.
Read access to registers below can be corrupted :
CTRL_CORE_DTEMP_MPU/GPU/CORE/DSPEVE/IVA_n (n = 0 to 4)
CTRL_CORE_TEMP_SENSOR_MPU/GPU/CORE/DSPEVE/IVA_n

.. _`ti_errata814_bandgap_read_temp.return`:

Return
------

the register value.

.. _`ti_bandgap_read_temp`:

ti_bandgap_read_temp
====================

.. c:function:: u32 ti_bandgap_read_temp(struct ti_bandgap *bgp, int id)

    helper function to read sensor temperature

    :param bgp:
        pointer to ti_bandgap structure
    :type bgp: struct ti_bandgap \*

    :param id:
        bandgap sensor id
    :type id: int

.. _`ti_bandgap_read_temp.description`:

Description
-----------

Function to concentrate the steps to read sensor temperature register.
This function is desired because, depending on bandgap device version,
it might be needed to freeze the bandgap state machine, before fetching
the register value.

.. _`ti_bandgap_read_temp.return`:

Return
------

temperature in ADC values.

.. _`ti_bandgap_talert_irq_handler`:

ti_bandgap_talert_irq_handler
=============================

.. c:function:: irqreturn_t ti_bandgap_talert_irq_handler(int irq, void *data)

    handles Temperature alert IRQs

    :param irq:
        IRQ number
    :type irq: int

    :param data:
        private data (struct ti_bandgap \*)
    :type data: void \*

.. _`ti_bandgap_talert_irq_handler.description`:

Description
-----------

This is the Talert handler. Use it only if bandgap device features
HAS(TALERT). This handler goes over all sensors and checks their
conditions and acts accordingly. In case there are events pending,
it will reset the event mask to wait for the opposite event (next event).
Every time there is a new event, it will be reported to thermal layer.

.. _`ti_bandgap_talert_irq_handler.return`:

Return
------

IRQ_HANDLED

.. _`ti_bandgap_tshut_irq_handler`:

ti_bandgap_tshut_irq_handler
============================

.. c:function:: irqreturn_t ti_bandgap_tshut_irq_handler(int irq, void *data)

    handles Temperature shutdown signal

    :param irq:
        IRQ number
    :type irq: int

    :param data:
        private data (unused)
    :type data: void \*

.. _`ti_bandgap_tshut_irq_handler.description`:

Description
-----------

This is the Tshut handler. Use it only if bandgap device features
HAS(TSHUT). If any sensor fires the Tshut signal, we simply shutdown
the system.

.. _`ti_bandgap_tshut_irq_handler.return`:

Return
------

IRQ_HANDLED

.. _`ti_bandgap_adc_to_mcelsius`:

ti_bandgap_adc_to_mcelsius
==========================

.. c:function:: int ti_bandgap_adc_to_mcelsius(struct ti_bandgap *bgp, int adc_val, int *t)

    converts an ADC value to mCelsius scale

    :param bgp:
        struct ti_bandgap pointer
    :type bgp: struct ti_bandgap \*

    :param adc_val:
        value in ADC representation
    :type adc_val: int

    :param t:
        address where to write the resulting temperature in mCelsius
    :type t: int \*

.. _`ti_bandgap_adc_to_mcelsius.description`:

Description
-----------

Simple conversion from ADC representation to mCelsius. In case the ADC value
is out of the ADC conv table range, it returns -ERANGE, 0 on success.
The conversion table is indexed by the ADC values.

.. _`ti_bandgap_adc_to_mcelsius.return`:

Return
------

0 if conversion was successful, else -ERANGE in case the \ ``adc_val``\ 
argument is out of the ADC conv table range.

.. _`ti_bandgap_validate`:

ti_bandgap_validate
===================

.. c:function:: int ti_bandgap_validate(struct ti_bandgap *bgp, int id)

    helper to check the sanity of a struct ti_bandgap

    :param bgp:
        struct ti_bandgap pointer
    :type bgp: struct ti_bandgap \*

    :param id:
        bandgap sensor id
    :type id: int

.. _`ti_bandgap_validate.description`:

Description
-----------

Checks if the bandgap pointer is valid and if the sensor id is also
applicable.

.. _`ti_bandgap_validate.return`:

Return
------

0 if no errors, -EINVAL for invalid \ ``bgp``\  pointer or -ERANGE if
\ ``id``\  cannot index \ ``bgp``\  sensors.

.. _`ti_bandgap_read_counter`:

ti_bandgap_read_counter
=======================

.. c:function:: void ti_bandgap_read_counter(struct ti_bandgap *bgp, int id, int *interval)

    read the sensor counter

    :param bgp:
        pointer to bandgap instance
    :type bgp: struct ti_bandgap \*

    :param id:
        sensor id
    :type id: int

    :param interval:
        resulting update interval in miliseconds
    :type interval: int \*

.. _`ti_bandgap_read_counter_delay`:

ti_bandgap_read_counter_delay
=============================

.. c:function:: void ti_bandgap_read_counter_delay(struct ti_bandgap *bgp, int id, int *interval)

    read the sensor counter delay

    :param bgp:
        pointer to bandgap instance
    :type bgp: struct ti_bandgap \*

    :param id:
        sensor id
    :type id: int

    :param interval:
        resulting update interval in miliseconds
    :type interval: int \*

.. _`ti_bandgap_read_update_interval`:

ti_bandgap_read_update_interval
===============================

.. c:function:: int ti_bandgap_read_update_interval(struct ti_bandgap *bgp, int id, int *interval)

    read the sensor update interval

    :param bgp:
        pointer to bandgap instance
    :type bgp: struct ti_bandgap \*

    :param id:
        sensor id
    :type id: int

    :param interval:
        resulting update interval in miliseconds
    :type interval: int \*

.. _`ti_bandgap_read_update_interval.return`:

Return
------

0 on success or the proper error code

.. _`ti_bandgap_write_counter_delay`:

ti_bandgap_write_counter_delay
==============================

.. c:function:: int ti_bandgap_write_counter_delay(struct ti_bandgap *bgp, int id, u32 interval)

    set the counter_delay

    :param bgp:
        pointer to bandgap instance
    :type bgp: struct ti_bandgap \*

    :param id:
        sensor id
    :type id: int

    :param interval:
        desired update interval in miliseconds
    :type interval: u32

.. _`ti_bandgap_write_counter_delay.return`:

Return
------

0 on success or the proper error code

.. _`ti_bandgap_write_counter`:

ti_bandgap_write_counter
========================

.. c:function:: void ti_bandgap_write_counter(struct ti_bandgap *bgp, int id, u32 interval)

    set the bandgap sensor counter

    :param bgp:
        pointer to bandgap instance
    :type bgp: struct ti_bandgap \*

    :param id:
        sensor id
    :type id: int

    :param interval:
        desired update interval in miliseconds
    :type interval: u32

.. _`ti_bandgap_write_update_interval`:

ti_bandgap_write_update_interval
================================

.. c:function:: int ti_bandgap_write_update_interval(struct ti_bandgap *bgp, int id, u32 interval)

    set the update interval

    :param bgp:
        pointer to bandgap instance
    :type bgp: struct ti_bandgap \*

    :param id:
        sensor id
    :type id: int

    :param interval:
        desired update interval in miliseconds
    :type interval: u32

.. _`ti_bandgap_write_update_interval.return`:

Return
------

0 on success or the proper error code

.. _`ti_bandgap_read_temperature`:

ti_bandgap_read_temperature
===========================

.. c:function:: int ti_bandgap_read_temperature(struct ti_bandgap *bgp, int id, int *temperature)

    report current temperature

    :param bgp:
        pointer to bandgap instance
    :type bgp: struct ti_bandgap \*

    :param id:
        sensor id
    :type id: int

    :param temperature:
        resulting temperature
    :type temperature: int \*

.. _`ti_bandgap_read_temperature.return`:

Return
------

0 on success or the proper error code

.. _`ti_bandgap_set_sensor_data`:

ti_bandgap_set_sensor_data
==========================

.. c:function:: int ti_bandgap_set_sensor_data(struct ti_bandgap *bgp, int id, void *data)

    helper function to store thermal framework related data.

    :param bgp:
        pointer to bandgap instance
    :type bgp: struct ti_bandgap \*

    :param id:
        sensor id
    :type id: int

    :param data:
        thermal framework related data to be stored
    :type data: void \*

.. _`ti_bandgap_set_sensor_data.return`:

Return
------

0 on success or the proper error code

.. _`ti_bandgap_get_sensor_data`:

ti_bandgap_get_sensor_data
==========================

.. c:function:: void *ti_bandgap_get_sensor_data(struct ti_bandgap *bgp, int id)

    helper function to get thermal framework related data.

    :param bgp:
        pointer to bandgap instance
    :type bgp: struct ti_bandgap \*

    :param id:
        sensor id
    :type id: int

.. _`ti_bandgap_get_sensor_data.return`:

Return
------

data stored by set function with sensor id on success or NULL

.. _`ti_bandgap_force_single_read`:

ti_bandgap_force_single_read
============================

.. c:function:: int ti_bandgap_force_single_read(struct ti_bandgap *bgp, int id)

    executes 1 single ADC conversion

    :param bgp:
        pointer to struct ti_bandgap
    :type bgp: struct ti_bandgap \*

    :param id:
        sensor id which it is desired to read 1 temperature
    :type id: int

.. _`ti_bandgap_force_single_read.description`:

Description
-----------

Used to initialize the conversion state machine and set it to a valid
state. Called during device initialization and context restore events.

.. _`ti_bandgap_force_single_read.return`:

Return
------

0

.. _`ti_bandgap_set_continuous_mode`:

ti_bandgap_set_continuous_mode
==============================

.. c:function:: int ti_bandgap_set_continuous_mode(struct ti_bandgap *bgp)

    One time enabling of continuous mode

    :param bgp:
        pointer to struct ti_bandgap
    :type bgp: struct ti_bandgap \*

.. _`ti_bandgap_set_continuous_mode.description`:

Description
-----------

Call this function only if HAS(MODE_CONFIG) is set. As this driver may
be used for junction temperature monitoring, it is desirable that the
sensors are operational all the time, so that alerts are generated
properly.

.. _`ti_bandgap_set_continuous_mode.return`:

Return
------

0

.. _`ti_bandgap_get_trend`:

ti_bandgap_get_trend
====================

.. c:function:: int ti_bandgap_get_trend(struct ti_bandgap *bgp, int id, int *trend)

    To fetch the temperature trend of a sensor

    :param bgp:
        pointer to struct ti_bandgap
    :type bgp: struct ti_bandgap \*

    :param id:
        id of the individual sensor
    :type id: int

    :param trend:
        Pointer to trend.
    :type trend: int \*

.. _`ti_bandgap_get_trend.description`:

Description
-----------

This function needs to be called to fetch the temperature trend of a
Particular sensor. The function computes the difference in temperature
w.r.t time. For the bandgaps with built in history buffer the temperatures
are read from the buffer and for those without the Buffer -ENOTSUPP is
returned.

.. _`ti_bandgap_get_trend.return`:

Return
------

0 if no error, else return corresponding error. If no
error then the trend value is passed on to trend parameter

.. _`ti_bandgap_tshut_init`:

ti_bandgap_tshut_init
=====================

.. c:function:: int ti_bandgap_tshut_init(struct ti_bandgap *bgp, struct platform_device *pdev)

    setup and initialize tshut handling

    :param bgp:
        pointer to struct ti_bandgap
    :type bgp: struct ti_bandgap \*

    :param pdev:
        pointer to device struct platform_device
    :type pdev: struct platform_device \*

.. _`ti_bandgap_tshut_init.description`:

Description
-----------

Call this function only in case the bandgap features HAS(TSHUT).
In this case, the driver needs to handle the TSHUT signal as an IRQ.
The IRQ is wired as a GPIO, and for this purpose, it is required
to specify which GPIO line is used. TSHUT IRQ is fired anytime
one of the bandgap sensors violates the TSHUT high/hot threshold.
And in that case, the system must go off.

.. _`ti_bandgap_tshut_init.return`:

Return
------

0 if no error, else error status

.. _`ti_bandgap_talert_init`:

ti_bandgap_talert_init
======================

.. c:function:: int ti_bandgap_talert_init(struct ti_bandgap *bgp, struct platform_device *pdev)

    setup and initialize talert handling

    :param bgp:
        pointer to struct ti_bandgap
    :type bgp: struct ti_bandgap \*

    :param pdev:
        pointer to device struct platform_device
    :type pdev: struct platform_device \*

.. _`ti_bandgap_talert_init.description`:

Description
-----------

Call this function only in case the bandgap features HAS(TALERT).
In this case, the driver needs to handle the TALERT signals as an IRQs.
TALERT is a normal IRQ and it is fired any time thresholds (hot or cold)
are violated. In these situation, the driver must reprogram the thresholds,
accordingly to specified policy.

.. _`ti_bandgap_talert_init.return`:

Return
------

0 if no error, else return corresponding error.

.. _`ti_bandgap_build`:

ti_bandgap_build
================

.. c:function:: struct ti_bandgap *ti_bandgap_build(struct platform_device *pdev)

    parse DT and setup a struct ti_bandgap

    :param pdev:
        pointer to device struct platform_device
    :type pdev: struct platform_device \*

.. _`ti_bandgap_build.description`:

Description
-----------

Used to read the device tree properties accordingly to the bandgap
matching version. Based on bandgap version and its capabilities it
will build a struct ti_bandgap out of the required DT entries.

.. _`ti_bandgap_build.return`:

Return
------

valid bandgap structure if successful, else returns ERR_PTR
return value must be verified with IS_ERR.

.. This file was automatic generated / don't edit.

