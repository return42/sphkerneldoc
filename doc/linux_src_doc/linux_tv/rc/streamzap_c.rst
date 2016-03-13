.. -*- coding: utf-8; mode: rst -*-

===========
streamzap.c
===========



.. _xref_streamzap_callback:

streamzap_callback
==================

.. c:function:: void streamzap_callback (struct urb * urb)

    usb IRQ handler callback

    :param struct urb * urb:

        _undescribed_



Description
-----------



This procedure is invoked on reception of data from
the usb remote.




.. _xref_streamzap_probe:

streamzap_probe
===============

.. c:function:: int streamzap_probe (struct usb_interface * intf, const struct usb_device_id * id)

    

    :param struct usb_interface * intf:

        _undescribed_

    :param const struct usb_device_id * id:

        _undescribed_



Description
-----------



	Called by usb-core to associated with a candidate device
	On any failure the return value is the ERROR
	On success return 0




.. _xref_streamzap_disconnect:

streamzap_disconnect
====================

.. c:function:: void streamzap_disconnect (struct usb_interface * interface)

    

    :param struct usb_interface * interface:

        _undescribed_



Description
-----------



Called by the usb core when the device is removed from the system.


This routine guarantees that the driver will not submit any more urbs
by clearing dev->usbdev.  It is also supposed to terminate any currently
active urbs.  Unfortunately, :c:func:`usb_bulk_msg`, used in :c:func:`streamzap_read`,
does not provide any way to do this.


