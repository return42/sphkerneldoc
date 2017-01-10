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
        unsigned long (*get_static_power)(struct devfreq *devfreq,unsigned long voltage);
        unsigned long (*get_dynamic_power)(struct devfreq *devfreq,unsigned long freq,unsigned long voltage);
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

dyn_power_coeff
    Coefficient for the simple dynamic power model in
    mW/(MHz mV mV).
    If \ :c:func:`get_dynamic_power`\  is NULL, then the
    dynamic power is calculated as
    \ ``dyn_power_coeff``\  \* frequency \* voltage^2

.. This file was automatic generated / don't edit.

