.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/isa-bridge.c

.. _`isa_bridge_find_early`:

isa_bridge_find_early
=====================

.. c:function:: void isa_bridge_find_early(struct pci_controller *hose)

    Find and map the ISA IO space early before main PCI discovery. This is optionally called by the arch code when adding PCI PHBs to get early access to ISA IO ports

    :param hose:
        *undescribed*
    :type hose: struct pci_controller \*

.. _`isa_bridge_init_non_pci`:

isa_bridge_init_non_pci
=======================

.. c:function:: void isa_bridge_init_non_pci(struct device_node *np)

    Find and map the ISA IO space early before main PCI discovery. This is optionally called by the arch code when adding PCI PHBs to get early access to ISA IO ports

    :param np:
        *undescribed*
    :type np: struct device_node \*

.. _`isa_bridge_find_late`:

isa_bridge_find_late
====================

.. c:function:: void isa_bridge_find_late(struct pci_dev *pdev, struct device_node *devnode)

    Find and map the ISA IO space upon discovery of a new ISA bridge

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

    :param devnode:
        *undescribed*
    :type devnode: struct device_node \*

.. _`isa_bridge_remove`:

isa_bridge_remove
=================

.. c:function:: void isa_bridge_remove( void)

    Remove/unmap an ISA bridge

    :param void:
        no arguments
    :type void: 

.. _`isa_bridge_notify`:

isa_bridge_notify
=================

.. c:function:: int isa_bridge_notify(struct notifier_block *nb, unsigned long action, void *data)

    Get notified of PCI devices addition/removal

    :param nb:
        *undescribed*
    :type nb: struct notifier_block \*

    :param action:
        *undescribed*
    :type action: unsigned long

    :param data:
        *undescribed*
    :type data: void \*

.. _`isa_bridge_init`:

isa_bridge_init
===============

.. c:function:: int isa_bridge_init( void)

    register to be notified of ISA bridge addition/removal

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

