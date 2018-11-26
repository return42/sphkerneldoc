.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/phy/broadcom/phy-bcm-sr-pcie.c

.. _`sr_pcie_phy`:

struct sr_pcie_phy
==================

.. c:type:: struct sr_pcie_phy

    Stingray PCIe PHY

.. _`sr_pcie_phy.definition`:

Definition
----------

.. code-block:: c

    struct sr_pcie_phy {
        struct sr_pcie_phy_core *core;
        unsigned int index;
        struct phy *phy;
    }

.. _`sr_pcie_phy.members`:

Members
-------

core
    pointer to the Stingray PCIe PHY core control

index
    PHY index

phy
    pointer to the kernel PHY device

.. _`sr_pcie_phy_core`:

struct sr_pcie_phy_core
=======================

.. c:type:: struct sr_pcie_phy_core

    Stingray PCIe PHY core control

.. _`sr_pcie_phy_core.definition`:

Definition
----------

.. code-block:: c

    struct sr_pcie_phy_core {
        struct device *dev;
        void __iomem *base;
        struct regmap *cdru;
        struct regmap *mhb;
        u32 pipemux;
        struct sr_pcie_phy phys[SR_NR_PCIE_PHYS];
    }

.. _`sr_pcie_phy_core.members`:

Members
-------

dev
    pointer to device

base
    base register of PCIe SS

cdru
    regmap to the CDRU device

mhb
    regmap to the MHB device

pipemux
    pipemuex strap

phys
    array of PCIe PHYs

.. This file was automatic generated / don't edit.

