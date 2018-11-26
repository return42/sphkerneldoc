.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/clock_cooling.c

.. _`clock_cooling_device`:

struct clock_cooling_device
===========================

.. c:type:: struct clock_cooling_device

    data for cooling device with clock

.. _`clock_cooling_device.definition`:

Definition
----------

.. code-block:: c

    struct clock_cooling_device {
        int id;
        struct device *dev;
        struct thermal_cooling_device *cdev;
        struct notifier_block clk_rate_change_nb;
        struct cpufreq_frequency_table *freq_table;
        unsigned long clock_state;
        unsigned long clock_val;
        struct clk *clk;
        struct mutex lock;
    }

.. _`clock_cooling_device.members`:

Members
-------

id
    unique integer value corresponding to each clock_cooling_device
    registered.

dev
    struct device pointer to the device being used to cool off using
    clock frequencies.

cdev
    thermal_cooling_device pointer to keep track of the
    registered cooling device.

clk_rate_change_nb
    reference to notifier block used to receive clock
    rate changes.

freq_table
    frequency table used to keep track of available frequencies.

clock_state
    integer value representing the current state of clock
    cooling devices.

clock_val
    integer value representing the absolute value of the clipped
    frequency.

clk
    struct clk reference used to enforce clock limits.

lock
    mutex lock to protect this struct.

.. _`clock_cooling_device.description`:

Description
-----------

This structure is required for keeping information of each
clock_cooling_device registered. In order to prevent corruption of this a
mutex \ ``lock``\  is used.

.. _`clock_cooling_get_property`:

clock_cooling_get_property
==========================

.. c:function:: int clock_cooling_get_property(struct clock_cooling_device *ccdev, unsigned long input, unsigned long *output, enum clock_cooling_property property)

    fetch a property of interest for a give cpu.

    :param ccdev:
        clock cooling device reference
    :type ccdev: struct clock_cooling_device \*

    :param input:
        query parameter
    :type input: unsigned long

    :param output:
        query return
    :type output: unsigned long \*

    :param property:
        type of query (frequency, level, max level)
    :type property: enum clock_cooling_property

.. _`clock_cooling_get_property.description`:

Description
-----------

This is the common function to
1. get maximum clock cooling states
2. translate frequency to cooling state
3. translate cooling state to frequency
Note that the code may be not in good shape

.. _`clock_cooling_get_property.but-it-is-written-in-this-way-in-order-to`:

but it is written in this way in order to
-----------------------------------------

a) reduce duplicate code as most of the code can be shared.
b) make sure the logic is consistent when translating between
cooling states and frequencies.

.. _`clock_cooling_get_property.return`:

Return
------

0 on success, -EINVAL when invalid parameters are passed.

.. _`clock_cooling_get_level`:

clock_cooling_get_level
=======================

.. c:function:: unsigned long clock_cooling_get_level(struct thermal_cooling_device *cdev, unsigned long freq)

    return the cooling level of given clock cooling.

    :param cdev:
        reference of a thermal cooling device of used as clock cooling device
    :type cdev: struct thermal_cooling_device \*

    :param freq:
        the frequency of interest
    :type freq: unsigned long

.. _`clock_cooling_get_level.description`:

Description
-----------

This function will match the cooling level corresponding to the
requested \ ``freq``\  and return it.

.. _`clock_cooling_get_level.return`:

Return
------

The matched cooling level on success or THERMAL_CSTATE_INVALID
otherwise.

.. _`clock_cooling_get_frequency`:

clock_cooling_get_frequency
===========================

.. c:function:: unsigned long clock_cooling_get_frequency(struct clock_cooling_device *ccdev, unsigned long level)

    get the absolute value of frequency from level.

    :param ccdev:
        clock cooling device reference
    :type ccdev: struct clock_cooling_device \*

    :param level:
        cooling level
    :type level: unsigned long

.. _`clock_cooling_get_frequency.description`:

Description
-----------

This function matches cooling level with frequency. Based on a cooling level
of frequency, equals cooling state of cpu cooling device, it will return
the corresponding frequency.
e.g level=0 --> 1st MAX FREQ, level=1 ---> 2nd MAX FREQ, .... etc

.. _`clock_cooling_get_frequency.return`:

Return
------

0 on error, the corresponding frequency otherwise.

.. _`clock_cooling_apply`:

clock_cooling_apply
===================

.. c:function:: int clock_cooling_apply(struct clock_cooling_device *ccdev, unsigned long cooling_state)

    function to apply frequency clipping.

    :param ccdev:
        clock_cooling_device pointer containing frequency clipping data.
    :type ccdev: struct clock_cooling_device \*

    :param cooling_state:
        value of the cooling state.
    :type cooling_state: unsigned long

