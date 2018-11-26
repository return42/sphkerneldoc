.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mailbox/bcm-pdc-mailbox.c

.. _`pdc_setup_debugfs`:

pdc_setup_debugfs
=================

.. c:function:: void pdc_setup_debugfs(struct pdc_state *pdcs)

    Create the debug FS directories. If the top-level directory has not yet been created, create it now. Create a stats file in this directory for a SPU.

    :param pdcs:
        PDC state structure
    :type pdcs: struct pdc_state \*

.. _`pdc_build_rxd`:

pdc_build_rxd
=============

.. c:function:: void pdc_build_rxd(struct pdc_state *pdcs, dma_addr_t dma_addr, u32 buf_len, u32 flags)

    Build DMA descriptor to receive SPU result.

    :param pdcs:
        PDC state for SPU that will generate result
    :type pdcs: struct pdc_state \*

    :param dma_addr:
        DMA address of buffer that descriptor is being built for
    :type dma_addr: dma_addr_t

    :param buf_len:
        Length of the receive buffer, in bytes
    :type buf_len: u32

    :param flags:
        Flags to be stored in descriptor
    :type flags: u32

.. _`pdc_build_txd`:

pdc_build_txd
=============

.. c:function:: void pdc_build_txd(struct pdc_state *pdcs, dma_addr_t dma_addr, u32 buf_len, u32 flags)

    Build a DMA descriptor to transmit a SPU request to hardware.

    :param pdcs:
        PDC state for the SPU that will process this request
    :type pdcs: struct pdc_state \*

    :param dma_addr:
        DMA address of packet to be transmitted
    :type dma_addr: dma_addr_t

    :param buf_len:
        Length of tx buffer, in bytes
    :type buf_len: u32

    :param flags:
        Flags to be stored in descriptor
    :type flags: u32

.. _`pdc_receive_one`:

pdc_receive_one
===============

.. c:function:: int pdc_receive_one(struct pdc_state *pdcs)

    Receive a response message from a given SPU.

    :param pdcs:
        PDC state for the SPU to receive from
    :type pdcs: struct pdc_state \*

.. _`pdc_receive_one.description`:

Description
-----------

When the return code indicates success, the response message is available in
the receive buffers provided prior to submission of the request.

.. _`pdc_receive_one.return`:

Return
------

PDC_SUCCESS if one or more receive descriptors was processed
-EAGAIN indicates that no response message is available
-EIO an error occurred

.. _`pdc_receive`:

pdc_receive
===========

.. c:function:: int pdc_receive(struct pdc_state *pdcs)

    Process as many responses as are available in the rx ring.

    :param pdcs:
        PDC state
    :type pdcs: struct pdc_state \*

.. _`pdc_receive.description`:

Description
-----------

Called within the hard IRQ.

.. _`pdc_tx_list_sg_add`:

pdc_tx_list_sg_add
==================

.. c:function:: int pdc_tx_list_sg_add(struct pdc_state *pdcs, struct scatterlist *sg)

    Add the buffers in a scatterlist to the transmit descriptors for a given SPU. The scatterlist buffers contain the data for a SPU request message.

    :param pdcs:
        *undescribed*
    :type pdcs: struct pdc_state \*

    :param sg:
        Scatterlist whose buffers contain part of the SPU request
    :type sg: struct scatterlist \*

.. _`pdc_tx_list_sg_add.description`:

Description
-----------

If a scatterlist buffer is larger than PDC_DMA_BUF_MAX, multiple descriptors
are written for that buffer, each <= PDC_DMA_BUF_MAX byte in length.

.. _`pdc_tx_list_sg_add.return`:

Return
------

PDC_SUCCESS if successful
< 0 otherwise

.. _`pdc_tx_list_final`:

pdc_tx_list_final
=================

.. c:function:: int pdc_tx_list_final(struct pdc_state *pdcs)

    Initiate DMA transfer of last frame written to tx ring.

    :param pdcs:
        PDC state for SPU to process the request
    :type pdcs: struct pdc_state \*

.. _`pdc_tx_list_final.description`:

Description
-----------

Sets the index of the last descriptor written in both the rx and tx ring.

.. _`pdc_tx_list_final.return`:

Return
------

PDC_SUCCESS

.. _`pdc_rx_list_init`:

pdc_rx_list_init
================

.. c:function:: int pdc_rx_list_init(struct pdc_state *pdcs, struct scatterlist *dst_sg, void *ctx)

    Start a new receive descriptor list for a given PDC.

    :param pdcs:
        PDC state for SPU handling request
    :type pdcs: struct pdc_state \*

    :param dst_sg:
        scatterlist providing rx buffers for response to be returned to
        mailbox client
    :type dst_sg: struct scatterlist \*

    :param ctx:
        Opaque context for this request
    :type ctx: void \*

