.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/tdfxfb.c

.. _`tdfxfb_probe`:

tdfxfb_probe
============

.. c:function:: int tdfxfb_probe(struct pci_dev *pdev, const struct pci_device_id *id)

    Device Initializiation

    :param struct pci_dev \*pdev:
        PCI Device to initialize

    :param const struct pci_device_id \*id:
        PCI Device ID

.. _`tdfxfb_probe.description`:

Description
-----------

Initializes and allocates resources for PCI device \ ``pdev``\ .

.. _`tdfxfb_remove`:

tdfxfb_remove
=============

.. c:function:: void tdfxfb_remove(struct pci_dev *pdev)

    Device removal

    :param struct pci_dev \*pdev:
        PCI Device to cleanup

.. _`tdfxfb_remove.description`:

Description
-----------

Releases all resources allocated during the course of the driver's
lifetime for the PCI device \ ``pdev``\ .

.. This file was automatic generated / don't edit.

