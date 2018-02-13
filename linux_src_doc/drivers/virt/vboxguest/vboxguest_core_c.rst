.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/virt/vboxguest/vboxguest_core.c

.. _`vbg_guest_mappings_init`:

vbg_guest_mappings_init
=======================

.. c:function:: void vbg_guest_mappings_init(struct vbg_dev *gdev)

    that are floating around.

    :param struct vbg_dev \*gdev:
        The Guest extension device.

.. _`vbg_guest_mappings_init.description`:

Description
-----------

This operation is a little bit tricky since the VMM might not accept
just any address because of address clashes between the three contexts
it operates in, so we try several times.

Failure to reserve the guest mappings is ignored.

.. _`vbg_guest_mappings_exit`:

vbg_guest_mappings_exit
=======================

.. c:function:: void vbg_guest_mappings_exit(struct vbg_dev *gdev)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

.. _`vbg_report_guest_info`:

vbg_report_guest_info
=====================

.. c:function:: int vbg_report_guest_info(struct vbg_dev *gdev)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

.. _`vbg_report_guest_info.return`:

Return
------

0 or negative errno value.

.. _`vbg_report_driver_status`:

vbg_report_driver_status
========================

.. c:function:: int vbg_report_driver_status(struct vbg_dev *gdev, bool active)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

    :param bool active:
        Flag whether the driver is now active or not.

.. _`vbg_report_driver_status.return`:

Return
------

0 or negative errno value.

.. _`vbg_balloon_inflate`:

vbg_balloon_inflate
===================

.. c:function:: int vbg_balloon_inflate(struct vbg_dev *gdev, u32 chunk_idx)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

    :param u32 chunk_idx:
        Index of the chunk.

.. _`vbg_balloon_inflate.return`:

Return
------

0 or negative errno value.

.. _`vbg_balloon_deflate`:

vbg_balloon_deflate
===================

.. c:function:: int vbg_balloon_deflate(struct vbg_dev *gdev, u32 chunk_idx)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

    :param u32 chunk_idx:
        Index of the chunk.

.. _`vbg_balloon_deflate.return`:

Return
------

0 or negative errno value.

.. _`vbg_balloon_work`:

vbg_balloon_work
================

.. c:function:: void vbg_balloon_work(struct work_struct *work)

    the host wants the balloon to be and adjust accordingly.

    :param struct work_struct \*work:
        *undescribed*

.. _`vbg_heartbeat_timer`:

vbg_heartbeat_timer
===================

.. c:function:: void vbg_heartbeat_timer(struct timer_list *t)

    :param struct timer_list \*t:
        *undescribed*

.. _`vbg_heartbeat_host_config`:

vbg_heartbeat_host_config
=========================

.. c:function:: int vbg_heartbeat_host_config(struct vbg_dev *gdev, bool enabled)

    and get heartbeat interval from the host.

    :param struct vbg_dev \*gdev:
        The Guest extension device.

    :param bool enabled:
        Set true to enable guest heartbeat checks on host.

.. _`vbg_heartbeat_host_config.return`:

Return
------

0 or negative errno value.

.. _`vbg_heartbeat_init`:

vbg_heartbeat_init
==================

.. c:function:: int vbg_heartbeat_init(struct vbg_dev *gdev)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

.. _`vbg_heartbeat_init.return`:

Return
------

0 or negative errno value.

.. _`vbg_heartbeat_exit`:

vbg_heartbeat_exit
==================

.. c:function:: void vbg_heartbeat_exit(struct vbg_dev *gdev)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

.. _`vbg_track_bit_usage`:

vbg_track_bit_usage
===================

.. c:function:: bool vbg_track_bit_usage(struct vbg_bit_usage_tracker *tracker, u32 changed, u32 previous)

    :param struct vbg_bit_usage_tracker \*tracker:
        The bit usage tracker.

    :param u32 changed:
        The bits to change.

    :param u32 previous:
        The previous value of the bits.

.. _`vbg_track_bit_usage.return`:

Return
------

true if the mask changed, false if not.

.. _`vbg_reset_host_event_filter`:

vbg_reset_host_event_filter
===========================

.. c:function:: int vbg_reset_host_event_filter(struct vbg_dev *gdev, u32 fixed_events)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

    :param u32 fixed_events:
        Fixed events (init time).

.. _`vbg_reset_host_event_filter.return`:

Return
------

0 or negative errno value.

.. _`vbg_set_session_event_filter`:

vbg_set_session_event_filter
============================

.. c:function:: int vbg_set_session_event_filter(struct vbg_dev *gdev, struct vbg_session *session, u32 or_mask, u32 not_mask, bool session_termination)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

    :param struct vbg_session \*session:
        The session.

    :param u32 or_mask:
        The events to add.

    :param u32 not_mask:
        The events to remove.

    :param bool session_termination:
        Set if we're called by the session cleanup code.
        This tweaks the error handling so we perform
        proper session cleanup even if the host
        misbehaves.