.. _`pdc_rx_list_init.description`:

Description
-----------

Posts a single receive descriptor to hold the metadata that precedes a
response. For example, with SPU-M, the metadata is a 32-byte DMA header and
an 8-byte BCM header. Moves the msg_start descriptor indexes for both tx and
rx to indicate the start of a new message.

.. _`pdc_rx_list_init.return`:

Return
------

PDC_SUCCESS if successful
< 0 if an error (e.g., rx ring is full)

.. _`pdc_rx_list_sg_add`:

pdc_rx_list_sg_add
==================

.. c:function:: int pdc_rx_list_sg_add(struct pdc_state *pdcs, struct scatterlist *sg)

    Add the buffers in a scatterlist to the receive descriptors for a given SPU. The caller must have already DMA mapped the scatterlist.

    :param pdcs:
        *undescribed*
    :type pdcs: struct pdc_state \*

    :param sg:
        Scatterlist whose buffers are added to the receive ring
    :type sg: struct scatterlist \*

.. _`pdc_rx_list_sg_add.description`:

Description
-----------

If a receive buffer in the scatterlist is larger than PDC_DMA_BUF_MAX,
multiple receive descriptors are written, each with a buffer <=
PDC_DMA_BUF_MAX.

.. _`pdc_rx_list_sg_add.return`:

Return
------

PDC_SUCCESS if successful
< 0 otherwise (e.g., receive ring is full)

.. _`pdc_irq_handler`:

pdc_irq_handler
===============

.. c:function:: irqreturn_t pdc_irq_handler(int irq, void *data)

    Interrupt handler called in interrupt context.

    :param irq:
        Interrupt number that has fired
    :type irq: int

    :param data:
        device struct for DMA engine that generated the interrupt
    :type data: void \*

.. _`pdc_irq_handler.description`:

Description
-----------

We have to clear the device interrupt status flags here. So cache the
status for later use in the thread function. Other than that, just return
WAKE_THREAD to invoke the thread function.

.. _`pdc_irq_handler.return`:

Return
------

IRQ_WAKE_THREAD if interrupt is ours
IRQ_NONE otherwise

.. _`pdc_tasklet_cb`:

pdc_tasklet_cb
==============

.. c:function:: void pdc_tasklet_cb(unsigned long data)

    Tasklet callback that runs the deferred processing after a DMA receive interrupt. Reenables the receive interrupt.

    :param data:
        PDC state structure
    :type data: unsigned long

.. _`pdc_ring_init`:

pdc_ring_init
=============

.. c:function:: int pdc_ring_init(struct pdc_state *pdcs, int ringset)

    Allocate DMA rings and initialize constant fields of descriptors in one ringset.

    :param pdcs:
        PDC instance state
    :type pdcs: struct pdc_state \*

    :param ringset:
        index of ringset being used
    :type ringset: int

.. _`pdc_ring_init.return`:

Return
------

PDC_SUCCESS if ring initialized
< 0 otherwise

.. _`pdc_desc_count`:

pdc_desc_count
==============

.. c:function:: u32 pdc_desc_count(struct scatterlist *sg)

    Count the number of DMA descriptors that will be required for a given scatterlist. Account for the max length of a DMA buffer.

    :param sg:
        Scatterlist to be DMA'd
    :type sg: struct scatterlist \*

.. _`pdc_desc_count.return`:

Return
------

Number of descriptors required

.. _`pdc_rings_full`:

pdc_rings_full
==============

.. c:function:: bool pdc_rings_full(struct pdc_state *pdcs, int tx_cnt, int rx_cnt)

    Check whether the tx ring has room for tx_cnt descriptors and the rx ring has room for rx_cnt descriptors.

    :param pdcs:
        PDC state
    :type pdcs: struct pdc_state \*

    :param tx_cnt:
        The number of descriptors required in the tx ring
    :type tx_cnt: int

    :param rx_cnt:
        The number of descriptors required i the rx ring
    :type rx_cnt: int

.. _`pdc_rings_full.return`:

Return
------

true if one of the rings does not have enough space
false if sufficient space is available in both rings

.. _`pdc_last_tx_done`:

pdc_last_tx_done
================

.. c:function:: bool pdc_last_tx_done(struct mbox_chan *chan)

    If both the tx and rx rings have at least PDC_RING_SPACE_MIN descriptors available, then indicate that the mailbox framework can submit another message.

    :param chan:
        mailbox channel to check
    :type chan: struct mbox_chan \*

.. _`pdc_last_tx_done.return`:

Return
------

true if PDC can accept another message on this channel

.. _`pdc_send_data`:

pdc_send_data
=============

