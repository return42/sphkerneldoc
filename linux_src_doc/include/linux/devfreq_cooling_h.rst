.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/devfreq_cooling.h

.. _`devfreq_cooling_power`:

struct devfreq_cooling_power
============================

.. c:type:: struct devfreq_cooling_power

    Devfreq cooling power ops

.. _`devfreq_cooling_power.definition`:

Definition
----------

.. code-block:: c

    struct devfreq_cooling_power {
        unsigned long (*get_static_power)(struct devfreq *devfreq, unsigned long voltage);
        unsigned long (*get_dynamic_power)(struct devfreq *devfreq,unsigned long freq, unsigned long voltage);
        int (*get_real_power)(struct devfreq *df, u32 *power, unsigned long freq, unsigned long voltage);
        unsigned long dyn_power_coeff;
    }

.. _`devfreq_cooling_power.members`:

Members
-------

get_static_power
    Take voltage, in mV, and return the static power
    in mW.  If NULL, the static power is assumed
    to be 0.

get_dynamic_power
    Take voltage, in mV, and frequency, in HZ, and
    return the dynamic power draw in mW.  If NULL,
    a simple power model is used.

get_real_power
    When this is set, the framework uses it to ask the
    device driver for the actual power.
    Some devices have more sophisticated methods
    (like power counters) to approximate the actual power
    that they use.
    This function provides more accurate data to the
    thermal governor. When the driver does not provide
    such function, framework just uses pre-calculated
    table and scale the power by 'utilization'
    (based on 'busy_time' and 'total_time' taken from
    devfreq 'last_status').
    The value returned by this function must be lower
    or equal than the maximum power value
    for the current state
    (which can be found in power_table[state]).
    When this interface is used, the power_table holds
    max total (static + dynamic) power value for each OPP.

dyn_power_coeff
    Coefficient for the simple dynamic power model in
    mW/(MHz mV mV).
    If \ :c:func:`get_dynamic_power`\  is NULL, then the
    dynamic power is calculated as
    \ ``dyn_power_coeff``\  \* frequency \* voltage^2

.. This file was automatic generated / don't edit.

