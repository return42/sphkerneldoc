.. -*- coding: utf-8; mode: rst -*-

==============
vpif_capture.c
==============



.. _xref_vpif_buffer_prepare:

vpif_buffer_prepare
===================

.. c:function:: int vpif_buffer_prepare (struct vb2_buffer * vb)

    

    :param struct vb2_buffer * vb:
        ptr to vb2_buffer



Description
-----------

This is the callback function for buffer prepare when :c:func:`vb2_qbuf`
function is called. The buffer is prepared and user space virtual address
or user address is converted into  physical address




.. _xref_vpif_buffer_queue_setup:

vpif_buffer_queue_setup
=======================

.. c:function:: int vpif_buffer_queue_setup (struct vb2_queue * vq, unsigned int * nbuffers, unsigned int * nplanes, unsigned int sizes[], void * alloc_ctxs[])

    

    :param struct vb2_queue * vq:
        vb2_queue ptr

    :param unsigned int * nbuffers:
        ptr to number of buffers requested by application

    :param unsigned int * nplanes:
        : contains number of distinct video planes needed to hold a frame
        **sizes**[]: contains the size (in bytes) of each plane.

    :param unsigned int sizes[]:

    :param void * alloc_ctxs[]:



Description
-----------

This callback function is called when :c:func:`reqbuf` is called to adjust
the buffer count and buffer size




.. _xref_vpif_buffer_queue:

vpif_buffer_queue
=================

.. c:function:: void vpif_buffer_queue (struct vb2_buffer * vb)

    

    :param struct vb2_buffer * vb:
        ptr to vb2_buffer




.. _xref_vpif_start_streaming:

vpif_start_streaming
====================

.. c:function:: int vpif_start_streaming (struct vb2_queue * vq, unsigned int count)

    

    :param struct vb2_queue * vq:

        _undescribed_

    :param unsigned int count:
        number of buffers




.. _xref_vpif_stop_streaming:

vpif_stop_streaming
===================

.. c:function:: void vpif_stop_streaming (struct vb2_queue * vq)

    

    :param struct vb2_queue * vq:
        ptr to vb2_queue



Description
-----------

This callback stops the DMA engine and any remaining buffers
in the DMA queue are released.




.. _xref_vpif_process_buffer_complete:

vpif_process_buffer_complete
============================

.. c:function:: void vpif_process_buffer_complete (struct common_obj * common)

    

    :param struct common_obj * common:
        ptr to common channel object



Description
-----------

This function time stamp the buffer and mark it as DONE. It also
wake up any process waiting on the QUEUE and set the next buffer
as current




.. _xref_vpif_schedule_next_buffer:

vpif_schedule_next_buffer
=========================

.. c:function:: void vpif_schedule_next_buffer (struct common_obj * common)

    

    :param struct common_obj * common:
        ptr to common channel object



Description
-----------

This function will get next buffer from the dma queue and
set the buffer address in the vpif register for capture.
the buffer is marked active




.. _xref_vpif_channel_isr:

vpif_channel_isr
================

.. c:function:: irqreturn_t vpif_channel_isr (int irq, void * dev_id)

    

    :param int irq:
        irq number

    :param void * dev_id:
        dev_id ptr



Description
-----------

It changes status of the captured buffer, takes next buffer from the queue
and sets its address in VPIF registers




.. _xref_vpif_update_std_info:

vpif_update_std_info
====================

.. c:function:: int vpif_update_std_info (struct channel_obj * ch)

    update standard related info

    :param struct channel_obj * ch:
        ptr to channel object



Description
-----------

For a given standard selected by application, update values
in the device data structures




.. _xref_vpif_calculate_offsets:

vpif_calculate_offsets
======================

.. c:function:: void vpif_calculate_offsets (struct channel_obj * ch)

    

    :param struct channel_obj * ch:
        ptr to channel object



Description
-----------

This function calculates buffer offsets for Y and C in the top and
bottom field




.. _xref_vpif_get_default_field:

vpif_get_default_field
======================

.. c:function:: enum v4l2_field vpif_get_default_field (struct vpif_interface * iface)

    Get default field type based on interface @vpif_params - ptr to vpif params

    :param struct vpif_interface * iface:

        _undescribed_




.. _xref_vpif_config_addr:

vpif_config_addr
================

.. c:function:: void vpif_config_addr (struct channel_obj * ch, int muxmode)

    function to configure buffer address in vpif @ch - channel ptr @muxmode - channel mux mode

    :param struct channel_obj * ch:

        _undescribed_

    :param int muxmode:

        _undescribed_




.. _xref_vpif_input_to_subdev:

vpif_input_to_subdev
====================

.. c:function:: int vpif_input_to_subdev (struct vpif_capture_config * vpif_cfg, struct vpif_capture_chan_config * chan_cfg, int input_index)

    Maps input to sub device @vpif_cfg - global config ptr @chan_cfg - channel config ptr @input_index - Given input index from application

    :param struct vpif_capture_config * vpif_cfg:

        _undescribed_

    :param struct vpif_capture_chan_config * chan_cfg:

        _undescribed_

    :param int input_index:

        _undescribed_



Description
-----------



lookup the sub device information for a given input index.
we report all the inputs to application. inputs table also
has sub device name for the each input




.. _xref_vpif_set_input:

vpif_set_input
==============

.. c:function:: int vpif_set_input (struct vpif_capture_config * vpif_cfg, struct channel_obj * ch, int index)

    Select an input @vpif_cfg - global config ptr @ch - channel @_index - Given input index from application

    :param struct vpif_capture_config * vpif_cfg:

        _undescribed_

    :param struct channel_obj * ch:

        _undescribed_

    :param int index:

        _undescribed_



