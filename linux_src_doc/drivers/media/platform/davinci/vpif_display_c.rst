.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/davinci/vpif_display.c

.. _`vpif_buffer_prepare`:

vpif_buffer_prepare
===================

.. c:function:: int vpif_buffer_prepare(struct vb2_buffer *vb)

    callback function for buffer prepare

    :param vb:
        ptr to vb2_buffer
    :type vb: struct vb2_buffer \*

.. _`vpif_buffer_prepare.description`:

Description
-----------

This is the callback function for buffer prepare when \ :c:func:`vb2_qbuf`\ 
function is called. The buffer is prepared and user space virtual address
or user address is converted into  physical address

.. _`vpif_buffer_queue_setup`:

vpif_buffer_queue_setup
=======================

.. c:function:: int vpif_buffer_queue_setup(struct vb2_queue *vq, unsigned int *nbuffers, unsigned int *nplanes, unsigned int sizes, struct device  *alloc_devs)

    Callback function for buffer setup.

    :param vq:
        vb2_queue ptr
    :type vq: struct vb2_queue \*

    :param nbuffers:
        ptr to number of buffers requested by application
    :type nbuffers: unsigned int \*

    :param nplanes:
        : contains number of distinct video planes needed to hold a frame
    :type nplanes: unsigned int \*

    :param sizes:
        contains the size (in bytes) of each plane.
    :type sizes: unsigned int

    :param alloc_devs:
        ptr to allocation context
    :type alloc_devs: struct device  \*

.. _`vpif_buffer_queue_setup.description`:

Description
-----------

This callback function is called when \ :c:func:`reqbuf`\  is called to adjust
the buffer count and buffer size

.. _`vpif_buffer_queue`:

vpif_buffer_queue
=================

.. c:function:: void vpif_buffer_queue(struct vb2_buffer *vb)

    Callback function to add buffer to DMA queue

    :param vb:
        ptr to vb2_buffer
    :type vb: struct vb2_buffer \*

.. _`vpif_buffer_queue.description`:

Description
-----------

This callback fucntion queues the buffer to DMA engine

.. _`vpif_start_streaming`:

vpif_start_streaming
====================

.. c:function:: int vpif_start_streaming(struct vb2_queue *vq, unsigned int count)

    Starts the DMA engine for streaming

    :param vq:
        ptr to vb2_buffer
    :type vq: struct vb2_queue \*

    :param count:
        number of buffers
    :type count: unsigned int

.. _`vpif_stop_streaming`:

vpif_stop_streaming
===================

.. c:function:: void vpif_stop_streaming(struct vb2_queue *vq)

    Stop the DMA engine

    :param vq:
        ptr to vb2_queue
    :type vq: struct vb2_queue \*

.. _`vpif_stop_streaming.description`:

Description
-----------

This callback stops the DMA engine and any remaining buffers
in the DMA queue are released.

.. _`vpif_querycap`:

vpif_querycap
=============

.. c:function:: int vpif_querycap(struct file *file, void *priv, struct v4l2_capability *cap)

    QUERYCAP handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param cap:
        ptr to v4l2_capability structure
    :type cap: struct v4l2_capability \*

.. _`vpif_output_to_subdev`:

vpif_output_to_subdev
=====================

.. c:function:: int vpif_output_to_subdev(struct vpif_display_config *vpif_cfg, struct vpif_display_chan_config *chan_cfg, int index)

    Maps output to sub device

    :param vpif_cfg:
        global config ptr
    :type vpif_cfg: struct vpif_display_config \*

    :param chan_cfg:
        channel config ptr
    :type chan_cfg: struct vpif_display_chan_config \*

    :param index:
        Given output index from application
    :type index: int

.. _`vpif_output_to_subdev.description`:

Description
-----------

lookup the sub device information for a given output index.
we report all the output to application. output table also
has sub device name for the each output

.. _`vpif_set_output`:

vpif_set_output
===============

.. c:function:: int vpif_set_output(struct vpif_display_config *vpif_cfg, struct channel_obj *ch, int index)

    Select an output

    :param vpif_cfg:
        global config ptr
    :type vpif_cfg: struct vpif_display_config \*

    :param ch:
        channel
    :type ch: struct channel_obj \*

    :param index:
        Given output index from application
    :type index: int

.. _`vpif_set_output.description`:

Description
-----------

Select the given output.

.. _`vpif_enum_dv_timings`:

vpif_enum_dv_timings
====================

.. c:function:: int vpif_enum_dv_timings(struct file *file, void *priv, struct v4l2_enum_dv_timings *timings)

    ENUM_DV_TIMINGS handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param timings:
        input timings
    :type timings: struct v4l2_enum_dv_timings \*

.. _`vpif_s_dv_timings`:

vpif_s_dv_timings
=================

.. c:function:: int vpif_s_dv_timings(struct file *file, void *priv, struct v4l2_dv_timings *timings)

    S_DV_TIMINGS handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param timings:
        digital video timings
    :type timings: struct v4l2_dv_timings \*

.. _`vpif_g_dv_timings`:

vpif_g_dv_timings
=================

.. c:function:: int vpif_g_dv_timings(struct file *file, void *priv, struct v4l2_dv_timings *timings)

    G_DV_TIMINGS handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param timings:
        digital video timings
    :type timings: struct v4l2_dv_timings \*

.. This file was automatic generated / don't edit.

