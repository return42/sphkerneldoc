.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/neterion/vxge/vxge-traffic.c

.. _`vxge_hw_channel_msix_mask`:

vxge_hw_channel_msix_mask
=========================

.. c:function:: void vxge_hw_channel_msix_mask(struct __vxge_hw_channel *channel, int msix_id)

    Mask MSIX Vector.

    :param struct __vxge_hw_channel \*channel:
        *undescribed*

    :param int msix_id:
        MSIX ID

.. _`vxge_hw_channel_msix_mask.description`:

Description
-----------

The function masks the msix interrupt for the given msix_id

.. _`vxge_hw_channel_msix_mask.return`:

Return
------

0

.. _`vxge_hw_channel_msix_unmask`:

vxge_hw_channel_msix_unmask
===========================

.. c:function:: void vxge_hw_channel_msix_unmask(struct __vxge_hw_channel *channel, int msix_id)

    Unmask the MSIX Vector.

    :param struct __vxge_hw_channel \*channel:
        *undescribed*

    :param int msix_id:
        MSI ID

.. _`vxge_hw_channel_msix_unmask.description`:

Description
-----------

The function unmasks the msix interrupt for the given msix_id

.. _`vxge_hw_channel_msix_unmask.return`:

Return
------

0

.. _`vxge_hw_channel_msix_clear`:

vxge_hw_channel_msix_clear
==========================

.. c:function:: void vxge_hw_channel_msix_clear(struct __vxge_hw_channel *channel, int msix_id)

    Unmask the MSIX Vector.

    :param struct __vxge_hw_channel \*channel:
        Channel for rx or tx handle

    :param int msix_id:
        MSI ID

.. _`vxge_hw_channel_msix_clear.description`:

Description
-----------

The function unmasks the msix interrupt for the given msix_id
if configured in MSIX oneshot mode

.. _`vxge_hw_channel_msix_clear.return`:

Return
------

0

.. _`vxge_hw_device_set_intr_type`:

vxge_hw_device_set_intr_type
============================

.. c:function:: u32 vxge_hw_device_set_intr_type(struct __vxge_hw_device *hldev, u32 intr_mode)

    Updates the configuration with new interrupt type.

    :param struct __vxge_hw_device \*hldev:
        HW device handle.

    :param u32 intr_mode:
        New interrupt type

.. _`vxge_hw_device_intr_enable`:

vxge_hw_device_intr_enable
==========================

.. c:function:: void vxge_hw_device_intr_enable(struct __vxge_hw_device *hldev)

    Enable interrupts.

    :param struct __vxge_hw_device \*hldev:
        HW device handle.

.. _`vxge_hw_device_intr_enable.description`:

Description
-----------

Enable Titan interrupts. The function is to be executed the last in
Titan initialization sequence.

.. _`vxge_hw_device_intr_enable.see-also`:

See also
--------

vxge_hw_device_intr_disable()

.. _`vxge_hw_device_intr_disable`:

vxge_hw_device_intr_disable
===========================

.. c:function:: void vxge_hw_device_intr_disable(struct __vxge_hw_device *hldev)

    Disable Titan interrupts.

    :param struct __vxge_hw_device \*hldev:
        HW device handle.

.. _`vxge_hw_device_intr_disable.description`:

Description
-----------

Disable Titan interrupts.

.. _`vxge_hw_device_intr_disable.see-also`:

See also
--------

vxge_hw_device_intr_enable()

.. _`vxge_hw_device_mask_all`:

vxge_hw_device_mask_all
=======================

.. c:function:: void vxge_hw_device_mask_all(struct __vxge_hw_device *hldev)

    Mask all device interrupts.

    :param struct __vxge_hw_device \*hldev:
        HW device handle.

.. _`vxge_hw_device_mask_all.description`:

Description
-----------

Mask all device interrupts.

.. _`vxge_hw_device_mask_all.see-also`:

See also
--------

vxge_hw_device_unmask_all()

.. _`vxge_hw_device_unmask_all`:

vxge_hw_device_unmask_all
=========================

.. c:function:: void vxge_hw_device_unmask_all(struct __vxge_hw_device *hldev)

    Unmask all device interrupts.

    :param struct __vxge_hw_device \*hldev:
        HW device handle.

.. _`vxge_hw_device_unmask_all.description`:

Description
-----------

Unmask all device interrupts.

.. _`vxge_hw_device_unmask_all.see-also`:

See also
--------

vxge_hw_device_mask_all()

.. _`vxge_hw_device_flush_io`:

vxge_hw_device_flush_io
=======================

.. c:function:: void vxge_hw_device_flush_io(struct __vxge_hw_device *hldev)

    Flush io writes.

    :param struct __vxge_hw_device \*hldev:
        HW device handle.

.. _`vxge_hw_device_flush_io.description`:

