.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/iavf/iavf_txrx.c

.. _`iavf_unmap_and_free_tx_resource`:

iavf_unmap_and_free_tx_resource
===============================

.. c:function:: void iavf_unmap_and_free_tx_resource(struct iavf_ring *ring, struct iavf_tx_buffer *tx_buffer)

    Release a Tx buffer

    :param ring:
        the ring that owns the buffer
    :type ring: struct iavf_ring \*

    :param tx_buffer:
        the buffer to free
    :type tx_buffer: struct iavf_tx_buffer \*

.. _`iavf_clean_tx_ring`:

iavf_clean_tx_ring
==================

.. c:function:: void iavf_clean_tx_ring(struct iavf_ring *tx_ring)

    Free any empty Tx buffers

    :param tx_ring:
        ring to be cleaned
    :type tx_ring: struct iavf_ring \*

.. _`iavf_free_tx_resources`:

iavf_free_tx_resources
======================

.. c:function:: void iavf_free_tx_resources(struct iavf_ring *tx_ring)

    Free Tx resources per queue

    :param tx_ring:
        Tx descriptor ring for a specific queue
    :type tx_ring: struct iavf_ring \*

.. _`iavf_free_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`iavf_get_tx_pending`:

iavf_get_tx_pending
===================

.. c:function:: u32 iavf_get_tx_pending(struct iavf_ring *ring, bool in_sw)

    how many Tx descriptors not processed

    :param ring:
        the ring of descriptors
    :type ring: struct iavf_ring \*

    :param in_sw:
        is tx_pending being checked in SW or HW
    :type in_sw: bool

.. _`iavf_get_tx_pending.description`:

Description
-----------

Since there is no access to the ring head register
in XL710, we need to use our local copies

.. _`iavf_detect_recover_hung`:

iavf_detect_recover_hung
========================

.. c:function:: void iavf_detect_recover_hung(struct iavf_vsi *vsi)

    Function to detect and recover hung_queues

    :param vsi:
        pointer to vsi struct with tx queues
    :type vsi: struct iavf_vsi \*

.. _`iavf_detect_recover_hung.description`:

Description
-----------

VSI has netdev and netdev has TX queues. This function is to check each of
those TX queues if they are hung, trigger recovery by issuing SW interrupt.

.. _`iavf_clean_tx_irq`:

iavf_clean_tx_irq
=================

.. c:function:: bool iavf_clean_tx_irq(struct iavf_vsi *vsi, struct iavf_ring *tx_ring, int napi_budget)

    Reclaim resources after transmit completes

    :param vsi:
        the VSI we care about
    :type vsi: struct iavf_vsi \*

    :param tx_ring:
        Tx ring to clean
    :type tx_ring: struct iavf_ring \*

    :param napi_budget:
        Used to determine if we are in netpoll
    :type napi_budget: int

.. _`iavf_clean_tx_irq.description`:

Description
-----------

Returns true if there's any budget left (e.g. the clean is finished)

.. _`iavf_enable_wb_on_itr`:

iavf_enable_wb_on_itr
=====================

.. c:function:: void iavf_enable_wb_on_itr(struct iavf_vsi *vsi, struct iavf_q_vector *q_vector)

    Arm hardware to do a wb, interrupts are not enabled

    :param vsi:
        the VSI we care about
    :type vsi: struct iavf_vsi \*

    :param q_vector:
        the vector on which to enable writeback
    :type q_vector: struct iavf_q_vector \*

.. _`iavf_force_wb`:

iavf_force_wb
=============

.. c:function:: void iavf_force_wb(struct iavf_vsi *vsi, struct iavf_q_vector *q_vector)

    Issue SW Interrupt so HW does a wb

    :param vsi:
        the VSI we care about
    :type vsi: struct iavf_vsi \*

    :param q_vector:
        the vector  on which to force writeback
    :type q_vector: struct iavf_q_vector \*

.. _`iavf_update_itr`:

iavf_update_itr
===============

.. c:function:: void iavf_update_itr(struct iavf_q_vector *q_vector, struct iavf_ring_container *rc)

    update the dynamic ITR value based on statistics

    :param q_vector:
        structure containing interrupt and ring information
    :type q_vector: struct iavf_q_vector \*

    :param rc:
        structure containing ring performance data
    :type rc: struct iavf_ring_container \*

.. _`iavf_update_itr.description`:

Description
-----------

Stores a new ITR value based on packets and byte
counts during the last interrupt.  The advantage of per interrupt
computation is faster updates and more accurate ITR for the current
traffic pattern.  Constants in this function were computed
based on theoretical maximum wire speed and thresholds were set based
on testing data as well as attempting to minimize response time
while increasing bulk throughput.

.. _`iavf_setup_tx_descriptors`:

iavf_setup_tx_descriptors
=========================

.. c:function:: int iavf_setup_tx_descriptors(struct iavf_ring *tx_ring)

    Allocate the Tx descriptors

    :param tx_ring:
        the tx ring to set up
    :type tx_ring: struct iavf_ring \*

.. _`iavf_setup_tx_descriptors.description`:

Description
-----------

Return 0 on success, negative on error

.. _`iavf_clean_rx_ring`:

iavf_clean_rx_ring
==================

.. c:function:: void iavf_clean_rx_ring(struct iavf_ring *rx_ring)

    Free Rx buffers

    :param rx_ring:
        ring to be cleaned
    :type rx_ring: struct iavf_ring \*

.. _`iavf_free_rx_resources`:

iavf_free_rx_resources
======================

.. c:function:: void iavf_free_rx_resources(struct iavf_ring *rx_ring)

    Free Rx resources

    :param rx_ring:
        ring to clean the resources from
    :type rx_ring: struct iavf_ring \*

.. _`iavf_free_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`iavf_setup_rx_descriptors`:

