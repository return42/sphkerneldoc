.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/ti-soc-thermal/ti-bandgap.c

.. _`ti_bandgap_readl`:

ti_bandgap_readl
================

.. c:function:: u32 ti_bandgap_readl(struct ti_bandgap *bgp, u32 reg)

    simple read helper function

    :param struct ti_bandgap \*bgp:
        pointer to ti_bandgap structure

    :param u32 reg:
        desired register (offset) to be read

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

    :param struct ti_bandgap \*bgp:
        pointer to ti_bandgap structure

    :param u32 val:
        desired register value to be written

    :param u32 reg:
        desired register (offset) to be written

.. _`ti_bandgap_writel.description`:

Description
-----------

Helper function to write bandgap registers. It uses the io remapped area.

.. _`ti_bandgap_power`:

ti_bandgap_power
================

.. c:function:: int ti_bandgap_power(struct ti_bandgap *bgp, bool on)

    controls the power state of a bandgap device

    :param struct ti_bandgap \*bgp:
        pointer to ti_bandgap structure

    :param bool on:
        desired power state (1 - on, 0 - off)

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

    :param struct ti_bandgap \*bgp:
        pointer to ti_bandgap structure

    :param u32 reg:
        desired register (offset) to be read

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

    :param struct ti_bandgap \*bgp:
        pointer to ti_bandgap structure

    :param int id:
        bandgap sensor id

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

    :param int irq:
        IRQ number

    :param void \*data:
        private data (struct ti_bandgap \*)

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

    :param int irq:
        IRQ number

    :param void \*data:
        private data (unused)

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

    :param struct ti_bandgap \*bgp:
        struct ti_bandgap pointer

    :param int adc_val:
        value in ADC representation

    :param int \*t:
        address where to write the resulting temperature in mCelsius

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

.. _`ti_bandgap_mcelsius_to_adc`:

ti_bandgap_mcelsius_to_adc
==========================

.. c:function:: int ti_bandgap_mcelsius_to_adc(struct ti_bandgap *bgp, long temp, int *adc)

    converts a mCelsius value to ADC scale

    :param struct ti_bandgap \*bgp:
        struct ti_bandgap pointer

    :param long temp:
        value in mCelsius

    :param int \*adc:
        address where to write the resulting temperature in ADC representation

.. _`ti_bandgap_mcelsius_to_adc.description`:

Description
-----------

Simple conversion from mCelsius to ADC values. In case the temp value
is out of the ADC conv table range, it returns -ERANGE, 0 on success.
The conversion table is indexed by the ADC values.

.. _`ti_bandgap_mcelsius_to_adc.return`:

Return
------

0 if conversion was successful, else -ERANGE in case the \ ``temp``\ 
argument is out of the ADC conv table range.

.. _`ti_bandgap_add_hyst`:

ti_bandgap_add_hyst
===================

.. c:function:: int ti_bandgap_add_hyst(struct ti_bandgap *bgp, int adc_val, int hyst_val, u32 *sum)

    add hysteresis (in mCelsius) to an ADC value

    :param struct ti_bandgap \*bgp:
        struct ti_bandgap pointer

    :param int adc_val:
        temperature value in ADC representation

    :param int hyst_val:
        hysteresis value in mCelsius

    :param u32 \*sum:
        address where to write the resulting temperature (in ADC scale)

.. _`ti_bandgap_add_hyst.description`:

Description
-----------

Adds an hysteresis value (in mCelsius) to a ADC temperature value.

.. _`ti_bandgap_add_hyst.return`:

Return
------

0 on success, -ERANGE otherwise.

.. _`ti_bandgap_unmask_interrupts`:

ti_bandgap_unmask_interrupts
============================

.. c:function:: void ti_bandgap_unmask_interrupts(struct ti_bandgap *bgp, int id, u32 t_hot, u32 t_cold)

    unmasks the events of thot & tcold

    :param struct ti_bandgap \*bgp:
        struct ti_bandgap pointer

    :param int id:
        bandgap sensor id

    :param u32 t_hot:
        hot temperature value to trigger alert signal

    :param u32 t_cold:
        cold temperature value to trigger alert signal

.. _`ti_bandgap_unmask_interrupts.description`:

Description
-----------

Checks the requested t_hot and t_cold values and configures the IRQ event
masks accordingly. Call this function only if bandgap features HAS(TALERT).

.. _`ti_bandgap_update_alert_threshold`:

ti_bandgap_update_alert_threshold
=================================

.. c:function:: int ti_bandgap_update_alert_threshold(struct ti_bandgap *bgp, int id, int val, bool hot)

    sequence to update thresholds

    :param struct ti_bandgap \*bgp:
        struct ti_bandgap pointer

    :param int id:
        bandgap sensor id

    :param int val:
        value (ADC) of a new threshold

    :param bool hot:
        desired threshold to be updated. true if threshold hot, false if
        threshold cold

.. _`ti_bandgap_update_alert_threshold.description`:

Description
-----------

