.. -*- coding: utf-8; mode: rst -*-

=====
sge.c
=====


.. _`txq_avail`:

txq_avail
=========

.. c:function:: unsigned int txq_avail (const struct sge_txq *q)

    return the number of available slots in a Tx queue

    :param const struct sge_txq \*q:
        the Tx queue



.. _`txq_avail.description`:

Description
-----------

Returns the number of descriptors in a Tx queue available to write new
packets.



.. _`fl_cap`:

fl_cap
======

.. c:function:: unsigned int fl_cap (const struct sge_fl *fl)

    return the capacity of a free-buffer list

    :param const struct sge_fl \*fl:
        the FL



.. _`fl_cap.description`:

Description
-----------

Returns the capacity of a free-buffer list.  The capacity is less than
the size because one descriptor needs to be left unpopulated, otherwise
HW will think the FL is empty.



.. _`fl_starving`:

fl_starving
===========

.. c:function:: bool fl_starving (const struct adapter *adapter, const struct sge_fl *fl)

    return whether a Free List is starving.

    :param const struct adapter \*adapter:
        pointer to the adapter

    :param const struct sge_fl \*fl:
        the Free List



.. _`fl_starving.description`:

Description
-----------

Tests specified Free List to see whether the number of buffers
available to the hardware has falled below our "starvation"
threshold.



.. _`deferred_unmap_destructor`:

deferred_unmap_destructor
=========================

.. c:function:: void deferred_unmap_destructor (struct sk_buff *skb)

    unmap a packet when it is freed

    :param struct sk_buff \*skb:
        the packet



.. _`deferred_unmap_destructor.description`:

Description
-----------

This is the packet destructor used for Tx packets that need to remain
mapped until they are freed rather than until their Tx descriptors are
freed.



.. _`free_tx_desc`:

free_tx_desc
============

.. c:function:: void free_tx_desc (struct adapter *adap, struct sge_txq *q, unsigned int n, bool unmap)

    reclaims Tx descriptors and their buffers

    :param struct adapter \*adap:

        *undescribed*

    :param struct sge_txq \*q:
        the Tx queue to reclaim descriptors from

    :param unsigned int n:
        the number of descriptors to reclaim

    :param bool unmap:
        whether the buffers should be unmapped for DMA



.. _`free_tx_desc.description`:

Description
-----------

Reclaims Tx descriptors from an SGE Tx queue and frees the associated
Tx buffers.  Called with the Tx queue lock held.



.. _`reclaim_completed_tx`:

reclaim_completed_tx
====================

.. c:function:: void reclaim_completed_tx (struct adapter *adap, struct sge_txq *q, bool unmap)

    reclaims completed Tx descriptors

    :param struct adapter \*adap:
        the adapter

    :param struct sge_txq \*q:
        the Tx queue to reclaim completed descriptors from

    :param bool unmap:
        whether the buffers should be unmapped for DMA



.. _`reclaim_completed_tx.description`:

Description
-----------

Reclaims Tx descriptors that the SGE has indicated it has processed,
and frees the associated buffers if possible.  Called with the Tx
queue locked.



.. _`free_rx_bufs`:

free_rx_bufs
============

.. c:function:: void free_rx_bufs (struct adapter *adap, struct sge_fl *q, int n)

    free the Rx buffers on an SGE free list

    :param struct adapter \*adap:
        the adapter

    :param struct sge_fl \*q:
        the SGE free list to free buffers from

    :param int n:
        how many buffers to free



.. _`free_rx_bufs.description`:

Description
-----------

Release the next ``n`` buffers on an SGE free-buffer Rx queue.   The
buffers must be made inaccessible to HW before calling this function.



.. _`unmap_rx_buf`:

unmap_rx_buf
============

.. c:function:: void unmap_rx_buf (struct adapter *adap, struct sge_fl *q)

    unmap the current Rx buffer on an SGE free list

    :param struct adapter \*adap:
        the adapter

    :param struct sge_fl \*q:
        the SGE free list



