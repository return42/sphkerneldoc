.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/dbx500-prcmu.h

.. _`dbx500_regulator_info`:

struct dbx500_regulator_info
============================

.. c:type:: struct dbx500_regulator_info

    dbx500 regulator information

.. _`dbx500_regulator_info.definition`:

Definition
----------

.. code-block:: c

    struct dbx500_regulator_info {
        struct device *dev;
        struct regulator_desc desc;
        struct regulator_dev *rdev;
        bool is_enabled;
        u16 epod_id;
        bool is_ramret;
        bool exclude_from_power_state;
    }

.. _`dbx500_regulator_info.members`:

Members
-------

dev
    device pointer

desc
    regulator description

rdev
    regulator device pointer

is_enabled
    status of the regulator

epod_id
    id for EPOD (power domain)

is_ramret
    RAM retention switch for EPOD (power domain)

exclude_from_power_state
    *undescribed*

.. This file was automatic generated / don't edit.

