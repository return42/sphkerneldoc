.. -*- coding: utf-8; mode: rst -*-

======
file.c
======

.. _`usb_register_dev`:

usb_register_dev
================

.. c:function:: int usb_register_dev (struct usb_interface *intf, struct usb_class_driver *class_driver)

    register a USB device, and ask for a minor number

    :param struct usb_interface \*intf:
        pointer to the usb_interface that is being registered

    :param struct usb_class_driver \*class_driver:
        pointer to the usb_class_driver for this device


.. _`usb_register_dev.description`:

Description
-----------

This should be called by all USB drivers that use the USB major number.
If CONFIG_USB_DYNAMIC_MINORS is enabled, the minor number will be
dynamically allocated out of the list of available ones.  If it is not
enabled, the minor number will be based on the next available free minor,
starting at the class_driver->minor_base.

This function also creates a usb class device in the sysfs tree.

:c:func:`usb_deregister_dev` must be called when the driver is done with
the minor numbers given out by this function.

Return: -EINVAL if something bad happens with trying to register a
device, and 0 on success.


.. _`usb_deregister_dev`:

usb_deregister_dev
==================

.. c:function:: void usb_deregister_dev (struct usb_interface *intf, struct usb_class_driver *class_driver)

    deregister a USB device's dynamic minor.

    :param struct usb_interface \*intf:
        pointer to the usb_interface that is being deregistered

    :param struct usb_class_driver \*class_driver:
        pointer to the usb_class_driver for this device


.. _`usb_deregister_dev.description`:

Description
-----------

Used in conjunction with :c:func:`usb_register_dev`.  This function is called
when the USB driver is finished with the minor numbers gotten from a
call to :c:func:`usb_register_dev` (usually when the device is disconnected
from the system.)

This function also removes the usb class device from the sysfs tree.

This should be called by all drivers that use the USB major number.

