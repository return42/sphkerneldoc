.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_txrx.c

.. _`ice_unmap_and_free_tx_buf`:

ice_unmap_and_free_tx_buf
=========================

.. c:function:: void ice_unmap_and_free_tx_buf(struct ice_ring *ring, struct ice_tx_buf *tx_buf)

    Release a Tx buffer

    :param ring:
        the ring that owns the buffer
    :type ring: struct ice_ring \*

    :param tx_buf:
        the buffer to free
    :type tx_buf: struct ice_tx_buf \*

.. _`ice_clean_tx_ring`:

ice_clean_tx_ring
=================

.. c:function:: void ice_clean_tx_ring(struct ice_ring *tx_ring)

    Free any empty Tx buffers

    :param tx_ring:
        ring to be cleaned
    :type tx_ring: struct ice_ring \*

.. _`ice_free_tx_ring`:

ice_free_tx_ring
================

.. c:function:: void ice_free_tx_ring(struct ice_ring *tx_ring)

    Free Tx resources per queue

    :param tx_ring:
        Tx descriptor ring for a specific queue
    :type tx_ring: struct ice_ring \*

.. _`ice_free_tx_ring.description`:

Description
-----------

Free all transmit software resources

.. _`ice_clean_tx_irq`:

ice_clean_tx_irq
================

.. c:function:: bool ice_clean_tx_irq(struct ice_vsi *vsi, struct ice_ring *tx_ring, int napi_budget)

    Reclaim resources after transmit completes

    :param vsi:
        the VSI we care about
    :type vsi: struct ice_vsi \*

    :param tx_ring:
        Tx ring to clean
    :type tx_ring: struct ice_ring \*

    :param napi_budget:
        Used to determine if we are in netpoll
    :type napi_budget: int

.. _`ice_clean_tx_irq.description`:

Description
-----------

Returns true if there's any budget left (e.g. the clean is finished)

.. _`ice_setup_tx_ring`:

ice_setup_tx_ring
=================

.. c:function:: int ice_setup_tx_ring(struct ice_ring *tx_ring)

    Allocate the Tx descriptors

    :param tx_ring:
        the tx ring to set up
    :type tx_ring: struct ice_ring \*

.. _`ice_setup_tx_ring.description`:

Description
-----------

Return 0 on success, negative on error

.. _`ice_clean_rx_ring`:

ice_clean_rx_ring
=================

.. c:function:: void ice_clean_rx_ring(struct ice_ring *rx_ring)

    Free Rx buffers

    :param rx_ring:
        ring to be cleaned
    :type rx_ring: struct ice_ring \*

.. _`ice_free_rx_ring`:

ice_free_rx_ring
================

.. c:function:: void ice_free_rx_ring(struct ice_ring *rx_ring)

    Free Rx resources

    :param rx_ring:
        ring to clean the resources from
    :type rx_ring: struct ice_ring \*

.. _`ice_free_rx_ring.description`:

Description
-----------

Free all receive software resources

.. _`ice_setup_rx_ring`:

ice_setup_rx_ring
=================

.. c:function:: int ice_setup_rx_ring(struct ice_ring *rx_ring)

    Allocate the Rx descriptors

    :param rx_ring:
        the rx ring to set up
    :type rx_ring: struct ice_ring \*

.. _`ice_setup_rx_ring.description`:

Description
-----------

Return 0 on success, negative on error

.. _`ice_release_rx_desc`:

ice_release_rx_desc
===================

.. c:function:: void ice_release_rx_desc(struct ice_ring *rx_ring, u32 val)

    Store the new tail and head values

    :param rx_ring:
        ring to bump
    :type rx_ring: struct ice_ring \*

    :param val:
        new head index
    :type val: u32

.. _`ice_alloc_mapped_page`:

ice_alloc_mapped_page
=====================

.. c:function:: bool ice_alloc_mapped_page(struct ice_ring *rx_ring, struct ice_rx_buf *bi)

    recycle or make a new page

    :param rx_ring:
        ring to use
    :type rx_ring: struct ice_ring \*

    :param bi:
        rx_buf struct to modify
    :type bi: struct ice_rx_buf \*

.. _`ice_alloc_mapped_page.description`:

Description
-----------

Returns true if the page was successfully allocated or
reused.

.. _`ice_alloc_rx_bufs`:

ice_alloc_rx_bufs
=================

