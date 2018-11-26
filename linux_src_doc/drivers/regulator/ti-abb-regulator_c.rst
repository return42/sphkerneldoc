.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/ti-abb-regulator.c

.. _`ti_abb_info`:

struct ti_abb_info
==================

.. c:type:: struct ti_abb_info

    ABB information per voltage setting

.. _`ti_abb_info.definition`:

Definition
----------

.. code-block:: c

    struct ti_abb_info {
        u32 opp_sel;
        u32 vset;
    }

.. _`ti_abb_info.members`:

Members
-------

opp_sel
    one of TI_ABB macro

vset
    (optional) vset value that LDOVBB needs to be overriden with.

.. _`ti_abb_info.description`:

Description
-----------

Array of per voltage entries organized in the same order as regulator_desc's
volt_table list. (selector is used to index from this array)

.. _`ti_abb_reg`:

struct ti_abb_reg
=================

.. c:type:: struct ti_abb_reg

    Register description for ABB block

.. _`ti_abb_reg.definition`:

Definition
----------

.. code-block:: c

    struct ti_abb_reg {
        u32 setup_off;
        u32 control_off;
        u32 sr2_wtcnt_value_mask;
        u32 fbb_sel_mask;
        u32 rbb_sel_mask;
        u32 sr2_en_mask;
        u32 opp_change_mask;
        u32 opp_sel_mask;
    }

.. _`ti_abb_reg.members`:

Members
-------

setup_off
    setup register offset from base

control_off
    control register offset from base

sr2_wtcnt_value_mask
    setup register- sr2_wtcnt_value mask

fbb_sel_mask
    setup register- FBB sel mask

rbb_sel_mask
    setup register- RBB sel mask

sr2_en_mask
    setup register- enable mask

opp_change_mask
    control register - mask to trigger LDOVBB change

opp_sel_mask
    control register - mask for mode to operate

.. _`ti_abb`:

struct ti_abb
=============

.. c:type:: struct ti_abb

    ABB instance data

.. _`ti_abb.definition`:

Definition
----------

.. code-block:: c

    struct ti_abb {
        struct regulator_desc rdesc;
        struct clk *clk;
        void __iomem *base;
        void __iomem *setup_reg;
        void __iomem *control_reg;
        void __iomem *int_base;
        void __iomem *efuse_base;
        void __iomem *ldo_base;
        const struct ti_abb_reg *regs;
        u32 txdone_mask;
        u32 ldovbb_override_mask;
        u32 ldovbb_vset_mask;
        struct ti_abb_info *info;
        int current_info_idx;
        u32 settling_time;
    }

.. _`ti_abb.members`:

Members
-------

rdesc
    regulator descriptor

clk
    clock(usually sysclk) supplying ABB block

base
    base address of ABB block

setup_reg
    setup register of ABB block

control_reg
    control register of ABB block

int_base
    interrupt register base address

efuse_base
    (optional) efuse base address for ABB modes

ldo_base
    (optional) LDOVBB vset override base address

regs
    pointer to struct ti_abb_reg for ABB block

txdone_mask
    mask on int_base for tranxdone interrupt

ldovbb_override_mask
    mask to ldo_base for overriding default LDO VBB
    vset with value from efuse

ldovbb_vset_mask
    mask to ldo_base for providing the VSET override

info
    array to per voltage ABB configuration

current_info_idx
    current index to info

settling_time
    SoC specific settling time for LDO VBB

.. _`ti_abb_rmw`:

ti_abb_rmw
==========

.. c:function:: u32 ti_abb_rmw(u32 mask, u32 value, void __iomem *reg)

    handy wrapper to set specific register bits

    :param mask:
        mask for register field
    :type mask: u32

    :param value:
        value shifted to mask location and written
    :type value: u32

    :param reg:
        register address
    :type reg: void __iomem \*

.. _`ti_abb_rmw.return`:

Return
------

final register value (may be unused)

.. _`ti_abb_check_txdone`:

ti_abb_check_txdone
===================

.. c:function:: bool ti_abb_check_txdone(const struct ti_abb *abb)

    handy wrapper to check ABB tranxdone status

    :param abb:
        pointer to the abb instance
    :type abb: const struct ti_abb \*

.. _`ti_abb_check_txdone.return`:

Return
------

true or false

.. _`ti_abb_clear_txdone`:

ti_abb_clear_txdone
===================

.. c:function:: void ti_abb_clear_txdone(const struct ti_abb *abb)

    handy wrapper to clear ABB tranxdone status

    :param abb:
        pointer to the abb instance
    :type abb: const struct ti_abb \*

.. _`ti_abb_wait_txdone`:

ti_abb_wait_txdone
==================

