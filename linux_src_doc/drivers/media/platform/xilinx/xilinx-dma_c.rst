.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/xilinx/xilinx-dma.c

.. _`xvip_pipeline_start_stop`:

xvip_pipeline_start_stop
========================

.. c:function:: int xvip_pipeline_start_stop(struct xvip_pipeline *pipe, bool start)

    Start ot stop streaming on a pipeline

    :param pipe:
        The pipeline
    :type pipe: struct xvip_pipeline \*

    :param start:
        Start (when true) or stop (when false) the pipeline
    :type start: bool

.. _`xvip_pipeline_start_stop.description`:

Description
-----------

Walk the entities chain starting at the pipeline output video node and start
or stop all of them.

Return: 0 if successful, or the return value of the failed video::s_stream
operation otherwise.

.. _`xvip_pipeline_set_stream`:

xvip_pipeline_set_stream
========================

.. c:function:: int xvip_pipeline_set_stream(struct xvip_pipeline *pipe, bool on)

    Enable/disable streaming on a pipeline

    :param pipe:
        The pipeline
    :type pipe: struct xvip_pipeline \*

    :param on:
        Turn the stream on when true or off when false
    :type on: bool

.. _`xvip_pipeline_set_stream.description`:

Description
-----------

The pipeline is shared between all DMA engines connect at its input and
output. While the stream state of DMA engines can be controlled
independently, pipelines have a shared stream state that enable or disable
all entities in the pipeline. For this reason the pipeline uses a streaming
counter that tracks the number of DMA engines that have requested the stream
to be enabled.

When called with the \ ``on``\  argument set to true, this function will increment
the pipeline streaming count. If the streaming count reaches the number of
DMA engines in the pipeline it will enable all entities that belong to the
pipeline.

Similarly, when called with the \ ``on``\  argument set to false, this function will
decrement the pipeline streaming count and disable all entities in the
pipeline when the streaming count reaches zero.

Return: 0 if successful, or the return value of the failed video::s_stream
operation otherwise. Stopping the pipeline never fails. The pipeline state is
not updated when the operation fails.

.. _`xvip_pipeline_cleanup`:

xvip_pipeline_cleanup
=====================

.. c:function:: void xvip_pipeline_cleanup(struct xvip_pipeline *pipe)

    Cleanup the pipeline after streaming

    :param pipe:
        the pipeline
    :type pipe: struct xvip_pipeline \*

.. _`xvip_pipeline_cleanup.description`:

Description
-----------

Decrease the pipeline use count and clean it up if we were the last user.

.. _`xvip_pipeline_prepare`:

xvip_pipeline_prepare
=====================

.. c:function:: int xvip_pipeline_prepare(struct xvip_pipeline *pipe, struct xvip_dma *dma)

    Prepare the pipeline for streaming

    :param pipe:
        the pipeline
    :type pipe: struct xvip_pipeline \*

    :param dma:
        DMA engine at one end of the pipeline
    :type dma: struct xvip_dma \*

.. _`xvip_pipeline_prepare.description`:

Description
-----------

Validate the pipeline if no user exists yet, otherwise just increase the use
count.

.. _`xvip_pipeline_prepare.return`:

Return
------

0 if successful or -EPIPE if the pipeline is not valid.

.. _`xvip_dma_buffer`:

struct xvip_dma_buffer
======================

.. c:type:: struct xvip_dma_buffer

    Video DMA buffer

.. _`xvip_dma_buffer.definition`:

Definition
----------

.. code-block:: c

    struct xvip_dma_buffer {
        struct vb2_v4l2_buffer buf;
        struct list_head queue;
        struct xvip_dma *dma;
    }

.. _`xvip_dma_buffer.members`:

Members
-------

buf
    vb2 buffer base object

queue
    buffer list entry in the DMA engine queued buffers list

dma
    DMA channel that uses the buffer

.. This file was automatic generated / don't edit.

