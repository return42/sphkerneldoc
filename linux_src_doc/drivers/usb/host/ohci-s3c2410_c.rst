.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/ohci-s3c2410.c

.. _`ohci_hcd_s3c2410_probe`:

ohci_hcd_s3c2410_probe
======================

.. c:function:: int ohci_hcd_s3c2410_probe(struct platform_device *dev)

    initialize S3C2410-based HCDs

    :param struct platform_device \*dev:
        *undescribed*

.. _`ohci_hcd_s3c2410_probe.context`:

Context
-------

!in_interrupt()

.. _`ohci_hcd_s3c2410_probe.description`:

Description
-----------

Allocates basic resources for this USB host controller, and
then invokes the \ :c:func:`start`\  method for the HCD associated with it
through the hotplug entry's driver_data.

.. This file was automatic generated / don't edit.

