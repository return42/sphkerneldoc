.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4vf/sge.c

.. _`get_buf_addr`:

get_buf_addr
============

.. c:function:: dma_addr_t get_buf_addr(const struct rx_sw_desc *sdesc)

    return DMA buffer address of software descriptor

    :param sdesc:
        pointer to the software buffer descriptor
    :type sdesc: const struct rx_sw_desc \*

.. _`get_buf_addr.description`:

Description
-----------

Return the DMA buffer address of a software descriptor (stripping out
our low-order flag bits).

.. _`is_buf_mapped`:

is_buf_mapped
=============

.. c:function:: bool is_buf_mapped(const struct rx_sw_desc *sdesc)

    is buffer mapped for DMA?

    :param sdesc:
        pointer to the software buffer descriptor
    :type sdesc: const struct rx_sw_desc \*

.. _`is_buf_mapped.description`:

Description
-----------

Determine whether the buffer associated with a software descriptor in
mapped for DMA or not.

.. _`need_skb_unmap`:

need_skb_unmap
==============

.. c:function:: int need_skb_unmap( void)

    does the platform need unmapping of sk_buffs?

    :param void:
        no arguments
    :type void: 

.. _`need_skb_unmap.description`:

Description
-----------

Returns true if the platform needs sk_buff unmapping.  The compiler
optimizes away unnecessary code if this returns true.

.. _`txq_avail`:

txq_avail
=========

.. c:function:: unsigned int txq_avail(const struct sge_txq *tq)

    return the number of available slots in a TX queue

    :param tq:
        the TX queue
    :type tq: const struct sge_txq \*

.. _`txq_avail.description`:

Description
-----------

Returns the number of available descriptors in a TX queue.

.. _`fl_cap`:

fl_cap
======

.. c:function:: unsigned int fl_cap(const struct sge_fl *fl)

    return the capacity of a Free List

    :param fl:
        the Free List
    :type fl: const struct sge_fl \*

.. _`fl_cap.description`:

Description
-----------

Returns the capacity of a Free List.  The capacity is less than the
size because an Egress Queue Index Unit worth of descriptors needs to
be left unpopulated, otherwise the Producer and Consumer indices PIDX
and CIDX will match and the hardware will think the FL is empty.

.. _`fl_starving`:

fl_starving
===========

.. c:function:: bool fl_starving(const struct adapter *adapter, const struct sge_fl *fl)

    return whether a Free List is starving.

    :param adapter:
        pointer to the adapter
    :type adapter: const struct adapter \*

    :param fl:
        the Free List
    :type fl: const struct sge_fl \*

.. _`fl_starving.description`:

Description
-----------

Tests specified Free List to see whether the number of buffers
available to the hardware has falled below our "starvation"
threshold.

.. _`map_skb`:

map_skb
=======

.. c:function:: int map_skb(struct device *dev, const struct sk_buff *skb, dma_addr_t *addr)

    map an skb for DMA to the device

    :param dev:
        the egress net device
    :type dev: struct device \*

    :param skb:
        the packet to map
    :type skb: const struct sk_buff \*

    :param addr:
        a pointer to the base of the DMA mapping array
    :type addr: dma_addr_t \*

.. _`map_skb.description`:

Description
-----------

Map an skb for DMA to the device and return an array of DMA addresses.

.. _`free_tx_desc`:

free_tx_desc
============

.. c:function:: void free_tx_desc(struct adapter *adapter, struct sge_txq *tq, unsigned int n, bool unmap)

    reclaims TX descriptors and their buffers

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param tq:
        the TX queue to reclaim descriptors from
    :type tq: struct sge_txq \*

    :param n:
        the number of descriptors to reclaim
    :type n: unsigned int

    :param unmap:
        whether the buffers should be unmapped for DMA
    :type unmap: bool

.. _`free_tx_desc.description`:

Description
-----------

Reclaims TX descriptors from an SGE TX queue and frees the associated
TX buffers.  Called with the TX queue lock held.

.. _`reclaim_completed_tx`:

reclaim_completed_tx
====================

.. c:function:: void reclaim_completed_tx(struct adapter *adapter, struct sge_txq *tq, bool unmap)

    reclaims completed TX descriptors

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param tq:
        the TX queue to reclaim completed descriptors from
    :type tq: struct sge_txq \*

    :param unmap:
        whether the buffers should be unmapped for DMA
    :type unmap: bool

