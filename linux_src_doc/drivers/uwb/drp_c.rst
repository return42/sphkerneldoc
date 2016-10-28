.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/drp.c

.. _`uwb_rc_send_all_drp_ie`:

uwb_rc_send_all_drp_ie
======================

.. c:function:: int uwb_rc_send_all_drp_ie(struct uwb_rc *rc)

    :param struct uwb_rc \*rc:
        UWB Host controller

.. _`uwb_rc_send_all_drp_ie.description`:

Description
-----------

See WUSB[8.6.2.7]: The host must set all the DRP IEs that it wants the
device to include in its beacon at the same time. We thus have to
traverse all reservations and include the DRP IEs of all PENDING
and NEGOTIATED reservations in a SET DRP command for transmission.

A DRP Availability IE is appended.

rc->rsvs_mutex is held

FIXME We currently ignore the returned value indicating the remaining space
in beacon. This could be used to deny reservation requests earlier if
determined that they would cause the beacon space to be exceeded.

.. _`uwbd_evt_handle_rc_drp`:

uwbd_evt_handle_rc_drp
======================

.. c:function:: int uwbd_evt_handle_rc_drp(struct uwb_event *evt)

    handle a DRP_IE event

    :param struct uwb_event \*evt:
        the DRP_IE event from the radio controller

.. _`uwbd_evt_handle_rc_drp.description`:

Description
-----------

This processes DRP notifications from the radio controller, either
initiating a new reservation or transitioning an existing
reservation into a different state.

.. _`uwbd_evt_handle_rc_drp.drp-notifications-can-occur-for-three-different-reasons`:

DRP notifications can occur for three different reasons
-------------------------------------------------------


- UWB_DRP_NOTIF_DRP_IE_RECVD: one or more DRP IEs with the RC as
the target or source have been received.

These DRP IEs could be new or for an existing reservation.

If the DRP IE for an existing reservation ceases to be to
received for at least mMaxLostBeacons, the reservation should be
considered to be terminated.  Note that the TERMINATE reason (see
below) may not always be signalled (e.g., the remote device has
two or more reservations established with the RC).

- UWB_DRP_NOTIF_CONFLICT: DRP IEs from any device in the beacon
group conflict with the RC's reservations.

- UWB_DRP_NOTIF_TERMINATE: DRP IEs are no longer being received
from a device (i.e., it's terminated all reservations).

Only the software state of the reservations is changed; the setting
of the radio controller's DRP IEs is done after all the events in
an event buffer are processed.  This saves waiting multiple times
for the SET_DRP_IE command to complete.

.. This file was automatic generated / don't edit.