iavf_setup_rx_descriptors
=========================

.. c:function:: int iavf_setup_rx_descriptors(struct iavf_ring *rx_ring)

    Allocate Rx descriptors

    :param rx_ring:
        Rx descriptor ring (for a specific queue) to setup
    :type rx_ring: struct iavf_ring \*

.. _`iavf_setup_rx_descriptors.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`iavf_release_rx_desc`:

iavf_release_rx_desc
====================

.. c:function:: void iavf_release_rx_desc(struct iavf_ring *rx_ring, u32 val)

    Store the new tail and head values

    :param rx_ring:
        ring to bump
    :type rx_ring: struct iavf_ring \*

    :param val:
        new head index
    :type val: u32

.. _`iavf_rx_offset`:

iavf_rx_offset
==============

.. c:function:: unsigned int iavf_rx_offset(struct iavf_ring *rx_ring)

    Return expected offset into page to access data

    :param rx_ring:
        Ring we are requesting offset of
    :type rx_ring: struct iavf_ring \*

.. _`iavf_rx_offset.description`:

Description
-----------

Returns the offset value for ring into the data buffer.

.. _`iavf_alloc_mapped_page`:

iavf_alloc_mapped_page
======================

.. c:function:: bool iavf_alloc_mapped_page(struct iavf_ring *rx_ring, struct iavf_rx_buffer *bi)

    recycle or make a new page

    :param rx_ring:
        ring to use
    :type rx_ring: struct iavf_ring \*

    :param bi:
        rx_buffer struct to modify
    :type bi: struct iavf_rx_buffer \*

.. _`iavf_alloc_mapped_page.description`:

Description
-----------

Returns true if the page was successfully allocated or
reused.

.. _`iavf_receive_skb`:

iavf_receive_skb
================

.. c:function:: void iavf_receive_skb(struct iavf_ring *rx_ring, struct sk_buff *skb, u16 vlan_tag)

    Send a completed packet up the stack

    :param rx_ring:
        rx ring in play
    :type rx_ring: struct iavf_ring \*

    :param skb:
        packet to send up
    :type skb: struct sk_buff \*

    :param vlan_tag:
        vlan tag for packet
    :type vlan_tag: u16

.. _`iavf_alloc_rx_buffers`:

iavf_alloc_rx_buffers
=====================

.. c:function:: bool iavf_alloc_rx_buffers(struct iavf_ring *rx_ring, u16 cleaned_count)

    Replace used receive buffers

    :param rx_ring:
        ring to place buffers on
    :type rx_ring: struct iavf_ring \*

    :param cleaned_count:
        number of buffers to replace
    :type cleaned_count: u16

.. _`iavf_alloc_rx_buffers.description`:

Description
-----------

Returns false if all allocations were successful, true if any fail

.. _`iavf_rx_checksum`:

iavf_rx_checksum
================

.. c:function:: void iavf_rx_checksum(struct iavf_vsi *vsi, struct sk_buff *skb, union iavf_rx_desc *rx_desc)

    Indicate in skb if hw indicated a good cksum

    :param vsi:
        the VSI we care about
    :type vsi: struct iavf_vsi \*

    :param skb:
        skb currently being received and modified
    :type skb: struct sk_buff \*

    :param rx_desc:
        the receive descriptor
    :type rx_desc: union iavf_rx_desc \*

.. _`iavf_ptype_to_htype`:

iavf_ptype_to_htype
===================

.. c:function:: int iavf_ptype_to_htype(u8 ptype)

    get a hash type

    :param ptype:
        the ptype value from the descriptor
    :type ptype: u8

.. _`iavf_ptype_to_htype.description`:

Description
-----------

Returns a hash type to be used by skb_set_hash

.. _`iavf_rx_hash`:

iavf_rx_hash
============

.. c:function:: void iavf_rx_hash(struct iavf_ring *ring, union iavf_rx_desc *rx_desc, struct sk_buff *skb, u8 rx_ptype)

    set the hash value in the skb

    :param ring:
        descriptor ring
    :type ring: struct iavf_ring \*

    :param rx_desc:
        specific descriptor
    :type rx_desc: union iavf_rx_desc \*

    :param skb:
        skb currently being received and modified
    :type skb: struct sk_buff \*

    :param rx_ptype:
        Rx packet type
    :type rx_ptype: u8

.. _`iavf_process_skb_fields`:

iavf_process_skb_fields
=======================

.. c:function:: void iavf_process_skb_fields(struct iavf_ring *rx_ring, union iavf_rx_desc *rx_desc, struct sk_buff *skb, u8 rx_ptype)

    Populate skb header fields from Rx descriptor

    :param rx_ring:
        rx descriptor ring packet is being transacted on
    :type rx_ring: struct iavf_ring \*

    :param rx_desc:
        pointer to the EOP Rx descriptor
    :type rx_desc: union iavf_rx_desc \*

    :param skb:
        pointer to current skb being populated
    :type skb: struct sk_buff \*

    :param rx_ptype:
        the packet type decoded by hardware
    :type rx_ptype: u8

.. _`iavf_process_skb_fields.description`:

Description
-----------

This function checks the ring, descriptor, and packet information in
order to populate the hash, checksum, VLAN, protocol, and
other fields within the skb.

.. _`iavf_cleanup_headers`:

iavf_cleanup_headers
====================

.. c:function:: bool iavf_cleanup_headers(struct iavf_ring *rx_ring, struct sk_buff *skb)

    Correct empty headers

    :param rx_ring:
        rx descriptor ring packet is being transacted on
    :type rx_ring: struct iavf_ring \*

    :param skb:
        pointer to current skb being fixed
    :type skb: struct sk_buff \*

.. _`iavf_cleanup_headers.description`:

Description
-----------

Also address the case where we are pulling data in on pages only
and as such no data is present in the skb header.

In addition if skb is not at least 60 bytes we need to pad it so that
it is large enough to qualify as a valid Ethernet frame.

Returns true if an error was encountered and skb was freed.

.. _`iavf_reuse_rx_page`:

iavf_reuse_rx_page
==================

.. c:function:: void iavf_reuse_rx_page(struct iavf_ring *rx_ring, struct iavf_rx_buffer *old_buff)

    page flip buffer and store it back on the ring

    :param rx_ring:
        rx descriptor ring to store buffers on
    :type rx_ring: struct iavf_ring \*

    :param old_buff:
        donor buffer to have page reused
    :type old_buff: struct iavf_rx_buffer \*

.. _`iavf_reuse_rx_page.description`:

Description
-----------

Synchronizes page for reuse by the adapter

.. _`iavf_page_is_reusable`:

iavf_page_is_reusable
=====================

.. c:function:: bool iavf_page_is_reusable(struct page *page)

    check if any reuse is possible

    :param page:
        page struct to check
    :type page: struct page \*

.. _`iavf_page_is_reusable.description`:

Description
-----------

A page is not reusable if it was allocated under low memory
conditions, or it's not in the same NUMA node as this CPU.

.. _`iavf_can_reuse_rx_page`:

iavf_can_reuse_rx_page
======================

.. c:function:: bool iavf_can_reuse_rx_page(struct iavf_rx_buffer *rx_buffer)

    Determine if this page can be reused by the adapter for another receive

    :param rx_buffer:
        buffer containing the page
    :type rx_buffer: struct iavf_rx_buffer \*

.. _`iavf_can_reuse_rx_page.description`:

Description
-----------

If page is reusable, rx_buffer->page_offset is adjusted to point to
an unused region in the page.

For small pages, \ ``truesize``\  will be a constant value, half the size
of the memory at page.  We'll attempt to alternate between high and
low halves of the page, with one half ready for use by the hardware
and the other half being consumed by the stack.  We use the page
ref count to determine whether the stack has finished consuming the
portion of this page that was passed up with a previous packet.  If
the page ref count is >1, we'll assume the "other" half page is
still busy, and this page cannot be reused.

For larger pages, \ ``truesize``\  will be the actual space used by the
received packet (adjusted upward to an even multiple of the cache
line size).  This will advance through the page by the amount
actually consumed by the received packets while there is still
space for a buffer.  Each region of larger pages will be used at
most once, after which the page will not be reused.

In either case, if the page is reusable its refcount is increased.

.. _`iavf_add_rx_frag`:

iavf_add_rx_frag
================

.. c:function:: void iavf_add_rx_frag(struct iavf_ring *rx_ring, struct iavf_rx_buffer *rx_buffer, struct sk_buff *skb, unsigned int size)

    Add contents of Rx buffer to sk_buff

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct iavf_ring \*

    :param rx_buffer:
        buffer containing page to add
    :type rx_buffer: struct iavf_rx_buffer \*

    :param skb:
        sk_buff to place the data into
    :type skb: struct sk_buff \*

    :param size:
        packet length from rx_desc
    :type size: unsigned int

.. _`iavf_add_rx_frag.description`:

Description
-----------

This function will add the data contained in rx_buffer->page to the skb.
It will just attach the page as a frag to the skb.

The function will then update the page offset.

.. _`iavf_get_rx_buffer`:

iavf_get_rx_buffer
==================

.. c:function:: struct iavf_rx_buffer *iavf_get_rx_buffer(struct iavf_ring *rx_ring, const unsigned int size)

    Fetch Rx buffer and synchronize data for use

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct iavf_ring \*

    :param size:
        size of buffer to add to skb
    :type size: const unsigned int

.. _`iavf_get_rx_buffer.description`:

Description
-----------

This function will pull an Rx buffer from the ring and synchronize it
for use by the CPU.

.. _`iavf_construct_skb`:

iavf_construct_skb
==================

.. c:function:: struct sk_buff *iavf_construct_skb(struct iavf_ring *rx_ring, struct iavf_rx_buffer *rx_buffer, unsigned int size)

    Allocate skb and populate it

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct iavf_ring \*

    :param rx_buffer:
        rx buffer to pull data from
    :type rx_buffer: struct iavf_rx_buffer \*

    :param size:
        size of buffer to add to skb
    :type size: unsigned int

.. _`iavf_construct_skb.description`:

Description
-----------

This function allocates an skb.  It then populates it with the page
data from the current receive descriptor, taking care to set up the
skb correctly.

.. _`iavf_build_skb`:

iavf_build_skb
==============

.. c:function:: struct sk_buff *iavf_build_skb(struct iavf_ring *rx_ring, struct iavf_rx_buffer *rx_buffer, unsigned int size)

    Build skb around an existing buffer

    :param rx_ring:
        Rx descriptor ring to transact packets on
    :type rx_ring: struct iavf_ring \*

    :param rx_buffer:
        Rx buffer to pull data from
    :type rx_buffer: struct iavf_rx_buffer \*

    :param size:
        size of buffer to add to skb
    :type size: unsigned int

.. _`iavf_build_skb.description`:

Description
-----------

This function builds an skb around an existing Rx buffer, taking care
to set up the skb correctly and avoid any memcpy overhead.

.. _`iavf_put_rx_buffer`:

iavf_put_rx_buffer
==================

.. c:function:: void iavf_put_rx_buffer(struct iavf_ring *rx_ring, struct iavf_rx_buffer *rx_buffer)

    Clean up used buffer and either recycle or free

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct iavf_ring \*

    :param rx_buffer:
        rx buffer to pull data from
    :type rx_buffer: struct iavf_rx_buffer \*

.. _`iavf_put_rx_buffer.description`:

Description
-----------

This function will clean up the contents of the rx_buffer.  It will
either recycle the buffer or unmap it and free the associated resources.

.. _`iavf_is_non_eop`:

iavf_is_non_eop
===============

.. c:function:: bool iavf_is_non_eop(struct iavf_ring *rx_ring, union iavf_rx_desc *rx_desc, struct sk_buff *skb)

    process handling of non-EOP buffers

    :param rx_ring:
        Rx ring being processed
    :type rx_ring: struct iavf_ring \*

    :param rx_desc:
        Rx descriptor for current buffer
    :type rx_desc: union iavf_rx_desc \*

    :param skb:
        Current socket buffer containing buffer in progress
    :type skb: struct sk_buff \*

.. _`iavf_is_non_eop.description`:

Description
-----------

This function updates next to clean.  If the buffer is an EOP buffer
this function exits returning false, otherwise it will place the
sk_buff in the next buffer to be chained and return true indicating
that this is in fact a non-EOP buffer.

.. _`iavf_clean_rx_irq`:

iavf_clean_rx_irq
=================

.. c:function:: int iavf_clean_rx_irq(struct iavf_ring *rx_ring, int budget)

    Clean completed descriptors from Rx ring - bounce buf

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct iavf_ring \*

    :param budget:
        Total limit on number of packets to process
    :type budget: int

.. _`iavf_clean_rx_irq.description`:

Description
-----------

This function provides a "bounce buffer" approach to Rx interrupt
processing.  The advantage to this is that on systems that have
expensive overhead for IOMMU access this provides a means of avoiding
it by maintaining the mapping of the page to the system.

Returns amount of work completed

.. _`iavf_update_enable_itr`:

iavf_update_enable_itr
======================

.. c:function:: void iavf_update_enable_itr(struct iavf_vsi *vsi, struct iavf_q_vector *q_vector)

    Update itr and re-enable MSIX interrupt

    :param vsi:
        the VSI we care about
    :type vsi: struct iavf_vsi \*

    :param q_vector:
        q_vector for which itr is being updated and interrupt enabled
    :type q_vector: struct iavf_q_vector \*

.. _`iavf_napi_poll`:

iavf_napi_poll
==============

.. c:function:: int iavf_napi_poll(struct napi_struct *napi, int budget)

    NAPI polling Rx/Tx cleanup routine

    :param napi:
        napi struct with our devices info in it
    :type napi: struct napi_struct \*

    :param budget:
        amount of work driver is allowed to do this pass, in packets
    :type budget: int

.. _`iavf_napi_poll.description`:

Description
-----------

This function will clean all queues associated with a q_vector.

Returns the amount of work done

.. _`iavf_tx_prepare_vlan_flags`:

iavf_tx_prepare_vlan_flags
==========================

.. c:function:: int iavf_tx_prepare_vlan_flags(struct sk_buff *skb, struct iavf_ring *tx_ring, u32 *flags)

    prepare generic TX VLAN tagging flags for HW

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

    :param tx_ring:
        ring to send buffer on
    :type tx_ring: struct iavf_ring \*

    :param flags:
        the tx flags to be set
    :type flags: u32 \*

.. _`iavf_tx_prepare_vlan_flags.description`:

Description
-----------

Checks the skb and set up correspondingly several generic transmit flags
related to VLAN tagging for the HW, such as VLAN, DCB, etc.

Returns error code indicate the frame should be dropped upon error and the
otherwise  returns 0 to indicate the flags has been set properly.

.. _`iavf_tso`:

iavf_tso
========

.. c:function:: int iavf_tso(struct iavf_tx_buffer *first, u8 *hdr_len, u64 *cd_type_cmd_tso_mss)

    set up the tso context descriptor

    :param first:
        pointer to first Tx buffer for xmit
    :type first: struct iavf_tx_buffer \*

    :param hdr_len:
        ptr to the size of the packet header
    :type hdr_len: u8 \*

    :param cd_type_cmd_tso_mss:
        Quad Word 1
    :type cd_type_cmd_tso_mss: u64 \*

.. _`iavf_tso.description`:

Description
-----------

Returns 0 if no TSO can happen, 1 if tso is going, or error

.. _`iavf_tx_enable_csum`:

iavf_tx_enable_csum
===================

.. c:function:: int iavf_tx_enable_csum(struct sk_buff *skb, u32 *tx_flags, u32 *td_cmd, u32 *td_offset, struct iavf_ring *tx_ring, u32 *cd_tunneling)

    Enable Tx checksum offloads

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

    :param tx_flags:
        pointer to Tx flags currently set
    :type tx_flags: u32 \*

    :param td_cmd:
        Tx descriptor command bits to set
    :type td_cmd: u32 \*

    :param td_offset:
        Tx descriptor header offsets to set
    :type td_offset: u32 \*

    :param tx_ring:
        Tx descriptor ring
    :type tx_ring: struct iavf_ring \*

    :param cd_tunneling:
        ptr to context desc bits
    :type cd_tunneling: u32 \*

.. _`iavf_create_tx_ctx`:

iavf_create_tx_ctx
==================

.. c:function:: void iavf_create_tx_ctx(struct iavf_ring *tx_ring, const u64 cd_type_cmd_tso_mss, const u32 cd_tunneling, const u32 cd_l2tag2)

    :param tx_ring:
        ring to create the descriptor on
    :type tx_ring: struct iavf_ring \*

    :param cd_type_cmd_tso_mss:
        Quad Word 1
    :type cd_type_cmd_tso_mss: const u64

    :param cd_tunneling:
        Quad Word 0 - bits 0-31
    :type cd_tunneling: const u32

    :param cd_l2tag2:
        Quad Word 0 - bits 32-63
    :type cd_l2tag2: const u32

.. _`__iavf_chk_linearize`:

\__iavf_chk_linearize
=====================

.. c:function:: bool __iavf_chk_linearize(struct sk_buff *skb)

    Check if there are more than 8 buffers per packet

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

.. _`__iavf_chk_linearize.note`:

Note
----

Our HW can't DMA more than 8 buffers to build a packet on the wire
and so we need to figure out the cases where we need to linearize the skb.

For TSO we need to count the TSO header and segment payload separately.
As such we need to check cases where we have 7 fragments or more as we
can potentially require 9 DMA transactions, 1 for the TSO header, 1 for
the segment payload in the first descriptor, and another 7 for the
fragments.

.. _`__iavf_maybe_stop_tx`:

\__iavf_maybe_stop_tx
=====================

.. c:function:: int __iavf_maybe_stop_tx(struct iavf_ring *tx_ring, int size)

    2nd level check for tx stop conditions

    :param tx_ring:
        the ring to be checked
    :type tx_ring: struct iavf_ring \*

    :param size:
        the size buffer we want to assure is available
    :type size: int

.. _`__iavf_maybe_stop_tx.description`:

Description
-----------

Returns -EBUSY if a stop is needed, else 0

.. _`iavf_tx_map`:

iavf_tx_map
===========

.. c:function:: void iavf_tx_map(struct iavf_ring *tx_ring, struct sk_buff *skb, struct iavf_tx_buffer *first, u32 tx_flags, const u8 hdr_len, u32 td_cmd, u32 td_offset)

    Build the Tx descriptor

    :param tx_ring:
        ring to send buffer on
    :type tx_ring: struct iavf_ring \*

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

    :param first:
        first buffer info buffer to use
    :type first: struct iavf_tx_buffer \*

    :param tx_flags:
        collected send information
    :type tx_flags: u32

    :param hdr_len:
        size of the packet header
    :type hdr_len: const u8

    :param td_cmd:
        the command field in the descriptor
    :type td_cmd: u32

    :param td_offset:
        offset for checksum or crc
    :type td_offset: u32

.. _`iavf_xmit_frame_ring`:

iavf_xmit_frame_ring
====================

.. c:function:: netdev_tx_t iavf_xmit_frame_ring(struct sk_buff *skb, struct iavf_ring *tx_ring)

    Sends buffer on Tx ring

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

    :param tx_ring:
        ring to send buffer on
    :type tx_ring: struct iavf_ring \*

.. _`iavf_xmit_frame_ring.description`:

Description
-----------

Returns NETDEV_TX_OK if sent, else an error code

.. _`iavf_xmit_frame`:

iavf_xmit_frame
===============

.. c:function:: netdev_tx_t iavf_xmit_frame(struct sk_buff *skb, struct net_device *netdev)

    Selects the correct VSI and Tx queue to send buffer

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`iavf_xmit_frame.description`:

Description
-----------

Returns NETDEV_TX_OK if sent, else an error code

.. This file was automatic generated / don't edit.