It will program the required thresholds (hot and cold) for TALERT signal.
This function can be used to update t_hot or t_cold, depending on \ ``hot``\  value.
It checks the resulting t_hot and t_cold values, based on the new passed \ ``val``\ 
and configures the thresholds so that t_hot is always greater than t_cold.
Call this function only if bandgap features HAS(TALERT).

.. _`ti_bandgap_update_alert_threshold.return`:

Return
------

0 if no error, else corresponding error

.. _`ti_bandgap_validate`:

ti_bandgap_validate
===================

.. c:function:: int ti_bandgap_validate(struct ti_bandgap *bgp, int id)

    helper to check the sanity of a struct ti_bandgap

    :param struct ti_bandgap \*bgp:
        struct ti_bandgap pointer

    :param int id:
        bandgap sensor id

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

.. _`_ti_bandgap_write_threshold`:

_ti_bandgap_write_threshold
===========================

.. c:function:: int _ti_bandgap_write_threshold(struct ti_bandgap *bgp, int id, int val, bool hot)

    helper to update TALERT t_cold or t_hot

    :param struct ti_bandgap \*bgp:
        struct ti_bandgap pointer

    :param int id:
        bandgap sensor id

    :param int val:
        value (mCelsius) of a new threshold

    :param bool hot:
        desired threshold to be updated. true if threshold hot, false if
        threshold cold

.. _`_ti_bandgap_write_threshold.description`:

Description
-----------

It will update the required thresholds (hot and cold) for TALERT signal.
This function can be used to update t_hot or t_cold, depending on \ ``hot``\  value.
Validates the mCelsius range and update the requested threshold.
Call this function only if bandgap features HAS(TALERT).

.. _`_ti_bandgap_write_threshold.return`:

Return
------

0 if no error, else corresponding error value.

.. _`_ti_bandgap_read_threshold`:

_ti_bandgap_read_threshold
==========================

.. c:function:: int _ti_bandgap_read_threshold(struct ti_bandgap *bgp, int id, int *val, bool hot)

    helper to read TALERT t_cold or t_hot

    :param struct ti_bandgap \*bgp:
        struct ti_bandgap pointer

    :param int id:
        bandgap sensor id

    :param int \*val:
        value (mCelsius) of a threshold

    :param bool hot:
        desired threshold to be read. true if threshold hot, false if
        threshold cold

.. _`_ti_bandgap_read_threshold.description`:

Description
-----------

It will fetch the required thresholds (hot and cold) for TALERT signal.
This function can be used to read t_hot or t_cold, depending on \ ``hot``\  value.
Call this function only if bandgap features HAS(TALERT).

.. _`_ti_bandgap_read_threshold.return`:

Return
------

0 if no error, -ENOTSUPP if it has no TALERT support, or the
corresponding error value if some operation fails.

.. _`ti_bandgap_read_thot`:

ti_bandgap_read_thot
====================

.. c:function:: int ti_bandgap_read_thot(struct ti_bandgap *bgp, int id, int *thot)

    reads sensor current thot

    :param struct ti_bandgap \*bgp:
        pointer to bandgap instance

    :param int id:
        sensor id

    :param int \*thot:
        resulting current thot value

.. _`ti_bandgap_read_thot.return`:

Return
------

0 on success or the proper error code

.. _`ti_bandgap_write_thot`:

ti_bandgap_write_thot
=====================

.. c:function:: int ti_bandgap_write_thot(struct ti_bandgap *bgp, int id, int val)

    sets sensor current thot

    :param struct ti_bandgap \*bgp:
        pointer to bandgap instance

    :param int id:
        sensor id

    :param int val:
        desired thot value

.. _`ti_bandgap_write_thot.return`:

Return
------

0 on success or the proper error code

.. _`ti_bandgap_read_tcold`:

ti_bandgap_read_tcold
=====================

.. c:function:: int ti_bandgap_read_tcold(struct ti_bandgap *bgp, int id, int *tcold)

    reads sensor current tcold

    :param struct ti_bandgap \*bgp:
        pointer to bandgap instance

    :param int id:
        sensor id

    :param int \*tcold:
        resulting current tcold value

.. _`ti_bandgap_read_tcold.return`:

Return
------

0 on success or the proper error code

.. _`ti_bandgap_write_tcold`:

ti_bandgap_write_tcold
======================

.. c:function:: int ti_bandgap_write_tcold(struct ti_bandgap *bgp, int id, int val)

    sets the sensor tcold

    :param struct ti_bandgap \*bgp:
        pointer to bandgap instance

    :param int id:
        sensor id

    :param int val:
        desired tcold value

.. _`ti_bandgap_write_tcold.return`:

Return
------

0 on success or the proper error code

.. _`ti_bandgap_read_counter`:

ti_bandgap_read_counter
=======================

.. c:function:: void ti_bandgap_read_counter(struct ti_bandgap *bgp, int id, int *interval)

    read the sensor counter

    :param struct ti_bandgap \*bgp:
        pointer to bandgap instance

    :param int id:
        sensor id

    :param int \*interval:
        resulting update interval in miliseconds