Description
-----------

The function performs a read operation to flush io writes.

.. _`vxge_hw_device_flush_io.return`:

Return
------

void

.. _`__vxge_hw_device_handle_error`:

__vxge_hw_device_handle_error
=============================

.. c:function:: enum vxge_hw_status __vxge_hw_device_handle_error(struct __vxge_hw_device *hldev, u32 vp_id, enum vxge_hw_event type)

    Handle error

    :param struct __vxge_hw_device \*hldev:
        HW device

    :param u32 vp_id:
        Vpath Id

    :param enum vxge_hw_event type:
        Error type. Please see enum vxge_hw_event{}

.. _`__vxge_hw_device_handle_error.description`:

Description
-----------

Handle error.

.. _`vxge_hw_device_begin_irq`:

vxge_hw_device_begin_irq
========================

.. c:function:: enum vxge_hw_status vxge_hw_device_begin_irq(struct __vxge_hw_device *hldev, u32 skip_alarms, u64 *reason)

    Begin IRQ processing.

    :param struct __vxge_hw_device \*hldev:
        HW device handle.

    :param u32 skip_alarms:
        Do not clear the alarms

    :param u64 \*reason:
        "Reason" for the interrupt, the value of Titan's
        general_int_status register.

.. _`vxge_hw_device_begin_irq.description`:

Description
-----------

The function performs two actions, It first checks whether (shared IRQ) the
interrupt was raised by the device. Next, it masks the device interrupts.

.. _`vxge_hw_device_begin_irq.note`:

Note
----

vxge_hw_device_begin_irq() does not flush MMIO writes through the
bridge. Therefore, two back-to-back interrupts are potentially possible.

.. _`vxge_hw_device_begin_irq.return`:

Return
------

0, if the interrupt is not "ours" (note that in this case the
device remain enabled).
Otherwise, \ :c:func:`vxge_hw_device_begin_irq`\  returns 64bit general adapter
status.

.. _`vxge_hw_device_clear_tx_rx`:

vxge_hw_device_clear_tx_rx
==========================

.. c:function:: void vxge_hw_device_clear_tx_rx(struct __vxge_hw_device *hldev)

    Acknowledge (that is, clear) the condition that has caused the Tx and RX interrupt.

    :param struct __vxge_hw_device \*hldev:
        HW device.

.. _`vxge_hw_device_clear_tx_rx.description`:

Description
-----------

Acknowledge (that is, clear) the condition that has caused
the Tx and Rx interrupt.

.. _`vxge_hw_device_clear_tx_rx.see-also`:

See also
--------

vxge_hw_device_begin_irq(),
\ :c:func:`vxge_hw_device_mask_tx_rx`\ , \ :c:func:`vxge_hw_device_unmask_tx_rx`\ .

.. _`vxge_hw_ring_rxd_reserve`:

vxge_hw_ring_rxd_reserve
========================

.. c:function:: enum vxge_hw_status vxge_hw_ring_rxd_reserve(struct __vxge_hw_ring *ring, void **rxdh)

    Reserve ring descriptor.

    :param struct __vxge_hw_ring \*ring:
        Handle to the ring object used for receive

    :param void \*\*rxdh:
        Reserved descriptor. On success HW fills this "out" parameter
        with a valid handle.

.. _`vxge_hw_ring_rxd_reserve.description`:

Description
-----------

Reserve Rx descriptor for the subsequent filling-in driver
and posting on the corresponding channel (@channelh)
via \ :c:func:`vxge_hw_ring_rxd_post`\ .

.. _`vxge_hw_ring_rxd_reserve.return`:

Return
------

VXGE_HW_OK - success.
VXGE_HW_INF_OUT_OF_DESCRIPTORS - Currently no descriptors available.

.. _`vxge_hw_ring_rxd_free`:

vxge_hw_ring_rxd_free
=====================

.. c:function:: void vxge_hw_ring_rxd_free(struct __vxge_hw_ring *ring, void *rxdh)

    Free descriptor.

    :param struct __vxge_hw_ring \*ring:
        Handle to the ring object used for receive

    :param void \*rxdh:
        Descriptor handle.

.. _`vxge_hw_ring_rxd_free.description`:

Description
-----------

Free the reserved descriptor. This operation is "symmetrical" to
vxge_hw_ring_rxd_reserve. The "free-ing" completes the descriptor's
lifecycle.

After free-ing (see \ :c:func:`vxge_hw_ring_rxd_free`\ ) the descriptor again can
be:

- reserved (vxge_hw_ring_rxd_reserve);

- posted     (vxge_hw_ring_rxd_post);

- completed (vxge_hw_ring_rxd_next_completed);

- and recycled again (vxge_hw_ring_rxd_free).

For alternative state transitions and more details please refer to
the design doc.

