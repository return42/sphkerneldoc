.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_xsk.c

.. _`i40e_alloc_xsk_umems`:

i40e_alloc_xsk_umems
====================

.. c:function:: int i40e_alloc_xsk_umems(struct i40e_vsi *vsi)

    Allocate an array to store per ring UMEMs

    :param vsi:
        Current VSI
    :type vsi: struct i40e_vsi \*

.. _`i40e_alloc_xsk_umems.description`:

Description
-----------

Returns 0 on success, <0 on failure

.. _`i40e_add_xsk_umem`:

i40e_add_xsk_umem
=================

.. c:function:: int i40e_add_xsk_umem(struct i40e_vsi *vsi, struct xdp_umem *umem, u16 qid)

    Store an UMEM for a certain ring/qid

    :param vsi:
        Current VSI
    :type vsi: struct i40e_vsi \*

    :param umem:
        UMEM to store
    :type umem: struct xdp_umem \*

    :param qid:
        Ring/qid to associate with the UMEM
    :type qid: u16

.. _`i40e_add_xsk_umem.description`:

Description
-----------

Returns 0 on success, <0 on failure

.. _`i40e_remove_xsk_umem`:

i40e_remove_xsk_umem
====================

.. c:function:: void i40e_remove_xsk_umem(struct i40e_vsi *vsi, u16 qid)

    Remove an UMEM for a certain ring/qid

    :param vsi:
        Current VSI
    :type vsi: struct i40e_vsi \*

    :param qid:
        Ring/qid associated with the UMEM
    :type qid: u16

.. _`i40e_xsk_umem_dma_map`:

i40e_xsk_umem_dma_map
=====================

.. c:function:: int i40e_xsk_umem_dma_map(struct i40e_vsi *vsi, struct xdp_umem *umem)

    DMA maps all UMEM memory for the netdev

    :param vsi:
        Current VSI
    :type vsi: struct i40e_vsi \*

    :param umem:
        UMEM to DMA map
    :type umem: struct xdp_umem \*

.. _`i40e_xsk_umem_dma_map.description`:

Description
-----------

Returns 0 on success, <0 on failure

.. _`i40e_xsk_umem_dma_unmap`:

i40e_xsk_umem_dma_unmap
=======================

.. c:function:: void i40e_xsk_umem_dma_unmap(struct i40e_vsi *vsi, struct xdp_umem *umem)

    DMA unmaps all UMEM memory for the netdev

    :param vsi:
        Current VSI
    :type vsi: struct i40e_vsi \*

    :param umem:
        UMEM to DMA map
    :type umem: struct xdp_umem \*

.. _`i40e_xsk_umem_enable`:

i40e_xsk_umem_enable
====================

.. c:function:: int i40e_xsk_umem_enable(struct i40e_vsi *vsi, struct xdp_umem *umem, u16 qid)

    Enable/associate an UMEM to a certain ring/qid

    :param vsi:
        Current VSI
    :type vsi: struct i40e_vsi \*

    :param umem:
        UMEM
    :type umem: struct xdp_umem \*

    :param qid:
        Rx ring to associate UMEM to
    :type qid: u16

.. _`i40e_xsk_umem_enable.description`:

Description
-----------

Returns 0 on success, <0 on failure

.. _`i40e_xsk_umem_disable`:

i40e_xsk_umem_disable
=====================

.. c:function:: int i40e_xsk_umem_disable(struct i40e_vsi *vsi, u16 qid)

    Diassociate an UMEM from a certain ring/qid

    :param vsi:
        Current VSI
    :type vsi: struct i40e_vsi \*

    :param qid:
        Rx ring to associate UMEM to
    :type qid: u16

.. _`i40e_xsk_umem_disable.description`:

Description
-----------

Returns 0 on success, <0 on failure

.. _`i40e_xsk_umem_query`:

i40e_xsk_umem_query
===================

.. c:function:: int i40e_xsk_umem_query(struct i40e_vsi *vsi, struct xdp_umem **umem, u16 qid)

    Queries a certain ring/qid for its UMEM

    :param vsi:
        Current VSI
    :type vsi: struct i40e_vsi \*

    :param umem:
        UMEM associated to the ring, if any
    :type umem: struct xdp_umem \*\*

    :param qid:
        Rx ring to associate UMEM to
    :type qid: u16

.. _`i40e_xsk_umem_query.description`:

Description
-----------

This function will store, if any, the UMEM associated to certain ring.

Returns 0 on success, <0 on failure

.. _`i40e_xsk_umem_setup`:

i40e_xsk_umem_setup
===================

.. c:function:: int i40e_xsk_umem_setup(struct i40e_vsi *vsi, struct xdp_umem *umem, u16 qid)

    Queries a certain ring/qid for its UMEM

    :param vsi:
        Current VSI
    :type vsi: struct i40e_vsi \*

    :param umem:
        UMEM to enable/associate to a ring, or NULL to disable
    :type umem: struct xdp_umem \*

    :param qid:
        Rx ring to (dis)associate UMEM (from)to
    :type qid: u16