.. _`unmap_rx_buf.description`:

Description
-----------

Unmap the current buffer on an SGE free-buffer Rx queue.   The
buffer must be made inaccessible to HW before calling this function.

This is similar to ``free_rx_bufs`` above but does not free the buffer.
Do note that the FL still loses any further access to the buffer.



.. _`refill_fl`:

refill_fl
=========

.. c:function:: unsigned int refill_fl (struct adapter *adap, struct sge_fl *q, int n, gfp_t gfp)

    refill an SGE Rx buffer ring

    :param struct adapter \*adap:
        the adapter

    :param struct sge_fl \*q:
        the ring to refill

    :param int n:
        the number of new buffers to allocate

    :param gfp_t gfp:
        the gfp flags for the allocations



.. _`refill_fl.description`:

Description
-----------

(Re)populate an SGE free-buffer queue with up to ``n`` new packet buffers,
allocated with the supplied gfp flags.  The caller must assure that
``n`` does not exceed the queue's capacity.  If afterwards the queue is
found critically low mark it as starving in the bitmap of starving FLs.

Returns the number of buffers allocated.



.. _`alloc_ring`:

alloc_ring
==========

.. c:function:: void *alloc_ring (struct device *dev, size_t nelem, size_t elem_size, size_t sw_size, dma_addr_t *phys, void *metadata, size_t stat_size, int node)

    allocate resources for an SGE descriptor ring

    :param struct device \*dev:
        the PCI device's core device

    :param size_t nelem:
        the number of descriptors

    :param size_t elem_size:
        the size of each descriptor

    :param size_t sw_size:
        the size of the SW state associated with each ring element

    :param dma_addr_t \*phys:
        the physical address of the allocated ring

    :param void \*metadata:
        address of the array holding the SW state for the ring

    :param size_t stat_size:
        extra space in HW ring for status information

    :param int node:
        preferred node for memory allocations



.. _`alloc_ring.description`:

Description
-----------

Allocates resources for an SGE descriptor ring, such as Tx queues,
free buffer lists, or response queues.  Each SGE ring requires
space for its HW descriptors plus, optionally, space for the SW state
associated with each HW entry (the metadata).  The function returns



.. _`alloc_ring.three-values`:

three values
------------

the virtual address for the HW ring (the return value
of the function), the bus address of the HW ring, and the address
of the SW ring.



.. _`sgl_len`:

sgl_len
=======

.. c:function:: unsigned int sgl_len (unsigned int n)

    calculates the size of an SGL of the given capacity

    :param unsigned int n:
        the number of SGL entries



.. _`sgl_len.description`:

Description
-----------

Calculates the number of flits needed for a scatter/gather list that
can hold the given number of entries.



.. _`flits_to_desc`:

flits_to_desc
=============

.. c:function:: unsigned int flits_to_desc (unsigned int n)

    returns the num of Tx descriptors for the given flits

    :param unsigned int n:
        the number of flits



.. _`flits_to_desc.description`:

Description
-----------

Returns the number of Tx descriptors needed for the supplied number
of flits.



.. _`is_eth_imm`:

is_eth_imm
==========

.. c:function:: int is_eth_imm (const struct sk_buff *skb)

    can an Ethernet packet be sent as immediate data?

    :param const struct sk_buff \*skb:
        the packet



.. _`is_eth_imm.description`:

Description
-----------

Returns whether an Ethernet packet is small enough to fit as
immediate data. Return value corresponds to headroom required.



.. _`calc_tx_flits`:

calc_tx_flits
=============

.. c:function:: unsigned int calc_tx_flits (const struct sk_buff *skb)

    calculate the number of flits for a packet Tx WR

    :param const struct sk_buff \*skb:
        the packet



.. _`calc_tx_flits.description`:

Description
-----------

Returns the number of flits needed for a Tx WR for the given Ethernet
packet, including the needed WR and CPL headers.



.. _`calc_tx_descs`:

calc_tx_descs
=============

