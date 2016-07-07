.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/ab8500-ext.c

.. _`ab8500_ext_regulator_info`:

struct ab8500_ext_regulator_info
================================

.. c:type:: struct ab8500_ext_regulator_info

    ab8500 regulator information

.. _`ab8500_ext_regulator_info.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_ext_regulator_info {
        struct device *dev;
        struct regulator_desc desc;
        struct regulator_dev *rdev;
        struct ab8500_ext_regulator_cfg *cfg;
        u8 update_bank;
        u8 update_reg;
        u8 update_mask;
        u8 update_val;
        u8 update_val_hp;
        u8 update_val_lp;
        u8 update_val_hw;
    }

.. _`ab8500_ext_regulator_info.members`:

Members
-------

dev
    device pointer

desc
    regulator description

rdev
    regulator device

cfg
    regulator configuration (extension of regulator FW configuration)

update_bank
    bank to control on/off

update_reg
    register to control on/off

update_mask
    mask to enable/disable and set mode of regulator

update_val
    bits holding the regulator current mode

update_val_hp
    bits to set EN pin active (LPn pin deactive)
    normally this means high power mode

update_val_lp
    bits to set EN pin active and LPn pin active
    normally this means low power mode

update_val_hw
    bits to set regulator pins in HW control
    SysClkReq pins and logic will choose mode

.. This file was automatic generated / don't edit.

