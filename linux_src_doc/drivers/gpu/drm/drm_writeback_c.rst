.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_writeback.c

.. _`overview`:

overview
========

Writeback connectors are used to expose hardware which can write the output
from a CRTC to a memory buffer. They are used and act similarly to other
types of connectors, with some important differences:

* Writeback connectors don't provide a way to output visually to the user.

* Writeback connectors are visible to userspace only when the client sets
  DRM_CLIENT_CAP_WRITEBACK_CONNECTORS.

* Writeback connectors don't have EDID.

A framebuffer may only be attached to a writeback connector when the
connector is attached to a CRTC. The WRITEBACK_FB_ID property which sets the
framebuffer applies only to a single commit (see below). A framebuffer may
not be attached while the CRTC is off.

Unlike with planes, when a writeback framebuffer is removed by userspace DRM
makes no attempt to remove it from active use by the connector. This is
because no method is provided to abort a writeback operation, and in any
case making a new commit whilst a writeback is ongoing is undefined (see
WRITEBACK_OUT_FENCE_PTR below). As soon as the current writeback is finished,
the framebuffer will automatically no longer be in active use. As it will
also have already been removed from the framebuffer list, there will be no
way for any userspace application to retrieve a reference to it in the
intervening period.

Writeback connectors have some additional properties, which userspace
can use to query and control them:

 "WRITEBACK_FB_ID":
     Write-only object property storing a DRM_MODE_OBJECT_FB: it stores the
     framebuffer to be written by the writeback connector. This property is
     similar to the FB_ID property on planes, but will always read as zero
     and is not preserved across commits.
     Userspace must set this property to an output buffer every time it
     wishes the buffer to get filled.

 "WRITEBACK_PIXEL_FORMATS":
     Immutable blob property to store the supported pixel formats table. The
     data is an array of u32 DRM_FORMAT_* fourcc values.
     Userspace can use this blob to find out what pixel formats are supported
     by the connector's writeback engine.

 "WRITEBACK_OUT_FENCE_PTR":
     Userspace can use this property to provide a pointer for the kernel to
     fill with a sync_file file descriptor, which will signal once the
     writeback is finished. The value should be the address of a 32-bit
     signed integer, cast to a u64.
     Userspace should wait for this fence to signal before making another
     commit affecting any of the same CRTCs, Planes or Connectors.
     **Failure to do so will result in undefined behaviour.**
     For this reason it is strongly recommended that all userspace
     applications making use of writeback connectors *always* retrieve an
     out-fence for the commit and use it appropriately.
     From userspace, this property will always read as zero.

.. _`drm_writeback_connector_init`:

drm_writeback_connector_init
============================

.. c:function:: int drm_writeback_connector_init(struct drm_device *dev, struct drm_writeback_connector *wb_connector, const struct drm_connector_funcs *con_funcs, const struct drm_encoder_helper_funcs *enc_helper_funcs, const u32 *formats, int n_formats)

    Initialize a writeback connector and its properties

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param wb_connector:
        Writeback connector to initialize
    :type wb_connector: struct drm_writeback_connector \*

    :param con_funcs:
        Connector funcs vtable
    :type con_funcs: const struct drm_connector_funcs \*

    :param enc_helper_funcs:
        Encoder helper funcs vtable to be used by the internal encoder
    :type enc_helper_funcs: const struct drm_encoder_helper_funcs \*

    :param formats:
        Array of supported pixel formats for the writeback engine
    :type formats: const u32 \*

    :param n_formats:
        Length of the formats array
    :type n_formats: int

.. _`drm_writeback_connector_init.description`:

Description
-----------

This function creates the writeback-connector-specific properties if they
have not been already created, initializes the connector as
type DRM_MODE_CONNECTOR_WRITEBACK, and correctly initializes the property
values. It will also create an internal encoder associated with the
drm_writeback_connector and set it to use the \ ``enc_helper_funcs``\  vtable for
the encoder helper.

Drivers should always use this function instead of \ :c:func:`drm_connector_init`\  to
set up writeback connectors.

.. _`drm_writeback_connector_init.return`:

Return
------

0 on success, or a negative error code

.. _`drm_writeback_queue_job`:

drm_writeback_queue_job
=======================

.. c:function:: void drm_writeback_queue_job(struct drm_writeback_connector *wb_connector, struct drm_writeback_job *job)

    Queue a writeback job for later signalling

    :param wb_connector:
        The writeback connector to queue a job on
    :type wb_connector: struct drm_writeback_connector \*

    :param job:
        The job to queue
    :type job: struct drm_writeback_job \*

.. _`drm_writeback_queue_job.description`:

Description
-----------

This function adds a job to the job_queue for a writeback connector. It
should be considered to take ownership of the writeback job, and so any other
references to the job must be cleared after calling this function.

Drivers must ensure that for a given writeback connector, jobs are queued in
exactly the same order as they will be completed by the hardware (and
signaled via drm_writeback_signal_completion).

For every call to \ :c:func:`drm_writeback_queue_job`\  there must be exactly one call to
\ :c:func:`drm_writeback_signal_completion`\ 

See also: \ :c:func:`drm_writeback_signal_completion`\ 

.. _`drm_writeback_signal_completion`:

drm_writeback_signal_completion
===============================

.. c:function:: void drm_writeback_signal_completion(struct drm_writeback_connector *wb_connector, int status)

    Signal the completion of a writeback job

    :param wb_connector:
        The writeback connector whose job is complete
    :type wb_connector: struct drm_writeback_connector \*

    :param status:
        Status code to set in the writeback out_fence (0 for success)
    :type status: int

.. _`drm_writeback_signal_completion.description`:

Description
-----------

Drivers should call this to signal the completion of a previously queued
writeback job. It should be called as soon as possible after the hardware
has finished writing, and may be called from interrupt context.
It is the driver's responsibility to ensure that for a given connector, the
hardware completes writeback jobs in the same order as they are queued.

Unless the driver is holding its own reference to the framebuffer, it must
not be accessed after calling this function.

See also: \ :c:func:`drm_writeback_queue_job`\ 

.. This file was automatic generated / don't edit.