.. _`reclaim_completed_tx.description`:

Description
-----------

Reclaims TX descriptors that the SGE has indicated it has processed,
and frees the associated buffers if possible.  Called with the TX
queue locked.

.. _`get_buf_size`:

get_buf_size
============

.. c:function:: int get_buf_size(const struct adapter *adapter, const struct rx_sw_desc *sdesc)

    return the size of an RX Free List buffer.

    :param adapter:
        pointer to the associated adapter
    :type adapter: const struct adapter \*

    :param sdesc:
        pointer to the software buffer descriptor
    :type sdesc: const struct rx_sw_desc \*

.. _`free_rx_bufs`:

free_rx_bufs
============

.. c:function:: void free_rx_bufs(struct adapter *adapter, struct sge_fl *fl, int n)

    free RX buffers on an SGE Free List

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param fl:
        the SGE Free List to free buffers from
    :type fl: struct sge_fl \*

    :param n:
        how many buffers to free
    :type n: int

.. _`free_rx_bufs.description`:

Description
-----------

Release the next \ ``n``\  buffers on an SGE Free List RX queue.   The
buffers must be made inaccessible to hardware before calling this
function.

.. _`unmap_rx_buf`:

unmap_rx_buf
============

.. c:function:: void unmap_rx_buf(struct adapter *adapter, struct sge_fl *fl)

    unmap the current RX buffer on an SGE Free List

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param fl:
        the SGE Free List
    :type fl: struct sge_fl \*

.. _`unmap_rx_buf.description`:

Description
-----------

Unmap the current buffer on an SGE Free List RX queue.   The
buffer must be made inaccessible to HW before calling this function.