.. _`i40e_xsk_umem_setup.description`:

Description
-----------

This function enables or disables an UMEM to a certain ring.

Returns 0 on success, <0 on failure

.. _`i40e_run_xdp_zc`:

i40e_run_xdp_zc
===============

.. c:function:: int i40e_run_xdp_zc(struct i40e_ring *rx_ring, struct xdp_buff *xdp)

    Executes an XDP program on an xdp_buff

    :param rx_ring:
        Rx ring
    :type rx_ring: struct i40e_ring \*

    :param xdp:
        xdp_buff used as input to the XDP program
    :type xdp: struct xdp_buff \*

.. _`i40e_run_xdp_zc.description`:

Description
-----------

This function enables or disables an UMEM to a certain ring.

Returns any of I40E_XDP_{PASS, CONSUMED, TX, REDIR}

.. _`i40e_alloc_buffer_zc`:

i40e_alloc_buffer_zc
====================

.. c:function:: bool i40e_alloc_buffer_zc(struct i40e_ring *rx_ring, struct i40e_rx_buffer *bi)

    Allocates an i40e_rx_buffer

    :param rx_ring:
        Rx ring
    :type rx_ring: struct i40e_ring \*

    :param bi:
        Rx buffer to populate
    :type bi: struct i40e_rx_buffer \*

.. _`i40e_alloc_buffer_zc.description`:

Description
-----------

This function allocates an Rx buffer. The buffer can come from fill
queue, or via the recycle queue (next_to_alloc).

Returns true for a successful allocation, false otherwise

.. _`i40e_alloc_buffer_slow_zc`:

i40e_alloc_buffer_slow_zc
=========================

.. c:function:: bool i40e_alloc_buffer_slow_zc(struct i40e_ring *rx_ring, struct i40e_rx_buffer *bi)

    Allocates an i40e_rx_buffer

    :param rx_ring:
        Rx ring
    :type rx_ring: struct i40e_ring \*

    :param bi:
        Rx buffer to populate
    :type bi: struct i40e_rx_buffer \*

.. _`i40e_alloc_buffer_slow_zc.description`:

Description
-----------

This function allocates an Rx buffer. The buffer can come from fill
queue, or via the reuse queue.

Returns true for a successful allocation, false otherwise

.. _`i40e_alloc_rx_buffers_zc`:

i40e_alloc_rx_buffers_zc
========================

.. c:function:: bool i40e_alloc_rx_buffers_zc(struct i40e_ring *rx_ring, u16 count)

    Allocates a number of Rx buffers

    :param rx_ring:
        Rx ring
    :type rx_ring: struct i40e_ring \*

    :param count:
        The number of buffers to allocate
    :type count: u16

.. _`i40e_alloc_rx_buffers_zc.description`:

Description
-----------

This function allocates a number of Rx buffers from the reuse queue
or fill ring and places them on the Rx ring.

Returns true for a successful allocation, false otherwise

.. _`i40e_alloc_rx_buffers_fast_zc`:

i40e_alloc_rx_buffers_fast_zc
=============================

.. c:function:: bool i40e_alloc_rx_buffers_fast_zc(struct i40e_ring *rx_ring, u16 count)

    Allocates a number of Rx buffers

    :param rx_ring:
        Rx ring
    :type rx_ring: struct i40e_ring \*

    :param count:
        The number of buffers to allocate
    :type count: u16

.. _`i40e_alloc_rx_buffers_fast_zc.description`:

Description
-----------

This function allocates a number of Rx buffers from the fill ring
or the internal recycle mechanism and places them on the Rx ring.

Returns true for a successful allocation, false otherwise

.. _`i40e_get_rx_buffer_zc`:

i40e_get_rx_buffer_zc
=====================

.. c:function:: struct i40e_rx_buffer *i40e_get_rx_buffer_zc(struct i40e_ring *rx_ring, const unsigned int size)

    Return the current Rx buffer

    :param rx_ring:
        Rx ring
    :type rx_ring: struct i40e_ring \*

    :param size:
        The size of the rx buffer (read from descriptor)
    :type size: const unsigned int

.. _`i40e_get_rx_buffer_zc.description`:

Description
-----------

This function returns the current, received Rx buffer, and also
does DMA synchronization.  the Rx ring.

Returns the received Rx buffer

.. _`i40e_reuse_rx_buffer_zc`:

i40e_reuse_rx_buffer_zc
=======================

.. c:function:: void i40e_reuse_rx_buffer_zc(struct i40e_ring *rx_ring, struct i40e_rx_buffer *old_bi)

    Recycle an Rx buffer

    :param rx_ring:
        Rx ring
    :type rx_ring: struct i40e_ring \*

    :param old_bi:
        The Rx buffer to recycle
    :type old_bi: struct i40e_rx_buffer \*

.. _`i40e_reuse_rx_buffer_zc.description`:

Description
-----------

This function recycles a finished Rx buffer, and places it on the
recycle queue (next_to_alloc).

.. _`i40e_zca_free`:

i40e_zca_free
=============

