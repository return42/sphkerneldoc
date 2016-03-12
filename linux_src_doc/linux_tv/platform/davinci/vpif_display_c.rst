.. -*- coding: utf-8; mode: rst -*-

==============
vpif_display.c
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



Description
-----------

This callback fucntion queues the buffer to DMA engine




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




.. _xref_vpif_output_to_subdev:

vpif_output_to_subdev
=====================

.. c:function:: int vpif_output_to_subdev (struct vpif_display_config * vpif_cfg, struct vpif_display_chan_config * chan_cfg, int index)

    Maps output to sub device @vpif_cfg - global config ptr @chan_cfg - channel config ptr @index - Given output index from application

    :param struct vpif_display_config * vpif_cfg:

        _undescribed_

    :param struct vpif_display_chan_config * chan_cfg:

        _undescribed_

    :param int index:

        _undescribed_



Description
-----------



lookup the sub device information for a given output index.
we report all the output to application. output table also
has sub device name for the each output




.. _xref_vpif_set_output:

vpif_set_output
===============

.. c:function:: int vpif_set_output (struct vpif_display_config * vpif_cfg, struct channel_obj * ch, int index)

    Select an output @vpif_cfg - global config ptr @ch - channel @index - Given output index from application

    :param struct vpif_display_config * vpif_cfg:

        _undescribed_

    :param struct channel_obj * ch:

        _undescribed_

    :param int index:

        _undescribed_



Description
-----------



Select the given output.




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


