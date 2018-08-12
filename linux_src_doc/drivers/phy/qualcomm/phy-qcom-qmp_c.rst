.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/phy/qualcomm/phy-qcom-qmp.c

.. _`qmp_phy`:

struct qmp_phy
==============

.. c:type:: struct qmp_phy

    per-lane phy descriptor

.. _`qmp_phy.definition`:

Definition
----------

.. code-block:: c

    struct qmp_phy {
        struct phy *phy;
        void __iomem *tx;
        void __iomem *rx;
        void __iomem *pcs;
        void __iomem *pcs_misc;
        struct clk *pipe_clk;
        unsigned int index;
        struct qcom_qmp *qmp;
        struct reset_control *lane_rst;
    }

.. _`qmp_phy.members`:

Members
-------

phy
    generic phy

tx
    iomapped memory space for lane's tx

rx
    iomapped memory space for lane's rx

pcs
    iomapped memory space for lane's pcs

pcs_misc
    iomapped memory space for lane's pcs_misc

pipe_clk
    pipe lock

index
    lane index

qmp
    QMP phy to which this lane belongs

lane_rst
    lane's reset controller

.. _`qcom_qmp`:

struct qcom_qmp
===============

.. c:type:: struct qcom_qmp

    structure holding QMP phy block attributes

.. _`qcom_qmp.definition`:

Definition
----------

.. code-block:: c

    struct qcom_qmp {
        struct device *dev;
        void __iomem *serdes;
        void __iomem *dp_com;
        struct clk_bulk_data *clks;
        struct reset_control **resets;
        struct regulator_bulk_data *vregs;
        const struct qmp_phy_cfg *cfg;
        struct qmp_phy **phys;
        struct mutex phy_mutex;
        int init_count;
        bool phy_initialized;
        enum phy_mode mode;
    }

.. _`qcom_qmp.members`:

Members
-------

dev
    device

serdes
    iomapped memory space for phy's serdes

dp_com
    iomapped memory space for phy's dp_com control block

clks
    array of clocks required by phy

resets
    array of resets required by phy

vregs
    regulator supplies bulk data

cfg
    phy specific configuration

phys
    array of per-lane phy descriptors

phy_mutex
    mutex lock for PHY common block initialization

init_count
    phy common block initialization count

phy_initialized
    indicate if PHY has been initialized

mode
    current PHY mode

.. This file was automatic generated / don't edit.