.. _`clock_cooling_apply.description`:

Description
-----------

Function used to make sure the clock layer is aware of current thermal
limits. The limits are applied by updating the clock rate in case it is
higher than the corresponding frequency based on the requested cooling_state.

.. _`clock_cooling_apply.return`:

Return
------

0 on success, an error code otherwise (-EINVAL in case wrong
cooling state).

.. _`clock_cooling_clock_notifier`:

clock_cooling_clock_notifier
============================

.. c:function:: int clock_cooling_clock_notifier(struct notifier_block *nb, unsigned long event, void *data)

    notifier callback on clock rate changes.

    :param nb:
        struct notifier_block \* with callback info.
    :type nb: struct notifier_block \*

    :param event:
        value showing clock event for which this function invoked.
    :type event: unsigned long

    :param data:
        callback-specific data
    :type data: void \*

.. _`clock_cooling_clock_notifier.description`:

Description
-----------

Callback to hijack the notification on clock transition.
Every time there is a clock change, we intercept all pre change events
and block the transition in case the new rate infringes thermal limits.

.. _`clock_cooling_clock_notifier.return`:

Return
------

NOTIFY_DONE (success) or NOTIFY_BAD (new_rate > thermal limit).

.. _`clock_cooling_get_max_state`:

clock_cooling_get_max_state
===========================

.. c:function:: int clock_cooling_get_max_state(struct thermal_cooling_device *cdev, unsigned long *state)

    callback function to get the max cooling state.

    :param cdev:
        thermal cooling device pointer.
    :type cdev: struct thermal_cooling_device \*

    :param state:
        fill this variable with the max cooling state.
    :type state: unsigned long \*

.. _`clock_cooling_get_max_state.description`:

Description
-----------

Callback for the thermal cooling device to return the clock
max cooling state.

.. _`clock_cooling_get_max_state.return`:

Return
------

0 on success, an error code otherwise.

.. _`clock_cooling_get_cur_state`:

clock_cooling_get_cur_state
===========================

.. c:function:: int clock_cooling_get_cur_state(struct thermal_cooling_device *cdev, unsigned long *state)

    function to get the current cooling state.

    :param cdev:
        thermal cooling device pointer.
    :type cdev: struct thermal_cooling_device \*

    :param state:
        fill this variable with the current cooling state.
    :type state: unsigned long \*

.. _`clock_cooling_get_cur_state.description`:

Description
-----------

Callback for the thermal cooling device to return the clock
current cooling state.

.. _`clock_cooling_get_cur_state.return`:

Return
------

0 (success)

.. _`clock_cooling_set_cur_state`:

clock_cooling_set_cur_state
===========================

.. c:function:: int clock_cooling_set_cur_state(struct thermal_cooling_device *cdev, unsigned long state)

    function to set the current cooling state.

    :param cdev:
        thermal cooling device pointer.
    :type cdev: struct thermal_cooling_device \*

    :param state:
        set this variable to the current cooling state.
    :type state: unsigned long

.. _`clock_cooling_set_cur_state.description`:

Description
-----------

Callback for the thermal cooling device to change the clock cooling
current cooling state.

.. _`clock_cooling_set_cur_state.return`:

Return
------

0 on success, an error code otherwise.

.. _`clock_cooling_register`:

clock_cooling_register
======================

.. c:function:: struct thermal_cooling_device *clock_cooling_register(struct device *dev, const char *clock_name)

    function to create clock cooling device.

    :param dev:
        struct device pointer to the device used as clock cooling device.
    :type dev: struct device \*

    :param clock_name:
        string containing the clock used as cooling mechanism.
    :type clock_name: const char \*

.. _`clock_cooling_register.description`:

Description
-----------

This interface function registers the clock cooling device with the name
"thermal-clock-%x". The cooling device is based on clock frequencies.
The struct device is assumed to be capable of DVFS transitions.
The OPP layer is used to fetch and fill the available frequencies for
the referred device. The ordered frequency table is used to control
the clock cooling device cooling states and to limit clock transitions
based on the cooling state requested by the thermal framework.

.. _`clock_cooling_register.return`:

Return
------

a valid struct thermal_cooling_device pointer on success,
on failure, it returns a corresponding \ :c:func:`ERR_PTR`\ .

.. _`clock_cooling_unregister`:

clock_cooling_unregister
========================

.. c:function:: void clock_cooling_unregister(struct thermal_cooling_device *cdev)

    function to remove clock cooling device.

    :param cdev:
        thermal cooling device pointer.
    :type cdev: struct thermal_cooling_device \*

.. _`clock_cooling_unregister.description`:

Description
-----------

This interface function unregisters the "thermal-clock-%x" cooling device.

.. This file was automatic generated / don't edit.

