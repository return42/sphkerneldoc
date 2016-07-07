.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/drivers/mite.c

.. _`mite_bytes_in_transit`:

mite_bytes_in_transit
=====================

.. c:function:: u32 mite_bytes_in_transit(struct mite_channel *mite_chan)

    Returns the number of unread bytes in the fifo.

    :param struct mite_channel \*mite_chan:
        MITE dma channel.

.. _`mite_sync_dma`:

mite_sync_dma
=============

.. c:function:: void mite_sync_dma(struct mite_channel *mite_chan, struct comedi_subdevice *s)

    Sync the MITE dma with the COMEDI async buffer.

    :param struct mite_channel \*mite_chan:
        MITE dma channel.

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.

.. _`mite_ack_linkc`:

mite_ack_linkc
==============

.. c:function:: void mite_ack_linkc(struct mite_channel *mite_chan, struct comedi_subdevice *s, bool sync)

    Check and ack the LINKC interrupt,

    :param struct mite_channel \*mite_chan:
        MITE dma channel.

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.

    :param bool sync:
        flag to force a \ :c:func:`mite_sync_dma`\ .

.. _`mite_ack_linkc.description`:

Description
-----------

This will also ack the DONE interrupt if active.

.. _`mite_done`:

mite_done
=========

.. c:function:: int mite_done(struct mite_channel *mite_chan)

    Check is a MITE dma transfer is complete.

    :param struct mite_channel \*mite_chan:
        MITE dma channel.

.. _`mite_done.description`:

Description
-----------

This will also ack the DONE interrupt if active.

.. _`mite_dma_arm`:

mite_dma_arm
============

.. c:function:: void mite_dma_arm(struct mite_channel *mite_chan)

    Start a MITE dma transfer.

    :param struct mite_channel \*mite_chan:
        MITE dma channel.

.. _`mite_dma_disarm`:

mite_dma_disarm
===============

.. c:function:: void mite_dma_disarm(struct mite_channel *mite_chan)

    Stop a MITE dma transfer.

    :param struct mite_channel \*mite_chan:
        MITE dma channel.

.. _`mite_prep_dma`:

mite_prep_dma
=============

.. c:function:: void mite_prep_dma(struct mite_channel *mite_chan, unsigned int num_device_bits, unsigned int num_memory_bits)

    Prepare a MITE dma channel for transfers.

    :param struct mite_channel \*mite_chan:
        MITE dma channel.

    :param unsigned int num_device_bits:
        device transfer size (8, 16, or 32-bits).

    :param unsigned int num_memory_bits:
        memory transfer size (8, 16, or 32-bits).

.. _`mite_request_channel_in_range`:

mite_request_channel_in_range
=============================

.. c:function:: struct mite_channel *mite_request_channel_in_range(struct mite *mite, struct mite_ring *ring, unsigned int min_channel, unsigned int max_channel)

    Request a MITE dma channel.

    :param struct mite \*mite:
        MITE device.

    :param struct mite_ring \*ring:
        MITE dma ring.

    :param unsigned int min_channel:
        minimum channel index to use.

    :param unsigned int max_channel:
        maximum channel index to use.

.. _`mite_request_channel`:

mite_request_channel
====================

.. c:function:: struct mite_channel *mite_request_channel(struct mite *mite, struct mite_ring *ring)

    Request a MITE dma channel.

    :param struct mite \*mite:
        MITE device.

    :param struct mite_ring \*ring:
        MITE dma ring.

.. _`mite_release_channel`:

mite_release_channel
====================

.. c:function:: void mite_release_channel(struct mite_channel *mite_chan)

    Release a MITE dma channel.

    :param struct mite_channel \*mite_chan:
        MITE dma channel.

.. _`mite_init_ring_descriptors`:

mite_init_ring_descriptors
==========================

.. c:function:: int mite_init_ring_descriptors(struct mite_ring *ring, struct comedi_subdevice *s, unsigned int nbytes)

    Initialize a MITE dma ring descriptors.

    :param struct mite_ring \*ring:
        MITE dma ring.

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.

    :param unsigned int nbytes:
        the size of the dma ring (in bytes).

.. _`mite_init_ring_descriptors.description`:

Description
-----------

Initializes the ring buffer descriptors to provide correct DMA transfer
links to the exact amount of memory required. When the ring buffer is
allocated by \ :c:func:`mite_buf_change`\ , the default is to initialize the ring
to refer to the entire DMA data buffer. A command may call this function
later to re-initialize and shorten the amount of memory that will be
transferred.

.. _`mite_buf_change`:

mite_buf_change
===============

.. c:function:: int mite_buf_change(struct mite_ring *ring, struct comedi_subdevice *s)

    COMEDI subdevice (\*buf_change) for a MITE dma ring.

    :param struct mite_ring \*ring:
        MITE dma ring.

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.

.. _`mite_alloc_ring`:

mite_alloc_ring
===============

.. c:function:: struct mite_ring *mite_alloc_ring(struct mite *mite)

    Allocate a MITE dma ring.

    :param struct mite \*mite:
        MITE device.

.. _`mite_free_ring`:

mite_free_ring
==============

.. c:function:: void mite_free_ring(struct mite_ring *ring)

    Free a MITE dma ring and its descriptors.

    :param struct mite_ring \*ring:
        MITE dma ring.

.. _`mite_attach`:

mite_attach
===========

.. c:function:: struct mite *mite_attach(struct comedi_device *dev, bool use_win1)

    Allocate and initialize a MITE device for a comedi driver.

    :param struct comedi_device \*dev:
        COMEDI device.

    :param bool use_win1:
        flag to use I/O Window 1 instead of I/O Window 0.

.. _`mite_attach.description`:

Description
-----------

Called by a COMEDI drivers (\*auto_attach).

Returns a pointer to the MITE device on success, or NULL if the MITE cannot
be allocated or remapped.

.. _`mite_detach`:

mite_detach
===========

.. c:function:: void mite_detach(struct mite *mite)

    Unmap and free a MITE device for a comedi driver.

    :param struct mite \*mite:
        MITE device.

.. _`mite_detach.description`:

Description
-----------

Called by a COMEDI drivers (\*detach).

.. This file was automatic generated / don't edit.

