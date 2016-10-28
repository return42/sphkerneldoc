.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/qcom/gdsc.h

.. _`gdsc`:

struct gdsc
===========

.. c:type:: struct gdsc

    Globally Distributed Switch Controller

.. _`gdsc.definition`:

Definition
----------

.. code-block:: c

    struct gdsc {
        struct generic_pm_domain pd;
        struct generic_pm_domain *parent;
        struct regmap *regmap;
        unsigned int gdscr;
        unsigned int gds_hw_ctrl;
        unsigned int *cxcs;
        unsigned int cxc_count;
        const u8 pwrsts;
    #define PWRSTS_OFF BIT(0)
    #define PWRSTS_RET BIT(1)
    #define PWRSTS_ON BIT(2)
    #define PWRSTS_OFF_ON (PWRSTS_OFF | PWRSTS_ON)
    #define PWRSTS_RET_ON (PWRSTS_RET | PWRSTS_ON)
        const u8 flags;
    #define VOTABLE BIT(0)
        struct reset_controller_dev *rcdev;
        unsigned int *resets;
        unsigned int reset_count;
    }

.. _`gdsc.members`:

Members
-------

pd
    generic power domain

parent
    *undescribed*

regmap
    regmap for MMIO accesses

gdscr
    gsdc control register

gds_hw_ctrl
    gds_hw_ctrl register

cxcs
    offsets of branch registers to toggle mem/periph bits in

cxc_count
    number of \ ``cxcs``\ 

pwrsts
    Possible powerdomain power states

flags
    *undescribed*

rcdev
    reset controller

resets
    ids of resets associated with this gdsc

reset_count
    number of \ ``resets``\ 

.. This file was automatic generated / don't edit.

