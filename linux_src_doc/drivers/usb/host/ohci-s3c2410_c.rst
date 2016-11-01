.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/ohci-s3c2410.c

.. _`usb_hcd_s3c2410_probe`:

usb_hcd_s3c2410_probe
=====================

.. c:function:: int usb_hcd_s3c2410_probe(const struct hc_driver *driver, struct platform_device *dev)

    initialize S3C2410-based HCDs

    :param const struct hc_driver \*driver:
        *undescribed*

    :param struct platform_device \*dev:
        *undescribed*

.. _`usb_hcd_s3c2410_probe.context`:

Context
-------

!in_interrupt()

.. _`usb_hcd_s3c2410_probe.description`:

Description
-----------

Allocates basic resources for this USB host controller, and
then invokes the \ :c:func:`start`\  method for the HCD associated with it
through the hotplug entry's driver_data.

.. This file was automatic generated / don't edit.