.. _`vxge_hw_ring_rxd_pre_post`:

vxge_hw_ring_rxd_pre_post
=========================

.. c:function:: void vxge_hw_ring_rxd_pre_post(struct __vxge_hw_ring *ring, void *rxdh)

    Prepare rxd and post

    :param struct __vxge_hw_ring \*ring:
        Handle to the ring object used for receive

    :param void \*rxdh:
        Descriptor handle.

.. _`vxge_hw_ring_rxd_pre_post.description`:

Description
-----------

This routine prepares a rxd and posts

.. _`vxge_hw_ring_rxd_post_post`:

vxge_hw_ring_rxd_post_post
==========================

.. c:function:: void vxge_hw_ring_rxd_post_post(struct __vxge_hw_ring *ring, void *rxdh)

    Process rxd after post.

    :param struct __vxge_hw_ring \*ring:
        Handle to the ring object used for receive

    :param void \*rxdh:
        Descriptor handle.

.. _`vxge_hw_ring_rxd_post_post.description`:

Description
-----------

Processes rxd after post

.. _`vxge_hw_ring_rxd_post`:

vxge_hw_ring_rxd_post
=====================

.. c:function:: void vxge_hw_ring_rxd_post(struct __vxge_hw_ring *ring, void *rxdh)

    Post descriptor on the ring.

    :param struct __vxge_hw_ring \*ring:
        Handle to the ring object used for receive

    :param void \*rxdh:
        Descriptor obtained via \ :c:func:`vxge_hw_ring_rxd_reserve`\ .

.. _`vxge_hw_ring_rxd_post.description`:

Description
-----------

Post descriptor on the ring.
Prior to posting the descriptor should be filled in accordance with
Host/Titan interface specification for a given service (LL, etc.).

.. _`vxge_hw_ring_rxd_post_post_wmb`:

vxge_hw_ring_rxd_post_post_wmb
==============================

.. c:function:: void vxge_hw_ring_rxd_post_post_wmb(struct __vxge_hw_ring *ring, void *rxdh)

    Process rxd after post with memory barrier.

    :param struct __vxge_hw_ring \*ring:
        Handle to the ring object used for receive

    :param void \*rxdh:
        Descriptor handle.

.. _`vxge_hw_ring_rxd_post_post_wmb.description`:

Description
-----------

Processes rxd after post with memory barrier.

.. _`vxge_hw_ring_rxd_next_completed`:

vxge_hw_ring_rxd_next_completed
===============================

.. c:function:: enum vxge_hw_status vxge_hw_ring_rxd_next_completed(struct __vxge_hw_ring *ring, void **rxdh, u8 *t_code)

    Get the \_next\_ completed descriptor.

    :param struct __vxge_hw_ring \*ring:
        Handle to the ring object used for receive

    :param void \*\*rxdh:
        Descriptor handle. Returned by HW.

    :param u8 \*t_code:
        Transfer code, as per Titan User Guide,
        Receive Descriptor Format. Returned by HW.

.. _`vxge_hw_ring_rxd_next_completed.description`:

Description
-----------

Retrieve the \_next\_ completed descriptor.
HW uses ring callback (\*vxge_hw_ring_callback_f) to notifiy
driver of new completed descriptors. After that
the driver can use vxge_hw_ring_rxd_next_completed to retrieve the rest
completions (the very first completion is passed by HW via
vxge_hw_ring_callback_f).

Implementation-wise, the driver is free to call
vxge_hw_ring_rxd_next_completed either immediately from inside the
ring callback, or in a deferred fashion and separate (from HW)
context.

Non-zero \ ``t_code``\  means failure to fill-in receive buffer(s)
of the descriptor.
For instance, parity error detected during the data transfer.
In this case Titan will complete the descriptor and indicate
for the host that the received data is not to be used.
For details please refer to Titan User Guide.

.. _`vxge_hw_ring_rxd_next_completed.return`:

Return
------

VXGE_HW_OK - success.
VXGE_HW_INF_NO_MORE_COMPLETED_DESCRIPTORS - No completed descriptors
are currently available for processing.

.. _`vxge_hw_ring_rxd_next_completed.see-also`:

See also
--------

vxge_hw_ring_callback_f{},
\ :c:func:`vxge_hw_fifo_rxd_next_completed`\ , enum vxge_hw_status{}.

.. _`vxge_hw_ring_handle_tcode`:

vxge_hw_ring_handle_tcode
=========================

.. c:function:: enum vxge_hw_status vxge_hw_ring_handle_tcode(struct __vxge_hw_ring *ring, void *rxdh, u8 t_code)

    Handle transfer code.

    :param struct __vxge_hw_ring \*ring:
        Handle to the ring object used for receive

    :param void \*rxdh:
        Descriptor handle.

    :param u8 t_code:
        One of the enumerated (and documented in the Titan user guide)
        "transfer codes".