Description
-----------



Select the given input.




.. _xref_vpif_querystd:

vpif_querystd
=============

.. c:function:: int vpif_querystd (struct file * file, void * priv, v4l2_std_id * std_id)

    querystd handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param v4l2_std_id * std_id:
        ptr to std id



Description
-----------

This function is called to detect standard at the selected input




.. _xref_vpif_g_std:

vpif_g_std
==========

.. c:function:: int vpif_g_std (struct file * file, void * priv, v4l2_std_id * std)

    get STD handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param v4l2_std_id * std:

        _undescribed_




.. _xref_vpif_s_std:

vpif_s_std
==========

.. c:function:: int vpif_s_std (struct file * file, void * priv, v4l2_std_id std_id)

    set STD handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param v4l2_std_id std_id:
        ptr to std id




.. _xref_vpif_enum_input:

vpif_enum_input
===============

.. c:function:: int vpif_enum_input (struct file * file, void * priv, struct v4l2_input * input)

    ENUMINPUT handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param struct v4l2_input * input:
        ptr to input structure




.. _xref_vpif_g_input:

vpif_g_input
============

.. c:function:: int vpif_g_input (struct file * file, void * priv, unsigned int * index)

    Get INPUT handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param unsigned int * index:
        ptr to input index




.. _xref_vpif_s_input:

vpif_s_input
============

.. c:function:: int vpif_s_input (struct file * file, void * priv, unsigned int index)

    Set INPUT handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param unsigned int index:
        input index




.. _xref_vpif_enum_fmt_vid_cap:

vpif_enum_fmt_vid_cap
=====================

.. c:function:: int vpif_enum_fmt_vid_cap (struct file * file, void * priv, struct v4l2_fmtdesc * fmt)

    ENUM_FMT handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param struct v4l2_fmtdesc * fmt:

        _undescribed_




.. _xref_vpif_try_fmt_vid_cap:

vpif_try_fmt_vid_cap
====================

.. c:function:: int vpif_try_fmt_vid_cap (struct file * file, void * priv, struct v4l2_format * fmt)

    TRY_FMT handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param struct v4l2_format * fmt:
        ptr to v4l2 format structure




.. _xref_vpif_g_fmt_vid_cap:

vpif_g_fmt_vid_cap
==================

.. c:function:: int vpif_g_fmt_vid_cap (struct file * file, void * priv, struct v4l2_format * fmt)

    Set INPUT handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param struct v4l2_format * fmt:
        ptr to v4l2 format structure




.. _xref_vpif_s_fmt_vid_cap:

vpif_s_fmt_vid_cap
==================

.. c:function:: int vpif_s_fmt_vid_cap (struct file * file, void * priv, struct v4l2_format * fmt)

    Set FMT handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param struct v4l2_format * fmt:
        ptr to v4l2 format structure




.. _xref_vpif_querycap:

vpif_querycap
=============

.. c:function:: int vpif_querycap (struct file * file, void * priv, struct v4l2_capability * cap)

    QUERYCAP handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param struct v4l2_capability * cap:
        ptr to v4l2_capability structure




.. _xref_vpif_enum_dv_timings:

vpif_enum_dv_timings
====================

.. c:function:: int vpif_enum_dv_timings (struct file * file, void * priv, struct v4l2_enum_dv_timings * timings)

    ENUM_DV_TIMINGS handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param struct v4l2_enum_dv_timings * timings:
        input timings




.. _xref_vpif_query_dv_timings:

vpif_query_dv_timings
=====================

.. c:function:: int vpif_query_dv_timings (struct file * file, void * priv, struct v4l2_dv_timings * timings)

    QUERY_DV_TIMINGS handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param struct v4l2_dv_timings * timings:
        input timings




.. _xref_vpif_s_dv_timings:

vpif_s_dv_timings
=================

.. c:function:: int vpif_s_dv_timings (struct file * file, void * priv, struct v4l2_dv_timings * timings)

    S_DV_TIMINGS handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param struct v4l2_dv_timings * timings:
        digital video timings




.. _xref_vpif_g_dv_timings:

vpif_g_dv_timings
=================

.. c:function:: int vpif_g_dv_timings (struct file * file, void * priv, struct v4l2_dv_timings * timings)

    G_DV_TIMINGS handler

    :param struct file * file:
        file ptr

    :param void * priv:
        file handle

    :param struct v4l2_dv_timings * timings:
        digital video timings




.. _xref_initialize_vpif:

initialize_vpif
===============

.. c:function:: int initialize_vpif ( void)

    Initialize vpif data structures

    :param void:
        no arguments



Description
-----------



Allocate memory for data structures and initialize them




.. _xref_vpif_probe:

vpif_probe
==========

.. c:function:: int vpif_probe (struct platform_device * pdev)

    

    :param struct platform_device * pdev:
        platform device pointer



Description
-----------

This creates device entries by register itself to the V4L2 driver and
initializes fields of each channel objects




.. _xref_vpif_remove:

vpif_remove
===========

.. c:function:: int vpif_remove (struct platform_device * device)

    driver remove handler

    :param struct platform_device * device:
        ptr to platform device structure



Description
-----------

The vidoe device is unregistered




.. _xref_vpif_suspend:

vpif_suspend
============

.. c:function:: int vpif_suspend (struct device * dev)

    

    :param struct device * dev:

        _undescribed_


