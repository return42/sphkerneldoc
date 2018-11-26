.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/video/imx-ipu-image-convert.h

.. _`ipu_image_convert_run`:

struct ipu_image_convert_run
============================

.. c:type:: struct ipu_image_convert_run

    image conversion run request struct

.. _`ipu_image_convert_run.definition`:

Definition
----------

.. code-block:: c

    struct ipu_image_convert_run {
        struct ipu_image_convert_ctx *ctx;
        dma_addr_t in_phys;
        dma_addr_t out_phys;
        int status;
        struct list_head list;
    }

.. _`ipu_image_convert_run.members`:

Members
-------

ctx
    the conversion context

in_phys
    dma addr of input image buffer for this run

out_phys
    dma addr of output image buffer for this run

status
    completion status of this run

list
    *undescribed*

.. _`ipu_image_convert_cb_t`:

ipu_image_convert_cb_t
======================

.. c:function:: void ipu_image_convert_cb_t(struct ipu_image_convert_run *run, void *ctx)

    conversion callback function prototype

    :param run:
        the completed conversion run pointer
    :type run: struct ipu_image_convert_run \*

    :param ctx:
        a private context pointer for the callback
    :type ctx: void \*

.. _`ipu_image_convert_enum_format`:

ipu_image_convert_enum_format
=============================

.. c:function:: int ipu_image_convert_enum_format(int index, u32 *fourcc)

    enumerate the image converter's supported input and output pixel formats.

    :param index:
        pixel format index
    :type index: int

    :param fourcc:
        v4l2 fourcc for this index
    :type fourcc: u32 \*

.. _`ipu_image_convert_enum_format.description`:

Description
-----------

Returns 0 with a valid index and fills in v4l2 fourcc, -EINVAL otherwise.

In V4L2, drivers can call \ :c:func:`ipu_image_enum_format`\  in .enum_fmt.

.. _`ipu_image_convert_adjust`:

ipu_image_convert_adjust
========================

.. c:function:: void ipu_image_convert_adjust(struct ipu_image *in, struct ipu_image *out, enum ipu_rotate_mode rot_mode)

    adjust input/output images to IPU restrictions.

    :param in:
        input image format, adjusted on return
    :type in: struct ipu_image \*

    :param out:
        output image format, adjusted on return
    :type out: struct ipu_image \*

    :param rot_mode:
        rotation mode
    :type rot_mode: enum ipu_rotate_mode

.. _`ipu_image_convert_adjust.description`:

Description
-----------

In V4L2, drivers can call \ :c:func:`ipu_image_convert_adjust`\  in .try_fmt.

.. _`ipu_image_convert_verify`:

ipu_image_convert_verify
========================

.. c:function:: int ipu_image_convert_verify(struct ipu_image *in, struct ipu_image *out, enum ipu_rotate_mode rot_mode)

    verify that input/output image formats and rotation mode meet IPU restrictions.

    :param in:
        input image format
    :type in: struct ipu_image \*

    :param out:
        output image format
    :type out: struct ipu_image \*

    :param rot_mode:
        rotation mode
    :type rot_mode: enum ipu_rotate_mode

.. _`ipu_image_convert_verify.description`:

Description
-----------

Returns 0 if the formats and rotation mode meet IPU restrictions,
-EINVAL otherwise.

.. _`ipu_image_convert_prepare`:

ipu_image_convert_prepare
=========================

.. c:function:: struct ipu_image_convert_ctx *ipu_image_convert_prepare(struct ipu_soc *ipu, enum ipu_ic_task ic_task, struct ipu_image *in, struct ipu_image *out, enum ipu_rotate_mode rot_mode, ipu_image_convert_cb_t complete, void *complete_context)

    prepare a conversion context.

    :param ipu:
        the IPU handle to use for the conversions
    :type ipu: struct ipu_soc \*

    :param ic_task:
        the IC task to use for the conversions
    :type ic_task: enum ipu_ic_task

    :param in:
        input image format
    :type in: struct ipu_image \*

    :param out:
        output image format
    :type out: struct ipu_image \*

    :param rot_mode:
        rotation mode
    :type rot_mode: enum ipu_rotate_mode

    :param complete:
        run completion callback
    :type complete: ipu_image_convert_cb_t

    :param complete_context:
        a context pointer for the completion callback
    :type complete_context: void \*

.. _`ipu_image_convert_prepare.description`:

Description
-----------

Returns an opaque conversion context pointer on success, error pointer
on failure. The input/output formats and rotation mode must already meet
IPU retrictions.

In V4L2, drivers should call \ :c:func:`ipu_image_convert_prepare`\  at streamon.