.. _`vxge_hw_ring_handle_tcode.description`:

Description
-----------

Handle descriptor's transfer code. The latter comes with each completed
descriptor.

.. _`vxge_hw_ring_handle_tcode.return`:

Return
------

one of the enum vxge_hw_status{} enumerated types.
VXGE_HW_OK                   - for success.
VXGE_HW_ERR_CRITICAL         - when encounters critical error.

.. _`__vxge_hw_non_offload_db_post`:

__vxge_hw_non_offload_db_post
=============================

.. c:function:: void __vxge_hw_non_offload_db_post(struct __vxge_hw_fifo *fifo, u64 txdl_ptr, u32 num_txds, u32 no_snoop)

    Post non offload doorbell

    :param struct __vxge_hw_fifo \*fifo:
        fifohandle

    :param u64 txdl_ptr:
        The starting location of the TxDL in host memory

    :param u32 num_txds:
        The highest TxD in this TxDL (0 to 255 means 1 to 256)

    :param u32 no_snoop:
        No snoop flags

.. _`__vxge_hw_non_offload_db_post.description`:

Description
-----------

This function posts a non-offload doorbell to doorbell FIFO

.. _`vxge_hw_fifo_free_txdl_count_get`:

vxge_hw_fifo_free_txdl_count_get
================================

.. c:function:: u32 vxge_hw_fifo_free_txdl_count_get(struct __vxge_hw_fifo *fifoh)

    returns the number of txdls available in the fifo

    :param struct __vxge_hw_fifo \*fifoh:
        Handle to the fifo object used for non offload send

.. _`vxge_hw_fifo_txdl_reserve`:

vxge_hw_fifo_txdl_reserve
=========================

.. c:function:: enum vxge_hw_status vxge_hw_fifo_txdl_reserve(struct __vxge_hw_fifo *fifo, void **txdlh, void **txdl_priv)

    Reserve fifo descriptor.

    :param struct __vxge_hw_fifo \*fifo:
        *undescribed*

    :param void \*\*txdlh:
        Reserved descriptor. On success HW fills this "out" parameter
        with a valid handle.

    :param void \*\*txdl_priv:
        Buffer to return the pointer to per txdl space

.. _`vxge_hw_fifo_txdl_reserve.description`:

Description
-----------

Reserve a single TxDL (that is, fifo descriptor)
for the subsequent filling-in by driver)
and posting on the corresponding channel (@channelh)
via \ :c:func:`vxge_hw_fifo_txdl_post`\ .

.. _`vxge_hw_fifo_txdl_reserve.note`:

Note
----

it is the responsibility of driver to reserve multiple descriptors
for lengthy (e.g., LSO) transmit operation. A single fifo descriptor
carries up to configured number (fifo.max_frags) of contiguous buffers.

.. _`vxge_hw_fifo_txdl_reserve.return`:

Return
------

VXGE_HW_OK - success;
VXGE_HW_INF_OUT_OF_DESCRIPTORS - Currently no descriptors available

.. _`vxge_hw_fifo_txdl_buffer_set`:

vxge_hw_fifo_txdl_buffer_set
============================

.. c:function:: void vxge_hw_fifo_txdl_buffer_set(struct __vxge_hw_fifo *fifo, void *txdlh, u32 frag_idx, dma_addr_t dma_pointer, u32 size)

    Set transmit buffer pointer in the descriptor.

    :param struct __vxge_hw_fifo \*fifo:
        Handle to the fifo object used for non offload send

    :param void \*txdlh:
        Descriptor handle.

    :param u32 frag_idx:
        Index of the data buffer in the caller's scatter-gather list
        (of buffers).

    :param dma_addr_t dma_pointer:
        DMA address of the data buffer referenced by \ ``frag_idx``\ .

    :param u32 size:
        Size of the data buffer (in bytes).

.. _`vxge_hw_fifo_txdl_buffer_set.description`:

Description
-----------

This API is part of the preparation of the transmit descriptor for posting
(via \ :c:func:`vxge_hw_fifo_txdl_post`\ ). The related "preparation" APIs include
\ :c:func:`vxge_hw_fifo_txdl_mss_set`\  and \ :c:func:`vxge_hw_fifo_txdl_cksum_set_bits`\ .
All three APIs fill in the fields of the fifo descriptor,
in accordance with the Titan specification.

.. _`vxge_hw_fifo_txdl_post`:

vxge_hw_fifo_txdl_post
======================

.. c:function:: void vxge_hw_fifo_txdl_post(struct __vxge_hw_fifo *fifo, void *txdlh)

    Post descriptor on the fifo channel.

    :param struct __vxge_hw_fifo \*fifo:
        Handle to the fifo object used for non offload send

    :param void \*txdlh:
        Descriptor obtained via \ :c:func:`vxge_hw_fifo_txdl_reserve`\ 