.. c:function:: unsigned int calc_tx_descs (const struct sk_buff *skb)

    calculate the number of Tx descriptors for a packet

    :param const struct sk_buff \*skb:
        the packet



.. _`calc_tx_descs.description`:

Description
-----------

Returns the number of Tx descriptors needed for the given Ethernet
packet, including the needed WR and CPL headers.



.. _`write_sgl`:

write_sgl
=========

.. c:function:: void write_sgl (const struct sk_buff *skb, struct sge_txq *q, struct ulptx_sgl *sgl, u64 *end, unsigned int start, const dma_addr_t *addr)

    populate a scatter/gather list for a packet

    :param const struct sk_buff \*skb:
        the packet

    :param struct sge_txq \*q:
        the Tx queue we are writing into

    :param struct ulptx_sgl \*sgl:
        starting location for writing the SGL

    :param u64 \*end:
        points right after the end of the SGL

    :param unsigned int start:
        start offset into skb main-body data to include in the SGL

    :param const dma_addr_t \*addr:
        the list of bus addresses for the SGL elements



.. _`write_sgl.description`:

Description
-----------

Generates a gather list for the buffers that make up a packet.
The caller must provide adequate space for the SGL that will be written.
The SGL includes all of the packet's page fragments and the data in its
main body except for the first ``start`` bytes.  ``sgl`` must be 16-byte
aligned and within a Tx descriptor with available space.  ``end`` points
right after the end of the SGL but does not account for any potential
wrap around, i.e., ``end`` > ``sgl``\ .



.. _`ring_tx_db`:

ring_tx_db
==========

.. c:function:: void ring_tx_db (struct adapter *adap, struct sge_txq *q, int n)

    check and potentially ring a Tx queue's doorbell

    :param struct adapter \*adap:
        the adapter

    :param struct sge_txq \*q:
        the Tx queue

    :param int n:
        number of new descriptors to give to HW



.. _`ring_tx_db.description`:

Description
-----------

Ring the doorbel for a Tx queue.



.. _`inline_tx_skb`:

inline_tx_skb
=============

.. c:function:: void inline_tx_skb (const struct sk_buff *skb, const struct sge_txq *q, void *pos)

    inline a packet's data into Tx descriptors

    :param const struct sk_buff \*skb:
        the packet

    :param const struct sge_txq \*q:
        the Tx queue where the packet will be inlined

    :param void \*pos:
        starting position in the Tx queue where to inline the packet



.. _`inline_tx_skb.description`:

Description
-----------

Inline a packet's contents directly into Tx descriptors, starting at
the given position within the Tx DMA ring.
Most of the complexity of this operation is dealing with wrap arounds
in the middle of the packet we want to inline.



.. _`t4_eth_xmit`:

t4_eth_xmit
===========

.. c:function:: netdev_tx_t t4_eth_xmit (struct sk_buff *skb, struct net_device *dev)

    add a packet to an Ethernet Tx queue

    :param struct sk_buff \*skb:
        the packet

    :param struct net_device \*dev:
        the egress net device



.. _`t4_eth_xmit.description`:

Description
-----------

Add a packet to an SGE Ethernet Tx queue.  Runs with softirqs disabled.



.. _`reclaim_completed_tx_imm`:

reclaim_completed_tx_imm
========================

.. c:function:: void reclaim_completed_tx_imm (struct sge_txq *q)

    reclaim completed control-queue Tx descs

    :param struct sge_txq \*q:
        the SGE control Tx queue



.. _`reclaim_completed_tx_imm.description`:

Description
-----------

This is a variant of :c:func:`reclaim_completed_tx` that is used for Tx queues
that send only immediate data (presently just the control queues) and
thus do not have any sk_buffs to release.



.. _`is_imm`:

is_imm
======

.. c:function:: int is_imm (const struct sk_buff *skb)

    check whether a packet can be sent as immediate data

    :param const struct sk_buff \*skb:
        the packet



.. _`is_imm.description`:

Description
-----------

Returns true if a packet can be sent as a WR with immediate data.



