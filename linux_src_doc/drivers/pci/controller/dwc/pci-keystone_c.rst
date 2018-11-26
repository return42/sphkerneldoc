.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/controller/dwc/pci-keystone.c

.. _`ks_pcie_set_dbi_mode`:

ks_pcie_set_dbi_mode
====================

.. c:function:: void ks_pcie_set_dbi_mode(struct keystone_pcie *ks_pcie)

    Set DBI mode to access overlaid BAR mask registers

    :param ks_pcie:
        *undescribed*
    :type ks_pcie: struct keystone_pcie \*

.. _`ks_pcie_set_dbi_mode.description`:

Description
-----------

Since modification of dbi_cs2 involves different clock domain, read the
status back to ensure the transition is complete.

.. _`ks_pcie_clear_dbi_mode`:

ks_pcie_clear_dbi_mode
======================

.. c:function:: void ks_pcie_clear_dbi_mode(struct keystone_pcie *ks_pcie)

    Disable DBI mode

    :param ks_pcie:
        *undescribed*
    :type ks_pcie: struct keystone_pcie \*

.. _`ks_pcie_clear_dbi_mode.description`:

Description
-----------

Since modification of dbi_cs2 involves different clock domain, read the
status back to ensure the transition is complete.

.. _`ks_pcie_v3_65_scan_bus`:

ks_pcie_v3_65_scan_bus
======================

.. c:function:: void ks_pcie_v3_65_scan_bus(struct pcie_port *pp)

    keystone scan_bus post initialization

    :param pp:
        *undescribed*
    :type pp: struct pcie_port \*

.. _`ks_pcie_v3_65_scan_bus.description`:

Description
-----------

This sets BAR0 to enable inbound access for MSI_IRQ register

.. _`ks_pcie_link_up`:

ks_pcie_link_up
===============

.. c:function:: int ks_pcie_link_up(struct dw_pcie *pci)

    Check if link up

    :param pci:
        *undescribed*
    :type pci: struct dw_pcie \*

.. _`ks_pcie_dw_host_init`:

ks_pcie_dw_host_init
====================

.. c:function:: int ks_pcie_dw_host_init(struct keystone_pcie *ks_pcie)

    initialize host for v3_65 dw hardware

    :param ks_pcie:
        *undescribed*
    :type ks_pcie: struct keystone_pcie \*

.. _`ks_pcie_dw_host_init.description`:

Description
-----------

Ioremap the register resources, initialize legacy irq domain
and call \ :c:func:`dw_pcie_v3_65_host_init`\  API to initialize the Keystone
PCI host controller.

.. _`ks_pcie_legacy_irq_handler`:

ks_pcie_legacy_irq_handler
==========================

.. c:function:: void ks_pcie_legacy_irq_handler(struct irq_desc *desc)

    Handle legacy interrupt

    :param desc:
        Pointer to irq descriptor
    :type desc: struct irq_desc \*

.. _`ks_pcie_legacy_irq_handler.description`:

Description
-----------

Traverse through pending legacy interrupts and invoke handler for each. Also
takes care of interrupt controller level mask/ack operation.

.. This file was automatic generated / don't edit.

