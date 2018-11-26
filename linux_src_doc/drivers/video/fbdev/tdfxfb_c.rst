.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/tdfxfb.c

.. _`tdfxfb_probe`:

tdfxfb_probe
============

.. c:function:: int tdfxfb_probe(struct pci_dev *pdev, const struct pci_device_id *id)

    Device Initializiation

    :param pdev:
        PCI Device to initialize
    :type pdev: struct pci_dev \*

    :param id:
        PCI Device ID
    :type id: const struct pci_device_id \*

.. _`tdfxfb_probe.description`:

Description
-----------

Initializes and allocates resources for PCI device \ ``pdev``\ .

.. _`tdfxfb_remove`:

tdfxfb_remove
=============

.. c:function:: void tdfxfb_remove(struct pci_dev *pdev)

    Device removal

    :param pdev:
        PCI Device to cleanup
    :type pdev: struct pci_dev \*

.. _`tdfxfb_remove.description`:

Description
-----------

Releases all resources allocated during the course of the driver's
lifetime for the PCI device \ ``pdev``\ .

.. This file was automatic generated / don't edit.