.. _`ti_bandgap_read_counter_delay`:

ti_bandgap_read_counter_delay
=============================

.. c:function:: void ti_bandgap_read_counter_delay(struct ti_bandgap *bgp, int id, int *interval)

    read the sensor counter delay

    :param struct ti_bandgap \*bgp:
        pointer to bandgap instance

    :param int id:
        sensor id

    :param int \*interval:
        resulting update interval in miliseconds

.. _`ti_bandgap_read_update_interval`:

ti_bandgap_read_update_interval
===============================

.. c:function:: int ti_bandgap_read_update_interval(struct ti_bandgap *bgp, int id, int *interval)

    read the sensor update interval

    :param struct ti_bandgap \*bgp:
        pointer to bandgap instance

    :param int id:
        sensor id

    :param int \*interval:
        resulting update interval in miliseconds

.. _`ti_bandgap_read_update_interval.return`:

Return
------

0 on success or the proper error code

.. _`ti_bandgap_write_counter_delay`:

ti_bandgap_write_counter_delay
==============================

.. c:function:: int ti_bandgap_write_counter_delay(struct ti_bandgap *bgp, int id, u32 interval)

    set the counter_delay

    :param struct ti_bandgap \*bgp:
        pointer to bandgap instance

    :param int id:
        sensor id

    :param u32 interval:
        desired update interval in miliseconds

.. _`ti_bandgap_write_counter_delay.return`:

Return
------

0 on success or the proper error code

.. _`ti_bandgap_write_counter`:

ti_bandgap_write_counter
========================

.. c:function:: void ti_bandgap_write_counter(struct ti_bandgap *bgp, int id, u32 interval)

    set the bandgap sensor counter

    :param struct ti_bandgap \*bgp:
        pointer to bandgap instance

    :param int id:
        sensor id

    :param u32 interval:
        desired update interval in miliseconds

.. _`ti_bandgap_write_update_interval`:

ti_bandgap_write_update_interval
================================

.. c:function:: int ti_bandgap_write_update_interval(struct ti_bandgap *bgp, int id, u32 interval)

    set the update interval

    :param struct ti_bandgap \*bgp:
        pointer to bandgap instance

    :param int id:
        sensor id

    :param u32 interval:
        desired update interval in miliseconds

.. _`ti_bandgap_write_update_interval.return`:

Return
------

0 on success or the proper error code

.. _`ti_bandgap_read_temperature`:

ti_bandgap_read_temperature
===========================

.. c:function:: int ti_bandgap_read_temperature(struct ti_bandgap *bgp, int id, int *temperature)

    report current temperature

    :param struct ti_bandgap \*bgp:
        pointer to bandgap instance

    :param int id:
        sensor id

    :param int \*temperature:
        resulting temperature

.. _`ti_bandgap_read_temperature.return`:

Return
------

0 on success or the proper error code

.. _`ti_bandgap_set_sensor_data`:

ti_bandgap_set_sensor_data
==========================

.. c:function:: int ti_bandgap_set_sensor_data(struct ti_bandgap *bgp, int id, void *data)

    helper function to store thermal framework related data.

    :param struct ti_bandgap \*bgp:
        pointer to bandgap instance

    :param int id:
        sensor id

    :param void \*data:
        thermal framework related data to be stored

.. _`ti_bandgap_set_sensor_data.return`:

Return
------

0 on success or the proper error code

.. _`ti_bandgap_get_sensor_data`:

ti_bandgap_get_sensor_data
==========================

.. c:function:: void *ti_bandgap_get_sensor_data(struct ti_bandgap *bgp, int id)

    helper function to get thermal framework related data.

    :param struct ti_bandgap \*bgp:
        pointer to bandgap instance

    :param int id:
        sensor id

.. _`ti_bandgap_get_sensor_data.return`:

Return
------

data stored by set function with sensor id on success or NULL

.. _`ti_bandgap_force_single_read`:

ti_bandgap_force_single_read
============================

.. c:function:: int ti_bandgap_force_single_read(struct ti_bandgap *bgp, int id)

    executes 1 single ADC conversion

    :param struct ti_bandgap \*bgp:
        pointer to struct ti_bandgap

    :param int id:
        sensor id which it is desired to read 1 temperature

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

    :param struct ti_bandgap \*bgp:
        pointer to struct ti_bandgap

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

    :param struct ti_bandgap \*bgp:
        pointer to struct ti_bandgap

    :param int id:
        id of the individual sensor

    :param int \*trend:
        Pointer to trend.

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

    :param struct ti_bandgap \*bgp:
        pointer to struct ti_bandgap

    :param struct platform_device \*pdev:
        pointer to device struct platform_device

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

    :param struct ti_bandgap \*bgp:
        pointer to struct ti_bandgap

    :param struct platform_device \*pdev:
        pointer to device struct platform_device

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

    :param struct platform_device \*pdev:
        pointer to device struct platform_device

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