.. _`vxge_hw_fifo_txdl_post.description`:

Description
-----------

Post descriptor on the 'fifo' type channel for transmission.
Prior to posting the descriptor should be filled in accordance with
Host/Titan interface specification for a given service (LL, etc.).

.. _`vxge_hw_fifo_txdl_next_completed`:

vxge_hw_fifo_txdl_next_completed
================================

.. c:function:: enum vxge_hw_status vxge_hw_fifo_txdl_next_completed(struct __vxge_hw_fifo *fifo, void **txdlh, enum vxge_hw_fifo_tcode *t_code)

    Retrieve next completed descriptor.

    :param struct __vxge_hw_fifo \*fifo:
        Handle to the fifo object used for non offload send

    :param void \*\*txdlh:
        Descriptor handle. Returned by HW.

    :param enum vxge_hw_fifo_tcode \*t_code:
        Transfer code, as per Titan User Guide,
        Transmit Descriptor Format.
        Returned by HW.

.. _`vxge_hw_fifo_txdl_next_completed.description`:

Description
-----------

Retrieve the \_next\_ completed descriptor.
HW uses channel callback (\*vxge_hw_channel_callback_f) to notifiy
driver of new completed descriptors. After that
the driver can use vxge_hw_fifo_txdl_next_completed to retrieve the rest
completions (the very first completion is passed by HW via
vxge_hw_channel_callback_f).

Implementation-wise, the driver is free to call
vxge_hw_fifo_txdl_next_completed either immediately from inside the
channel callback, or in a deferred fashion and separate (from HW)
context.

Non-zero \ ``t_code``\  means failure to process the descriptor.
The failure could happen, for instance, when the link is
down, in which case Titan completes the descriptor because it
is not able to send the data out.

For details please refer to Titan User Guide.

.. _`vxge_hw_fifo_txdl_next_completed.return`:

Return
------

VXGE_HW_OK - success.
VXGE_HW_INF_NO_MORE_COMPLETED_DESCRIPTORS - No completed descriptors
are currently available for processing.

.. _`vxge_hw_fifo_handle_tcode`:

vxge_hw_fifo_handle_tcode
=========================

.. c:function:: enum vxge_hw_status vxge_hw_fifo_handle_tcode(struct __vxge_hw_fifo *fifo, void *txdlh, enum vxge_hw_fifo_tcode t_code)

    Handle transfer code.

    :param struct __vxge_hw_fifo \*fifo:
        Handle to the fifo object used for non offload send

    :param void \*txdlh:
        Descriptor handle.

    :param enum vxge_hw_fifo_tcode t_code:
        One of the enumerated (and documented in the Titan user guide)
        "transfer codes".

.. _`vxge_hw_fifo_handle_tcode.description`:

Description
-----------

Handle descriptor's transfer code. The latter comes with each completed
descriptor.

.. _`vxge_hw_fifo_handle_tcode.return`:

Return
------

one of the enum vxge_hw_status{} enumerated types.
VXGE_HW_OK - for success.
VXGE_HW_ERR_CRITICAL - when encounters critical error.

.. _`vxge_hw_fifo_txdl_free`:

vxge_hw_fifo_txdl_free
======================

.. c:function:: void vxge_hw_fifo_txdl_free(struct __vxge_hw_fifo *fifo, void *txdlh)

    Free descriptor.

    :param struct __vxge_hw_fifo \*fifo:
        Handle to the fifo object used for non offload send

    :param void \*txdlh:
        Descriptor handle.

.. _`vxge_hw_fifo_txdl_free.description`:

Description
-----------

Free the reserved descriptor. This operation is "symmetrical" to
vxge_hw_fifo_txdl_reserve. The "free-ing" completes the descriptor's
lifecycle.

After free-ing (see \ :c:func:`vxge_hw_fifo_txdl_free`\ ) the descriptor again can
be:

- reserved (vxge_hw_fifo_txdl_reserve);

- posted (vxge_hw_fifo_txdl_post);

- completed (vxge_hw_fifo_txdl_next_completed);

- and recycled again (vxge_hw_fifo_txdl_free).

For alternative state transitions and more details please refer to
the design doc.

.. _`vxge_hw_vpath_mac_addr_add`:

vxge_hw_vpath_mac_addr_add
==========================