.. c:function:: int ti_abb_wait_txdone(struct device *dev, struct ti_abb *abb)

    waits for ABB tranxdone event

    :param dev:
        device
    :type dev: struct device \*

    :param abb:
        pointer to the abb instance
    :type abb: struct ti_abb \*

.. _`ti_abb_wait_txdone.return`:

Return
------

0 on success or -ETIMEDOUT if the event is not cleared on time.

.. _`ti_abb_clear_all_txdone`:

ti_abb_clear_all_txdone
=======================

.. c:function:: int ti_abb_clear_all_txdone(struct device *dev, const struct ti_abb *abb)

    clears ABB tranxdone event

    :param dev:
        device
    :type dev: struct device \*

    :param abb:
        pointer to the abb instance
    :type abb: const struct ti_abb \*

.. _`ti_abb_clear_all_txdone.return`:

Return
------

0 on success or -ETIMEDOUT if the event is not cleared on time.

.. _`ti_abb_program_ldovbb`:

ti_abb_program_ldovbb
=====================

.. c:function:: void ti_abb_program_ldovbb(struct device *dev, const struct ti_abb *abb, struct ti_abb_info *info)

    program LDOVBB register for override value

    :param dev:
        device
    :type dev: struct device \*

    :param abb:
        pointer to the abb instance
    :type abb: const struct ti_abb \*

    :param info:
        ABB info to program
    :type info: struct ti_abb_info \*

.. _`ti_abb_set_opp`:

ti_abb_set_opp
==============

.. c:function:: int ti_abb_set_opp(struct regulator_dev *rdev, struct ti_abb *abb, struct ti_abb_info *info)

    Setup ABB and LDO VBB for required bias

    :param rdev:
        regulator device
    :type rdev: struct regulator_dev \*

    :param abb:
        pointer to the abb instance
    :type abb: struct ti_abb \*

    :param info:
        ABB info to program
    :type info: struct ti_abb_info \*

.. _`ti_abb_set_opp.return`:

Return
------

0 on success or appropriate error value when fails

.. _`ti_abb_set_voltage_sel`:

ti_abb_set_voltage_sel
======================

.. c:function:: int ti_abb_set_voltage_sel(struct regulator_dev *rdev, unsigned sel)

    regulator accessor function to set ABB LDO

    :param rdev:
        regulator device
    :type rdev: struct regulator_dev \*

    :param sel:
        selector to index into required ABB LDO settings (maps to
        regulator descriptor's volt_table)
    :type sel: unsigned

.. _`ti_abb_set_voltage_sel.return`:

Return
------

0 on success or appropriate error value when fails

.. _`ti_abb_get_voltage_sel`:

ti_abb_get_voltage_sel
======================

.. c:function:: int ti_abb_get_voltage_sel(struct regulator_dev *rdev)

    Regulator accessor to get current ABB LDO setting

    :param rdev:
        regulator device
    :type rdev: struct regulator_dev \*

.. _`ti_abb_get_voltage_sel.return`:

Return
------

0 on success or appropriate error value when fails

.. _`ti_abb_init_timings`:

ti_abb_init_timings
===================

.. c:function:: int ti_abb_init_timings(struct device *dev, struct ti_abb *abb)

    setup ABB clock timing for the current platform

    :param dev:
        device
    :type dev: struct device \*

    :param abb:
        pointer to the abb instance
    :type abb: struct ti_abb \*

.. _`ti_abb_init_timings.return`:

Return
------

0 if timing is updated, else returns error result.

.. _`ti_abb_init_table`:

ti_abb_init_table
=================

.. c:function:: int ti_abb_init_table(struct device *dev, struct ti_abb *abb, struct regulator_init_data *rinit_data)

    Initialize ABB table from device tree

    :param dev:
        device
    :type dev: struct device \*

    :param abb:
        pointer to the abb instance
    :type abb: struct ti_abb \*

    :param rinit_data:
        regulator initdata
    :type rinit_data: struct regulator_init_data \*

.. _`ti_abb_init_table.return`:

Return
------

0 on success or appropriate error value when fails

.. _`ti_abb_probe`:

ti_abb_probe
============

.. c:function:: int ti_abb_probe(struct platform_device *pdev)

    Initialize an ABB ldo instance

    :param pdev:
        ABB platform device
    :type pdev: struct platform_device \*

.. _`ti_abb_probe.description`:

Description
-----------

Initializes an individual ABB LDO for required Body-Bias. ABB is used to
addional bias supply to SoC modules for power savings or mandatory stability
configuration at certain Operating Performance Points(OPPs).

.. _`ti_abb_probe.return`:

Return
------

0 on success or appropriate error value when fails

.. This file was automatic generated / don't edit.

