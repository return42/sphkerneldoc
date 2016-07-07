.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/wusbcore/reservation.c

.. _`wusbhc_rsv_complete_cb`:

wusbhc_rsv_complete_cb
======================

.. c:function:: void wusbhc_rsv_complete_cb(struct uwb_rsv *rsv)

    WUSB HC reservation complete callback

    :param struct uwb_rsv \*rsv:
        the reservation

.. _`wusbhc_rsv_complete_cb.description`:

Description
-----------

Either set or clear the HC's view of the reservation.

.. _`wusbhc_rsv_complete_cb.fixme`:

FIXME
-----

when a reservation is denied the HC should be stopped.

.. _`wusbhc_rsv_establish`:

wusbhc_rsv_establish
====================

.. c:function:: int wusbhc_rsv_establish(struct wusbhc *wusbhc)

    establish a reservation for the cluster

    :param struct wusbhc \*wusbhc:
        the WUSB HC requesting a bandwidth reservation

.. _`wusbhc_rsv_terminate`:

wusbhc_rsv_terminate
====================

.. c:function:: void wusbhc_rsv_terminate(struct wusbhc *wusbhc)

    terminate the cluster reservation

    :param struct wusbhc \*wusbhc:
        the WUSB host whose reservation is to be terminated

.. This file was automatic generated / don't edit.