.. _`ctrlq_check_stop`:

ctrlq_check_stop
================

.. c:function:: void ctrlq_check_stop (struct sge_ctrl_txq *q, struct fw_wr_hdr *wr)

    check if a control queue is full and should stop

    :param struct sge_ctrl_txq \*q:
        the queue

    :param struct fw_wr_hdr \*wr:
        most recent WR written to the queue



.. _`ctrlq_check_stop.description`:

Description
-----------

Check if a control queue has become full and should be stopped.
We clean up control queue descriptors very lazily, only when we are out.
If the queue is still full after reclaiming any completed descriptors
we suspend it and have the last WR wake it up.



.. _`ctrl_xmit`:

ctrl_xmit
=========

.. c:function:: int ctrl_xmit (struct sge_ctrl_txq *q, struct sk_buff *skb)

    send a packet through an SGE control Tx queue

    :param struct sge_ctrl_txq \*q:
        the control queue

    :param struct sk_buff \*skb:
        the packet



.. _`ctrl_xmit.description`:

Description
-----------

Send a packet through an SGE control Tx queue.  Packets sent through
a control queue must fit entirely as immediate data.



.. _`restart_ctrlq`:

restart_ctrlq
=============

.. c:function:: void restart_ctrlq (unsigned long data)

    restart a suspended control queue

    :param unsigned long data:
        the control queue to restart



.. _`restart_ctrlq.description`:

Description
-----------

Resumes transmission on a suspended Tx control queue.



.. _`t4_mgmt_tx`:

t4_mgmt_tx
==========

.. c:function:: int t4_mgmt_tx (struct adapter *adap, struct sk_buff *skb)

    send a management message

    :param struct adapter \*adap:
        the adapter

    :param struct sk_buff \*skb:
        the packet containing the management message



.. _`t4_mgmt_tx.description`:

Description
-----------

Send a management message through control queue 0.



.. _`is_ofld_imm`:

is_ofld_imm
===========

.. c:function:: int is_ofld_imm (const struct sk_buff *skb)

    check whether a packet can be sent as immediate data

    :param const struct sk_buff \*skb:
        the packet



.. _`is_ofld_imm.description`:

Description
-----------

Returns true if a packet can be sent as an offload WR with immediate
data.  We currently use the same limit as for Ethernet packets.



.. _`calc_tx_flits_ofld`:

calc_tx_flits_ofld
==================

.. c:function:: unsigned int calc_tx_flits_ofld (const struct sk_buff *skb)

    calculate # of flits for an offload packet

    :param const struct sk_buff \*skb:
        the packet



.. _`calc_tx_flits_ofld.description`:

Description
-----------

Returns the number of flits needed for the given offload packet.
These packets are already fully constructed and no additional headers
will be added.



.. _`txq_stop_maperr`:

txq_stop_maperr
===============

.. c:function:: void txq_stop_maperr (struct sge_ofld_txq *q)

    stop a Tx queue due to I/O MMU exhaustion

    :param struct sge_ofld_txq \*q:
        the queue to stop



.. _`txq_stop_maperr.description`:

Description
-----------

Mark a Tx queue stopped due to I/O MMU exhaustion and resulting
inability to map packets.  A periodic timer attempts to restart
queues so marked.



.. _`ofldtxq_stop`:

ofldtxq_stop
============

.. c:function:: void ofldtxq_stop (struct sge_ofld_txq *q, struct sk_buff *skb)

    stop an offload Tx queue that has become full

    :param struct sge_ofld_txq \*q:
        the queue to stop

    :param struct sk_buff \*skb:
        the packet causing the queue to become full



.. _`ofldtxq_stop.description`:

Description
-----------

Stops an offload Tx queue that has become full and modifies the packet
being written to request a wakeup.



.. _`service_ofldq`:

service_ofldq
=============

.. c:function:: void service_ofldq (struct sge_ofld_txq *q)

    service/restart a suspended offload queue

    :param struct sge_ofld_txq \*q:
        the offload queue



.. _`service_ofldq.description`:

