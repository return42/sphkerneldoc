.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/block/drbd/drbd_worker.c

.. _`w_e_end_data_req`:

w_e_end_data_req
================

.. c:function:: int w_e_end_data_req(struct drbd_work *w, int cancel)

    Worker callback, to send a P_DATA_REPLY packet in response to a P_DATA_REQUEST

    :param struct drbd_work \*w:
        work object.

    :param int cancel:
        The connection will be closed anyways

.. _`w_e_end_rsdata_req`:

w_e_end_rsdata_req
==================

.. c:function:: int w_e_end_rsdata_req(struct drbd_work *w, int cancel)

    Worker callback to send a P_RS_DATA_REPLY packet in response to a P_RS_DATA_REQUEST

    :param struct drbd_work \*w:
        work object.

    :param int cancel:
        The connection will be closed anyways

.. _`w_send_dblock`:

w_send_dblock
=============

.. c:function:: int w_send_dblock(struct drbd_work *w, int cancel)

    Worker callback to send a P_DATA packet in order to mirror a write request

    :param struct drbd_work \*w:
        work object.

    :param int cancel:
        The connection will be closed anyways

.. _`w_send_read_req`:

w_send_read_req
===============

.. c:function:: int w_send_read_req(struct drbd_work *w, int cancel)

    Worker callback to send a read request (P_DATA_REQUEST) packet

    :param struct drbd_work \*w:
        work object.

    :param int cancel:
        The connection will be closed anyways

.. _`drbd_pause_after`:

drbd_pause_after
================

.. c:function:: bool drbd_pause_after(struct drbd_device *device)

    Pause resync on all devices that may not resync now

    :param struct drbd_device \*device:
        DRBD device.

.. _`drbd_pause_after.description`:

Description
-----------

Called from process context only (admin command and after_state_ch).

.. _`drbd_resume_next`:

drbd_resume_next
================

.. c:function:: bool drbd_resume_next(struct drbd_device *device)

    Resume resync on all devices that may resync now

    :param struct drbd_device \*device:
        DRBD device.

.. _`drbd_resume_next.description`:

Description
-----------

Called from process context only (admin command and worker).

.. _`drbd_start_resync`:

drbd_start_resync
=================

.. c:function:: void drbd_start_resync(struct drbd_device *device, enum drbd_conns side)

    Start the resync process

    :param struct drbd_device \*device:
        DRBD device.

    :param enum drbd_conns side:
        Either C_SYNC_SOURCE or C_SYNC_TARGET

.. _`drbd_start_resync.description`:

Description
-----------

This function might bring you directly into one of the
C_PAUSED_SYNC\_\* states.

.. This file was automatic generated / don't edit.