.. c:function:: int pdc_send_data(struct mbox_chan *chan, void *data)

    mailbox send_data function

    :param chan:
        The mailbox channel on which the data is sent. The channel
        corresponds to a DMA ringset.
    :type chan: struct mbox_chan \*

    :param data:
        The mailbox message to be sent. The message must be a
        brcm_message structure.
    :type data: void \*

.. _`pdc_send_data.description`:

Description
-----------

This function is registered as the send_data function for the mailbox
controller. From the destination scatterlist in the mailbox message, it
creates a sequence of receive descriptors in the rx ring. From the source
scatterlist, it creates a sequence of transmit descriptors in the tx ring.
After creating the descriptors, it writes the rx ptr and tx ptr registers to
initiate the DMA transfer.

This function does the DMA map and unmap of the src and dst scatterlists in
the mailbox message.

.. _`pdc_send_data.return`:

Return
------

0 if successful
-ENOTSUPP if the mailbox message is a type this driver does not
support
< 0 if an error

.. _`pdc_hw_init`:

pdc_hw_init
===========

.. c:function:: void pdc_hw_init(struct pdc_state *pdcs)

    Use the given initialization parameters to initialize the state for one of the PDCs.

    :param pdcs:
        state of the PDC
    :type pdcs: struct pdc_state \*

.. _`pdc_hw_disable`:

pdc_hw_disable
==============

.. c:function:: void pdc_hw_disable(struct pdc_state *pdcs)

    Disable the tx and rx control in the hw.

    :param pdcs:
        PDC state structure
    :type pdcs: struct pdc_state \*

.. _`pdc_rx_buf_pool_create`:

pdc_rx_buf_pool_create
======================

.. c:function:: int pdc_rx_buf_pool_create(struct pdc_state *pdcs)

    Pool of receive buffers used to catch the metadata header returned with each response message.

    :param pdcs:
        PDC state structure
    :type pdcs: struct pdc_state \*

.. _`pdc_rx_buf_pool_create.description`:

Description
-----------

The metadata is not returned to the mailbox client. So the PDC driver
manages these buffers.

.. _`pdc_rx_buf_pool_create.return`:

Return
------

PDC_SUCCESS
-ENOMEM if pool creation fails

.. _`pdc_interrupts_init`:

pdc_interrupts_init
===================

.. c:function:: int pdc_interrupts_init(struct pdc_state *pdcs)

    Initialize the interrupt configuration for a PDC and specify a threaded IRQ handler for deferred handling of interrupts outside of interrupt context.

    :param pdcs:
        PDC state
    :type pdcs: struct pdc_state \*

.. _`pdc_interrupts_init.description`:

Description
-----------

Set the interrupt mask for transmit and receive done.
Set the lazy interrupt frame count to generate an interrupt for just one pkt.

.. _`pdc_interrupts_init.return`:

Return
------

PDC_SUCCESS
<0 if threaded irq request fails

.. _`pdc_mb_init`:

pdc_mb_init
===========

.. c:function:: int pdc_mb_init(struct pdc_state *pdcs)

    Initialize the mailbox controller.

    :param pdcs:
        PDC state
    :type pdcs: struct pdc_state \*

.. _`pdc_mb_init.description`:

Description
-----------

Each PDC is a mailbox controller. Each ringset is a mailbox channel. Kernel
driver only uses one ringset and thus one mb channel. PDC uses the transmit
complete interrupt to determine when a mailbox message has successfully been
transmitted.

.. _`pdc_mb_init.return`:

Return
------

0 on success
< 0 if there is an allocation or registration failure

.. _`pdc_dt_read`:

pdc_dt_read
===========

.. c:function:: int pdc_dt_read(struct platform_device *pdev, struct pdc_state *pdcs)

    Read application-specific data from device tree.

    :param pdev:
        Platform device
    :type pdev: struct platform_device \*

    :param pdcs:
        PDC state
    :type pdcs: struct pdc_state \*

.. _`pdc_dt_read.description`:

Description
-----------

Reads the number of bytes of receive status that precede each received frame.
Reads whether transmit and received frames should be preceded by an 8-byte
BCM header.

.. _`pdc_dt_read.return`:

Return
------

0 if successful
-ENODEV if device not available

.. _`pdc_probe`:

pdc_probe
=========

.. c:function:: int pdc_probe(struct platform_device *pdev)

    Probe function for PDC driver.

    :param pdev:
        PDC platform device
    :type pdev: struct platform_device \*

.. _`pdc_probe.description`:

Description
-----------

Reserve and map register regions defined in device tree.
Allocate and initialize tx and rx DMA rings.
Initialize a mailbox controller for each PDC.

.. _`pdc_probe.return`:

Return
------

0 if successful
< 0 if an error

.. This file was automatic generated / don't edit.