.. _`ipu_image_convert_unprepare`:

ipu_image_convert_unprepare
===========================

.. c:function:: void ipu_image_convert_unprepare(struct ipu_image_convert_ctx *ctx)

    unprepare a conversion context.

    :param ctx:
        the conversion context pointer to unprepare
    :type ctx: struct ipu_image_convert_ctx \*

.. _`ipu_image_convert_unprepare.description`:

Description
-----------

Aborts any active or pending conversions for this context and
frees the context. Any currently active or pending runs belonging
to this context are returned via the completion callback with an
error run status.

In V4L2, drivers should call \ :c:func:`ipu_image_convert_unprepare`\  at
streamoff.

.. _`ipu_image_convert_queue`:

ipu_image_convert_queue
=======================

.. c:function:: int ipu_image_convert_queue(struct ipu_image_convert_run *run)

    queue a conversion run

    :param run:
        the run request pointer
    :type run: struct ipu_image_convert_run \*

.. _`ipu_image_convert_queue.description`:

Description
-----------

ipu_image_convert_run must be dynamically allocated (_not\_ as a local
var) by callers and filled in with a previously prepared conversion
context handle and the dma addr's of the input and output image buffers
for this conversion run.

When this conversion completes, the run pointer is returned via the
completion callback. The caller is responsible for freeing the run
object after it completes.

In V4L2, drivers should call \ :c:func:`ipu_image_convert_queue`\  while
streaming to queue the conversion of a received input buffer.
For example mem2mem devices this would be called in .device_run.

.. _`ipu_image_convert_abort`:

ipu_image_convert_abort
=======================

.. c:function:: void ipu_image_convert_abort(struct ipu_image_convert_ctx *ctx)

    abort conversions

    :param ctx:
        the conversion context pointer
    :type ctx: struct ipu_image_convert_ctx \*

.. _`ipu_image_convert_abort.description`:

Description
-----------

This will abort any active or pending conversions for this context.
Any currently active or pending runs belonging to this context are
returned via the completion callback with an error run status.

.. _`ipu_image_convert`:

ipu_image_convert
=================

.. c:function:: struct ipu_image_convert_run *ipu_image_convert(struct ipu_soc *ipu, enum ipu_ic_task ic_task, struct ipu_image *in, struct ipu_image *out, enum ipu_rotate_mode rot_mode, ipu_image_convert_cb_t complete, void *complete_context)

    asynchronous image conversion request

    :param ipu:
        the IPU handle to use for the conversion
    :type ipu: struct ipu_soc \*

    :param ic_task:
        the IC task to use for the conversion
    :type ic_task: enum ipu_ic_task

    :param in:
        input image format
    :type in: struct ipu_image \*

    :param out:
        output image format
    :type out: struct ipu_image \*

    :param rot_mode:
        rotation mode
    :type rot_mode: enum ipu_rotate_mode

    :param complete:
        run completion callback
    :type complete: ipu_image_convert_cb_t

    :param complete_context:
        a context pointer for the completion callback
    :type complete_context: void \*

.. _`ipu_image_convert.description`:

Description
-----------

Request a single image conversion. Returns the run that has been queued.
A conversion context is automatically created and is available in run->ctx.
As with \ :c:func:`ipu_image_convert_prepare`\ , the input/output formats and rotation
mode must already meet IPU retrictions.

On successful return the caller can queue more run requests if needed, using
the prepared context in run->ctx. The caller is responsible for unpreparing
the context when no more conversion requests are needed.

.. _`ipu_image_convert_sync`:

ipu_image_convert_sync
======================

.. c:function:: int ipu_image_convert_sync(struct ipu_soc *ipu, enum ipu_ic_task ic_task, struct ipu_image *in, struct ipu_image *out, enum ipu_rotate_mode rot_mode)

    synchronous single image conversion request

    :param ipu:
        the IPU handle to use for the conversion
    :type ipu: struct ipu_soc \*

    :param ic_task:
        the IC task to use for the conversion
    :type ic_task: enum ipu_ic_task

    :param in:
        input image format
    :type in: struct ipu_image \*

    :param out:
        output image format
    :type out: struct ipu_image \*

    :param rot_mode:
        rotation mode
    :type rot_mode: enum ipu_rotate_mode

.. _`ipu_image_convert_sync.description`:

Description
-----------

Carry out a single image conversion. Returns when the conversion
completes. The input/output formats and rotation mode must already
meet IPU retrictions. The created context is automatically unprepared
and the run freed on return.

.. This file was automatic generated / don't edit.

