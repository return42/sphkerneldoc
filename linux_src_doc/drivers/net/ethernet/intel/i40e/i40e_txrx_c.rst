.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_txrx.c

.. _`i40e_fdir`:

i40e_fdir
=========

.. c:function:: void i40e_fdir(struct i40e_ring *tx_ring, struct i40e_fdir_filter *fdata, bool add)

    Generate a Flow Director descriptor based on fdata

    :param tx_ring:
        Tx ring to send buffer on
    :type tx_ring: struct i40e_ring \*

    :param fdata:
        Flow director filter data
    :type fdata: struct i40e_fdir_filter \*

    :param add:
        Indicate if we are adding a rule or deleting one
    :type add: bool

.. _`i40e_program_fdir_filter`:

i40e_program_fdir_filter
========================

.. c:function:: int i40e_program_fdir_filter(struct i40e_fdir_filter *fdir_data, u8 *raw_packet, struct i40e_pf *pf, bool add)

    Program a Flow Director filter

    :param fdir_data:
        Packet data that will be filter parameters
    :type fdir_data: struct i40e_fdir_filter \*

    :param raw_packet:
        the pre-allocated packet buffer for FDir
    :type raw_packet: u8 \*

    :param pf:
        The PF pointer
    :type pf: struct i40e_pf \*

    :param add:
        True for add/update, False for remove
    :type add: bool

.. _`i40e_add_del_fdir_udpv4`:

i40e_add_del_fdir_udpv4
=======================

.. c:function:: int i40e_add_del_fdir_udpv4(struct i40e_vsi *vsi, struct i40e_fdir_filter *fd_data, bool add)

    Add/Remove UDPv4 filters

    :param vsi:
        pointer to the targeted VSI
    :type vsi: struct i40e_vsi \*

    :param fd_data:
        the flow director data required for the FDir descriptor
    :type fd_data: struct i40e_fdir_filter \*

    :param add:
        true adds a filter, false removes it
    :type add: bool

.. _`i40e_add_del_fdir_udpv4.description`:

Description
-----------

Returns 0 if the filters were successfully added or removed

.. _`i40e_add_del_fdir_tcpv4`:

i40e_add_del_fdir_tcpv4
=======================

.. c:function:: int i40e_add_del_fdir_tcpv4(struct i40e_vsi *vsi, struct i40e_fdir_filter *fd_data, bool add)

    Add/Remove TCPv4 filters

    :param vsi:
        pointer to the targeted VSI
    :type vsi: struct i40e_vsi \*

    :param fd_data:
        the flow director data required for the FDir descriptor
    :type fd_data: struct i40e_fdir_filter \*

    :param add:
        true adds a filter, false removes it
    :type add: bool

.. _`i40e_add_del_fdir_tcpv4.description`:

Description
-----------

Returns 0 if the filters were successfully added or removed

.. _`i40e_add_del_fdir_sctpv4`:

i40e_add_del_fdir_sctpv4
========================

.. c:function:: int i40e_add_del_fdir_sctpv4(struct i40e_vsi *vsi, struct i40e_fdir_filter *fd_data, bool add)

    Add/Remove SCTPv4 Flow Director filters for a specific flow spec

    :param vsi:
        pointer to the targeted VSI
    :type vsi: struct i40e_vsi \*

    :param fd_data:
        the flow director data required for the FDir descriptor
    :type fd_data: struct i40e_fdir_filter \*

    :param add:
        true adds a filter, false removes it
    :type add: bool

.. _`i40e_add_del_fdir_sctpv4.description`:

Description
-----------

Returns 0 if the filters were successfully added or removed

.. _`i40e_add_del_fdir_ipv4`:

i40e_add_del_fdir_ipv4
======================

.. c:function:: int i40e_add_del_fdir_ipv4(struct i40e_vsi *vsi, struct i40e_fdir_filter *fd_data, bool add)

    Add/Remove IPv4 Flow Director filters for a specific flow spec

    :param vsi:
        pointer to the targeted VSI
    :type vsi: struct i40e_vsi \*

    :param fd_data:
        the flow director data required for the FDir descriptor
    :type fd_data: struct i40e_fdir_filter \*

    :param add:
        true adds a filter, false removes it
    :type add: bool

.. _`i40e_add_del_fdir_ipv4.description`:

Description
-----------

Returns 0 if the filters were successfully added or removed

.. _`i40e_add_del_fdir`:

i40e_add_del_fdir
=================

.. c:function:: int i40e_add_del_fdir(struct i40e_vsi *vsi, struct i40e_fdir_filter *input, bool add)

    Build raw packets to add/del fdir filter

    :param vsi:
        pointer to the targeted VSI
    :type vsi: struct i40e_vsi \*

    :param input:
        filter to add or delete
    :type input: struct i40e_fdir_filter \*

    :param add:
        true adds a filter, false removes it
    :type add: bool

