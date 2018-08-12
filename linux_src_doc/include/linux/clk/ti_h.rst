.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/clk/ti.h

.. _`clk_omap_reg`:

struct clk_omap_reg
===================

.. c:type:: struct clk_omap_reg

    OMAP register declaration

.. _`clk_omap_reg.definition`:

Definition
----------

.. code-block:: c

    struct clk_omap_reg {
        void __iomem *ptr;
        u16 offset;
        u8 index;
        u8 flags;
    }

.. _`clk_omap_reg.members`:

Members
-------

ptr
    *undescribed*

offset
    offset from the master IP module base address

index
    index of the master IP module

flags
    *undescribed*

.. _`dpll_data`:

struct dpll_data
================

.. c:type:: struct dpll_data

    DPLL registers and integration data

.. _`dpll_data.definition`:

Definition
----------

.. code-block:: c

    struct dpll_data {
        struct clk_omap_reg mult_div1_reg;
        u32 mult_mask;
        u32 div1_mask;
        struct clk_hw *clk_bypass;
        struct clk_hw *clk_ref;
        struct clk_omap_reg control_reg;
        u32 enable_mask;
        unsigned long last_rounded_rate;
        u16 last_rounded_m;
        u8 last_rounded_m4xen;
        u8 last_rounded_lpmode;
        u16 max_multiplier;
        u8 last_rounded_n;
        u8 min_divider;
        u16 max_divider;
        unsigned long max_rate;
        u8 modes;
        struct clk_omap_reg autoidle_reg;
        struct clk_omap_reg idlest_reg;
        u32 autoidle_mask;
        u32 freqsel_mask;
        u32 idlest_mask;
        u32 dco_mask;
        u32 sddiv_mask;
        u32 dcc_mask;
        unsigned long dcc_rate;
        u32 lpmode_mask;
        u32 m4xen_mask;
        u8 auto_recal_bit;
        u8 recal_en_bit;
        u8 recal_st_bit;
        u8 flags;
    }

.. _`dpll_data.members`:

Members
-------

mult_div1_reg
    register containing the DPLL M and N bitfields

mult_mask
    mask of the DPLL M bitfield in \ ``mult_div1_reg``\ 

div1_mask
    mask of the DPLL N bitfield in \ ``mult_div1_reg``\ 

clk_bypass
    struct clk_hw pointer to the clock's bypass clock input

clk_ref
    struct clk_hw pointer to the clock's reference clock input

control_reg
    register containing the DPLL mode bitfield

enable_mask
    mask of the DPLL mode bitfield in \ ``control_reg``\ 

last_rounded_rate
    cache of the last rate result of \ :c:func:`omap2_dpll_round_rate`\ 

last_rounded_m
    cache of the last M result of \ :c:func:`omap2_dpll_round_rate`\ 

last_rounded_m4xen
    cache of the last M4X result of
    \ :c:func:`omap4_dpll_regm4xen_round_rate`\ 

last_rounded_lpmode
    cache of the last lpmode result of
    \ :c:func:`omap4_dpll_lpmode_recalc`\ 

max_multiplier
    maximum valid non-bypass multiplier value (actual)

last_rounded_n
    cache of the last N result of \ :c:func:`omap2_dpll_round_rate`\ 

min_divider
    minimum valid non-bypass divider value (actual)

max_divider
    maximum valid non-bypass divider value (actual)

max_rate
    maximum clock rate for the DPLL

modes
    possible values of \ ``enable_mask``\ 

autoidle_reg
    register containing the DPLL autoidle mode bitfield

idlest_reg
    register containing the DPLL idle status bitfield

autoidle_mask
    mask of the DPLL autoidle mode bitfield in \ ``autoidle_reg``\ 

freqsel_mask
    mask of the DPLL jitter correction bitfield in \ ``control_reg``\ 

idlest_mask
    mask of the DPLL idle status bitfield in \ ``idlest_reg``\ 

dco_mask
    *undescribed*

sddiv_mask
    *undescribed*

dcc_mask
    mask of the DPLL DCC correction bitfield \ ``mult_div1_reg``\ 

dcc_rate
    rate atleast which DCC \ ``dcc_mask``\  must be set

lpmode_mask
    mask of the DPLL low-power mode bitfield in \ ``control_reg``\ 

m4xen_mask
    mask of the DPLL M4X multiplier bitfield in \ ``control_reg``\ 

auto_recal_bit
    bitshift of the driftguard enable bit in \ ``control_reg``\ 

recal_en_bit
    bitshift of the PRM_IRQENABLE\_\* bit for recalibration IRQs

recal_st_bit
    bitshift of the PRM_IRQSTATUS\_\* bit for recalibration IRQs

flags
    DPLL type/features (see below)

.. _`dpll_data.description`:

Description
-----------

Possible values for \ ``flags``\ :

.. _`dpll_data.dpll_j_type`:

DPLL_J_TYPE
-----------

"J-type DPLL" (only some 36xx, 4xxx DPLLs)

