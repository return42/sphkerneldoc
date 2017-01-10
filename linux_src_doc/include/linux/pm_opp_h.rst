.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pm_opp.h

.. _`dev_pm_opp_supply`:

struct dev_pm_opp_supply
========================

.. c:type:: struct dev_pm_opp_supply

    Power supply voltage/current values

.. _`dev_pm_opp_supply.definition`:

Definition
----------

.. code-block:: c

    struct dev_pm_opp_supply {
        unsigned long u_volt;
        unsigned long u_volt_min;
        unsigned long u_volt_max;
        unsigned long u_amp;
    }

.. _`dev_pm_opp_supply.members`:

Members
-------

u_volt
    Target voltage in microvolts corresponding to this OPP

u_volt_min
    Minimum voltage in microvolts corresponding to this OPP

u_volt_max
    Maximum voltage in microvolts corresponding to this OPP

u_amp
    Maximum current drawn by the device in microamperes

.. _`dev_pm_opp_supply.description`:

Description
-----------

This structure stores the voltage/current values for a single power supply.

.. _`dev_pm_opp_info`:

struct dev_pm_opp_info
======================

.. c:type:: struct dev_pm_opp_info

    OPP freq/voltage/current values

.. _`dev_pm_opp_info.definition`:

Definition
----------

.. code-block:: c

    struct dev_pm_opp_info {
        unsigned long rate;
        struct dev_pm_opp_supply *supplies;
    }

.. _`dev_pm_opp_info.members`:

Members
-------

rate
    Target clk rate in hz

supplies
    Array of voltage/current values for all power supplies

.. _`dev_pm_opp_info.description`:

Description
-----------

This structure stores the freq/voltage/current values for a single OPP.

.. _`dev_pm_set_opp_data`:

struct dev_pm_set_opp_data
==========================

.. c:type:: struct dev_pm_set_opp_data

    Set OPP data

.. _`dev_pm_set_opp_data.definition`:

Definition
----------

.. code-block:: c

    struct dev_pm_set_opp_data {
        struct dev_pm_opp_info old_opp;
        struct dev_pm_opp_info new_opp;
        struct regulator **regulators;
        unsigned int regulator_count;
        struct clk *clk;
        struct device *dev;
    }

.. _`dev_pm_set_opp_data.members`:

Members
-------

old_opp
    Old OPP info

new_opp
    New OPP info

regulators
    Array of regulator pointers

regulator_count
    Number of regulators

clk
    Pointer to clk

dev
    Pointer to the struct device

.. _`dev_pm_set_opp_data.description`:

Description
-----------

This structure contains all information required for setting an OPP.

.. This file was automatic generated / don't edit.