.. _`i40e_fd_handle_status`:

i40e_fd_handle_status
=====================

.. c:function:: void i40e_fd_handle_status(struct i40e_ring *rx_ring, union i40e_rx_desc *rx_desc, u8 prog_id)

    check the Programming Status for FD

    :param rx_ring:
        the Rx ring for this descriptor
    :type rx_ring: struct i40e_ring \*

    :param rx_desc:
        the Rx descriptor for programming Status, not a packet descriptor.
    :type rx_desc: union i40e_rx_desc \*

    :param prog_id:
        the id originally used for programming
    :type prog_id: u8

.. _`i40e_fd_handle_status.description`:

Description
-----------

This is used to verify if the FD programming or invalidation
requested by SW to the HW is successful or not and take actions accordingly.

.. _`i40e_unmap_and_free_tx_resource`:

i40e_unmap_and_free_tx_resource
===============================

.. c:function:: void i40e_unmap_and_free_tx_resource(struct i40e_ring *ring, struct i40e_tx_buffer *tx_buffer)

    Release a Tx buffer

    :param ring:
        the ring that owns the buffer
    :type ring: struct i40e_ring \*

    :param tx_buffer:
        the buffer to free
    :type tx_buffer: struct i40e_tx_buffer \*

.. _`i40e_clean_tx_ring`:

i40e_clean_tx_ring
==================

.. c:function:: void i40e_clean_tx_ring(struct i40e_ring *tx_ring)

    Free any empty Tx buffers

    :param tx_ring:
        ring to be cleaned
    :type tx_ring: struct i40e_ring \*

.. _`i40e_free_tx_resources`:

i40e_free_tx_resources
======================

.. c:function:: void i40e_free_tx_resources(struct i40e_ring *tx_ring)

    Free Tx resources per queue

    :param tx_ring:
        Tx descriptor ring for a specific queue
    :type tx_ring: struct i40e_ring \*