Description
-----------

Services an offload Tx queue by moving packets from its Pending Send
Queue to the Hardware TX ring.  The function starts and ends with the
Send Queue locked, but drops the lock while putting the skb at the
head of the Send Queue onto the Hardware TX Ring.  Dropping the lock
allows more skbs to be added to the Send Queue by other threads.
The packet being processed at the head of the Pending Send Queue is
left on the queue in case we experience DMA Mapping errors, etc.
and need to give up and restart later.

:c:func:`service_ofldq` can be thought of as a task which opportunistically
uses other threads execution contexts.  We use the Offload Queue
boolean "service_ofldq_running" to make sure that only one instance
is ever running at a time ...



.. _`ofld_xmit`:

ofld_xmit
=========

.. c:function:: int ofld_xmit (struct sge_ofld_txq *q, struct sk_buff *skb)

    send a packet through an offload queue

    :param struct sge_ofld_txq \*q:
        the Tx offload queue

    :param struct sk_buff \*skb:
        the packet



.. _`ofld_xmit.description`:

Description
-----------

Send an offload packet through an SGE offload queue.



.. _`restart_ofldq`:

restart_ofldq
=============

.. c:function:: void restart_ofldq (unsigned long data)

    restart a suspended offload queue

    :param unsigned long data:
        the offload queue to restart



.. _`restart_ofldq.description`:

Description
-----------

Resumes transmission on a suspended Tx offload queue.



.. _`skb_txq`:

skb_txq
=======

.. c:function:: unsigned int skb_txq (const struct sk_buff *skb)

    return the Tx queue an offload packet should use

    :param const struct sk_buff \*skb:
        the packet



.. _`skb_txq.description`:

Description
-----------

Returns the Tx queue an offload packet should use as indicated by bits
1-15 in the packet's queue_mapping.



.. _`is_ctrl_pkt`:

is_ctrl_pkt
===========

.. c:function:: unsigned int is_ctrl_pkt (const struct sk_buff *skb)

    return whether an offload packet is a control packet

    :param const struct sk_buff \*skb:
        the packet



.. _`is_ctrl_pkt.description`:

Description
-----------

Returns whether an offload packet should use an OFLD or a CTRL
Tx queue as indicated by bit 0 in the packet's queue_mapping.



.. _`t4_ofld_send`:

t4_ofld_send
============

.. c:function:: int t4_ofld_send (struct adapter *adap, struct sk_buff *skb)

    send an offload packet

    :param struct adapter \*adap:
        the adapter

    :param struct sk_buff \*skb:
        the packet



.. _`t4_ofld_send.description`:

Description
-----------

Sends an offload packet.  We use the packet queue_mapping to select the



.. _`t4_ofld_send.appropriate-tx-queue-as-follows`:

appropriate Tx queue as follows
-------------------------------

bit 0 indicates whether the packet
should be sent as regular or control, bits 1-15 select the queue.



.. _`cxgb4_ofld_send`:

cxgb4_ofld_send
===============

.. c:function:: int cxgb4_ofld_send (struct net_device *dev, struct sk_buff *skb)

    send an offload packet

    :param struct net_device \*dev:
        the net device

    :param struct sk_buff \*skb:
        the packet



.. _`cxgb4_ofld_send.description`:

Description
-----------

Sends an offload packet.  This is an exported version of ``t4_ofld_send``\ ,
intended for ULDs.



.. _`cxgb4_pktgl_to_skb`:

cxgb4_pktgl_to_skb
==================

.. c:function:: struct sk_buff *cxgb4_pktgl_to_skb (const struct pkt_gl *gl, unsigned int skb_len, unsigned int pull_len)

    build an sk_buff from a packet gather list

    :param const struct pkt_gl \*gl:
        the gather list

    :param unsigned int skb_len:
        size of sk_buff main body if it carries fragments

    :param unsigned int pull_len:
        amount of data to move to the sk_buff's main body



.. _`cxgb4_pktgl_to_skb.description`:

Description
-----------