\ ``freqsel_mask``\  is only used on the OMAP34xx family and AM35xx.

XXX Some DPLLs have multiple bypass inputs, so it's not technically
correct to only have one \ ``clk_bypass``\  pointer.

XXX The runtime-variable fields (@last_rounded_rate, \ ``last_rounded_m``\ ,
\ ``last_rounded_n``\ ) should be separated from the runtime-fixed fields
and placed into a different structure, so that the runtime-fixed data
can be placed into read-only space.

.. _`clk_hw_omap_ops`:

struct clk_hw_omap_ops
======================

.. c:type:: struct clk_hw_omap_ops

    OMAP clk ops

.. _`clk_hw_omap_ops.definition`:

Definition
----------

.. code-block:: c

    struct clk_hw_omap_ops {
        void (*find_idlest)(struct clk_hw_omap *oclk,struct clk_omap_reg *idlest_reg, u8 *idlest_bit, u8 *idlest_val);
        void (*find_companion)(struct clk_hw_omap *oclk,struct clk_omap_reg *other_reg, u8 *other_bit);
        void (*allow_idle)(struct clk_hw_omap *oclk);
        void (*deny_idle)(struct clk_hw_omap *oclk);
    }

.. _`clk_hw_omap_ops.members`:

Members
-------

find_idlest
    find idlest register information for a clock

find_companion
    find companion clock register information for a clock,
    basically converts CM_ICLKEN\* <-> CM_FCLKEN\*

allow_idle
    enables autoidle hardware functionality for a clock

deny_idle
    prevent autoidle hardware functionality for a clock

.. _`clk_hw_omap`:

struct clk_hw_omap
==================

.. c:type:: struct clk_hw_omap

    OMAP struct clk

.. _`clk_hw_omap.definition`:

Definition
----------

.. code-block:: c

    struct clk_hw_omap {
        struct clk_hw hw;
        struct list_head node;
        unsigned long fixed_rate;
        u8 fixed_div;
        struct clk_omap_reg enable_reg;
        u8 enable_bit;
        u8 flags;
        struct clk_omap_reg clksel_reg;
        struct dpll_data *dpll_data;
        const char *clkdm_name;
        struct clockdomain *clkdm;
        const struct clk_hw_omap_ops *ops;
    }

.. _`clk_hw_omap.members`:

Members
-------

hw
    *undescribed*

node
    list_head connecting this clock into the full clock list

fixed_rate
    *undescribed*

fixed_div
    *undescribed*

enable_reg
    register to write to enable the clock (see \ ``enable_bit``\ )

enable_bit
    bitshift to write to enable/disable the clock (see \ ``enable_reg``\ )

flags
    see "struct clk.flags possibilities" above

clksel_reg
    for clksel clks, register va containing src/divisor select

dpll_data
    for DPLLs, pointer to struct dpll_data for this clock

clkdm_name
    clockdomain name that this clock is contained in

clkdm
    pointer to struct clockdomain, resolved from \ ``clkdm_name``\  at runtime

ops
    clock ops for this clock

.. _`ti_clk_ll_ops`:

struct ti_clk_ll_ops
====================

.. c:type:: struct ti_clk_ll_ops

    low-level ops for clocks

.. _`ti_clk_ll_ops.definition`:

Definition
----------

.. code-block:: c

    struct ti_clk_ll_ops {
        u32 (*clk_readl)(const struct clk_omap_reg *reg);
        void (*clk_writel)(u32 val, const struct clk_omap_reg *reg);
        void (*clk_rmw)(u32 val, u32 mask, const struct clk_omap_reg *reg);
        int (*clkdm_clk_enable)(struct clockdomain *clkdm, struct clk *clk);
        int (*clkdm_clk_disable)(struct clockdomain *clkdm, struct clk *clk);
        struct clockdomain * (*clkdm_lookup)(const char *name);
        int (*cm_wait_module_ready)(u8 part, s16 prcm_mod, u16 idlest_reg, u8 idlest_shift);
        int (*cm_split_idlest_reg)(struct clk_omap_reg *idlest_reg, s16 *prcm_inst, u8 *idlest_reg_id);
    }

.. _`ti_clk_ll_ops.members`:

Members
-------

clk_readl
    pointer to register read function

clk_writel
    pointer to register write function

clk_rmw
    pointer to register read-modify-write function

clkdm_clk_enable
    pointer to clockdomain enable function

clkdm_clk_disable
    pointer to clockdomain disable function

clkdm_lookup
    pointer to clockdomain lookup function

cm_wait_module_ready
    pointer to CM module wait ready function

cm_split_idlest_reg
    pointer to CM module function to split idlest reg

.. _`ti_clk_ll_ops.description`:

Description
-----------

Low-level ops are generally used by the basic clock types (clk-gate,
clk-mux, clk-divider etc.) to provide support for various low-level
hadrware interfaces (direct MMIO, regmap etc.), and is initialized
by board code. Low-level ops also contain some other platform specific
operations not provided directly by clock drivers.

.. This file was automatic generated / don't edit.

