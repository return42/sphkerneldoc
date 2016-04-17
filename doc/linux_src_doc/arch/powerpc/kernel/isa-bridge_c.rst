.. -*- coding: utf-8; mode: rst -*-

============
isa-bridge.c
============


.. _`isa_bridge_find_early`:

isa_bridge_find_early
=====================

.. c:function:: void isa_bridge_find_early (struct pci_controller *hose)

    Find and map the ISA IO space early before main PCI discovery. This is optionally called by the arch code when adding PCI PHBs to get early access to ISA IO ports

    :param struct pci_controller \*hose:

        *undescribed*



.. _`isa_bridge_find_late`:

isa_bridge_find_late
====================

.. c:function:: void isa_bridge_find_late (struct pci_dev *pdev, struct device_node *devnode)

    Find and map the ISA IO space upon discovery of a new ISA bridge

    :param struct pci_dev \*pdev:

        *undescribed*

    :param struct device_node \*devnode:

        *undescribed*



.. _`isa_bridge_remove`:

isa_bridge_remove
=================

.. c:function:: void isa_bridge_remove ( void)

    Remove/unmap an ISA bridge

    :param void:
        no arguments



.. _`isa_bridge_notify`:

isa_bridge_notify
=================

.. c:function:: int isa_bridge_notify (struct notifier_block *nb, unsigned long action, void *data)

    Get notified of PCI devices addition/removal

    :param struct notifier_block \*nb:

        *undescribed*

    :param unsigned long action:

        *undescribed*

    :param void \*data:

        *undescribed*



.. _`isa_bridge_init`:

isa_bridge_init
===============

.. c:function:: int isa_bridge_init ( void)

    register to be notified of ISA bridge addition/removal

    :param void:
        no arguments

