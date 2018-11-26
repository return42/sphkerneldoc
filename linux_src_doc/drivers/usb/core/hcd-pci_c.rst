.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/core/hcd-pci.c

.. _`usb_hcd_pci_probe`:

usb_hcd_pci_probe
=================

.. c:function:: int usb_hcd_pci_probe(struct pci_dev *dev, const struct pci_device_id *id)

    initialize PCI-based HCDs

    :param dev:
        USB Host Controller being probed
    :type dev: struct pci_dev \*

    :param id:
        pci hotplug id connecting controller to HCD framework
    :type id: const struct pci_device_id \*

.. _`usb_hcd_pci_probe.context`:

Context
-------

!in_interrupt()

.. _`usb_hcd_pci_probe.description`:

Description
-----------

Allocates basic PCI resources for this USB host controller, and
then invokes the \ :c:func:`start`\  method for the HCD associated with it
through the hotplug entry's driver_data.

Store this function in the HCD's struct pci_driver as \ :c:func:`probe`\ .

.. _`usb_hcd_pci_probe.return`:

Return
------

0 if successful.

.. _`usb_hcd_pci_remove`:

usb_hcd_pci_remove
==================

.. c:function:: void usb_hcd_pci_remove(struct pci_dev *dev)

    shutdown processing for PCI-based HCDs

    :param dev:
        USB Host Controller being removed
    :type dev: struct pci_dev \*

.. _`usb_hcd_pci_remove.context`:

Context
-------

!in_interrupt()

.. _`usb_hcd_pci_remove.description`:

Description
-----------

Reverses the effect of \ :c:func:`usb_hcd_pci_probe`\ , first invoking
the HCD's \ :c:func:`stop`\  method.  It is always called from a thread
context, normally "rmmod", "apmd", or something similar.

Store this function in the HCD's struct pci_driver as \ :c:func:`remove`\ .

.. _`usb_hcd_pci_shutdown`:

usb_hcd_pci_shutdown
====================

.. c:function:: void usb_hcd_pci_shutdown(struct pci_dev *dev)

    shutdown host controller

    :param dev:
        USB Host Controller being shutdown
    :type dev: struct pci_dev \*

.. This file was automatic generated / don't edit.

