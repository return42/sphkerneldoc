.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pm2301_charger.h

.. _`pm2xxx_bm_charger_parameters`:

struct pm2xxx_bm_charger_parameters
===================================

.. c:type:: struct pm2xxx_bm_charger_parameters

    Charger specific parameters

.. _`pm2xxx_bm_charger_parameters.definition`:

Definition
----------

.. code-block:: c

    struct pm2xxx_bm_charger_parameters {
        int ac_volt_max;
        int ac_curr_max;
    }

.. _`pm2xxx_bm_charger_parameters.members`:

Members
-------

ac_volt_max
    maximum allowed AC charger voltage in mV

ac_curr_max
    maximum allowed AC charger current in mA

.. _`pm2xxx_bm_data`:

struct pm2xxx_bm_data
=====================

.. c:type:: struct pm2xxx_bm_data

    pm2xxx battery management data \ ``enable_overshoot``\     flag to enable VBAT overshoot control \ ``chg_params``\     charger parameters

.. _`pm2xxx_bm_data.definition`:

Definition
----------

.. code-block:: c

    struct pm2xxx_bm_data {
        bool enable_overshoot;
        const struct pm2xxx_bm_charger_parameters *chg_params;
    }

.. _`pm2xxx_bm_data.members`:

Members
-------

enable_overshoot
    *undescribed*

chg_params
    *undescribed*

.. This file was automatic generated / don't edit.

