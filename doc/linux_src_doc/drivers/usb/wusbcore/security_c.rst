.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/wusbcore/security.c

.. _`wusbhc_next_tkid`:

wusbhc_next_tkid
================

.. c:function:: u32 wusbhc_next_tkid(struct wusbhc *wusbhc, struct wusb_dev *wusb_dev)

    generate a new, currently unused, TKID

    :param struct wusbhc \*wusbhc:
        the WUSB host controller

    :param struct wusb_dev \*wusb_dev:
        the device whose PTK the TKID is for
        (or NULL for a TKID for a GTK)

.. _`wusbhc_next_tkid.the-generated-tkid-consists-of-two-parts`:

The generated TKID consists of two parts
----------------------------------------

the device's authenticated
address (or 0 or a GTK); and an incrementing number.  This ensures
that TKIDs cannot be shared between devices and by the time the
incrementing number wraps around the older TKIDs will no longer be
in use (a maximum of two keys may be active at any one time).

.. _`wusbhc_sec_start`:

wusbhc_sec_start
================

.. c:function:: int wusbhc_sec_start(struct wusbhc *wusbhc)

    start the security management process

    :param struct wusbhc \*wusbhc:
        the WUSB host controller

.. _`wusbhc_sec_start.description`:

Description
-----------

Generate and set an initial GTK on the host controller.

Called when the HC is started.

.. _`wusbhc_sec_stop`:

wusbhc_sec_stop
===============

.. c:function:: void wusbhc_sec_stop(struct wusbhc *wusbhc)

    stop the security management process

    :param struct wusbhc \*wusbhc:
        the WUSB host controller

.. _`wusbhc_sec_stop.description`:

Description
-----------

Wait for any pending GTK rekeys to stop.

.. _`wusb_dev_update_address`:

wusb_dev_update_address
=======================

.. c:function:: int wusb_dev_update_address(struct wusbhc *wusbhc, struct wusb_dev *wusb_dev)

    :param struct wusbhc \*wusbhc:
        *undescribed*

    :param struct wusb_dev \*wusb_dev:
        *undescribed*

.. _`wusb_dev_update_address.description`:

Description
-----------

Once we have successfully authenticated, we take it to addr0 state
and then to a normal address.

Before the device's address (as known by it) was usb_dev->devnum \|
0x80 (unauthenticated address). With this we update it to usb_dev->devnum.

.. _`wusbhc_gtk_rekey`:

wusbhc_gtk_rekey
================

.. c:function:: void wusbhc_gtk_rekey(struct wusbhc *wusbhc)

    generate and distribute a new GTK

    :param struct wusbhc \*wusbhc:
        the WUSB host controller

.. _`wusbhc_gtk_rekey.description`:

Description
-----------

Generate a new GTK and distribute it to all connected and
authenticated devices.  When all devices have the new GTK, the host
starts using it.

This must be called after every device disconnect (see [WUSB]
section 6.2.11.2).

.. This file was automatic generated / don't edit.