Builds an sk_buff from the given packet gather list.  Returns the
sk_buff or ``NULL`` if sk_buff allocation failed.



.. _`t4_pktgl_free`:

t4_pktgl_free
=============

.. c:function:: void t4_pktgl_free (const struct pkt_gl *gl)

    free a packet gather list

    :param const struct pkt_gl \*gl:
        the gather list



.. _`t4_pktgl_free.description`:

Description
-----------

Releases the pages of a packet gather list.  We do not own the last
page on the list and do not free it.



.. _`cxgb4_sgetim_to_hwtstamp`:

cxgb4_sgetim_to_hwtstamp
========================

.. c:function:: void cxgb4_sgetim_to_hwtstamp (struct adapter *adap, struct skb_shared_hwtstamps *hwtstamps, u64 sgetstamp)

    convert sge time stamp to hw time stamp

    :param struct adapter \*adap:
        the adapter

    :param struct skb_shared_hwtstamps \*hwtstamps:
        time stamp structure to update

    :param u64 sgetstamp:
        60bit iqe timestamp



.. _`cxgb4_sgetim_to_hwtstamp.description`:

Description
-----------

Every ingress queue entry has the 60-bit timestamp, convert that timestamp
which is in Core Clock ticks into ktime_t and assign it



.. _`t4_ethrx_handler`:

t4_ethrx_handler
================

.. c:function:: int t4_ethrx_handler (struct sge_rspq *q, const __be64 *rsp, const struct pkt_gl *si)

    process an ingress ethernet packet

    :param struct sge_rspq \*q:
        the response queue that received the packet

    :param const __be64 \*rsp:
        the response queue descriptor holding the RX_PKT message

    :param const struct pkt_gl \*si:
        the gather list of packet fragments



.. _`t4_ethrx_handler.description`:

Description
-----------

Process an ingress ethernet packet and deliver it to the stack.



.. _`restore_rx_bufs`:

restore_rx_bufs
===============

.. c:function:: void restore_rx_bufs (const struct pkt_gl *si, struct sge_fl *q, int frags)

    put back a packet's Rx buffers

    :param const struct pkt_gl \*si:
        the packet gather list

    :param struct sge_fl \*q:
        the SGE free list

    :param int frags:
        number of FL buffers to restore



.. _`restore_rx_bufs.description`:

Description
-----------

Puts back on an FL the Rx buffers associated with ``si``\ .  The buffers
have already been unmapped and are left unmapped, we mark them so to
prevent further unmapping attempts.

This function undoes a series of ``unmap_rx_buf`` calls when we find out
that the current packet can't be processed right away afterall and we
need to come back to it later.  This is a very rare event and there's
no effort to make this particularly efficient.



.. _`is_new_response`:

is_new_response
===============

.. c:function:: bool is_new_response (const struct rsp_ctrl *r, const struct sge_rspq *q)

    check if a response is newly written

    :param const struct rsp_ctrl \*r:
        the response descriptor

    :param const struct sge_rspq \*q:
        the response queue



.. _`is_new_response.description`:

Description
-----------

Returns true if a response descriptor contains a yet unprocessed
response.



.. _`rspq_next`:

rspq_next
=========

.. c:function:: void rspq_next (struct sge_rspq *q)

    advance to the next entry in a response queue

    :param struct sge_rspq \*q:
        the queue



.. _`rspq_next.description`:

Description
-----------

Updates the state of a response queue to advance it to the next entry.



.. _`process_responses`:

process_responses
=================

.. c:function:: int process_responses (struct sge_rspq *q, int budget)

    process responses from an SGE response queue

    :param struct sge_rspq \*q:
        the ingress queue to process

    :param int budget:
        how many responses can be processed in this round



.. _`process_responses.description`:

Description
-----------

Process responses from an SGE response queue up to the supplied budget.
Responses include received packets as well as control messages from FW
or HW.

Additionally choose the interrupt holdoff time for the next interrupt
on this queue.  If the system is under memory shortage use a fairly
long delay to help recovery.