.. _`vbg_set_session_event_filter.description`:

Description
-----------

This is called in response to VBG_IOCTL_CHANGE_FILTER_MASK as well as to
do session cleanup. Takes the session spinlock.

.. _`vbg_set_session_event_filter.return`:

Return
------

0 or negative errno value.

.. _`vbg_reset_host_capabilities`:

vbg_reset_host_capabilities
===========================

.. c:function:: int vbg_reset_host_capabilities(struct vbg_dev *gdev)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

.. _`vbg_reset_host_capabilities.return`:

Return
------

0 or negative errno value.

.. _`vbg_set_session_capabilities`:

vbg_set_session_capabilities
============================

.. c:function:: int vbg_set_session_capabilities(struct vbg_dev *gdev, struct vbg_session *session, u32 or_mask, u32 not_mask, bool session_termination)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

    :param struct vbg_session \*session:
        The session.

    :param u32 or_mask:
        The capabilities to add.

    :param u32 not_mask:
        The capabilities to remove.

    :param bool session_termination:
        Set if we're called by the session cleanup code.
        This tweaks the error handling so we perform
        proper session cleanup even if the host
        misbehaves.

.. _`vbg_set_session_capabilities.return`:

Return
------

0 or negative errno value.

.. _`vbg_query_host_version`:

vbg_query_host_version
======================

.. c:function:: int vbg_query_host_version(struct vbg_dev *gdev)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

.. _`vbg_query_host_version.return`:

Return
------

0 or negative errno value.

.. _`vbg_core_init`:

vbg_core_init
=============

.. c:function:: int vbg_core_init(struct vbg_dev *gdev, u32 fixed_events)

    device driver is loaded.

    :param struct vbg_dev \*gdev:
        The Guest extension device.

    :param u32 fixed_events:
        Events that will be enabled upon init and no client
        will ever be allowed to mask.

.. _`vbg_core_init.description`:

Description
-----------

The native code locates the VMMDev on the PCI bus and retrieve
the MMIO and I/O port ranges, this function will take care of
mapping the MMIO memory (if present). Upon successful return
the native code should set up the interrupt handler.

.. _`vbg_core_init.return`:

Return
------

0 or negative errno value.

.. _`vbg_core_exit`:

vbg_core_exit
=============

.. c:function:: void vbg_core_exit(struct vbg_dev *gdev)

    up vboxguest-core managed resources.

    :param struct vbg_dev \*gdev:
        The Guest extension device.

.. _`vbg_core_exit.description`:

Description
-----------

The native code should call this before the driver is loaded,
but don't call this on shutdown.

.. _`vbg_core_open_session`:

vbg_core_open_session
=====================

.. c:function:: struct vbg_session *vbg_core_open_session(struct vbg_dev *gdev, bool user)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

    :param bool user:
        Set if this is a session for the vboxuser device.

.. _`vbg_core_open_session.description`:

Description
-----------

vboxguest_linux.c calls this when userspace opens the char-device.

.. _`vbg_core_open_session.return`:

Return
------

A pointer to the new session or an ERR_PTR on error.

.. _`vbg_core_close_session`:

vbg_core_close_session
======================

.. c:function:: void vbg_core_close_session(struct vbg_session *session)

    :param struct vbg_session \*session:
        The session to close (and free).

.. _`vbg_req_allowed`:

vbg_req_allowed
===============

.. c:function:: int vbg_req_allowed(struct vbg_dev *gdev, struct vbg_session *session, const struct vmmdev_request_header *req)

    :param struct vbg_dev \*gdev:
        The Guest extension device.

    :param struct vbg_session \*session:
        The calling session.

    :param const struct vmmdev_request_header \*req:
        The request.

.. _`vbg_req_allowed.return`:

Return
------

0 or negative errno value.

.. _`vbg_core_ioctl`:

vbg_core_ioctl
==============

.. c:function:: int vbg_core_ioctl(struct vbg_session *session, unsigned int req, void *data)

    :param struct vbg_session \*session:
        The client session.

    :param unsigned int req:
        The requested function.

    :param void \*data:
        The i/o data buffer, minimum size sizeof(struct vbg_ioctl_hdr).

.. _`vbg_core_ioctl.return`:

Return
------

0 or negative errno value.

.. _`vbg_core_set_mouse_status`:

vbg_core_set_mouse_status
=========================

.. c:function:: int vbg_core_set_mouse_status(struct vbg_dev *gdev, u32 features)

    features to the host.

    :param struct vbg_dev \*gdev:
        The Guest extension device.

    :param u32 features:
        The set of features to report to the host.

.. _`vbg_core_set_mouse_status.return`:

Return
------

0 or negative errno value.

.. This file was automatic generated / don't edit.

