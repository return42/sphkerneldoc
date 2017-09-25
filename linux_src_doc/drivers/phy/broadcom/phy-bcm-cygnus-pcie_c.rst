.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/phy/broadcom/phy-bcm-cygnus-pcie.c

.. _`cygnus_pcie_phy`:

struct cygnus_pcie_phy
======================

.. c:type:: struct cygnus_pcie_phy

    Cygnus PCIe PHY device

.. _`cygnus_pcie_phy.definition`:

Definition
----------

.. code-block:: c

    struct cygnus_pcie_phy {
        struct cygnus_pcie_phy_core *core;
        enum cygnus_pcie_phy_id id;
        struct phy *phy;
    }

.. _`cygnus_pcie_phy.members`:

Members
-------

core
    pointer to the Cygnus PCIe PHY core control

id
    internal ID to identify the Cygnus PCIe PHY

phy
    pointer to the kernel PHY device

.. _`cygnus_pcie_phy_core`:

struct cygnus_pcie_phy_core
===========================

.. c:type:: struct cygnus_pcie_phy_core

    Cygnus PCIe PHY core control

.. _`cygnus_pcie_phy_core.definition`:

Definition
----------

.. code-block:: c

    struct cygnus_pcie_phy_core {
        struct device *dev;
        void __iomem *base;
        struct mutex lock;
        struct cygnus_pcie_phy phys[MAX_NUM_PHYS];
    }

.. _`cygnus_pcie_phy_core.members`:

Members
-------

dev
    pointer to device

base
    base register

lock
    mutex to protect access to individual PHYs

phys
    pointer to Cygnus PHY device

.. This file was automatic generated / don't edit.

