.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/abx500/ux500_chargalg.h

.. _`ux500_charger`:

struct ux500_charger
====================

.. c:type:: struct ux500_charger

    power supply ux500 charger sub class \ ``psy``\                  power supply base class \ ``ops``\                  ux500 charger operations \ ``max_out_volt``\         maximum output charger voltage in mV \ ``max_out_curr``\         maximum output charger current in mA \ ``enabled``\              indicates if this charger is used or not \ ``external``\             external charger unit (pm2xxx)

.. _`ux500_charger.definition`:

Definition
----------

.. code-block:: c

    struct ux500_charger {
        struct power_supply *psy;
        struct ux500_charger_ops ops;
        int max_out_volt;
        int max_out_curr;
        int wdt_refresh;
        bool enabled;
        bool external;
    }

.. _`ux500_charger.members`:

Members
-------

psy
    *undescribed*

ops
    *undescribed*

max_out_volt
    *undescribed*

max_out_curr
    *undescribed*

wdt_refresh
    *undescribed*

enabled
    *undescribed*

external
    *undescribed*

.. This file was automatic generated / don't edit.