.. c:function:: bool ice_alloc_rx_bufs(struct ice_ring *rx_ring, u16 cleaned_count)

    Replace used receive buffers

    :param rx_ring:
        ring to place buffers on
    :type rx_ring: struct ice_ring \*

    :param cleaned_count:
        number of buffers to replace
    :type cleaned_count: u16

.. _`ice_alloc_rx_bufs.description`:

Description
-----------

Returns false if all allocations were successful, true if any fail

.. _`ice_page_is_reserved`:

ice_page_is_reserved
====================

.. c:function:: bool ice_page_is_reserved(struct page *page)

    check if reuse is possible

    :param page:
        page struct to check
    :type page: struct page \*

.. _`ice_add_rx_frag`:

ice_add_rx_frag
===============

.. c:function:: bool ice_add_rx_frag(struct ice_rx_buf *rx_buf, union ice_32b_rx_flex_desc *rx_desc, struct sk_buff *skb)

    Add contents of Rx buffer to sk_buff

    :param rx_buf:
        buffer containing page to add
    :type rx_buf: struct ice_rx_buf \*

    :param rx_desc:
        descriptor containing length of buffer written by hardware
    :type rx_desc: union ice_32b_rx_flex_desc \*

    :param skb:
        sk_buf to place the data into
    :type skb: struct sk_buff \*

.. _`ice_add_rx_frag.description`:

Description
-----------

This function will add the data contained in rx_buf->page to the skb.
This is done either through a direct copy if the data in the buffer is
less than the skb header size, otherwise it will just attach the page as
a frag to the skb.

The function will then update the page offset if necessary and return
true if the buffer can be reused by the adapter.

.. _`ice_reuse_rx_page`:

ice_reuse_rx_page
=================

.. c:function:: void ice_reuse_rx_page(struct ice_ring *rx_ring, struct ice_rx_buf *old_buf)

    page flip buffer and store it back on the ring

    :param rx_ring:
        rx descriptor ring to store buffers on
    :type rx_ring: struct ice_ring \*

    :param old_buf:
        donor buffer to have page reused
    :type old_buf: struct ice_rx_buf \*

.. _`ice_reuse_rx_page.description`:

Description
-----------

Synchronizes page for reuse by the adapter

.. _`ice_fetch_rx_buf`:

ice_fetch_rx_buf
================

.. c:function:: struct sk_buff *ice_fetch_rx_buf(struct ice_ring *rx_ring, union ice_32b_rx_flex_desc *rx_desc)

    Allocate skb and populate it

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct ice_ring \*

    :param rx_desc:
        descriptor containing info written by hardware
    :type rx_desc: union ice_32b_rx_flex_desc \*

.. _`ice_fetch_rx_buf.description`:

Description
-----------

This function allocates an skb on the fly, and populates it with the page
data from the current receive descriptor, taking care to set up the skb
correctly, as well as handling calling the page recycle function if
necessary.

.. _`ice_pull_tail`:

ice_pull_tail
=============

.. c:function:: void ice_pull_tail(struct sk_buff *skb)

    ice specific version of skb_pull_tail

    :param skb:
        pointer to current skb being adjusted
    :type skb: struct sk_buff \*

.. _`ice_pull_tail.description`:

Description
-----------

This function is an ice specific version of \__pskb_pull_tail.  The
main difference between this version and the original function is that
this function can make several assumptions about the state of things
that allow for significant optimizations versus the standard function.
As a result we can do things like drop a frag and maintain an accurate
truesize for the skb.

.. _`ice_cleanup_headers`:

ice_cleanup_headers
===================

.. c:function:: bool ice_cleanup_headers(struct sk_buff *skb)

    Correct empty headers

    :param skb:
        pointer to current skb being fixed
    :type skb: struct sk_buff \*

.. _`ice_cleanup_headers.description`:

Description
-----------

Also address the case where we are pulling data in on pages only
and as such no data is present in the skb header.

In addition if skb is not at least 60 bytes we need to pad it so that
it is large enough to qualify as a valid Ethernet frame.

Returns true if an error was encountered and skb was freed.

.. _`ice_test_staterr`:

ice_test_staterr
================

.. c:function:: bool ice_test_staterr(union ice_32b_rx_flex_desc *rx_desc, const u16 stat_err_bits)

    tests bits in Rx descriptor status and error fields

    :param rx_desc:
        pointer to receive descriptor (in le64 format)
    :type rx_desc: union ice_32b_rx_flex_desc \*

    :param stat_err_bits:
        value to mask
    :type stat_err_bits: const u16