.. c:function:: enum vxge_hw_status vxge_hw_vpath_mac_addr_add(struct __vxge_hw_vpath_handle *vp, u8 macaddr, u8 macaddr_mask, enum vxge_hw_vpath_mac_addr_add_mode duplicate_mode)

    Add the mac address entry for this vpath to MAC address table.

    :param struct __vxge_hw_vpath_handle \*vp:
        Vpath handle.

    :param u8 macaddr:
        MAC address to be added for this vpath into the list

    :param u8 macaddr_mask:
        MAC address mask for macaddr

    :param enum vxge_hw_vpath_mac_addr_add_mode duplicate_mode:
        Duplicate MAC address add mode. Please see
        enum vxge_hw_vpath_mac_addr_add_mode{}

.. _`vxge_hw_vpath_mac_addr_add.description`:

Description
-----------

Adds the given mac address and mac address mask into the list for this
vpath.

.. _`vxge_hw_vpath_mac_addr_add.see-also`:

see also
--------

vxge_hw_vpath_mac_addr_delete, vxge_hw_vpath_mac_addr_get and
vxge_hw_vpath_mac_addr_get_next

.. _`vxge_hw_vpath_mac_addr_get`:

vxge_hw_vpath_mac_addr_get
==========================

.. c:function:: enum vxge_hw_status vxge_hw_vpath_mac_addr_get(struct __vxge_hw_vpath_handle *vp, u8 macaddr, u8 macaddr_mask)

    Get the first mac address entry for this vpath from MAC address table.

    :param struct __vxge_hw_vpath_handle \*vp:
        Vpath handle.

    :param u8 macaddr:
        First MAC address entry for this vpath in the list

    :param u8 macaddr_mask:
        MAC address mask for macaddr

.. _`vxge_hw_vpath_mac_addr_get.description`:

Description
-----------

Returns the first mac address and mac address mask in the list for this
vpath.

.. _`vxge_hw_vpath_mac_addr_get.see-also`:

see also
--------

vxge_hw_vpath_mac_addr_get_next

.. _`vxge_hw_vpath_mac_addr_get_next`:

vxge_hw_vpath_mac_addr_get_next
===============================

.. c:function:: enum vxge_hw_status vxge_hw_vpath_mac_addr_get_next(struct __vxge_hw_vpath_handle *vp, u8 macaddr, u8 macaddr_mask)

    Get the next mac address entry for this vpath from MAC address table.

    :param struct __vxge_hw_vpath_handle \*vp:
        Vpath handle.

    :param u8 macaddr:
        Next MAC address entry for this vpath in the list

    :param u8 macaddr_mask:
        MAC address mask for macaddr

.. _`vxge_hw_vpath_mac_addr_get_next.description`:

Description
-----------

Returns the next mac address and mac address mask in the list for this
vpath.

.. _`vxge_hw_vpath_mac_addr_get_next.see-also`:

see also
--------

vxge_hw_vpath_mac_addr_get

.. _`vxge_hw_vpath_mac_addr_delete`:

vxge_hw_vpath_mac_addr_delete
=============================

.. c:function:: enum vxge_hw_status vxge_hw_vpath_mac_addr_delete(struct __vxge_hw_vpath_handle *vp, u8 macaddr, u8 macaddr_mask)

    Delete the mac address entry for this vpath to MAC address table.

    :param struct __vxge_hw_vpath_handle \*vp:
        Vpath handle.

    :param u8 macaddr:
        MAC address to be added for this vpath into the list

    :param u8 macaddr_mask:
        MAC address mask for macaddr

.. _`vxge_hw_vpath_mac_addr_delete.description`:

Description
-----------

Delete the given mac address and mac address mask into the list for this
vpath.

.. _`vxge_hw_vpath_mac_addr_delete.see-also`:

see also
--------

vxge_hw_vpath_mac_addr_add, vxge_hw_vpath_mac_addr_get and
vxge_hw_vpath_mac_addr_get_next

.. _`vxge_hw_vpath_vid_add`:

vxge_hw_vpath_vid_add
=====================

.. c:function:: enum vxge_hw_status vxge_hw_vpath_vid_add(struct __vxge_hw_vpath_handle *vp, u64 vid)

    Add the vlan id entry for this vpath to vlan id table.

    :param struct __vxge_hw_vpath_handle \*vp:
        Vpath handle.

    :param u64 vid:
        vlan id to be added for this vpath into the list

.. _`vxge_hw_vpath_vid_add.description`:

Description
-----------

Adds the given vlan id into the list for this  vpath.

.. _`vxge_hw_vpath_vid_add.see-also`:

see also
--------

vxge_hw_vpath_vid_delete

.. _`vxge_hw_vpath_vid_delete`:

vxge_hw_vpath_vid_delete
========================

.. c:function:: enum vxge_hw_status vxge_hw_vpath_vid_delete(struct __vxge_hw_vpath_handle *vp, u64 vid)

    Delete the vlan id entry for this vpath to vlan id table.

    :param struct __vxge_hw_vpath_handle \*vp:
        Vpath handle.

    :param u64 vid:
        vlan id to be added for this vpath into the list

