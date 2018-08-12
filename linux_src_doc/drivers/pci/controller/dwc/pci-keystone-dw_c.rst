.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/controller/dwc/pci-keystone-dw.c

.. _`ks_dw_pcie_set_dbi_mode`:

ks_dw_pcie_set_dbi_mode
=======================

.. c:function:: void ks_dw_pcie_set_dbi_mode(struct keystone_pcie *ks_pcie)

    Set DBI mode to access overlaid BAR mask registers

    :param struct keystone_pcie \*ks_pcie:
        *undescribed*

.. _`ks_dw_pcie_set_dbi_mode.description`:

Description
-----------

Since modification of dbi_cs2 involves different clock domain, read the
status back to ensure the transition is complete.

.. _`ks_dw_pcie_clear_dbi_mode`:

ks_dw_pcie_clear_dbi_mode
=========================

.. c:function:: void ks_dw_pcie_clear_dbi_mode(struct keystone_pcie *ks_pcie)

    Disable DBI mode

    :param struct keystone_pcie \*ks_pcie:
        *undescribed*

.. _`ks_dw_pcie_clear_dbi_mode.description`:

Description
-----------

Since modification of dbi_cs2 involves different clock domain, read the
status back to ensure the transition is complete.

.. _`ks_pcie_cfg_setup`:

ks_pcie_cfg_setup
=================

.. c:function:: void __iomem *ks_pcie_cfg_setup(struct keystone_pcie *ks_pcie, u8 bus, unsigned int devfn)

    Set up configuration space address for a device

    :param struct keystone_pcie \*ks_pcie:
        ptr to keystone_pcie structure

    :param u8 bus:
        Bus number the device is residing on

    :param unsigned int devfn:
        device, function number info

.. _`ks_pcie_cfg_setup.description`:

Description
-----------

Forms and returns the address of configuration space mapped in PCIESS
address space 0.  Also configures CFG_SETUP for remote configuration space
access.

The address space has two regions to access configuration - local and remote.
We access local region for bus 0 (as RC is attached on bus 0) and remote
region for others with TYPE 1 access when bus > 1.  As for device on bus = 1,
we will do TYPE 0 access as it will be on our secondary bus (logical).
CFG_SETUP is needed only for remote configuration access.

.. _`ks_dw_pcie_v3_65_scan_bus`:

ks_dw_pcie_v3_65_scan_bus
=========================

.. c:function:: void ks_dw_pcie_v3_65_scan_bus(struct pcie_port *pp)

    keystone scan_bus post initialization

    :param struct pcie_port \*pp:
        *undescribed*

.. _`ks_dw_pcie_v3_65_scan_bus.description`:

Description
-----------

This sets BAR0 to enable inbound access for MSI_IRQ register

.. _`ks_dw_pcie_link_up`:

ks_dw_pcie_link_up
==================

.. c:function:: int ks_dw_pcie_link_up(struct dw_pcie *pci)

    Check if link up

    :param struct dw_pcie \*pci:
        *undescribed*

.. _`ks_dw_pcie_host_init`:

ks_dw_pcie_host_init
====================

.. c:function:: int ks_dw_pcie_host_init(struct keystone_pcie *ks_pcie, struct device_node *msi_intc_np)

    initialize host for v3_65 dw hardware

    :param struct keystone_pcie \*ks_pcie:
        *undescribed*

    :param struct device_node \*msi_intc_np:
        *undescribed*

.. _`ks_dw_pcie_host_init.description`:

Description
-----------

Ioremap the register resources, initialize legacy irq domain
and call \ :c:func:`dw_pcie_v3_65_host_init`\  API to initialize the Keystone
PCI host controller.

.. This file was automatic generated / don't edit.

