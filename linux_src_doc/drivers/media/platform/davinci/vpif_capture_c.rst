.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/davinci/vpif_capture.c

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

.. _`vpif_process_buffer_complete`:

vpif_process_buffer_complete
============================

.. c:function:: void vpif_process_buffer_complete(struct common_obj *common)

    process a completed buffer

    :param common:
        ptr to common channel object
    :type common: struct common_obj \*

.. _`vpif_process_buffer_complete.description`:

Description
-----------

This function time stamp the buffer and mark it as DONE. It also
wake up any process waiting on the QUEUE and set the next buffer
as current

.. _`vpif_schedule_next_buffer`:

vpif_schedule_next_buffer
=========================

.. c:function:: void vpif_schedule_next_buffer(struct common_obj *common)

    set next buffer address for capture

    :param common:
        ptr to common channel object
    :type common: struct common_obj \*

.. _`vpif_schedule_next_buffer.description`:

Description
-----------

This function will get next buffer from the dma queue and
set the buffer address in the vpif register for capture.
the buffer is marked active

.. _`vpif_channel_isr`:

vpif_channel_isr
================

.. c:function:: irqreturn_t vpif_channel_isr(int irq, void *dev_id)

    ISR handler for vpif capture

    :param irq:
        irq number
    :type irq: int

    :param dev_id:
        dev_id ptr
    :type dev_id: void \*

.. _`vpif_channel_isr.description`:

Description
-----------

It changes status of the captured buffer, takes next buffer from the queue
and sets its address in VPIF registers

.. _`vpif_update_std_info`:

vpif_update_std_info
====================

.. c:function:: int vpif_update_std_info(struct channel_obj *ch)

    update standard related info

    :param ch:
        ptr to channel object
    :type ch: struct channel_obj \*

.. _`vpif_update_std_info.description`:

Description
-----------

For a given standard selected by application, update values
in the device data structures

.. _`vpif_calculate_offsets`:

vpif_calculate_offsets
======================

.. c:function:: void vpif_calculate_offsets(struct channel_obj *ch)

    This function calculates buffers offsets

    :param ch:
        ptr to channel object
    :type ch: struct channel_obj \*

.. _`vpif_calculate_offsets.description`:

Description
-----------

This function calculates buffer offsets for Y and C in the top and
bottom field

.. _`vpif_get_default_field`:

vpif_get_default_field
======================

.. c:function:: enum v4l2_field vpif_get_default_field(struct vpif_interface *iface)

    Get default field type based on interface

    :param iface:
        ptr to vpif interface
    :type iface: struct vpif_interface \*

.. _`vpif_config_addr`:

vpif_config_addr
================

.. c:function:: void vpif_config_addr(struct channel_obj *ch, int muxmode)

    function to configure buffer address in vpif

    :param ch:
        channel ptr
    :type ch: struct channel_obj \*

    :param muxmode:
        channel mux mode
    :type muxmode: int

.. _`vpif_input_to_subdev`:

vpif_input_to_subdev
====================

.. c:function:: int vpif_input_to_subdev(struct vpif_capture_config *vpif_cfg, struct vpif_capture_chan_config *chan_cfg, int input_index)

    Maps input to sub device

    :param vpif_cfg:
        global config ptr
    :type vpif_cfg: struct vpif_capture_config \*

    :param chan_cfg:
        channel config ptr
    :type chan_cfg: struct vpif_capture_chan_config \*

    :param input_index:
        Given input index from application
    :type input_index: int

.. _`vpif_input_to_subdev.description`:

Description
-----------

lookup the sub device information for a given input index.
we report all the inputs to application. inputs table also
has sub device name for the each input

.. _`vpif_set_input`:

vpif_set_input
==============

.. c:function:: int vpif_set_input(struct vpif_capture_config *vpif_cfg, struct channel_obj *ch, int index)

    Select an input

    :param vpif_cfg:
        global config ptr
    :type vpif_cfg: struct vpif_capture_config \*

    :param ch:
        channel
    :type ch: struct channel_obj \*

    :param index:
        Given input index from application
    :type index: int

.. _`vpif_set_input.description`:

Description
-----------

Select the given input.

.. _`vpif_querystd`:

vpif_querystd
=============

.. c:function:: int vpif_querystd(struct file *file, void *priv, v4l2_std_id *std_id)

    querystd handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param std_id:
        ptr to std id
    :type std_id: v4l2_std_id \*