.. _`napi_rx_handler`:

napi_rx_handler
===============

.. c:function:: int napi_rx_handler (struct napi_struct *napi, int budget)

    the NAPI handler for Rx processing

    :param struct napi_struct \*napi:
        the napi instance

    :param int budget:
        how many packets we can process in this round



.. _`napi_rx_handler.description`:

Description
-----------

Handler for new data events when using NAPI.  This does not need any
locking or protection from interrupts as data interrupts are off at
this point and other adapter interrupts do not interfere (the latter
in not a concern at all with MSI-X as non-data interrupts then have
a separate handler).



.. _`t4_intr_handler`:

t4_intr_handler
===============

.. c:function:: irq_handler_t t4_intr_handler (struct adapter *adap)

    select the top-level interrupt handler

    :param struct adapter \*adap:
        the adapter



.. _`t4_intr_handler.description`:

Description
-----------

Selects the top-level interrupt handler based on the type of interrupts
(MSI-X, MSI, or INTx).



.. _`bar2_address`:

bar2_address
============

.. c:function:: void __iomem *bar2_address (struct adapter *adapter, unsigned int qid, enum t4_bar2_qtype qtype, unsigned int *pbar2_qid)

    return the BAR2 address for an SGE Queue's Registers

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int qid:
        the SGE Queue ID

    :param enum t4_bar2_qtype qtype:
        the SGE Queue Type (Egress or Ingress)

    :param unsigned int \*pbar2_qid:
        BAR2 Queue ID or 0 for Queue ID inferred SGE Queues



.. _`bar2_address.description`:

Description
-----------

Returns the BAR2 address for the SGE Queue Registers associated with
``qid``\ .  If BAR2 SGE Registers aren't available, returns NULL.  Also
returns the BAR2 Queue ID to be used with writes to the BAR2 SGE
Queue Registers.  If the BAR2 Queue ID is 0, then "Inferred Queue ID"
Registers are supported (e.g. the Write Combining Doorbell Buffer).



.. _`t4_free_ofld_rxqs`:

t4_free_ofld_rxqs
=================

.. c:function:: void t4_free_ofld_rxqs (struct adapter *adap, int n, struct sge_ofld_rxq *q)

    free a block of consecutive Rx queues

    :param struct adapter \*adap:
        the adapter

    :param int n:
        number of queues

    :param struct sge_ofld_rxq \*q:
        pointer to first queue



.. _`t4_free_ofld_rxqs.description`:

Description
-----------

Release the resources of a consecutive block of offload Rx queues.



.. _`t4_free_sge_resources`:

t4_free_sge_resources
=====================

.. c:function:: void t4_free_sge_resources (struct adapter *adap)

    free SGE resources

    :param struct adapter \*adap:
        the adapter



.. _`t4_free_sge_resources.description`:

Description
-----------

Frees resources used by the SGE queue sets.



.. _`t4_sge_stop`:

t4_sge_stop
===========

.. c:function:: void t4_sge_stop (struct adapter *adap)

    disable SGE operation

    :param struct adapter \*adap:
        the adapter



.. _`t4_sge_stop.description`:

Description
-----------

Stop tasklets and timers associated with the DMA engine.  Note that
this is effective only if measures have been taken to disable any HW
events that may restart them.



.. _`t4_sge_init_soft`:

t4_sge_init_soft
================

.. c:function:: int t4_sge_init_soft (struct adapter *adap)

    grab core SGE values needed by SGE code

    :param struct adapter \*adap:
        the adapter



.. _`t4_sge_init_soft.description`:

Description
-----------

We need to grab the SGE operating parameters that we need to have
in order to do our job and make sure we can live with them.



.. _`t4_sge_init`:

t4_sge_init
===========

.. c:function:: int t4_sge_init (struct adapter *adap)

    initialize SGE

    :param struct adapter \*adap:
        the adapter



.. _`t4_sge_init.description`:

Description
-----------

Perform low-level SGE code initialization needed every time after a
chip reset.

