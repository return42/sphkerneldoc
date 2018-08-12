.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/phy/qualcomm/phy-qcom-qusb2.c

.. _`qusb2_phy`:

struct qusb2_phy
================

.. c:type:: struct qusb2_phy

    structure holding qusb2 phy attributes

.. _`qusb2_phy.definition`:

Definition
----------

.. code-block:: c

    struct qusb2_phy {
        struct phy *phy;
        void __iomem *base;
        struct clk *cfg_ahb_clk;
        struct clk *ref_clk;
        struct clk *iface_clk;
        struct reset_control *phy_reset;
        struct regulator_bulk_data vregs[QUSB2_NUM_VREGS];
        struct regmap *tcsr;
        struct nvmem_cell *cell;
        bool override_imp_res_offset;
        u8 imp_res_offset_value;
        bool override_hstx_trim;
        u8 hstx_trim_value;
        bool override_preemphasis;
        u8 preemphasis_level;
        bool override_preemphasis_width;
        u8 preemphasis_width;
        const struct qusb2_phy_cfg *cfg;
        bool has_se_clk_scheme;
        bool phy_initialized;
        enum phy_mode mode;
    }

.. _`qusb2_phy.members`:

Members
-------

phy
    generic phy

base
    iomapped memory space for qubs2 phy

cfg_ahb_clk
    AHB2PHY interface clock

ref_clk
    phy reference clock

iface_clk
    phy interface clock

phy_reset
    phy reset control

vregs
    regulator supplies bulk data

tcsr
    TCSR syscon register map

cell
    nvmem cell containing phy tuning value

override_imp_res_offset
    PHY should use different rescode offset

imp_res_offset_value
    rescode offset to be updated in IMP_CTRL1 register

override_hstx_trim
    PHY should use different HSTX o/p current value

hstx_trim_value
    HSTX_TRIM value to be updated in TUNE1 register

override_preemphasis
    PHY should use different pre-amphasis amplitude

preemphasis_level
    Amplitude Pre-Emphasis to be updated in TUNE1 register

override_preemphasis_width
    PHY should use different pre-emphasis duration

preemphasis_width
    half/full-width Pre-Emphasis updated via TUNE1

cfg
    phy config data

has_se_clk_scheme
    indicate if PHY has single-ended ref clock scheme

phy_initialized
    indicate if PHY has been initialized

mode
    current PHY mode

.. This file was automatic generated / don't edit.