.. _`vpif_querystd.description`:

Description
-----------

This function is called to detect standard at the selected input

.. _`vpif_g_std`:

vpif_g_std
==========

.. c:function:: int vpif_g_std(struct file *file, void *priv, v4l2_std_id *std)

    get STD handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param std:
        ptr to std id
    :type std: v4l2_std_id \*

.. _`vpif_s_std`:

vpif_s_std
==========

.. c:function:: int vpif_s_std(struct file *file, void *priv, v4l2_std_id std_id)

    set STD handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param std_id:
        ptr to std id
    :type std_id: v4l2_std_id

.. _`vpif_enum_input`:

vpif_enum_input
===============

.. c:function:: int vpif_enum_input(struct file *file, void *priv, struct v4l2_input *input)

    ENUMINPUT handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param input:
        ptr to input structure
    :type input: struct v4l2_input \*

.. _`vpif_g_input`:

vpif_g_input
============

.. c:function:: int vpif_g_input(struct file *file, void *priv, unsigned int *index)

    Get INPUT handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param index:
        ptr to input index
    :type index: unsigned int \*

.. _`vpif_s_input`:

vpif_s_input
============

.. c:function:: int vpif_s_input(struct file *file, void *priv, unsigned int index)

    Set INPUT handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param index:
        input index
    :type index: unsigned int

.. _`vpif_enum_fmt_vid_cap`:

vpif_enum_fmt_vid_cap
=====================

.. c:function:: int vpif_enum_fmt_vid_cap(struct file *file, void *priv, struct v4l2_fmtdesc *fmt)

    ENUM_FMT handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param fmt:
        ptr to V4L2 format descriptor
    :type fmt: struct v4l2_fmtdesc \*

.. _`vpif_try_fmt_vid_cap`:

vpif_try_fmt_vid_cap
====================

.. c:function:: int vpif_try_fmt_vid_cap(struct file *file, void *priv, struct v4l2_format *fmt)

    TRY_FMT handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param fmt:
        ptr to v4l2 format structure
    :type fmt: struct v4l2_format \*

.. _`vpif_g_fmt_vid_cap`:

vpif_g_fmt_vid_cap
==================

.. c:function:: int vpif_g_fmt_vid_cap(struct file *file, void *priv, struct v4l2_format *fmt)

    Set INPUT handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param fmt:
        ptr to v4l2 format structure
    :type fmt: struct v4l2_format \*

.. _`vpif_s_fmt_vid_cap`:

vpif_s_fmt_vid_cap
==================

.. c:function:: int vpif_s_fmt_vid_cap(struct file *file, void *priv, struct v4l2_format *fmt)

    Set FMT handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param fmt:
        ptr to v4l2 format structure
    :type fmt: struct v4l2_format \*

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

.. _`vpif_query_dv_timings`:

vpif_query_dv_timings
=====================

.. c:function:: int vpif_query_dv_timings(struct file *file, void *priv, struct v4l2_dv_timings *timings)

    QUERY_DV_TIMINGS handler

    :param file:
        file ptr
    :type file: struct file \*

    :param priv:
        file handle
    :type priv: void \*

    :param timings:
        input timings
    :type timings: struct v4l2_dv_timings \*

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

.. _`initialize_vpif`:

initialize_vpif
===============

.. c:function:: int initialize_vpif( void)

    Initialize vpif data structures

    :param void:
        no arguments
    :type void: 

.. _`initialize_vpif.description`:

Description
-----------

Allocate memory for data structures and initialize them

.. _`vpif_probe`:

vpif_probe
==========

.. c:function:: int vpif_probe(struct platform_device *pdev)

    This function probes the vpif capture driver

    :param pdev:
        platform device pointer
    :type pdev: struct platform_device \*

.. _`vpif_probe.description`:

Description
-----------

This creates device entries by register itself to the V4L2 driver and
initializes fields of each channel objects

.. _`vpif_remove`:

vpif_remove
===========

.. c:function:: int vpif_remove(struct platform_device *device)

    driver remove handler

    :param device:
        ptr to platform device structure
    :type device: struct platform_device \*

.. _`vpif_remove.description`:

Description
-----------

The vidoe device is unregistered

.. _`vpif_suspend`:

vpif_suspend
============

.. c:function:: int vpif_suspend(struct device *dev)

    vpif device suspend

    :param dev:
        pointer to \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

.. This file was automatic generated / don't edit.

