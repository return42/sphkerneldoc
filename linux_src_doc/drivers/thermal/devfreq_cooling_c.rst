.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/devfreq_cooling.c

.. _`devfreq_cooling_device`:

struct devfreq_cooling_device
=============================

.. c:type:: struct devfreq_cooling_device

    Devfreq cooling device

.. _`devfreq_cooling_device.definition`:

Definition
----------

.. code-block:: c

    struct devfreq_cooling_device {
        int id;
        struct thermal_cooling_device *cdev;
        struct devfreq *devfreq;
        unsigned long cooling_state;
        u32 *power_table;
        u32 *freq_table;
        size_t freq_table_size;
        struct devfreq_cooling_power *power_ops;
        u32 res_util;
        int capped_state;
    }

.. _`devfreq_cooling_device.members`:

Members
-------

id
    unique integer value corresponding to each
    devfreq_cooling_device registered.

cdev
    Pointer to associated thermal cooling device.

devfreq
    Pointer to associated devfreq device.

cooling_state
    Current cooling state.

power_table
    Pointer to table with maximum power draw for each
    cooling state. State is the index into the table, and
    the power is in mW.

freq_table
    Pointer to a table with the frequencies sorted in descending
    order.  You can index the table by cooling device state

freq_table_size
    Size of the \ ``freq_table``\  and \ ``power_table``\ 

power_ops
    Pointer to devfreq_cooling_power, used to generate the
    \ ``power_table``\ .

res_util
    Resource utilization scaling factor for the power.
    It is multiplied by 100 to minimize the error. It is used
    for estimation of the power budget instead of using
    'utilization' (which is 'busy_time / 'total_time').
    The 'res_util' range is from 100 to (power_table[state] \* 100)
    for the corresponding 'state'.

capped_state
    *undescribed*

.. _`partition_enable_opps`:

partition_enable_opps
=====================

.. c:function:: int partition_enable_opps(struct devfreq_cooling_device *dfc, unsigned long cdev_state)

    disable all opps above a given state

    :param dfc:
        Pointer to devfreq we are operating on
    :type dfc: struct devfreq_cooling_device \*

    :param cdev_state:
        cooling device state we're setting
    :type cdev_state: unsigned long

.. _`partition_enable_opps.description`:

Description
-----------

Go through the OPPs of the device, enabling all OPPs until
\ ``cdev_state``\  and disabling those frequencies above it.

.. _`freq_get_state`:

freq_get_state
==============

.. c:function:: unsigned long freq_get_state(struct devfreq_cooling_device *dfc, unsigned long freq)

    get the cooling state corresponding to a frequency

    :param dfc:
        Pointer to devfreq cooling device
    :type dfc: struct devfreq_cooling_device \*

    :param freq:
        frequency in Hz
    :type freq: unsigned long

.. _`freq_get_state.return`:

Return
------

the cooling state associated with the \ ``freq``\ , or
THERMAL_CSTATE_INVALID if it wasn't found.

.. _`get_static_power`:

get_static_power
================

.. c:function:: unsigned long get_static_power(struct devfreq_cooling_device *dfc, unsigned long freq)

    calculate the static power

    :param dfc:
        Pointer to devfreq cooling device
    :type dfc: struct devfreq_cooling_device \*

    :param freq:
        Frequency in Hz
    :type freq: unsigned long

.. _`get_static_power.description`:

Description
-----------

Calculate the static power in milliwatts using the supplied
\ :c:func:`get_static_power`\ .  The current voltage is calculated using the
OPP library.  If no \ :c:func:`get_static_power`\  was supplied, assume the
static power is negligible.

.. _`get_dynamic_power`:

get_dynamic_power
=================

.. c:function:: unsigned long get_dynamic_power(struct devfreq_cooling_device *dfc, unsigned long freq, unsigned long voltage)

    calculate the dynamic power

    :param dfc:
        Pointer to devfreq cooling device
    :type dfc: struct devfreq_cooling_device \*

    :param freq:
        Frequency in Hz
    :type freq: unsigned long

    :param voltage:
        Voltage in millivolts
    :type voltage: unsigned long

.. _`get_dynamic_power.description`:

Description
-----------

Calculate the dynamic power in milliwatts consumed by the device at
frequency \ ``freq``\  and voltage \ ``voltage``\ .  If the \ :c:func:`get_dynamic_power`\ 
was supplied as part of the devfreq_cooling_power struct, then that
function is used.  Otherwise, a simple power model (Pdyn = Coeff \*
Voltage^2 \* Frequency) is used.

.. _`devfreq_cooling_gen_tables`:

devfreq_cooling_gen_tables
==========================

.. c:function:: int devfreq_cooling_gen_tables(struct devfreq_cooling_device *dfc)

    Generate power and freq tables.

    :param dfc:
        Pointer to devfreq cooling device.
    :type dfc: struct devfreq_cooling_device \*

.. _`devfreq_cooling_gen_tables.generate-power-and-frequency-tables`:

Generate power and frequency tables
-----------------------------------

the power table hold the
device's maximum power usage at each cooling state (OPP).  The
static and dynamic power using the appropriate voltage and
frequency for the state, is acquired from the struct
devfreq_cooling_power, and summed to make the maximum power draw.

The frequency table holds the frequencies in descending order.
That way its indexed by cooling device state.

The tables are malloced, and pointers put in dfc.  They must be
freed when unregistering the devfreq cooling device.

.. _`devfreq_cooling_gen_tables.return`:

Return
------

0 on success, negative error code on failure.

.. _`of_devfreq_cooling_register_power`:

of_devfreq_cooling_register_power
=================================

.. c:function:: struct thermal_cooling_device *of_devfreq_cooling_register_power(struct device_node *np, struct devfreq *df, struct devfreq_cooling_power *dfc_power)

    Register devfreq cooling device, with OF and power information.

    :param np:
        Pointer to OF device_node.
    :type np: struct device_node \*

    :param df:
        Pointer to devfreq device.
    :type df: struct devfreq \*

    :param dfc_power:
        Pointer to devfreq_cooling_power.
    :type dfc_power: struct devfreq_cooling_power \*

.. _`of_devfreq_cooling_register_power.description`:

Description
-----------

Register a devfreq cooling device.  The available OPPs must be
registered on the device.

If \ ``dfc_power``\  is provided, the cooling device is registered with the
power extensions.  For the power extensions to work correctly,
devfreq should use the simple_ondemand governor, other governors
are not currently supported.

.. _`of_devfreq_cooling_register`:

of_devfreq_cooling_register
===========================

.. c:function:: struct thermal_cooling_device *of_devfreq_cooling_register(struct device_node *np, struct devfreq *df)

    Register devfreq cooling device, with OF information.

    :param np:
        Pointer to OF device_node.
    :type np: struct device_node \*

    :param df:
        Pointer to devfreq device.
    :type df: struct devfreq \*

.. _`devfreq_cooling_register`:

devfreq_cooling_register
========================

.. c:function:: struct thermal_cooling_device *devfreq_cooling_register(struct devfreq *df)

    Register devfreq cooling device.

    :param df:
        Pointer to devfreq device.
    :type df: struct devfreq \*

.. _`devfreq_cooling_unregister`:

devfreq_cooling_unregister
==========================

.. c:function:: void devfreq_cooling_unregister(struct thermal_cooling_device *cdev)

    Unregister devfreq cooling device.

    :param cdev:
        *undescribed*
    :type cdev: struct thermal_cooling_device \*

.. This file was automatic generated / don't edit.