.. _`i40e_free_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`i40e_get_tx_pending`:

i40e_get_tx_pending
===================

.. c:function:: u32 i40e_get_tx_pending(struct i40e_ring *ring, bool in_sw)

    how many tx descriptors not processed

    :param ring:
        the ring of descriptors
    :type ring: struct i40e_ring \*

    :param in_sw:
        use SW variables
    :type in_sw: bool

.. _`i40e_get_tx_pending.description`:

Description
-----------

Since there is no access to the ring head register
in XL710, we need to use our local copies

.. _`i40e_detect_recover_hung`:

i40e_detect_recover_hung
========================

.. c:function:: void i40e_detect_recover_hung(struct i40e_vsi *vsi)

    Function to detect and recover hung_queues

    :param vsi:
        pointer to vsi struct with tx queues
    :type vsi: struct i40e_vsi \*

.. _`i40e_detect_recover_hung.description`:

Description
-----------

VSI has netdev and netdev has TX queues. This function is to check each of
those TX queues if they are hung, trigger recovery by issuing SW interrupt.

.. _`i40e_clean_tx_irq`:

i40e_clean_tx_irq
=================

.. c:function:: bool i40e_clean_tx_irq(struct i40e_vsi *vsi, struct i40e_ring *tx_ring, int napi_budget)

    Reclaim resources after transmit completes

    :param vsi:
        the VSI we care about
    :type vsi: struct i40e_vsi \*

    :param tx_ring:
        Tx ring to clean
    :type tx_ring: struct i40e_ring \*

    :param napi_budget:
        Used to determine if we are in netpoll
    :type napi_budget: int

.. _`i40e_clean_tx_irq.description`:

Description
-----------

Returns true if there's any budget left (e.g. the clean is finished)

.. _`i40e_enable_wb_on_itr`:

i40e_enable_wb_on_itr
=====================

.. c:function:: void i40e_enable_wb_on_itr(struct i40e_vsi *vsi, struct i40e_q_vector *q_vector)

    Arm hardware to do a wb, interrupts are not enabled

    :param vsi:
        the VSI we care about
    :type vsi: struct i40e_vsi \*

    :param q_vector:
        the vector on which to enable writeback
    :type q_vector: struct i40e_q_vector \*

.. _`i40e_force_wb`:

i40e_force_wb
=============

.. c:function:: void i40e_force_wb(struct i40e_vsi *vsi, struct i40e_q_vector *q_vector)

    Issue SW Interrupt so HW does a wb

    :param vsi:
        the VSI we care about
    :type vsi: struct i40e_vsi \*

    :param q_vector:
        the vector  on which to force writeback
    :type q_vector: struct i40e_q_vector \*

.. _`i40e_update_itr`:

i40e_update_itr
===============

.. c:function:: void i40e_update_itr(struct i40e_q_vector *q_vector, struct i40e_ring_container *rc)

    update the dynamic ITR value based on statistics

    :param q_vector:
        structure containing interrupt and ring information
    :type q_vector: struct i40e_q_vector \*

    :param rc:
        structure containing ring performance data
    :type rc: struct i40e_ring_container \*

.. _`i40e_update_itr.description`:

Description
-----------

Stores a new ITR value based on packets and byte
counts during the last interrupt.  The advantage of per interrupt
computation is faster updates and more accurate ITR for the current
traffic pattern.  Constants in this function were computed
based on theoretical maximum wire speed and thresholds were set based
on testing data as well as attempting to minimize response time
while increasing bulk throughput.

.. _`i40e_reuse_rx_page`:

i40e_reuse_rx_page
==================

.. c:function:: void i40e_reuse_rx_page(struct i40e_ring *rx_ring, struct i40e_rx_buffer *old_buff)

    page flip buffer and store it back on the ring

    :param rx_ring:
        rx descriptor ring to store buffers on
    :type rx_ring: struct i40e_ring \*

    :param old_buff:
        donor buffer to have page reused
    :type old_buff: struct i40e_rx_buffer \*

.. _`i40e_reuse_rx_page.description`:

Description
-----------

Synchronizes page for reuse by the adapter

.. _`i40e_rx_is_programming_status`:

i40e_rx_is_programming_status
=============================

.. c:function:: bool i40e_rx_is_programming_status(u64 qw)

    check for programming status descriptor

    :param qw:
        qword representing status_error_len in CPU ordering
    :type qw: u64

.. _`i40e_rx_is_programming_status.description`:

Description
-----------

The value of in the descriptor length field indicate if this
is a programming status descriptor for flow director or FCoE
by the value of I40E_RX_PROG_STATUS_DESC_LENGTH, otherwise
it is a packet descriptor.

.. _`i40e_clean_programming_status`:

i40e_clean_programming_status
=============================

.. c:function:: struct i40e_rx_buffer *i40e_clean_programming_status(struct i40e_ring *rx_ring, union i40e_rx_desc *rx_desc, u64 qw)

    try clean the programming status descriptor

    :param rx_ring:
        the rx ring that has this descriptor
    :type rx_ring: struct i40e_ring \*

    :param rx_desc:
        the rx descriptor written back by HW
    :type rx_desc: union i40e_rx_desc \*

    :param qw:
        qword representing status_error_len in CPU ordering
    :type qw: u64

.. _`i40e_clean_programming_status.description`:

Description
-----------

Flow director should handle FD_FILTER_STATUS to check its filter programming
status being successful or not and take actions accordingly. FCoE should
handle its context/filter programming/invalidation status and take actions.

Returns an i40e_rx_buffer to reuse if the cleanup occurred, otherwise NULL.

.. _`i40e_setup_tx_descriptors`:

i40e_setup_tx_descriptors
=========================

.. c:function:: int i40e_setup_tx_descriptors(struct i40e_ring *tx_ring)

    Allocate the Tx descriptors

    :param tx_ring:
        the tx ring to set up
    :type tx_ring: struct i40e_ring \*

.. _`i40e_setup_tx_descriptors.description`:

Description
-----------

Return 0 on success, negative on error

.. _`i40e_clean_rx_ring`:

i40e_clean_rx_ring
==================

.. c:function:: void i40e_clean_rx_ring(struct i40e_ring *rx_ring)

    Free Rx buffers

    :param rx_ring:
        ring to be cleaned
    :type rx_ring: struct i40e_ring \*

.. _`i40e_free_rx_resources`:

i40e_free_rx_resources
======================

.. c:function:: void i40e_free_rx_resources(struct i40e_ring *rx_ring)

    Free Rx resources

    :param rx_ring:
        ring to clean the resources from
    :type rx_ring: struct i40e_ring \*

.. _`i40e_free_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`i40e_setup_rx_descriptors`:

i40e_setup_rx_descriptors
=========================

.. c:function:: int i40e_setup_rx_descriptors(struct i40e_ring *rx_ring)

    Allocate Rx descriptors

    :param rx_ring:
        Rx descriptor ring (for a specific queue) to setup
    :type rx_ring: struct i40e_ring \*

