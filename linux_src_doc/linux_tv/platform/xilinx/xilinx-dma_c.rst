.. -*- coding: utf-8; mode: rst -*-

============
xilinx-dma.c
============



.. _xref_xvip_pipeline_start_stop:

xvip_pipeline_start_stop
========================

.. c:function:: int xvip_pipeline_start_stop (struct xvip_pipeline * pipe, bool start)

    Start ot stop streaming on a pipeline

    :param struct xvip_pipeline * pipe:
        The pipeline

    :param bool start:
        Start (when true) or stop (when false) the pipeline



Description
-----------

Walk the entities chain starting at the pipeline output video node and start
or stop all of them.



Return
------

0 if successful, or the return value of the failed video::s_stream
operation otherwise.




.. _xref_xvip_pipeline_set_stream:

xvip_pipeline_set_stream
========================

.. c:function:: int xvip_pipeline_set_stream (struct xvip_pipeline * pipe, bool on)

    Enable/disable streaming on a pipeline

    :param struct xvip_pipeline * pipe:
        The pipeline

    :param bool on:
        Turn the stream on when true or off when false



Description
-----------

The pipeline is shared between all DMA engines connect at its input and
output. While the stream state of DMA engines can be controlled
independently, pipelines have a shared stream state that enable or disable
all entities in the pipeline. For this reason the pipeline uses a streaming
counter that tracks the number of DMA engines that have requested the stream
to be enabled.


When called with the **on** argument set to true, this function will increment
the pipeline streaming count. If the streaming count reaches the number of
DMA engines in the pipeline it will enable all entities that belong to the
pipeline.


Similarly, when called with the **on** argument set to false, this function will
decrement the pipeline streaming count and disable all entities in the
pipeline when the streaming count reaches zero.



Return
------

0 if successful, or the return value of the failed video::s_stream
operation otherwise. Stopping the pipeline never fails. The pipeline state is
not updated when the operation fails.




.. _xref_xvip_pipeline_cleanup:

xvip_pipeline_cleanup
=====================

.. c:function:: void xvip_pipeline_cleanup (struct xvip_pipeline * pipe)

    Cleanup the pipeline after streaming

    :param struct xvip_pipeline * pipe:
        the pipeline



Description
-----------

Decrease the pipeline use count and clean it up if we were the last user.




.. _xref_xvip_pipeline_prepare:

xvip_pipeline_prepare
=====================

.. c:function:: int xvip_pipeline_prepare (struct xvip_pipeline * pipe, struct xvip_dma * dma)

    Prepare the pipeline for streaming

    :param struct xvip_pipeline * pipe:
        the pipeline

    :param struct xvip_dma * dma:
        DMA engine at one end of the pipeline



Description
-----------

Validate the pipeline if no user exists yet, otherwise just increase the use
count.



Return
------

0 if successful or -EPIPE if the pipeline is not valid.




.. _xref_struct_xvip_dma_buffer:

struct xvip_dma_buffer
======================

.. c:type:: struct xvip_dma_buffer

    Video DMA buffer



Definition
----------

.. code-block:: c

  struct xvip_dma_buffer {
    struct vb2_v4l2_buffer buf;
    struct list_head queue;
    struct xvip_dma * dma;
  };



Members
-------

:``struct vb2_v4l2_buffer buf``:
    vb2 buffer base object

:``struct list_head queue``:
    buffer list entry in the DMA engine queued buffers list

:``struct xvip_dma * dma``:
    DMA channel that uses the buffer