.. _`vxge_hw_vpath_vid_delete.description`:

Description
-----------

Adds the given vlan id into the list for this  vpath.

.. _`vxge_hw_vpath_vid_delete.see-also`:

see also
--------

vxge_hw_vpath_vid_add

.. _`vxge_hw_vpath_promisc_enable`:

vxge_hw_vpath_promisc_enable
============================

.. c:function:: enum vxge_hw_status vxge_hw_vpath_promisc_enable(struct __vxge_hw_vpath_handle *vp)

    Enable promiscuous mode.

    :param struct __vxge_hw_vpath_handle \*vp:
        Vpath handle.

.. _`vxge_hw_vpath_promisc_enable.description`:

Description
-----------

Enable promiscuous mode of Titan-e operation.

.. _`vxge_hw_vpath_promisc_enable.see-also`:

See also
--------

vxge_hw_vpath_promisc_disable().

.. _`vxge_hw_vpath_promisc_disable`:

vxge_hw_vpath_promisc_disable
=============================

.. c:function:: enum vxge_hw_status vxge_hw_vpath_promisc_disable(struct __vxge_hw_vpath_handle *vp)

    Disable promiscuous mode.

    :param struct __vxge_hw_vpath_handle \*vp:
        Vpath handle.

.. _`vxge_hw_vpath_promisc_disable.description`:

Description
-----------

Disable promiscuous mode of Titan-e operation.

.. _`vxge_hw_vpath_promisc_disable.see-also`:

See also
--------

vxge_hw_vpath_promisc_enable().

.. _`vxge_hw_vpath_mcast_enable`:

vxge_hw_vpath_mcast_enable
==========================

.. c:function:: enum vxge_hw_status vxge_hw_vpath_mcast_enable(struct __vxge_hw_vpath_handle *vp)

    Enable multicast addresses.

    :param struct __vxge_hw_vpath_handle \*vp:
        Vpath handle.

.. _`vxge_hw_vpath_mcast_enable.description`:

Description
-----------

Enable Titan-e multicast addresses.

.. _`vxge_hw_vpath_mcast_enable.return`:

Return
------

VXGE_HW_OK on success.

.. _`vxge_hw_vpath_mcast_disable`:

vxge_hw_vpath_mcast_disable
===========================

.. c:function:: enum vxge_hw_status vxge_hw_vpath_mcast_disable(struct __vxge_hw_vpath_handle *vp)

    Disable  multicast addresses.

    :param struct __vxge_hw_vpath_handle \*vp:
        Vpath handle.

.. _`vxge_hw_vpath_mcast_disable.description`:

Description
-----------

Disable Titan-e multicast addresses.

.. _`vxge_hw_vpath_mcast_disable.return`:

Return
------

VXGE_HW_OK - success.
VXGE_HW_ERR_INVALID_HANDLE - Invalid handle

.. _`vxge_hw_vpath_msix_set`:

vxge_hw_vpath_msix_set
======================

.. c:function:: void vxge_hw_vpath_msix_set(struct __vxge_hw_vpath_handle *vp, int *tim_msix_id, int alarm_msix_id)

    Associate MSIX vectors with TIM interrupts and alrms

    :param struct __vxge_hw_vpath_handle \*vp:
        Virtual Path handle.

    :param int \*tim_msix_id:
        MSIX vectors associated with VXGE_HW_MAX_INTR_PER_VP number of
        interrupts(Can be repeated). If fifo or ring are not enabled
        the MSIX vector for that should be set to 0

    :param int alarm_msix_id:
        MSIX vector for alarm.

.. _`vxge_hw_vpath_msix_set.description`:

Description
-----------

This API will associate a given MSIX vector numbers with the four TIM
interrupts and alarm interrupt.

.. _`vxge_hw_vpath_msix_mask`:

vxge_hw_vpath_msix_mask
=======================

.. c:function:: void vxge_hw_vpath_msix_mask(struct __vxge_hw_vpath_handle *vp, int msix_id)

    Mask MSIX Vector.

    :param struct __vxge_hw_vpath_handle \*vp:
        Virtual Path handle.

    :param int msix_id:
        MSIX ID

.. _`vxge_hw_vpath_msix_mask.description`:

Description
-----------

The function masks the msix interrupt for the given msix_id

.. _`vxge_hw_vpath_msix_mask.return`:

Return
------

0,
Otherwise, VXGE_HW_ERR_WRONG_IRQ if the msix index is out of range
status.

.. _`vxge_hw_vpath_msix_clear`:

vxge_hw_vpath_msix_clear
========================

.. c:function:: void vxge_hw_vpath_msix_clear(struct __vxge_hw_vpath_handle *vp, int msix_id)

    Clear MSIX Vector.

    :param struct __vxge_hw_vpath_handle \*vp:
        Virtual Path handle.

    :param int msix_id:
        MSI ID

