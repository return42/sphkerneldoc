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
        const struct qusb2_phy_cfg *cfg;
        bool has_se_clk_scheme;
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

cfg
    phy config data

has_se_clk_scheme
    indicate if PHY has single-ended ref clock scheme

.. This file was automatic generated / don't edit.