.. _`ice_test_staterr.description`:

Description
-----------

This function does some fast chicanery in order to return the
value of the mask which is really only used for boolean tests.
The status_error_len doesn't need to be shifted because it begins
at offset zero.

.. _`ice_is_non_eop`:

ice_is_non_eop
==============

.. c:function:: bool ice_is_non_eop(struct ice_ring *rx_ring, union ice_32b_rx_flex_desc *rx_desc, struct sk_buff *skb)

    process handling of non-EOP buffers

    :param rx_ring:
        Rx ring being processed
    :type rx_ring: struct ice_ring \*

    :param rx_desc:
        Rx descriptor for current buffer
    :type rx_desc: union ice_32b_rx_flex_desc \*

    :param skb:
        Current socket buffer containing buffer in progress
    :type skb: struct sk_buff \*

.. _`ice_is_non_eop.description`:

Description
-----------

This function updates next to clean.  If the buffer is an EOP buffer
this function exits returning false, otherwise it will place the
sk_buff in the next buffer to be chained and return true indicating
that this is in fact a non-EOP buffer.

.. _`ice_ptype_to_htype`:

ice_ptype_to_htype
==================

.. c:function:: enum pkt_hash_types ice_ptype_to_htype(u8 __always_unused ptype)

    get a hash type

    :param ptype:
        the ptype value from the descriptor
    :type ptype: u8 __always_unused

.. _`ice_ptype_to_htype.description`:

Description
-----------

Returns a hash type to be used by skb_set_hash

.. _`ice_rx_hash`:

ice_rx_hash
===========

.. c:function:: void ice_rx_hash(struct ice_ring *rx_ring, union ice_32b_rx_flex_desc *rx_desc, struct sk_buff *skb, u8 rx_ptype)

    set the hash value in the skb

    :param rx_ring:
        descriptor ring
    :type rx_ring: struct ice_ring \*

    :param rx_desc:
        specific descriptor
    :type rx_desc: union ice_32b_rx_flex_desc \*

    :param skb:
        pointer to current skb
    :type skb: struct sk_buff \*

    :param rx_ptype:
        the ptype value from the descriptor
    :type rx_ptype: u8

.. _`ice_rx_csum`:

ice_rx_csum
===========

.. c:function:: void ice_rx_csum(struct ice_vsi *vsi, struct sk_buff *skb, union ice_32b_rx_flex_desc *rx_desc, u8 ptype)

    Indicate in skb if checksum is good

    :param vsi:
        the VSI we care about
    :type vsi: struct ice_vsi \*

    :param skb:
        skb currently being received and modified
    :type skb: struct sk_buff \*

    :param rx_desc:
        the receive descriptor
    :type rx_desc: union ice_32b_rx_flex_desc \*

    :param ptype:
        the packet type decoded by hardware
    :type ptype: u8

.. _`ice_rx_csum.description`:

Description
-----------

skb->protocol must be set before this function is called

.. _`ice_process_skb_fields`:

ice_process_skb_fields
======================

.. c:function:: void ice_process_skb_fields(struct ice_ring *rx_ring, union ice_32b_rx_flex_desc *rx_desc, struct sk_buff *skb, u8 ptype)

    Populate skb header fields from Rx descriptor

    :param rx_ring:
        rx descriptor ring packet is being transacted on
    :type rx_ring: struct ice_ring \*

    :param rx_desc:
        pointer to the EOP Rx descriptor
    :type rx_desc: union ice_32b_rx_flex_desc \*

    :param skb:
        pointer to current skb being populated
    :type skb: struct sk_buff \*

    :param ptype:
        the packet type decoded by hardware
    :type ptype: u8

.. _`ice_process_skb_fields.description`:

Description
-----------

This function checks the ring, descriptor, and packet information in
order to populate the hash, checksum, VLAN, protocol, and
other fields within the skb.

.. _`ice_receive_skb`:

ice_receive_skb
===============

.. c:function:: void ice_receive_skb(struct ice_ring *rx_ring, struct sk_buff *skb, u16 vlan_tag)

    Send a completed packet up the stack

    :param rx_ring:
        rx ring in play
    :type rx_ring: struct ice_ring \*

    :param skb:
        packet to send up
    :type skb: struct sk_buff \*

    :param vlan_tag:
        vlan tag for packet
    :type vlan_tag: u16

.. _`ice_receive_skb.description`:

Description
-----------

