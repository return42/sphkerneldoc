.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/block/drbd/drbd_state.h

.. _`drbd_request_state`:

drbd_request_state
==================

.. c:function:: int drbd_request_state(struct drbd_device *device, union drbd_state mask, union drbd_state val)

    Reqest a state change

    :param struct drbd_device \*device:
        DRBD device.

    :param union drbd_state mask:
        mask of state bits to change.

    :param union drbd_state val:
        value of new state bits.

.. _`drbd_request_state.description`:

Description
-----------

This is the most graceful way of requesting a state change. It is verbose
quite verbose in case the state change is not possible, and all those
state changes are globally serialized.

.. This file was automatic generated / don't edit.

