.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/streamzap.c

.. _`streamzap_callback`:

streamzap_callback
==================

.. c:function:: void streamzap_callback(struct urb *urb)

    usb IRQ handler callback

    :param struct urb \*urb:
        *undescribed*

.. _`streamzap_callback.description`:

Description
-----------

This procedure is invoked on reception of data from
the usb remote.

.. _`streamzap_probe`:

streamzap_probe
===============

.. c:function:: int streamzap_probe(struct usb_interface *intf, const struct usb_device_id *id)

    :param struct usb_interface \*intf:
        *undescribed*

    :param const struct usb_device_id \*id:
        *undescribed*

.. _`streamzap_probe.description`:

Description
-----------

Called by usb-core to associated with a candidate device
On any failure the return value is the ERROR
On success return 0

.. _`streamzap_disconnect`:

streamzap_disconnect
====================

.. c:function:: void streamzap_disconnect(struct usb_interface *interface)

    :param struct usb_interface \*interface:
        *undescribed*

.. _`streamzap_disconnect.description`:

Description
-----------

Called by the usb core when the device is removed from the system.

This routine guarantees that the driver will not submit any more urbs
by clearing dev->usbdev.  It is also supposed to terminate any currently
active urbs.  Unfortunately, \ :c:func:`usb_bulk_msg`\ , used in \ :c:func:`streamzap_read`\ ,
does not provide any way to do this.

.. This file was automatic generated / don't edit.

