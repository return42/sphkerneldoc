.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/soc_camera/pxa_camera.c

.. _`pxa_init_dma_channel`:

pxa_init_dma_channel
====================

.. c:function:: int pxa_init_dma_channel(struct pxa_camera_dev *pcdev, struct pxa_buffer *buf, struct videobuf_dmabuf *dma, int channel, int cibr, int size, int offset)

    init dma descriptors

    :param struct pxa_camera_dev \*pcdev:
        pxa camera device

    :param struct pxa_buffer \*buf:
        pxa buffer to find pxa dma channel

    :param struct videobuf_dmabuf \*dma:
        dma video buffer

    :param int channel:
        dma channel (0 => 'Y', 1 => 'U', 2 => 'V')

    :param int cibr:
        camera Receive Buffer Register

    :param int size:
        bytes to transfer

    :param int offset:
        offset in videobuffer of the first byte to transfer

.. _`pxa_init_dma_channel.description`:

Description
-----------

Prepares the pxa dma descriptors to transfer one camera channel.

Returns 0 if success or -ENOMEM if no memory is available

.. _`pxa_dma_start_channels`:

pxa_dma_start_channels
======================

.. c:function:: void pxa_dma_start_channels(struct pxa_camera_dev *pcdev)

    start DMA channel for active buffer

    :param struct pxa_camera_dev \*pcdev:
        pxa camera device

.. _`pxa_dma_start_channels.description`:

Description
-----------

Initialize DMA channels to the beginning of the active video buffer, and
start these channels.

.. _`pxa_camera_start_capture`:

pxa_camera_start_capture
========================

.. c:function:: void pxa_camera_start_capture(struct pxa_camera_dev *pcdev)

    start video capturing

    :param struct pxa_camera_dev \*pcdev:
        camera device

.. _`pxa_camera_start_capture.description`:

Description
-----------

Launch capturing. DMA channels should not be active yet. They should get
activated at the end of frame interrupt, to capture only whole frames, and
never begin the capture of a partial frame.

.. _`pxa_camera_check_link_miss`:

pxa_camera_check_link_miss
==========================

.. c:function:: void pxa_camera_check_link_miss(struct pxa_camera_dev *pcdev, dma_cookie_t last_submitted, dma_cookie_t last_issued)

    check missed DMA linking

    :param struct pxa_camera_dev \*pcdev:
        camera device

    :param dma_cookie_t last_submitted:
        *undescribed*

    :param dma_cookie_t last_issued:
        *undescribed*

.. _`pxa_camera_check_link_miss.description`:

Description
-----------

The DMA chaining is done with DMA running. This means a tiny temporal window
remains, where a buffer is queued on the chain, while the chain is already
stopped. This means the tailed buffer would never be transferred by DMA.
This function restarts the capture for this corner case, where :
- \ :c:func:`DADR`\  == DADDR_STOP
- a videobuffer is queued on the pcdev->capture list

Please check the "DMA hot chaining timeslice issue" in
Documentation/video4linux/pxa_camera.txt

.. _`pxa_camera_check_link_miss.context`:

Context
-------

should only be called within the dma irq handler

.. This file was automatic generated / don't edit.