.. c:function:: void i40e_zca_free(struct zero_copy_allocator *alloc, unsigned long handle)

    Free callback for MEM_TYPE_ZERO_COPY allocations

    :param alloc:
        Zero-copy allocator
    :type alloc: struct zero_copy_allocator \*

    :param handle:
        Buffer handle
    :type handle: unsigned long

.. _`i40e_construct_skb_zc`:

i40e_construct_skb_zc
=====================

.. c:function:: struct sk_buff *i40e_construct_skb_zc(struct i40e_ring *rx_ring, struct i40e_rx_buffer *bi, struct xdp_buff *xdp)

    Create skbufff from zero-copy Rx buffer

    :param rx_ring:
        Rx ring
    :type rx_ring: struct i40e_ring \*

    :param bi:
        Rx buffer
    :type bi: struct i40e_rx_buffer \*

    :param xdp:
        xdp_buff
    :type xdp: struct xdp_buff \*

.. _`i40e_construct_skb_zc.description`:

Description
-----------

This functions allocates a new skb from a zero-copy Rx buffer.

Returns the skb, or NULL on failure.

.. _`i40e_inc_ntc`:

i40e_inc_ntc
============

.. c:function:: void i40e_inc_ntc(struct i40e_ring *rx_ring)

    Advance the next_to_clean index

    :param rx_ring:
        Rx ring
    :type rx_ring: struct i40e_ring \*

.. _`i40e_clean_rx_irq_zc`:

i40e_clean_rx_irq_zc
====================

.. c:function:: int i40e_clean_rx_irq_zc(struct i40e_ring *rx_ring, int budget)

    Consumes Rx packets from the hardware ring

    :param rx_ring:
        Rx ring
    :type rx_ring: struct i40e_ring \*

    :param budget:
        NAPI budget
    :type budget: int

.. _`i40e_clean_rx_irq_zc.description`:

Description
-----------

Returns amount of work completed

.. _`i40e_xmit_zc`:

i40e_xmit_zc
============

.. c:function:: bool i40e_xmit_zc(struct i40e_ring *xdp_ring, unsigned int budget)

    Performs zero-copy Tx AF_XDP

    :param xdp_ring:
        XDP Tx ring
    :type xdp_ring: struct i40e_ring \*

    :param budget:
        NAPI budget
    :type budget: unsigned int

.. _`i40e_xmit_zc.description`:

Description
-----------

Returns true if the work is finished.

.. _`i40e_clean_xdp_tx_buffer`:

i40e_clean_xdp_tx_buffer
========================

.. c:function:: void i40e_clean_xdp_tx_buffer(struct i40e_ring *tx_ring, struct i40e_tx_buffer *tx_bi)

    Frees and unmaps an XDP Tx entry

    :param tx_ring:
        XDP Tx ring
    :type tx_ring: struct i40e_ring \*

    :param tx_bi:
        Tx buffer info to clean
    :type tx_bi: struct i40e_tx_buffer \*

.. _`i40e_clean_xdp_tx_irq`:

i40e_clean_xdp_tx_irq
=====================

.. c:function:: bool i40e_clean_xdp_tx_irq(struct i40e_vsi *vsi, struct i40e_ring *tx_ring, int napi_budget)

    Completes AF_XDP entries, and cleans XDP entries

    :param vsi:
        *undescribed*
    :type vsi: struct i40e_vsi \*

    :param tx_ring:
        XDP Tx ring
    :type tx_ring: struct i40e_ring \*

    :param napi_budget:
        *undescribed*
    :type napi_budget: int

.. _`i40e_clean_xdp_tx_irq.description`:

Description
-----------

Returns true if cleanup/tranmission is done.

.. _`i40e_xsk_async_xmit`:

i40e_xsk_async_xmit
===================

.. c:function:: int i40e_xsk_async_xmit(struct net_device *dev, u32 queue_id)

    Implements the ndo_xsk_async_xmit

    :param dev:
        the netdevice
    :type dev: struct net_device \*

    :param queue_id:
        queue id to wake up
    :type queue_id: u32

.. _`i40e_xsk_async_xmit.description`:

Description
-----------

Returns <0 for errors, 0 otherwise.

.. _`i40e_xsk_clean_tx_ring`:

i40e_xsk_clean_tx_ring
======================

.. c:function:: void i40e_xsk_clean_tx_ring(struct i40e_ring *tx_ring)

    Clean the XDP Tx ring on shutdown

    :param tx_ring:
        *undescribed*
    :type tx_ring: struct i40e_ring \*

.. _`i40e_xsk_any_rx_ring_enabled`:

i40e_xsk_any_rx_ring_enabled
============================

.. c:function:: bool i40e_xsk_any_rx_ring_enabled(struct i40e_vsi *vsi)

    Checks if Rx rings have AF_XDP UMEM attached

    :param vsi:
        vsi
    :type vsi: struct i40e_vsi \*

.. _`i40e_xsk_any_rx_ring_enabled.description`:

Description
-----------

Returns true if any of the Rx rings has an AF_XDP UMEM attached

.. This file was automatic generated / don't edit.

