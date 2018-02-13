.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/comedi_usb.c

.. _`comedi_to_usb_interface`:

comedi_to_usb_interface
=======================

.. c:function:: struct usb_interface *comedi_to_usb_interface(struct comedi_device *dev)

    Return USB interface attached to COMEDI device

    :param struct comedi_device \*dev:
        COMEDI device.

.. _`comedi_to_usb_interface.description`:

Description
-----------

Assuming \ ``dev``\ ->hw_dev is non-%NULL, it is assumed to be pointing to a
a \ :c:type:`struct device <device>`\  embedded in a \ :c:type:`struct usb_interface <usb_interface>`\ .

.. _`comedi_to_usb_interface.return`:

Return
------

Attached USB interface if \ ``dev``\ ->hw_dev is non-%NULL.
Return \ ``NULL``\  if \ ``dev``\ ->hw_dev is \ ``NULL``\ .

.. _`comedi_to_usb_dev`:

comedi_to_usb_dev
=================

.. c:function:: struct usb_device *comedi_to_usb_dev(struct comedi_device *dev)

    Return USB device attached to COMEDI device

    :param struct comedi_device \*dev:
        COMEDI device.

.. _`comedi_to_usb_dev.description`:

Description
-----------

Assuming \ ``dev``\ ->hw_dev is non-%NULL, it is assumed to be pointing to a
a \ :c:type:`struct device <device>`\  embedded in a \ :c:type:`struct usb_interface <usb_interface>`\ .

.. _`comedi_to_usb_dev.return`:

Return
------

USB device to which the USB interface belongs if \ ``dev``\ ->hw_dev is
non-%NULL.  Return \ ``NULL``\  if \ ``dev``\ ->hw_dev is \ ``NULL``\ .

.. _`comedi_usb_auto_config`:

comedi_usb_auto_config
======================

.. c:function:: int comedi_usb_auto_config(struct usb_interface *intf, struct comedi_driver *driver, unsigned long context)

    Configure/probe a USB COMEDI driver

    :param struct usb_interface \*intf:
        USB interface.

    :param struct comedi_driver \*driver:
        Registered COMEDI driver.

    :param unsigned long context:
        Driver specific data, passed to \ :c:func:`comedi_auto_config`\ .

.. _`comedi_usb_auto_config.description`:

Description
-----------

Typically called from the usb_driver (\*probe) function.  Auto-configure a
COMEDI device, using a pointer to the \ :c:type:`struct device <device>`\  embedded in \*@intf as
the hardware device.  The \ ``context``\  value gets passed through to \ ``driver``\ 's
"auto_attach" handler.  The "auto_attach" handler may call
\ :c:func:`comedi_to_usb_interface`\  on the passed in COMEDI device to recover \ ``intf``\ .

.. _`comedi_usb_auto_config.return`:

Return
------

The result of calling \ :c:func:`comedi_auto_config`\  (%0 on success, or
a negative error number on failure).

.. _`comedi_usb_auto_unconfig`:

comedi_usb_auto_unconfig
========================

.. c:function:: void comedi_usb_auto_unconfig(struct usb_interface *intf)

    Unconfigure/disconnect a USB COMEDI device

    :param struct usb_interface \*intf:
        USB interface.

.. _`comedi_usb_auto_unconfig.description`:

Description
-----------

Typically called from the usb_driver (\*disconnect) function.
Auto-unconfigure a COMEDI device attached to this USB interface, using a
pointer to the \ :c:type:`struct device <device>`\  embedded in \*@intf as the hardware device.
The COMEDI driver's "detach" handler will be called during unconfiguration
of the COMEDI device.

Note that the COMEDI device may have already been unconfigured using the
\ ``COMEDI_DEVCONFIG``\  ioctl, in which case this attempt to unconfigure it
again should be ignored.

.. _`comedi_usb_driver_register`:

comedi_usb_driver_register
==========================

.. c:function:: int comedi_usb_driver_register(struct comedi_driver *comedi_driver, struct usb_driver *usb_driver)

    Register a USB COMEDI driver

    :param struct comedi_driver \*comedi_driver:
        COMEDI driver to be registered.

    :param struct usb_driver \*usb_driver:
        USB driver to be registered.

.. _`comedi_usb_driver_register.description`:

Description
-----------

This function is called from the \ :c:func:`module_init`\  of USB COMEDI driver modules
to register the COMEDI driver and the USB driver.  Do not call it directly,
use the \ :c:func:`module_comedi_usb_driver`\  helper macro instead.

.. _`comedi_usb_driver_register.return`:

Return
------

\ ``0``\  on success, or a negative error number on failure.

.. _`comedi_usb_driver_unregister`:

comedi_usb_driver_unregister
============================

.. c:function:: void comedi_usb_driver_unregister(struct comedi_driver *comedi_driver, struct usb_driver *usb_driver)

    Unregister a USB COMEDI driver

    :param struct comedi_driver \*comedi_driver:
        COMEDI driver to be registered.

    :param struct usb_driver \*usb_driver:
        USB driver to be registered.

.. _`comedi_usb_driver_unregister.description`:

Description
-----------

This function is called from the \ :c:func:`module_exit`\  of USB COMEDI driver modules
to unregister the USB driver and the COMEDI driver.  Do not call it
directly, use the \ :c:func:`module_comedi_usb_driver`\  helper macro instead.

.. This file was automatic generated / don't edit.

