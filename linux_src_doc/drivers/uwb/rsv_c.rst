.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/rsv.c

.. _`uwb_rsv_state_str`:

uwb_rsv_state_str
=================

.. c:function:: const char *uwb_rsv_state_str(enum uwb_rsv_state state)

    return a string for a reservation state

    :param enum uwb_rsv_state state:
        the reservation state.

.. _`uwb_rsv_type_str`:

uwb_rsv_type_str
================

.. c:function:: const char *uwb_rsv_type_str(enum uwb_drp_type type)

    return a string for a reservation type

    :param enum uwb_drp_type type:
        the reservation type

.. _`uwb_rsv_create`:

uwb_rsv_create
==============

.. c:function:: struct uwb_rsv *uwb_rsv_create(struct uwb_rc *rc, uwb_rsv_cb_f cb, void *pal_priv)

    allocate and initialize a UWB reservation structure

    :param struct uwb_rc \*rc:
        the radio controller

    :param uwb_rsv_cb_f cb:
        callback to use when the reservation completes or terminates

    :param void \*pal_priv:
        data private to the PAL to be passed in the callback

.. _`uwb_rsv_create.the-callback-is-called-when-the-state-of-the-reservation-changes-from`:

The callback is called when the state of the reservation changes from
---------------------------------------------------------------------


- pending to accepted
- pending to denined
- accepted to terminated
- pending to terminated

.. _`uwb_rsv_destroy`:

uwb_rsv_destroy
===============

.. c:function:: void uwb_rsv_destroy(struct uwb_rsv *rsv)

    free a UWB reservation structure

    :param struct uwb_rsv \*rsv:
        the reservation to free

.. _`uwb_rsv_destroy.description`:

Description
-----------

The reservation must already be terminated.

.. _`uwb_rsv_establish`:

uwb_rsv_establish
=================

.. c:function:: int uwb_rsv_establish(struct uwb_rsv *rsv)

    start a reservation establishment

    :param struct uwb_rsv \*rsv:
        the reservation

.. _`uwb_rsv_establish.description`:

Description
-----------

The PAL should fill in \ ``rsv``\ 's owner, target, type, max_mas,
min_mas, max_interval and is_multicast fields.  If the target is a
uwb_dev it must be referenced.

The reservation's callback will be called when the reservation is
accepted, denied or times out.

.. _`uwb_rsv_modify`:

uwb_rsv_modify
==============

.. c:function:: int uwb_rsv_modify(struct uwb_rsv *rsv, int max_mas, int min_mas, int max_interval)

    modify an already established reservation

    :param struct uwb_rsv \*rsv:
        the reservation to modify

    :param int max_mas:
        new maximum MAS to reserve

    :param int min_mas:
        new minimum MAS to reserve

    :param int max_interval:
        new max_interval to use

.. _`uwb_rsv_modify.fixme`:

FIXME
-----

implement this once there are PALs that use it.

.. _`uwb_rsv_terminate`:

uwb_rsv_terminate
=================

.. c:function:: void uwb_rsv_terminate(struct uwb_rsv *rsv)

    terminate an established reservation

    :param struct uwb_rsv \*rsv:
        the reservation to terminate

.. _`uwb_rsv_terminate.description`:

Description
-----------

A reservation is terminated by removing the DRP IE from the beacon,
the other end will consider the reservation to be terminated when
it does not see the DRP IE for at least mMaxLostBeacons.

If applicable, the reference to the target uwb_dev will be released.

.. _`uwb_rsv_accept`:

uwb_rsv_accept
==============

.. c:function:: void uwb_rsv_accept(struct uwb_rsv *rsv, uwb_rsv_cb_f cb, void *pal_priv)

    accept a new reservation from a peer

    :param struct uwb_rsv \*rsv:
        the reservation

    :param uwb_rsv_cb_f cb:
        call back for reservation changes

    :param void \*pal_priv:
        data to be passed in the above call back

.. _`uwb_rsv_accept.description`:

Description
-----------

Reservation requests from peers are denied unless a PAL accepts it
by calling this function.

The PAL call \ :c:func:`uwb_rsv_destroy`\  for all accepted reservations before
calling \ :c:func:`uwb_pal_unregister`\ .

.. _`uwb_rsv_get_usable_mas`:

uwb_rsv_get_usable_mas
======================

.. c:function:: void uwb_rsv_get_usable_mas(struct uwb_rsv *rsv, struct uwb_mas_bm *mas)

    get the bitmap of the usable MAS of a reservations

    :param struct uwb_rsv \*rsv:
        the reservation.

    :param struct uwb_mas_bm \*mas:
        returns the available MAS.

.. _`uwb_rsv_get_usable_mas.description`:

Description
-----------

The usable MAS of a reservation may be less than the negotiated MAS
if alien BPs are present.

.. _`uwb_rsv_find`:

uwb_rsv_find
============

.. c:function:: struct uwb_rsv *uwb_rsv_find(struct uwb_rc *rc, struct uwb_dev *src, struct uwb_ie_drp *drp_ie)

    find a reservation for a received DRP IE.

    :param struct uwb_rc \*rc:
        the radio controller

    :param struct uwb_dev \*src:
        source of the DRP IE

    :param struct uwb_ie_drp \*drp_ie:
        the DRP IE

.. _`uwb_rsv_find.description`:

Description
-----------

If the reservation cannot be found and the DRP IE is from a peer
attempting to establish a new reservation, create a new reservation
and add it to the list.

.. _`uwb_rsv_sched_update`:

uwb_rsv_sched_update
====================

.. c:function:: void uwb_rsv_sched_update(struct uwb_rc *rc)

    schedule an update of the DRP IEs

    :param struct uwb_rc \*rc:
        the radio controller.

.. _`uwb_rsv_sched_update.description`:

Description
-----------

To improve performance and ensure correctness with [ECMA-368] the
number of SET-DRP-IE commands that are done are limited.

.. _`uwb_rsv_sched_update.drp-ies-update-come-from-two-sources`:

DRP IEs update come from two sources
------------------------------------

DRP events from the hardware
which all occur at the beginning of the superframe ('syncronous'
events) and reservation establishment/termination requests from
PALs or timers ('asynchronous' events).

A delayed work ensures that all the synchronous events result in
one SET-DRP-IE command.

Additional logic (the set_drp_ie_pending and rsv_updated_postponed
flags) will prevent an asynchrous event starting a SET-DRP-IE
command if one is currently awaiting a response.

.. _`uwb_rsv_sched_update.fixme`:

FIXME
-----

this does leave a window where an asynchrous event can delay
the SET-DRP-IE for a synchronous event by one superframe.

.. _`uwb_rsv_remove_all`:

uwb_rsv_remove_all
==================

.. c:function:: void uwb_rsv_remove_all(struct uwb_rc *rc)

    remove all reservations

    :param struct uwb_rc \*rc:
        the radio controller

.. _`uwb_rsv_remove_all.description`:

Description
-----------

A DRP IE update is not done.

.. This file was automatic generated / don't edit.

