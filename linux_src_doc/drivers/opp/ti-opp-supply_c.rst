.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/opp/ti-opp-supply.c

.. _`ti_opp_supply_optimum_voltage_table`:

struct ti_opp_supply_optimum_voltage_table
==========================================

.. c:type:: struct ti_opp_supply_optimum_voltage_table

    optimized voltage table

.. _`ti_opp_supply_optimum_voltage_table.definition`:

Definition
----------

.. code-block:: c

    struct ti_opp_supply_optimum_voltage_table {
        unsigned int reference_uv;
        unsigned int optimized_uv;
    }

.. _`ti_opp_supply_optimum_voltage_table.members`:

Members
-------

reference_uv
    reference voltage (usually Nominal voltage)

optimized_uv
    Optimized voltage from efuse

.. _`ti_opp_supply_data`:

struct ti_opp_supply_data
=========================

.. c:type:: struct ti_opp_supply_data

    OMAP specific opp supply data

.. _`ti_opp_supply_data.definition`:

Definition
----------

.. code-block:: c

    struct ti_opp_supply_data {
        struct ti_opp_supply_optimum_voltage_table *vdd_table;
        u32 num_vdd_table;
        u32 vdd_absolute_max_voltage_uv;
    }

.. _`ti_opp_supply_data.members`:

Members
-------

vdd_table
    Optimized voltage mapping table

num_vdd_table
    number of entries in vdd_table

vdd_absolute_max_voltage_uv
    absolute maximum voltage in UV for the supply

.. _`ti_opp_supply_of_data`:

struct ti_opp_supply_of_data
============================

.. c:type:: struct ti_opp_supply_of_data

    device tree match data

.. _`ti_opp_supply_of_data.definition`:

Definition
----------

.. code-block:: c

    struct ti_opp_supply_of_data {
    #define OPPDM_EFUSE_CLASS0_OPTIMIZED_VOLTAGE BIT(1)
    #define OPPDM_HAS_NO_ABB BIT(2)
        const u8 flags;
        const u32 efuse_voltage_mask;
        const bool efuse_voltage_uv;
    }

.. _`ti_opp_supply_of_data.members`:

Members
-------

flags
    specific type of opp supply

efuse_voltage_mask
    mask required for efuse register representing voltage

efuse_voltage_uv
    Are the efuse entries in micro-volts? if not, assume
    milli-volts.

.. _`_store_optimized_voltages`:

_store_optimized_voltages
=========================

.. c:function:: int _store_optimized_voltages(struct device *dev, struct ti_opp_supply_data *data)

    store optimized voltages

    :param struct device \*dev:
        ti opp supply device for which we need to store info

    :param struct ti_opp_supply_data \*data:
        data specific to the device

.. _`_store_optimized_voltages.description`:

Description
-----------

Picks up efuse based optimized voltages for VDD unique per device and
stores it in internal data structure for use during transition requests.

.. _`_store_optimized_voltages.return`:

Return
------

If successful, 0, else appropriate error value.

.. _`_free_optimized_voltages`:

_free_optimized_voltages
========================

.. c:function:: void _free_optimized_voltages(struct device *dev, struct ti_opp_supply_data *data)

    free resources for optvoltages

    :param struct device \*dev:
        device for which we need to free info

    :param struct ti_opp_supply_data \*data:
        data specific to the device

.. _`_get_optimal_vdd_voltage`:

_get_optimal_vdd_voltage
========================

.. c:function:: int _get_optimal_vdd_voltage(struct device *dev, struct ti_opp_supply_data *data, int reference_uv)

    Finds optimal voltage for the supply

    :param struct device \*dev:
        device for which we need to find info

    :param struct ti_opp_supply_data \*data:
        data specific to the device

    :param int reference_uv:
        reference voltage (OPP voltage) for which we need value

.. _`_get_optimal_vdd_voltage.return`:

Return
------

if a match is found, return optimized voltage, else return
reference_uv, also return reference_uv if no optimization is needed.

.. _`ti_opp_supply_set_opp`:

ti_opp_supply_set_opp
=====================

.. c:function:: int ti_opp_supply_set_opp(struct dev_pm_set_opp_data *data)

    do the opp supply transition

    :param struct dev_pm_set_opp_data \*data:
        information on regulators and new and old opps provided by
        opp core to use in transition

.. _`ti_opp_supply_set_opp.return`:

Return
------

If successful, 0, else appropriate error value.

.. This file was automatic generated / don't edit.

