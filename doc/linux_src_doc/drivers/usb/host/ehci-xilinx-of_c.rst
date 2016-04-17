.. -*- coding: utf-8; mode: rst -*-

================
ehci-xilinx-of.c
================


.. _`ehci_xilinx_port_handed_over`:

ehci_xilinx_port_handed_over
============================

.. c:function:: int ehci_xilinx_port_handed_over (struct usb_hcd *hcd, int portnum)

    hand the port out if failed to enable it

    :param struct usb_hcd \*hcd:
        Pointer to the usb_hcd device to which the host controller bound

    :param int portnum:
        Port number to which the device is attached.



.. _`ehci_xilinx_port_handed_over.description`:

Description
-----------

This function is used as a place to tell the user that the Xilinx USB host
controller does support LS devices. And in an HS only configuration, it
does not support FS devices either. It is hoped that this can help a
confused user.

There are cases when the host controller fails to enable the port due to,
for example, insufficient power that can be supplied to the device from
the USB bus. In those cases, the messages printed here are not helpful.



.. _`ehci_hcd_xilinx_of_probe`:

ehci_hcd_xilinx_of_probe
========================

.. c:function:: int ehci_hcd_xilinx_of_probe (struct platform_device *op)

    Probe method for the USB host controller

    :param struct platform_device \*op:
        pointer to the platform_device bound to the host controller



.. _`ehci_hcd_xilinx_of_probe.description`:

Description
-----------

This function requests resources and sets up appropriate properties for the
host controller. Because the Xilinx USB host controller can be configured
as HS only or HS/FS only, it checks the configuration in the device tree
entry, and sets an appropriate value for hcd->has_tt.



.. _`ehci_hcd_xilinx_of_remove`:

ehci_hcd_xilinx_of_remove
=========================

.. c:function:: int ehci_hcd_xilinx_of_remove (struct platform_device *op)

    shutdown hcd and release resources

    :param struct platform_device \*op:
        pointer to platform_device structure that is to be removed



.. _`ehci_hcd_xilinx_of_remove.description`:

Description
-----------

Remove the hcd structure, and release resources that has been requested
during probe.

