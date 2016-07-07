.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/class/cdc-wdm.c

.. _`usb_cdc_wdm_register`:

usb_cdc_wdm_register
====================

.. c:function:: struct usb_driver *usb_cdc_wdm_register(struct usb_interface *intf, struct usb_endpoint_descriptor *ep, int bufsize, int (*) manage_power (struct usb_interface *, int)

    register a WDM subdriver

    :param struct usb_interface \*intf:
        usb interface the subdriver will associate with

    :param struct usb_endpoint_descriptor \*ep:
        interrupt endpoint to monitor for notifications

    :param int bufsize:
        maximum message size to support for read/write

    :param (int (\*) manage_power (struct usb_interface \*, int):
        *undescribed*

.. _`usb_cdc_wdm_register.description`:

Description
-----------

Create WDM usb class character device and associate it with intf
without binding, allowing another driver to manage the interface.

The subdriver will manage the given interrupt endpoint exclusively
and will issue control requests referring to the given intf. It
will otherwise avoid interferring, and in particular not do
usb_set_intfdata/usb_get_intfdata on intf.

The return value is a pointer to the subdriver's struct usb_driver.
The registering driver is responsible for calling this subdriver's
disconnect, suspend, resume, pre_reset and post_reset methods from
its own.

.. This file was automatic generated / don't edit.