.. _`vxge_hw_vpath_msix_clear.description`:

Description
-----------

The function clears the msix interrupt for the given msix_id

.. _`vxge_hw_vpath_msix_clear.return`:

Return
------

0,
Otherwise, VXGE_HW_ERR_WRONG_IRQ if the msix index is out of range
status.

.. _`vxge_hw_vpath_msix_unmask`:

vxge_hw_vpath_msix_unmask
=========================

.. c:function:: void vxge_hw_vpath_msix_unmask(struct __vxge_hw_vpath_handle *vp, int msix_id)

    Unmask the MSIX Vector.

    :param struct __vxge_hw_vpath_handle \*vp:
        Virtual Path handle.

    :param int msix_id:
        MSI ID

.. _`vxge_hw_vpath_msix_unmask.description`:

Description
-----------

The function unmasks the msix interrupt for the given msix_id

.. _`vxge_hw_vpath_msix_unmask.return`:

Return
------

0,
Otherwise, VXGE_HW_ERR_WRONG_IRQ if the msix index is out of range
status.

.. _`vxge_hw_vpath_inta_mask_tx_rx`:

vxge_hw_vpath_inta_mask_tx_rx
=============================

.. c:function:: void vxge_hw_vpath_inta_mask_tx_rx(struct __vxge_hw_vpath_handle *vp)

    Mask Tx and Rx interrupts.

    :param struct __vxge_hw_vpath_handle \*vp:
        Virtual Path handle.

.. _`vxge_hw_vpath_inta_mask_tx_rx.description`:

Description
-----------

Mask Tx and Rx vpath interrupts.

.. _`vxge_hw_vpath_inta_mask_tx_rx.see-also`:

See also
--------

vxge_hw_vpath_inta_mask_tx_rx()

.. _`vxge_hw_vpath_inta_unmask_tx_rx`:

vxge_hw_vpath_inta_unmask_tx_rx
===============================

.. c:function:: void vxge_hw_vpath_inta_unmask_tx_rx(struct __vxge_hw_vpath_handle *vp)

    Unmask Tx and Rx interrupts.

    :param struct __vxge_hw_vpath_handle \*vp:
        Virtual Path handle.

.. _`vxge_hw_vpath_inta_unmask_tx_rx.description`:

Description
-----------

Unmask Tx and Rx vpath interrupts.

.. _`vxge_hw_vpath_inta_unmask_tx_rx.see-also`:

See also
--------

vxge_hw_vpath_inta_mask_tx_rx()

.. _`vxge_hw_vpath_poll_rx`:

vxge_hw_vpath_poll_rx
=====================

.. c:function:: enum vxge_hw_status vxge_hw_vpath_poll_rx(struct __vxge_hw_ring *ring)

    Poll Rx Virtual Path for completed descriptors and process the same.

    :param struct __vxge_hw_ring \*ring:
        Handle to the ring object used for receive

.. _`vxge_hw_vpath_poll_rx.description`:

Description
-----------

The function polls the Rx for the completed  descriptors and calls
the driver via supplied completion   callback.

.. _`vxge_hw_vpath_poll_rx.return`:

Return
------

VXGE_HW_OK, if the polling is completed successful.

.. _`vxge_hw_vpath_poll_rx.vxge_hw_completions_remain`:

VXGE_HW_COMPLETIONS_REMAIN
--------------------------

There are still more completed
descriptors available which are yet to be processed.

.. _`vxge_hw_vpath_poll_rx.see-also`:

See also
--------

vxge_hw_vpath_poll_rx()

.. _`vxge_hw_vpath_poll_tx`:

vxge_hw_vpath_poll_tx
=====================

.. c:function:: enum vxge_hw_status vxge_hw_vpath_poll_tx(struct __vxge_hw_fifo *fifo, struct sk_buff ***skb_ptr, int nr_skb, int *more)

    Poll Tx for completed descriptors and process the same.

    :param struct __vxge_hw_fifo \*fifo:
        Handle to the fifo object used for non offload send

    :param struct sk_buff \*\*\*skb_ptr:
        *undescribed*

    :param int nr_skb:
        *undescribed*

    :param int \*more:
        *undescribed*

.. _`vxge_hw_vpath_poll_tx.description`:

Description
-----------

The function polls the Tx for the completed descriptors and calls
the driver via supplied completion callback.

.. _`vxge_hw_vpath_poll_tx.return`:

Return
------

VXGE_HW_OK, if the polling is completed successful.

.. _`vxge_hw_vpath_poll_tx.vxge_hw_completions_remain`:

VXGE_HW_COMPLETIONS_REMAIN
--------------------------

There are still more completed
descriptors available which are yet to be processed.

.. This file was automatic generated / don't edit.

