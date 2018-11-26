.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/block/drbd/drbd_state.h

.. _`drbd-state-macros`:

DRBD State macros
=================

These macros are used to express state changes in easily readable form.

The NS macros expand to a mask and a value, that can be bit ored onto the
current state as soon as the spinlock (req_lock) was taken.

The \_NS macros are used for state functions that get called with the
spinlock. These macros expand directly to the new state value.

Besides the basic forms \ :c:func:`NS`\  and \_NS() additional _?NS[23] are defined
to express state changes that affect more than one aspect of the state.

E.g. NS2(conn, C_CONNECTED, peer, R_SECONDARY)
Means that the network connection was established and that the peer
is in secondary role.

.. _`drbd_request_state`:

drbd_request_state
==================

.. c:function:: int drbd_request_state(struct drbd_device *device, union drbd_state mask, union drbd_state val)

    Request a state change

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param mask:
        mask of state bits to change.
    :type mask: union drbd_state

    :param val:
        value of new state bits.
    :type val: union drbd_state

.. _`drbd_request_state.description`:

Description
-----------

This is the most graceful way of requesting a state change. It is verbose
quite verbose in case the state change is not possible, and all those
state changes are globally serialized.

.. This file was automatic generated / don't edit.

