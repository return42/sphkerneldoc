.. -*- coding: utf-8; mode: rst -*-

============
pxa_camera.c
============



.. _xref_pxa_init_dma_channel:

pxa_init_dma_channel
====================

.. c:function:: int pxa_init_dma_channel (struct pxa_camera_dev * pcdev, struct pxa_buffer * buf, struct videobuf_dmabuf * dma, int channel, int cibr, int size, struct scatterlist ** sg_first, int * sg_first_ofs)

    init dma descriptors

    :param struct pxa_camera_dev * pcdev:
        pxa camera device

    :param struct pxa_buffer * buf:
        pxa buffer to find pxa dma channel

    :param struct videobuf_dmabuf * dma:
        dma video buffer

    :param int channel:
        dma channel (0 => 'Y', 1 => 'U', 2 => 'V')

    :param int cibr:
        camera Receive Buffer Register

    :param int size:
        bytes to transfer

    :param struct scatterlist ** sg_first:
        first element of sg_list

    :param int * sg_first_ofs:
        offset in first element of sg_list



Description
-----------

Prepares the pxa dma descriptors to transfer one camera channel.
Beware sg_first and sg_first_ofs are both input and output parameters.


Returns 0 or -ENOMEM if no coherent memory is available




.. _xref_pxa_dma_start_channels:

pxa_dma_start_channels
======================

.. c:function:: void pxa_dma_start_channels (struct pxa_camera_dev * pcdev)

    start DMA channel for active buffer

    :param struct pxa_camera_dev * pcdev:
        pxa camera device



Description
-----------

Initialize DMA channels to the beginning of the active video buffer, and
start these channels.




.. _xref_pxa_camera_start_capture:

pxa_camera_start_capture
========================

.. c:function:: void pxa_camera_start_capture (struct pxa_camera_dev * pcdev)

    start video capturing

    :param struct pxa_camera_dev * pcdev:
        camera device



Description
-----------

Launch capturing. DMA channels should not be active yet. They should get
activated at the end of frame interrupt, to capture only whole frames, and
never begin the capture of a partial frame.




.. _xref_pxa_camera_check_link_miss:

pxa_camera_check_link_miss
==========================

.. c:function:: void pxa_camera_check_link_miss (struct pxa_camera_dev * pcdev)

    check missed DMA linking

    :param struct pxa_camera_dev * pcdev:
        camera device



Description
-----------

The DMA chaining is done with DMA running. This means a tiny temporal window
remains, where a buffer is queued on the chain, while the chain is already
stopped. This means the tailed buffer would never be transferred by DMA.
This function restarts the capture for this corner case, where :
 - :c:func:`DADR` == DADDR_STOP
 - a videobuffer is queued on the pcdev->capture list


Please check the "DMA hot chaining timeslice issue" in
  Documentation/video4linux/pxa_camera.txt



Context
-------

should only be called within the dma irq handler