This function sends the completed packet (via. skb) up the stack using
gro receive functions (with/without vlan tag)

.. _`ice_clean_rx_irq`:

ice_clean_rx_irq
================

.. c:function:: int ice_clean_rx_irq(struct ice_ring *rx_ring, int budget)

    Clean completed descriptors from Rx ring - bounce buf

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct ice_ring \*

    :param budget:
        Total limit on number of packets to process
    :type budget: int

.. _`ice_clean_rx_irq.description`:

Description
-----------

This function provides a "bounce buffer" approach to Rx interrupt
processing.  The advantage to this is that on systems that have
expensive overhead for IOMMU access this provides a means of avoiding
it by maintaining the mapping of the page to the system.

Returns amount of work completed

.. _`ice_napi_poll`:

ice_napi_poll
=============

.. c:function:: int ice_napi_poll(struct napi_struct *napi, int budget)

    NAPI polling Rx/Tx cleanup routine

    :param napi:
        napi struct with our devices info in it
    :type napi: struct napi_struct \*

    :param budget:
        amount of work driver is allowed to do this pass, in packets
    :type budget: int

.. _`ice_napi_poll.description`:

Description
-----------

This function will clean all queues associated with a q_vector.

Returns the amount of work done

.. _`__ice_maybe_stop_tx`:

\__ice_maybe_stop_tx
====================

.. c:function:: int __ice_maybe_stop_tx(struct ice_ring *tx_ring, unsigned int size)

    2nd level check for tx stop conditions

    :param tx_ring:
        the ring to be checked
    :type tx_ring: struct ice_ring \*

    :param size:
        the size buffer we want to assure is available
    :type size: unsigned int

.. _`__ice_maybe_stop_tx.description`:

Description
-----------

Returns -EBUSY if a stop is needed, else 0

.. _`ice_maybe_stop_tx`:

ice_maybe_stop_tx
=================

.. c:function:: int ice_maybe_stop_tx(struct ice_ring *tx_ring, unsigned int size)

    1st level check for tx stop conditions

    :param tx_ring:
        the ring to be checked
    :type tx_ring: struct ice_ring \*

    :param size:
        the size buffer we want to assure is available
    :type size: unsigned int

.. _`ice_maybe_stop_tx.description`:

Description
-----------

Returns 0 if stop is not needed

.. _`ice_tx_map`:

ice_tx_map
==========

.. c:function:: void ice_tx_map(struct ice_ring *tx_ring, struct ice_tx_buf *first, struct ice_tx_offload_params *off)

    Build the Tx descriptor

    :param tx_ring:
        ring to send buffer on
    :type tx_ring: struct ice_ring \*

    :param first:
        first buffer info buffer to use
    :type first: struct ice_tx_buf \*

    :param off:
        pointer to struct that holds offload parameters
    :type off: struct ice_tx_offload_params \*

.. _`ice_tx_map.description`:

Description
-----------

This function loops over the skb data pointed to by \*first
and gets a physical address for each memory location and programs
it and the length into the transmit descriptor.

.. _`ice_tx_csum`:

ice_tx_csum
===========

.. c:function:: int ice_tx_csum(struct ice_tx_buf *first, struct ice_tx_offload_params *off)

    Enable Tx checksum offloads

    :param first:
        pointer to the first descriptor
    :type first: struct ice_tx_buf \*

    :param off:
        pointer to struct that holds offload parameters
    :type off: struct ice_tx_offload_params \*

.. _`ice_tx_csum.description`:

Description
-----------

Returns 0 or error (negative) if checksum offload can't happen, 1 otherwise.

.. _`ice_tx_prepare_vlan_flags`:

ice_tx_prepare_vlan_flags
=========================

.. c:function:: int ice_tx_prepare_vlan_flags(struct ice_ring *tx_ring, struct ice_tx_buf *first)

    prepare generic TX VLAN tagging flags for HW

    :param tx_ring:
        ring to send buffer on
    :type tx_ring: struct ice_ring \*

    :param first:
        pointer to struct ice_tx_buf
    :type first: struct ice_tx_buf \*

.. _`ice_tx_prepare_vlan_flags.description`:

Description
-----------

Checks the skb and set up correspondingly several generic transmit flags
related to VLAN tagging for the HW, such as VLAN, DCB, etc.

Returns error code indicate the frame should be dropped upon error and the
otherwise returns 0 to indicate the flags has been set properly.

.. _`ice_tso`:

ice_tso
=======

