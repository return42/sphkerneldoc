.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/microchip/lan743x_main.c

.. _`lan743x_pcidev_remove`:

lan743x_pcidev_remove
=====================

.. c:function:: void lan743x_pcidev_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`lan743x_pcidev_remove.description`:

Description
-----------

this is called by the PCI subsystem to alert the driver
that it should release a PCI device.  This could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. This file was automatic generated / don't edit.

