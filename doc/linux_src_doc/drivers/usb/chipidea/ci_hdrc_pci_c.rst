.. -*- coding: utf-8; mode: rst -*-

=============
ci_hdrc_pci.c
=============


.. _`ci_hdrc_pci_probe`:

ci_hdrc_pci_probe
=================

.. c:function:: int ci_hdrc_pci_probe (struct pci_dev *pdev, const struct pci_device_id *id)

    :param struct pci_dev \*pdev:
        USB device controller being probed

    :param const struct pci_device_id \*id:
        PCI hotplug ID connecting controller to UDC framework



.. _`ci_hdrc_pci_probe.description`:

Description
-----------

This function returns an error code
Allocates basic PCI resources for this USB device controller, and then
invokes the :c:func:`udc_probe` method to start the UDC associated with it



.. _`ci_hdrc_pci_remove`:

ci_hdrc_pci_remove
==================

.. c:function:: void ci_hdrc_pci_remove (struct pci_dev *pdev)

    :param struct pci_dev \*pdev:
        USB Device Controller being removed



.. _`ci_hdrc_pci_remove.description`:

Description
-----------

Reverses the effect of :c:func:`ci_hdrc_pci_probe`,
first invoking the :c:func:`udc_remove` and then releases
all PCI resources allocated for this USB device controller