.. c:function:: int ice_tso(struct ice_tx_buf *first, struct ice_tx_offload_params *off)

    computes mss and TSO length to prepare for TSO

    :param first:
        pointer to struct ice_tx_buf
    :type first: struct ice_tx_buf \*

    :param off:
        pointer to struct that holds offload parameters
    :type off: struct ice_tx_offload_params \*

.. _`ice_tso.description`:

Description
-----------

Returns 0 or error (negative) if TSO can't happen, 1 otherwise.

.. _`ice_txd_use_count`:

ice_txd_use_count
=================

.. c:function:: unsigned int ice_txd_use_count(unsigned int size)

    estimate the number of descriptors needed for Tx

    :param size:
        transmit request size in bytes
    :type size: unsigned int

.. _`ice_txd_use_count.description`:

Description
-----------

Due to hardware alignment restrictions (4K alignment), we need to
assume that we can have no more than 12K of data per descriptor, even
though each descriptor can take up to 16K - 1 bytes of aligned memory.
Thus, we need to divide by 12K. But division is slow! Instead,
we decompose the operation into shifts and one relatively cheap
multiply operation.

To divide by 12K, we first divide by 4K, then divide by 3:
To divide by 4K, shift right by 12 bits
To divide by 3, multiply by 85, then divide by 256
(Divide by 256 is done by shifting right by 8 bits)
Finally, we add one to round up. Because 256 isn't an exact multiple of
3, we'll underestimate near each multiple of 12K. This is actually more
accurate as we have 4K - 1 of wiggle room that we can fit into the last
segment.  For our purposes this is accurate out to 1M which is orders of
magnitude greater than our largest possible GSO size.

.. _`ice_txd_use_count.this-would-then-be-implemented-as`:

This would then be implemented as
---------------------------------

return (((size >> 12) \* 85) >> 8) + ICE_DESCS_FOR_SKB_DATA_PTR;

Since multiplication and division are commutative, we can reorder

.. _`ice_txd_use_count.operations-into`:

operations into
---------------

return ((size \* 85) >> 20) + ICE_DESCS_FOR_SKB_DATA_PTR;

.. _`ice_xmit_desc_count`:

ice_xmit_desc_count
===================

.. c:function:: unsigned int ice_xmit_desc_count(struct sk_buff *skb)

    calculate number of tx descriptors needed

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

.. _`ice_xmit_desc_count.description`:

Description
-----------

Returns number of data descriptors needed for this skb.

.. _`__ice_chk_linearize`:

\__ice_chk_linearize
====================

.. c:function:: bool __ice_chk_linearize(struct sk_buff *skb)

    Check if there are more than 8 buffers per packet

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

.. _`__ice_chk_linearize.note`:

Note
----

This HW can't DMA more than 8 buffers to build a packet on the wire
and so we need to figure out the cases where we need to linearize the skb.

For TSO we need to count the TSO header and segment payload separately.
As such we need to check cases where we have 7 fragments or more as we
can potentially require 9 DMA transactions, 1 for the TSO header, 1 for
the segment payload in the first descriptor, and another 7 for the
fragments.

.. _`ice_chk_linearize`:

ice_chk_linearize
=================

.. c:function:: bool ice_chk_linearize(struct sk_buff *skb, unsigned int count)

    Check if there are more than 8 fragments per packet

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

    :param count:
        number of buffers used
    :type count: unsigned int

.. _`ice_chk_linearize.note`:

Note
----

Our HW can't scatter-gather more than 8 fragments to build
a packet on the wire and so we need to figure out the cases where we
need to linearize the skb.

.. _`ice_xmit_frame_ring`:

ice_xmit_frame_ring
===================

.. c:function:: netdev_tx_t ice_xmit_frame_ring(struct sk_buff *skb, struct ice_ring *tx_ring)

    Sends buffer on Tx ring

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

    :param tx_ring:
        ring to send buffer on
    :type tx_ring: struct ice_ring \*

.. _`ice_xmit_frame_ring.description`:

Description
-----------

Returns NETDEV_TX_OK if sent, else an error code

.. _`ice_start_xmit`:

ice_start_xmit
==============

.. c:function:: netdev_tx_t ice_start_xmit(struct sk_buff *skb, struct net_device *netdev)

    Selects the correct VSI and Tx queue to send buffer

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`ice_start_xmit.description`:

Description
-----------

Returns NETDEV_TX_OK if sent, else an error code

.. This file was automatic generated / don't edit.