.. _`i40e_setup_rx_descriptors.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`i40e_release_rx_desc`:

i40e_release_rx_desc
====================

.. c:function:: void i40e_release_rx_desc(struct i40e_ring *rx_ring, u32 val)

    Store the new tail and head values

    :param rx_ring:
        ring to bump
    :type rx_ring: struct i40e_ring \*

    :param val:
        new head index
    :type val: u32

.. _`i40e_rx_offset`:

i40e_rx_offset
==============

.. c:function:: unsigned int i40e_rx_offset(struct i40e_ring *rx_ring)

    Return expected offset into page to access data

    :param rx_ring:
        Ring we are requesting offset of
    :type rx_ring: struct i40e_ring \*

.. _`i40e_rx_offset.description`:

Description
-----------

Returns the offset value for ring into the data buffer.

.. _`i40e_alloc_mapped_page`:

i40e_alloc_mapped_page
======================

.. c:function:: bool i40e_alloc_mapped_page(struct i40e_ring *rx_ring, struct i40e_rx_buffer *bi)

    recycle or make a new page

    :param rx_ring:
        ring to use
    :type rx_ring: struct i40e_ring \*

    :param bi:
        rx_buffer struct to modify
    :type bi: struct i40e_rx_buffer \*

.. _`i40e_alloc_mapped_page.description`:

Description
-----------

Returns true if the page was successfully allocated or
reused.

.. _`i40e_receive_skb`:

i40e_receive_skb
================

.. c:function:: void i40e_receive_skb(struct i40e_ring *rx_ring, struct sk_buff *skb, u16 vlan_tag)

    Send a completed packet up the stack

    :param rx_ring:
        rx ring in play
    :type rx_ring: struct i40e_ring \*

    :param skb:
        packet to send up
    :type skb: struct sk_buff \*

    :param vlan_tag:
        vlan tag for packet
    :type vlan_tag: u16

.. _`i40e_alloc_rx_buffers`:

i40e_alloc_rx_buffers
=====================

.. c:function:: bool i40e_alloc_rx_buffers(struct i40e_ring *rx_ring, u16 cleaned_count)

    Replace used receive buffers

    :param rx_ring:
        ring to place buffers on
    :type rx_ring: struct i40e_ring \*

    :param cleaned_count:
        number of buffers to replace
    :type cleaned_count: u16

.. _`i40e_alloc_rx_buffers.description`:

Description
-----------

Returns false if all allocations were successful, true if any fail

.. _`i40e_rx_checksum`:

i40e_rx_checksum
================

.. c:function:: void i40e_rx_checksum(struct i40e_vsi *vsi, struct sk_buff *skb, union i40e_rx_desc *rx_desc)

    Indicate in skb if hw indicated a good cksum

    :param vsi:
        the VSI we care about
    :type vsi: struct i40e_vsi \*

    :param skb:
        skb currently being received and modified
    :type skb: struct sk_buff \*

    :param rx_desc:
        the receive descriptor
    :type rx_desc: union i40e_rx_desc \*

.. _`i40e_ptype_to_htype`:

i40e_ptype_to_htype
===================

.. c:function:: int i40e_ptype_to_htype(u8 ptype)

    get a hash type

    :param ptype:
        the ptype value from the descriptor
    :type ptype: u8

.. _`i40e_ptype_to_htype.description`:

Description
-----------

Returns a hash type to be used by skb_set_hash

.. _`i40e_rx_hash`:

i40e_rx_hash
============

.. c:function:: void i40e_rx_hash(struct i40e_ring *ring, union i40e_rx_desc *rx_desc, struct sk_buff *skb, u8 rx_ptype)

    set the hash value in the skb

    :param ring:
        descriptor ring
    :type ring: struct i40e_ring \*

    :param rx_desc:
        specific descriptor
    :type rx_desc: union i40e_rx_desc \*

    :param skb:
        skb currently being received and modified
    :type skb: struct sk_buff \*

    :param rx_ptype:
        Rx packet type
    :type rx_ptype: u8

.. _`i40e_process_skb_fields`:

i40e_process_skb_fields
=======================

.. c:function:: void i40e_process_skb_fields(struct i40e_ring *rx_ring, union i40e_rx_desc *rx_desc, struct sk_buff *skb, u8 rx_ptype)

    Populate skb header fields from Rx descriptor

    :param rx_ring:
        rx descriptor ring packet is being transacted on
    :type rx_ring: struct i40e_ring \*

    :param rx_desc:
        pointer to the EOP Rx descriptor
    :type rx_desc: union i40e_rx_desc \*

    :param skb:
        pointer to current skb being populated
    :type skb: struct sk_buff \*

    :param rx_ptype:
        the packet type decoded by hardware
    :type rx_ptype: u8

.. _`i40e_process_skb_fields.description`:

Description
-----------

This function checks the ring, descriptor, and packet information in
order to populate the hash, checksum, VLAN, protocol, and
other fields within the skb.

.. _`i40e_cleanup_headers`:

i40e_cleanup_headers
====================

.. c:function:: bool i40e_cleanup_headers(struct i40e_ring *rx_ring, struct sk_buff *skb, union i40e_rx_desc *rx_desc)

    Correct empty headers

    :param rx_ring:
        rx descriptor ring packet is being transacted on
    :type rx_ring: struct i40e_ring \*

    :param skb:
        pointer to current skb being fixed
    :type skb: struct sk_buff \*

    :param rx_desc:
        pointer to the EOP Rx descriptor
    :type rx_desc: union i40e_rx_desc \*

.. _`i40e_cleanup_headers.description`:

Description
-----------

Also address the case where we are pulling data in on pages only
and as such no data is present in the skb header.

In addition if skb is not at least 60 bytes we need to pad it so that
it is large enough to qualify as a valid Ethernet frame.

Returns true if an error was encountered and skb was freed.

.. _`i40e_page_is_reusable`:

i40e_page_is_reusable
=====================

.. c:function:: bool i40e_page_is_reusable(struct page *page)

    check if any reuse is possible

    :param page:
        page struct to check
    :type page: struct page \*

.. _`i40e_page_is_reusable.description`:

Description
-----------

A page is not reusable if it was allocated under low memory
conditions, or it's not in the same NUMA node as this CPU.

.. _`i40e_can_reuse_rx_page`:

i40e_can_reuse_rx_page
======================

.. c:function:: bool i40e_can_reuse_rx_page(struct i40e_rx_buffer *rx_buffer)

    Determine if this page can be reused by the adapter for another receive

    :param rx_buffer:
        buffer containing the page
    :type rx_buffer: struct i40e_rx_buffer \*

.. _`i40e_can_reuse_rx_page.description`:

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

.. _`i40e_add_rx_frag`:

i40e_add_rx_frag
================

.. c:function:: void i40e_add_rx_frag(struct i40e_ring *rx_ring, struct i40e_rx_buffer *rx_buffer, struct sk_buff *skb, unsigned int size)

    Add contents of Rx buffer to sk_buff

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct i40e_ring \*

    :param rx_buffer:
        buffer containing page to add
    :type rx_buffer: struct i40e_rx_buffer \*

    :param skb:
        sk_buff to place the data into
    :type skb: struct sk_buff \*

    :param size:
        packet length from rx_desc
    :type size: unsigned int

.. _`i40e_add_rx_frag.description`:

Description
-----------

This function will add the data contained in rx_buffer->page to the skb.
It will just attach the page as a frag to the skb.

The function will then update the page offset.

.. _`i40e_get_rx_buffer`:

i40e_get_rx_buffer
==================

.. c:function:: struct i40e_rx_buffer *i40e_get_rx_buffer(struct i40e_ring *rx_ring, const unsigned int size)

    Fetch Rx buffer and synchronize data for use

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct i40e_ring \*

    :param size:
        size of buffer to add to skb
    :type size: const unsigned int

.. _`i40e_get_rx_buffer.description`:

Description
-----------

This function will pull an Rx buffer from the ring and synchronize it
for use by the CPU.

.. _`i40e_construct_skb`:

i40e_construct_skb
==================

.. c:function:: struct sk_buff *i40e_construct_skb(struct i40e_ring *rx_ring, struct i40e_rx_buffer *rx_buffer, struct xdp_buff *xdp)

    Allocate skb and populate it

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct i40e_ring \*

    :param rx_buffer:
        rx buffer to pull data from
    :type rx_buffer: struct i40e_rx_buffer \*

    :param xdp:
        xdp_buff pointing to the data
    :type xdp: struct xdp_buff \*

.. _`i40e_construct_skb.description`:

Description
-----------

This function allocates an skb.  It then populates it with the page
data from the current receive descriptor, taking care to set up the
skb correctly.

.. _`i40e_build_skb`:

i40e_build_skb
==============

.. c:function:: struct sk_buff *i40e_build_skb(struct i40e_ring *rx_ring, struct i40e_rx_buffer *rx_buffer, struct xdp_buff *xdp)

    Build skb around an existing buffer

    :param rx_ring:
        Rx descriptor ring to transact packets on
    :type rx_ring: struct i40e_ring \*

    :param rx_buffer:
        Rx buffer to pull data from
    :type rx_buffer: struct i40e_rx_buffer \*

    :param xdp:
        xdp_buff pointing to the data
    :type xdp: struct xdp_buff \*

.. _`i40e_build_skb.description`:

Description
-----------

This function builds an skb around an existing Rx buffer, taking care
to set up the skb correctly and avoid any memcpy overhead.

.. _`i40e_put_rx_buffer`:

i40e_put_rx_buffer
==================

.. c:function:: void i40e_put_rx_buffer(struct i40e_ring *rx_ring, struct i40e_rx_buffer *rx_buffer)

    Clean up used buffer and either recycle or free

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct i40e_ring \*

    :param rx_buffer:
        rx buffer to pull data from
    :type rx_buffer: struct i40e_rx_buffer \*

.. _`i40e_put_rx_buffer.description`:

Description
-----------

This function will clean up the contents of the rx_buffer.  It will
either recycle the buffer or unmap it and free the associated resources.

.. _`i40e_is_non_eop`:

i40e_is_non_eop
===============

.. c:function:: bool i40e_is_non_eop(struct i40e_ring *rx_ring, union i40e_rx_desc *rx_desc, struct sk_buff *skb)

    process handling of non-EOP buffers

    :param rx_ring:
        Rx ring being processed
    :type rx_ring: struct i40e_ring \*

    :param rx_desc:
        Rx descriptor for current buffer
    :type rx_desc: union i40e_rx_desc \*

    :param skb:
        Current socket buffer containing buffer in progress
    :type skb: struct sk_buff \*

.. _`i40e_is_non_eop.description`:

Description
-----------

This function updates next to clean.  If the buffer is an EOP buffer
this function exits returning false, otherwise it will place the
sk_buff in the next buffer to be chained and return true indicating
that this is in fact a non-EOP buffer.

.. _`i40e_run_xdp`:

i40e_run_xdp
============

.. c:function:: struct sk_buff *i40e_run_xdp(struct i40e_ring *rx_ring, struct xdp_buff *xdp)

    run an XDP program

    :param rx_ring:
        Rx ring being processed
    :type rx_ring: struct i40e_ring \*

    :param xdp:
        XDP buffer containing the frame
    :type xdp: struct xdp_buff \*

.. _`i40e_rx_buffer_flip`:

i40e_rx_buffer_flip
===================

.. c:function:: void i40e_rx_buffer_flip(struct i40e_ring *rx_ring, struct i40e_rx_buffer *rx_buffer, unsigned int size)

    adjusted rx_buffer to point to an unused region

    :param rx_ring:
        Rx ring
    :type rx_ring: struct i40e_ring \*

    :param rx_buffer:
        Rx buffer to adjust
    :type rx_buffer: struct i40e_rx_buffer \*

    :param size:
        Size of adjustment
    :type size: unsigned int

.. _`i40e_xdp_ring_update_tail`:

i40e_xdp_ring_update_tail
=========================

.. c:function:: void i40e_xdp_ring_update_tail(struct i40e_ring *xdp_ring)

    Updates the XDP Tx ring tail register

    :param xdp_ring:
        XDP Tx ring
    :type xdp_ring: struct i40e_ring \*

.. _`i40e_xdp_ring_update_tail.description`:

Description
-----------

This function updates the XDP Tx ring tail register.

.. _`i40e_update_rx_stats`:

i40e_update_rx_stats
====================

.. c:function:: void i40e_update_rx_stats(struct i40e_ring *rx_ring, unsigned int total_rx_bytes, unsigned int total_rx_packets)

    Update Rx ring statistics

    :param rx_ring:
        rx descriptor ring
    :type rx_ring: struct i40e_ring \*

    :param total_rx_bytes:
        number of bytes received
    :type total_rx_bytes: unsigned int

    :param total_rx_packets:
        number of packets received
    :type total_rx_packets: unsigned int

.. _`i40e_update_rx_stats.description`:

Description
-----------

This function updates the Rx ring statistics.

.. _`i40e_finalize_xdp_rx`:

i40e_finalize_xdp_rx
====================

.. c:function:: void i40e_finalize_xdp_rx(struct i40e_ring *rx_ring, unsigned int xdp_res)

    Bump XDP Tx tail and/or flush redirect map

    :param rx_ring:
        Rx ring
    :type rx_ring: struct i40e_ring \*

    :param xdp_res:
        Result of the receive batch
    :type xdp_res: unsigned int

.. _`i40e_finalize_xdp_rx.description`:

Description
-----------

This function bumps XDP Tx tail and/or flush redirect map, and
should be called when a batch of packets has been processed in the
napi loop.

.. _`i40e_clean_rx_irq`:

i40e_clean_rx_irq
=================

.. c:function:: int i40e_clean_rx_irq(struct i40e_ring *rx_ring, int budget)

    Clean completed descriptors from Rx ring - bounce buf

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct i40e_ring \*

    :param budget:
        Total limit on number of packets to process
    :type budget: int

.. _`i40e_clean_rx_irq.description`:

Description
-----------

This function provides a "bounce buffer" approach to Rx interrupt
processing.  The advantage to this is that on systems that have
expensive overhead for IOMMU access this provides a means of avoiding
it by maintaining the mapping of the page to the system.

Returns amount of work completed

.. _`i40e_update_enable_itr`:

i40e_update_enable_itr
======================

.. c:function:: void i40e_update_enable_itr(struct i40e_vsi *vsi, struct i40e_q_vector *q_vector)

    Update itr and re-enable MSIX interrupt

    :param vsi:
        the VSI we care about
    :type vsi: struct i40e_vsi \*

    :param q_vector:
        q_vector for which itr is being updated and interrupt enabled
    :type q_vector: struct i40e_q_vector \*

.. _`i40e_napi_poll`:

i40e_napi_poll
==============

.. c:function:: int i40e_napi_poll(struct napi_struct *napi, int budget)

    NAPI polling Rx/Tx cleanup routine

    :param napi:
        napi struct with our devices info in it
    :type napi: struct napi_struct \*

    :param budget:
        amount of work driver is allowed to do this pass, in packets
    :type budget: int

.. _`i40e_napi_poll.description`:

Description
-----------

This function will clean all queues associated with a q_vector.

Returns the amount of work done

.. _`i40e_atr`:

i40e_atr
========

.. c:function:: void i40e_atr(struct i40e_ring *tx_ring, struct sk_buff *skb, u32 tx_flags)

    Add a Flow Director ATR filter

    :param tx_ring:
        ring to add programming descriptor to
    :type tx_ring: struct i40e_ring \*

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

    :param tx_flags:
        send tx flags
    :type tx_flags: u32

.. _`i40e_tx_prepare_vlan_flags`:

i40e_tx_prepare_vlan_flags
==========================

.. c:function:: int i40e_tx_prepare_vlan_flags(struct sk_buff *skb, struct i40e_ring *tx_ring, u32 *flags)

    prepare generic TX VLAN tagging flags for HW

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

    :param tx_ring:
        ring to send buffer on
    :type tx_ring: struct i40e_ring \*

    :param flags:
        the tx flags to be set
    :type flags: u32 \*

.. _`i40e_tx_prepare_vlan_flags.description`:

Description
-----------

Checks the skb and set up correspondingly several generic transmit flags
related to VLAN tagging for the HW, such as VLAN, DCB, etc.

Returns error code indicate the frame should be dropped upon error and the
otherwise  returns 0 to indicate the flags has been set properly.

.. _`i40e_tso`:

i40e_tso
========

.. c:function:: int i40e_tso(struct i40e_tx_buffer *first, u8 *hdr_len, u64 *cd_type_cmd_tso_mss)

    set up the tso context descriptor

    :param first:
        pointer to first Tx buffer for xmit
    :type first: struct i40e_tx_buffer \*

    :param hdr_len:
        ptr to the size of the packet header
    :type hdr_len: u8 \*

    :param cd_type_cmd_tso_mss:
        Quad Word 1
    :type cd_type_cmd_tso_mss: u64 \*

.. _`i40e_tso.description`:

Description
-----------

Returns 0 if no TSO can happen, 1 if tso is going, or error

.. _`i40e_tsyn`:

i40e_tsyn
=========

.. c:function:: int i40e_tsyn(struct i40e_ring *tx_ring, struct sk_buff *skb, u32 tx_flags, u64 *cd_type_cmd_tso_mss)

    set up the tsyn context descriptor

    :param tx_ring:
        ptr to the ring to send
    :type tx_ring: struct i40e_ring \*

    :param skb:
        ptr to the skb we're sending
    :type skb: struct sk_buff \*

    :param tx_flags:
        the collected send information
    :type tx_flags: u32

    :param cd_type_cmd_tso_mss:
        Quad Word 1
    :type cd_type_cmd_tso_mss: u64 \*

.. _`i40e_tsyn.description`:

Description
-----------

Returns 0 if no Tx timestamp can happen and 1 if the timestamp will happen

.. _`i40e_tx_enable_csum`:

i40e_tx_enable_csum
===================

.. c:function:: int i40e_tx_enable_csum(struct sk_buff *skb, u32 *tx_flags, u32 *td_cmd, u32 *td_offset, struct i40e_ring *tx_ring, u32 *cd_tunneling)

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
    :type tx_ring: struct i40e_ring \*

    :param cd_tunneling:
        ptr to context desc bits
    :type cd_tunneling: u32 \*

.. _`i40e_create_tx_ctx`:

i40e_create_tx_ctx
==================

.. c:function:: void i40e_create_tx_ctx(struct i40e_ring *tx_ring, const u64 cd_type_cmd_tso_mss, const u32 cd_tunneling, const u32 cd_l2tag2)

    :param tx_ring:
        ring to create the descriptor on
    :type tx_ring: struct i40e_ring \*

    :param cd_type_cmd_tso_mss:
        Quad Word 1
    :type cd_type_cmd_tso_mss: const u64

    :param cd_tunneling:
        Quad Word 0 - bits 0-31
    :type cd_tunneling: const u32

    :param cd_l2tag2:
        Quad Word 0 - bits 32-63
    :type cd_l2tag2: const u32

.. _`__i40e_maybe_stop_tx`:

\__i40e_maybe_stop_tx
=====================

.. c:function:: int __i40e_maybe_stop_tx(struct i40e_ring *tx_ring, int size)

    2nd level check for tx stop conditions

    :param tx_ring:
        the ring to be checked
    :type tx_ring: struct i40e_ring \*

    :param size:
        the size buffer we want to assure is available
    :type size: int

.. _`__i40e_maybe_stop_tx.description`:

Description
-----------

Returns -EBUSY if a stop is needed, else 0

.. _`__i40e_chk_linearize`:

\__i40e_chk_linearize
=====================

.. c:function:: bool __i40e_chk_linearize(struct sk_buff *skb)

    Check if there are more than 8 buffers per packet

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

.. _`__i40e_chk_linearize.note`:

Note
----

Our HW can't DMA more than 8 buffers to build a packet on the wire
and so we need to figure out the cases where we need to linearize the skb.

For TSO we need to count the TSO header and segment payload separately.
As such we need to check cases where we have 7 fragments or more as we
can potentially require 9 DMA transactions, 1 for the TSO header, 1 for
the segment payload in the first descriptor, and another 7 for the
fragments.

.. _`i40e_tx_map`:

i40e_tx_map
===========

.. c:function:: int i40e_tx_map(struct i40e_ring *tx_ring, struct sk_buff *skb, struct i40e_tx_buffer *first, u32 tx_flags, const u8 hdr_len, u32 td_cmd, u32 td_offset)

    Build the Tx descriptor

    :param tx_ring:
        ring to send buffer on
    :type tx_ring: struct i40e_ring \*

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

    :param first:
        first buffer info buffer to use
    :type first: struct i40e_tx_buffer \*

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

.. _`i40e_tx_map.description`:

Description
-----------

Returns 0 on success, -1 on failure to DMA

.. _`i40e_xmit_xdp_ring`:

i40e_xmit_xdp_ring
==================

.. c:function:: int i40e_xmit_xdp_ring(struct xdp_frame *xdpf, struct i40e_ring *xdp_ring)

    transmits an XDP buffer to an XDP Tx ring

    :param xdpf:
        *undescribed*
    :type xdpf: struct xdp_frame \*

    :param xdp_ring:
        XDP Tx ring
    :type xdp_ring: struct i40e_ring \*

.. _`i40e_xmit_frame_ring`:

i40e_xmit_frame_ring
====================

.. c:function:: netdev_tx_t i40e_xmit_frame_ring(struct sk_buff *skb, struct i40e_ring *tx_ring)

    Sends buffer on Tx ring

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

    :param tx_ring:
        ring to send buffer on
    :type tx_ring: struct i40e_ring \*

.. _`i40e_xmit_frame_ring.description`:

Description
-----------

Returns NETDEV_TX_OK if sent, else an error code

.. _`i40e_lan_xmit_frame`:

i40e_lan_xmit_frame
===================

.. c:function:: netdev_tx_t i40e_lan_xmit_frame(struct sk_buff *skb, struct net_device *netdev)

    Selects the correct VSI and Tx queue to send buffer

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`i40e_lan_xmit_frame.description`:

Description
-----------

Returns NETDEV_TX_OK if sent, else an error code

.. _`i40e_xdp_xmit`:

i40e_xdp_xmit
=============

.. c:function:: int i40e_xdp_xmit(struct net_device *dev, int n, struct xdp_frame **frames, u32 flags)

    Implements ndo_xdp_xmit

    :param dev:
        netdev
    :type dev: struct net_device \*

    :param n:
        *undescribed*
    :type n: int

    :param frames:
        *undescribed*
    :type frames: struct xdp_frame \*\*

    :param flags:
        *undescribed*
    :type flags: u32

.. _`i40e_xdp_xmit.description`:

Description
-----------

Returns number of frames successfully sent. Frames that fail are
free'ed via XDP return API.

For error cases, a negative errno code is returned and no-frames
are transmitted (caller must handle freeing frames).

.. This file was automatic generated / don't edit.