This is similar to \ ``free_rx_bufs``\  above but does not free the buffer.
Do note that the FL still loses any further access to the buffer.
This is used predominantly to "transfer ownership" of an FL buffer
to another entity (typically an skb's fragment list).

.. _`ring_fl_db`:

ring_fl_db
==========

.. c:function:: void ring_fl_db(struct adapter *adapter, struct sge_fl *fl)

    righ doorbell on free list

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param fl:
        the Free List whose doorbell should be rung ...
    :type fl: struct sge_fl \*

.. _`ring_fl_db.description`:

Description
-----------

Tell the Scatter Gather Engine that there are new free list entries
available.

.. _`set_rx_sw_desc`:

set_rx_sw_desc
==============

.. c:function:: void set_rx_sw_desc(struct rx_sw_desc *sdesc, struct page *page, dma_addr_t dma_addr)

    initialize software RX buffer descriptor

    :param sdesc:
        pointer to the softwore RX buffer descriptor
    :type sdesc: struct rx_sw_desc \*

    :param page:
        pointer to the page data structure backing the RX buffer
    :type page: struct page \*

    :param dma_addr:
        PCI DMA address (possibly with low-bit flags)
    :type dma_addr: dma_addr_t

.. _`refill_fl`:

refill_fl
=========

.. c:function:: unsigned int refill_fl(struct adapter *adapter, struct sge_fl *fl, int n, gfp_t gfp)

    refill an SGE RX buffer ring

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param fl:
        the Free List ring to refill
    :type fl: struct sge_fl \*

    :param n:
        the number of new buffers to allocate
    :type n: int

    :param gfp:
        the gfp flags for the allocations
    :type gfp: gfp_t

.. _`refill_fl.description`:

Description
-----------

(Re)populate an SGE free-buffer queue with up to \ ``n``\  new packet buffers,
allocated with the supplied gfp flags.  The caller must assure that
\ ``n``\  does not exceed the queue's capacity -- i.e. (cidx == pidx) \_IN
EGRESS QUEUE UNITS\_ indicates an empty Free List!  Returns the number
of buffers allocated.  If afterwards the queue is found critically low,
mark it as starving in the bitmap of starving FLs.

.. _`alloc_ring`:

alloc_ring
==========

.. c:function:: void *alloc_ring(struct device *dev, size_t nelem, size_t hwsize, size_t swsize, dma_addr_t *busaddrp, void *swringp, size_t stat_size)

    allocate resources for an SGE descriptor ring

    :param dev:
        the PCI device's core device
    :type dev: struct device \*

    :param nelem:
        the number of descriptors
    :type nelem: size_t

    :param hwsize:
        the size of each hardware descriptor
    :type hwsize: size_t

    :param swsize:
        the size of each software descriptor
    :type swsize: size_t

    :param busaddrp:
        the physical PCI bus address of the allocated ring
    :type busaddrp: dma_addr_t \*

    :param swringp:
        return address pointer for software ring
    :type swringp: void \*

    :param stat_size:
        extra space in hardware ring for status information
    :type stat_size: size_t

.. _`alloc_ring.description`:

Description
-----------

Allocates resources for an SGE descriptor ring, such as TX queues,
free buffer lists, response queues, etc.  Each SGE ring requires
space for its hardware descriptors plus, optionally, space for software
state associated with each hardware entry (the metadata).  The function

.. _`alloc_ring.returns-three-values`:

returns three values
--------------------

the virtual address for the hardware ring (the
return value of the function), the PCI bus address of the hardware
ring (in \*busaddrp), and the address of the software ring (in swringp).
Both the hardware and software rings are returned zeroed out.

.. _`sgl_len`:

sgl_len
=======

.. c:function:: unsigned int sgl_len(unsigned int n)

    calculates the size of an SGL of the given capacity

    :param n:
        the number of SGL entries
    :type n: unsigned int

.. _`sgl_len.description`:

Description
-----------

Calculates the number of flits (8-byte units) needed for a Direct
Scatter/Gather List that can hold the given number of entries.

.. _`flits_to_desc`:

flits_to_desc
=============

.. c:function:: unsigned int flits_to_desc(unsigned int flits)

    returns the num of TX descriptors for the given flits

    :param flits:
        the number of flits
    :type flits: unsigned int

.. _`flits_to_desc.description`:

Description
-----------

Returns the number of TX descriptors needed for the supplied number
of flits.

.. _`is_eth_imm`:

is_eth_imm
==========

.. c:function:: int is_eth_imm(const struct sk_buff *skb)

    can an Ethernet packet be sent as immediate data?

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

.. _`is_eth_imm.description`:

Description
-----------

Returns whether an Ethernet packet is small enough to fit completely as
immediate data.

.. _`calc_tx_flits`:

calc_tx_flits
=============

.. c:function:: unsigned int calc_tx_flits(const struct sk_buff *skb)

    calculate the number of flits for a packet TX WR

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

.. _`calc_tx_flits.description`:

Description
-----------

Returns the number of flits needed for a TX Work Request for the
given Ethernet packet, including the needed WR and CPL headers.

.. _`write_sgl`:

write_sgl
=========

.. c:function:: void write_sgl(const struct sk_buff *skb, struct sge_txq *tq, struct ulptx_sgl *sgl, u64 *end, unsigned int start, const dma_addr_t *addr)

    populate a Scatter/Gather List for a packet

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

    :param tq:
        the TX queue we are writing into
    :type tq: struct sge_txq \*

    :param sgl:
        starting location for writing the SGL
    :type sgl: struct ulptx_sgl \*

    :param end:
        points right after the end of the SGL
    :type end: u64 \*

    :param start:
        start offset into skb main-body data to include in the SGL
    :type start: unsigned int

    :param addr:
        the list of DMA bus addresses for the SGL elements
    :type addr: const dma_addr_t \*

.. _`write_sgl.description`:

Description
-----------

Generates a Scatter/Gather List for the buffers that make up a packet.
The caller must provide adequate space for the SGL that will be written.
The SGL includes all of the packet's page fragments and the data in its
main body except for the first \ ``start``\  bytes.  \ ``pos``\  must be 16-byte
aligned and within a TX descriptor with available space.  \ ``end``\  points
write after the end of the SGL but does not account for any potential
wrap around, i.e., \ ``end``\  > \ ``tq->stat``\ .

.. _`ring_tx_db`:

ring_tx_db
==========

.. c:function:: void ring_tx_db(struct adapter *adapter, struct sge_txq *tq, int n)

    check and potentially ring a TX queue's doorbell

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param tq:
        the TX queue
    :type tq: struct sge_txq \*

    :param n:
        number of new descriptors to give to HW
    :type n: int

.. _`ring_tx_db.description`:

Description
-----------

Ring the doorbel for a TX queue.

.. _`inline_tx_skb`:

inline_tx_skb
=============

.. c:function:: void inline_tx_skb(const struct sk_buff *skb, const struct sge_txq *tq, void *pos)

    inline a packet's data into TX descriptors

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

    :param tq:
        the TX queue where the packet will be inlined
    :type tq: const struct sge_txq \*

    :param pos:
        starting position in the TX queue to inline the packet
    :type pos: void \*

.. _`inline_tx_skb.description`:

Description
-----------

Inline a packet's contents directly into TX descriptors, starting at
the given position within the TX DMA ring.
Most of the complexity of this operation is dealing with wrap arounds
in the middle of the packet we want to inline.

.. _`t4vf_eth_xmit`:

t4vf_eth_xmit
=============

.. c:function:: int t4vf_eth_xmit(struct sk_buff *skb, struct net_device *dev)

    add a packet to an Ethernet TX queue

    :param skb:
        the packet
    :type skb: struct sk_buff \*

    :param dev:
        the egress net device
    :type dev: struct net_device \*

.. _`t4vf_eth_xmit.description`:

Description
-----------

Add a packet to an SGE Ethernet TX queue.  Runs with softirqs disabled.

.. _`copy_frags`:

copy_frags
==========

.. c:function:: void copy_frags(struct sk_buff *skb, const struct pkt_gl *gl, unsigned int offset)

    copy fragments from gather list into skb_shared_info

    :param skb:
        destination skb
    :type skb: struct sk_buff \*

    :param gl:
        source internal packet gather list
    :type gl: const struct pkt_gl \*

    :param offset:
        packet start offset in first page
    :type offset: unsigned int

.. _`copy_frags.description`:

Description
-----------

Copy an internal packet gather list into a Linux skb_shared_info
structure.

.. _`t4vf_pktgl_to_skb`:

t4vf_pktgl_to_skb
=================

.. c:function:: struct sk_buff *t4vf_pktgl_to_skb(const struct pkt_gl *gl, unsigned int skb_len, unsigned int pull_len)

    build an sk_buff from a packet gather list

    :param gl:
        the gather list
    :type gl: const struct pkt_gl \*

    :param skb_len:
        size of sk_buff main body if it carries fragments
    :type skb_len: unsigned int

    :param pull_len:
        amount of data to move to the sk_buff's main body
    :type pull_len: unsigned int

.. _`t4vf_pktgl_to_skb.description`:

Description
-----------

Builds an sk_buff from the given packet gather list.  Returns the
sk_buff or \ ``NULL``\  if sk_buff allocation failed.

.. _`t4vf_pktgl_free`:

t4vf_pktgl_free
===============

.. c:function:: void t4vf_pktgl_free(const struct pkt_gl *gl)

    free a packet gather list

    :param gl:
        the gather list
    :type gl: const struct pkt_gl \*

.. _`t4vf_pktgl_free.description`:

Description
-----------

Releases the pages of a packet gather list.  We do not own the last
page on the list and do not free it.

.. _`do_gro`:

do_gro
======

.. c:function:: void do_gro(struct sge_eth_rxq *rxq, const struct pkt_gl *gl, const struct cpl_rx_pkt *pkt)

    perform Generic Receive Offload ingress packet processing

    :param rxq:
        ingress RX Ethernet Queue
    :type rxq: struct sge_eth_rxq \*

    :param gl:
        gather list for ingress packet
    :type gl: const struct pkt_gl \*

    :param pkt:
        CPL header for last packet fragment
    :type pkt: const struct cpl_rx_pkt \*

.. _`do_gro.description`:

Description
-----------

Perform Generic Receive Offload (GRO) ingress packet processing.
We use the standard Linux GRO interfaces for this.

.. _`t4vf_ethrx_handler`:

t4vf_ethrx_handler
==================

.. c:function:: int t4vf_ethrx_handler(struct sge_rspq *rspq, const __be64 *rsp, const struct pkt_gl *gl)

    process an ingress ethernet packet

    :param rspq:
        the response queue that received the packet
    :type rspq: struct sge_rspq \*

    :param rsp:
        the response queue descriptor holding the RX_PKT message
    :type rsp: const __be64 \*

    :param gl:
        the gather list of packet fragments
    :type gl: const struct pkt_gl \*

.. _`t4vf_ethrx_handler.description`:

Description
-----------

Process an ingress ethernet packet and deliver it to the stack.

.. _`is_new_response`:

is_new_response
===============

.. c:function:: bool is_new_response(const struct rsp_ctrl *rc, const struct sge_rspq *rspq)

    check if a response is newly written

    :param rc:
        the response control descriptor
    :type rc: const struct rsp_ctrl \*

    :param rspq:
        the response queue
    :type rspq: const struct sge_rspq \*

.. _`is_new_response.description`:

Description
-----------

Returns true if a response descriptor contains a yet unprocessed
response.

.. _`restore_rx_bufs`:

restore_rx_bufs
===============

.. c:function:: void restore_rx_bufs(const struct pkt_gl *gl, struct sge_fl *fl, int frags)

    put back a packet's RX buffers

    :param gl:
        the packet gather list
    :type gl: const struct pkt_gl \*

    :param fl:
        the SGE Free List
    :type fl: struct sge_fl \*

    :param frags:
        *undescribed*
    :type frags: int

.. _`restore_rx_bufs.description`:

Description
-----------

Called when we find out that the current packet, \ ``si``\ , can't be
processed right away for some reason.  This is a very rare event and
there's no effort to make this suspension/resumption process
particularly efficient.

We implement the suspension by putting all of the RX buffers associated
with the current packet back on the original Free List.  The buffers
have already been unmapped and are left unmapped, we mark them as
unmapped in order to prevent further unmapping attempts.  (Effectively
this function undoes the series of \ ``unmap_rx_buf``\  calls which were done
to create the current packet's gather list.)  This leaves us ready to
restart processing of the packet the next time we start processing the
RX Queue ...

.. _`rspq_next`:

rspq_next
=========

.. c:function:: void rspq_next(struct sge_rspq *rspq)

    advance to the next entry in a response queue

    :param rspq:
        the queue
    :type rspq: struct sge_rspq \*

.. _`rspq_next.description`:

Description
-----------

Updates the state of a response queue to advance it to the next entry.

.. _`process_responses`:

process_responses
=================

.. c:function:: int process_responses(struct sge_rspq *rspq, int budget)

    process responses from an SGE response queue

    :param rspq:
        the ingress response queue to process
    :type rspq: struct sge_rspq \*

    :param budget:
        how many responses can be processed in this round
    :type budget: int

.. _`process_responses.description`:

Description
-----------

Process responses from a Scatter Gather Engine response queue up to
the supplied budget.  Responses include received packets as well as
control messages from firmware or hardware.

Additionally choose the interrupt holdoff time for the next interrupt
on this queue.  If the system is under memory shortage use a fairly
long delay to help recovery.

.. _`napi_rx_handler`:

napi_rx_handler
===============

.. c:function:: int napi_rx_handler(struct napi_struct *napi, int budget)

    the NAPI handler for RX processing

    :param napi:
        the napi instance
    :type napi: struct napi_struct \*

    :param budget:
        how many packets we can process in this round
    :type budget: int

.. _`napi_rx_handler.description`:

Description
-----------

Handler for new data events when using NAPI.  This does not need any
locking or protection from interrupts as data interrupts are off at
this point and other adapter interrupts do not interfere (the latter
in not a concern at all with MSI-X as non-data interrupts then have
a separate handler).

.. _`t4vf_intr_handler`:

t4vf_intr_handler
=================

.. c:function:: irq_handler_t t4vf_intr_handler(struct adapter *adapter)

    select the top-level interrupt handler

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4vf_intr_handler.description`:

Description
-----------

Selects the top-level interrupt handler based on the type of interrupts
(MSI-X or MSI).

.. _`sge_rx_timer_cb`:

sge_rx_timer_cb
===============

.. c:function:: void sge_rx_timer_cb(struct timer_list *t)

    perform periodic maintenance of SGE RX queues

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`sge_rx_timer_cb.description`:

Description
-----------

Runs periodically from a timer to perform maintenance of SGE RX queues.

a) Replenishes RX queues that have run out due to memory shortage.
Normally new RX buffers are added when existing ones are consumed but
when out of memory a queue can become empty.  We schedule NAPI to do
the actual refill.

.. _`sge_tx_timer_cb`:

sge_tx_timer_cb
===============

.. c:function:: void sge_tx_timer_cb(struct timer_list *t)

    perform periodic maintenance of SGE Tx queues

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`sge_tx_timer_cb.description`:

Description
-----------

Runs periodically from a timer to perform maintenance of SGE TX queues.

b) Reclaims completed Tx packets for the Ethernet queues.  Normally
packets are cleaned up by new Tx packets, this timer cleans up packets
when no new packets are being submitted.  This is essential for pktgen,
at least.

.. _`bar2_address`:

bar2_address
============

.. c:function:: void __iomem *bar2_address(struct adapter *adapter, unsigned int qid, enum t4_bar2_qtype qtype, unsigned int *pbar2_qid)

    return the BAR2 address for an SGE Queue's Registers

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param qid:
        the SGE Queue ID
    :type qid: unsigned int

    :param qtype:
        the SGE Queue Type (Egress or Ingress)
    :type qtype: enum t4_bar2_qtype

    :param pbar2_qid:
        BAR2 Queue ID or 0 for Queue ID inferred SGE Queues
    :type pbar2_qid: unsigned int \*

.. _`bar2_address.description`:

Description
-----------

Returns the BAR2 address for the SGE Queue Registers associated with
\ ``qid``\ .  If BAR2 SGE Registers aren't available, returns NULL.  Also
returns the BAR2 Queue ID to be used with writes to the BAR2 SGE
Queue Registers.  If the BAR2 Queue ID is 0, then "Inferred Queue ID"
Registers are supported (e.g. the Write Combining Doorbell Buffer).

.. _`t4vf_sge_alloc_rxq`:

t4vf_sge_alloc_rxq
==================

.. c:function:: int t4vf_sge_alloc_rxq(struct adapter *adapter, struct sge_rspq *rspq, bool iqasynch, struct net_device *dev, int intr_dest, struct sge_fl *fl, rspq_handler_t hnd)

    allocate an SGE RX Queue

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param rspq:
        pointer to to the new rxq's Response Queue to be filled in
    :type rspq: struct sge_rspq \*

    :param iqasynch:
        if 0, a normal rspq; if 1, an asynchronous event queue
    :type iqasynch: bool

    :param dev:
        the network device associated with the new rspq
    :type dev: struct net_device \*

    :param intr_dest:
        MSI-X vector index (overriden in MSI mode)
    :type intr_dest: int

    :param fl:
        pointer to the new rxq's Free List to be filled in
    :type fl: struct sge_fl \*

    :param hnd:
        the interrupt handler to invoke for the rspq
    :type hnd: rspq_handler_t

.. _`t4vf_sge_alloc_eth_txq`:

t4vf_sge_alloc_eth_txq
======================

.. c:function:: int t4vf_sge_alloc_eth_txq(struct adapter *adapter, struct sge_eth_txq *txq, struct net_device *dev, struct netdev_queue *devq, unsigned int iqid)

    allocate an SGE Ethernet TX Queue

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param txq:
        pointer to the new txq to be filled in
    :type txq: struct sge_eth_txq \*

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param devq:
        the network TX queue associated with the new txq
    :type devq: struct netdev_queue \*

    :param iqid:
        the relative ingress queue ID to which events relating to
        the new txq should be directed
    :type iqid: unsigned int

.. _`t4vf_free_sge_resources`:

t4vf_free_sge_resources
=======================

.. c:function:: void t4vf_free_sge_resources(struct adapter *adapter)

    free SGE resources

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4vf_free_sge_resources.description`:

Description
-----------

Frees resources used by the SGE queue sets.

.. _`t4vf_sge_start`:

t4vf_sge_start
==============

.. c:function:: void t4vf_sge_start(struct adapter *adapter)

    enable SGE operation

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4vf_sge_start.description`:

Description
-----------

Start tasklets and timers associated with the DMA engine.

.. _`t4vf_sge_stop`:

t4vf_sge_stop
=============

.. c:function:: void t4vf_sge_stop(struct adapter *adapter)

    disable SGE operation

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4vf_sge_stop.description`:

Description
-----------

Stop tasklets and timers associated with the DMA engine.  Note that
this is effective only if measures have been taken to disable any HW
events that may restart them.

.. _`t4vf_sge_init`:

t4vf_sge_init
=============

.. c:function:: int t4vf_sge_init(struct adapter *adapter)

    initialize SGE

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4vf_sge_init.description`:

Description
-----------

Performs SGE initialization needed every time after a chip reset.
We do not initialize any of the queue sets here, instead the driver
top-level must request those individually.  We also do not enable DMA
here, that should be done after the queues have been set up.

.. This file was automatic generated / don't edit.

