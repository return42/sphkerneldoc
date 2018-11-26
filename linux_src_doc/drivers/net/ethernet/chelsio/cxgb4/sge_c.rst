.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4/sge.c

.. _`txq_avail`:

txq_avail
=========

.. c:function:: unsigned int txq_avail(const struct sge_txq *q)

    return the number of available slots in a Tx queue

    :param q:
        the Tx queue
    :type q: const struct sge_txq \*

.. _`txq_avail.description`:

Description
-----------

Returns the number of descriptors in a Tx queue available to write new
packets.

.. _`fl_cap`:

fl_cap
======

.. c:function:: unsigned int fl_cap(const struct sge_fl *fl)

    return the capacity of a free-buffer list

    :param fl:
        the FL
    :type fl: const struct sge_fl \*

.. _`fl_cap.description`:

Description
-----------

Returns the capacity of a free-buffer list.  The capacity is less than
the size because one descriptor needs to be left unpopulated, otherwise
HW will think the FL is empty.

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

.. _`deferred_unmap_destructor`:

deferred_unmap_destructor
=========================

.. c:function:: void deferred_unmap_destructor(struct sk_buff *skb)

    unmap a packet when it is freed

    :param skb:
        the packet
    :type skb: struct sk_buff \*

.. _`deferred_unmap_destructor.description`:

Description
-----------

This is the packet destructor used for Tx packets that need to remain
mapped until they are freed rather than until their Tx descriptors are
freed.

.. _`free_tx_desc`:

free_tx_desc
============

.. c:function:: void free_tx_desc(struct adapter *adap, struct sge_txq *q, unsigned int n, bool unmap)

    reclaims Tx descriptors and their buffers

    :param adap:
        *undescribed*
    :type adap: struct adapter \*

    :param q:
        the Tx queue to reclaim descriptors from
    :type q: struct sge_txq \*

    :param n:
        the number of descriptors to reclaim
    :type n: unsigned int

    :param unmap:
        whether the buffers should be unmapped for DMA
    :type unmap: bool

.. _`free_tx_desc.description`:

Description
-----------

Reclaims Tx descriptors from an SGE Tx queue and frees the associated
Tx buffers.  Called with the Tx queue lock held.

.. _`cxgb4_reclaim_completed_tx`:

cxgb4_reclaim_completed_tx
==========================

.. c:function:: void cxgb4_reclaim_completed_tx(struct adapter *adap, struct sge_txq *q, bool unmap)

    reclaims completed Tx descriptors

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param q:
        the Tx queue to reclaim completed descriptors from
    :type q: struct sge_txq \*

    :param unmap:
        whether the buffers should be unmapped for DMA
    :type unmap: bool

.. _`cxgb4_reclaim_completed_tx.description`:

Description
-----------

Reclaims Tx descriptors that the SGE has indicated it has processed,
and frees the associated buffers if possible.  Called with the Tx
queue locked.

.. _`free_rx_bufs`:

free_rx_bufs
============

.. c:function:: void free_rx_bufs(struct adapter *adap, struct sge_fl *q, int n)

    free the Rx buffers on an SGE free list

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param q:
        the SGE free list to free buffers from
    :type q: struct sge_fl \*

    :param n:
        how many buffers to free
    :type n: int

.. _`free_rx_bufs.description`:

Description
-----------

Release the next \ ``n``\  buffers on an SGE free-buffer Rx queue.   The
buffers must be made inaccessible to HW before calling this function.

.. _`unmap_rx_buf`:

unmap_rx_buf
============

.. c:function:: void unmap_rx_buf(struct adapter *adap, struct sge_fl *q)

    unmap the current Rx buffer on an SGE free list

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param q:
        the SGE free list
    :type q: struct sge_fl \*

.. _`unmap_rx_buf.description`:

Description
-----------

Unmap the current buffer on an SGE free-buffer Rx queue.   The
buffer must be made inaccessible to HW before calling this function.

This is similar to \ ``free_rx_bufs``\  above but does not free the buffer.
Do note that the FL still loses any further access to the buffer.

.. _`refill_fl`:

refill_fl
=========

.. c:function:: unsigned int refill_fl(struct adapter *adap, struct sge_fl *q, int n, gfp_t gfp)

    refill an SGE Rx buffer ring

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param q:
        the ring to refill
    :type q: struct sge_fl \*

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
\ ``n``\  does not exceed the queue's capacity.  If afterwards the queue is
found critically low mark it as starving in the bitmap of starving FLs.

Returns the number of buffers allocated.

.. _`alloc_ring`:

alloc_ring
==========

.. c:function:: void *alloc_ring(struct device *dev, size_t nelem, size_t elem_size, size_t sw_size, dma_addr_t *phys, void *metadata, size_t stat_size, int node)

    allocate resources for an SGE descriptor ring

    :param dev:
        the PCI device's core device
    :type dev: struct device \*

    :param nelem:
        the number of descriptors
    :type nelem: size_t

    :param elem_size:
        the size of each descriptor
    :type elem_size: size_t

    :param sw_size:
        the size of the SW state associated with each ring element
    :type sw_size: size_t

    :param phys:
        the physical address of the allocated ring
    :type phys: dma_addr_t \*

    :param metadata:
        address of the array holding the SW state for the ring
    :type metadata: void \*

    :param stat_size:
        extra space in HW ring for status information
    :type stat_size: size_t

    :param node:
        preferred node for memory allocations
    :type node: int

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

.. c:function:: unsigned int sgl_len(unsigned int n)

    calculates the size of an SGL of the given capacity

    :param n:
        the number of SGL entries
    :type n: unsigned int

.. _`sgl_len.description`:

Description
-----------

Calculates the number of flits needed for a scatter/gather list that
can hold the given number of entries.

.. _`flits_to_desc`:

flits_to_desc
=============

.. c:function:: unsigned int flits_to_desc(unsigned int n)

    returns the num of Tx descriptors for the given flits

    :param n:
        the number of flits
    :type n: unsigned int

.. _`flits_to_desc.description`:

Description
-----------

Returns the number of Tx descriptors needed for the supplied number
of flits.

.. _`is_eth_imm`:

is_eth_imm
==========

.. c:function:: int is_eth_imm(const struct sk_buff *skb, unsigned int chip_ver)

    can an Ethernet packet be sent as immediate data?

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

    :param chip_ver:
        *undescribed*
    :type chip_ver: unsigned int

.. _`is_eth_imm.description`:

Description
-----------

Returns whether an Ethernet packet is small enough to fit as
immediate data. Return value corresponds to headroom required.

.. _`calc_tx_flits`:

calc_tx_flits
=============

.. c:function:: unsigned int calc_tx_flits(const struct sk_buff *skb, unsigned int chip_ver)

    calculate the number of flits for a packet Tx WR

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

    :param chip_ver:
        *undescribed*
    :type chip_ver: unsigned int

.. _`calc_tx_flits.description`:

Description
-----------

Returns the number of flits needed for a Tx WR for the given Ethernet
packet, including the needed WR and CPL headers.

.. _`calc_tx_descs`:

calc_tx_descs
=============

.. c:function:: unsigned int calc_tx_descs(const struct sk_buff *skb, unsigned int chip_ver)

    calculate the number of Tx descriptors for a packet

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

    :param chip_ver:
        *undescribed*
    :type chip_ver: unsigned int

.. _`calc_tx_descs.description`:

Description
-----------

Returns the number of Tx descriptors needed for the given Ethernet
packet, including the needed WR and CPL headers.

.. _`cxgb4_write_sgl`:

cxgb4_write_sgl
===============

.. c:function:: void cxgb4_write_sgl(const struct sk_buff *skb, struct sge_txq *q, struct ulptx_sgl *sgl, u64 *end, unsigned int start, const dma_addr_t *addr)

    populate a scatter/gather list for a packet

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

    :param q:
        the Tx queue we are writing into
    :type q: struct sge_txq \*

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
        the list of bus addresses for the SGL elements
    :type addr: const dma_addr_t \*

.. _`cxgb4_write_sgl.description`:

Description
-----------

Generates a gather list for the buffers that make up a packet.
The caller must provide adequate space for the SGL that will be written.
The SGL includes all of the packet's page fragments and the data in its
main body except for the first \ ``start``\  bytes.  \ ``sgl``\  must be 16-byte
aligned and within a Tx descriptor with available space.  \ ``end``\  points
right after the end of the SGL but does not account for any potential
wrap around, i.e., \ ``end``\  > \ ``sgl``\ .

.. _`cxgb4_ring_tx_db`:

cxgb4_ring_tx_db
================

.. c:function:: void cxgb4_ring_tx_db(struct adapter *adap, struct sge_txq *q, int n)

    check and potentially ring a Tx queue's doorbell

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param q:
        the Tx queue
    :type q: struct sge_txq \*

    :param n:
        number of new descriptors to give to HW
    :type n: int

.. _`cxgb4_ring_tx_db.description`:

Description
-----------

Ring the doorbel for a Tx queue.

.. _`cxgb4_inline_tx_skb`:

cxgb4_inline_tx_skb
===================

.. c:function:: void cxgb4_inline_tx_skb(const struct sk_buff *skb, const struct sge_txq *q, void *pos)

    inline a packet's data into Tx descriptors

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

    :param q:
        the Tx queue where the packet will be inlined
    :type q: const struct sge_txq \*

    :param pos:
        starting position in the Tx queue where to inline the packet
    :type pos: void \*

.. _`cxgb4_inline_tx_skb.description`:

Description
-----------

Inline a packet's contents directly into Tx descriptors, starting at
the given position within the Tx DMA ring.
Most of the complexity of this operation is dealing with wrap arounds
in the middle of the packet we want to inline.

.. _`cxgb4_eth_xmit`:

cxgb4_eth_xmit
==============

.. c:function:: netdev_tx_t cxgb4_eth_xmit(struct sk_buff *skb, struct net_device *dev)

    add a packet to an Ethernet Tx queue

    :param skb:
        the packet
    :type skb: struct sk_buff \*

    :param dev:
        the egress net device
    :type dev: struct net_device \*

.. _`cxgb4_eth_xmit.description`:

Description
-----------

Add a packet to an SGE Ethernet Tx queue.  Runs with softirqs disabled.

.. _`t4vf_is_eth_imm`:

t4vf_is_eth_imm
===============

.. c:function:: int t4vf_is_eth_imm(const struct sk_buff *skb)

    can an Ethernet packet be sent as immediate data?

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

.. _`t4vf_is_eth_imm.description`:

Description
-----------

Returns whether an Ethernet packet is small enough to fit completely as
immediate data.

.. _`t4vf_calc_tx_flits`:

t4vf_calc_tx_flits
==================

.. c:function:: unsigned int t4vf_calc_tx_flits(const struct sk_buff *skb)

    calculate the number of flits for a packet TX WR

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

.. _`t4vf_calc_tx_flits.description`:

Description
-----------

Returns the number of flits needed for a TX Work Request for the
given Ethernet packet, including the needed WR and CPL headers.

.. _`cxgb4_vf_eth_xmit`:

cxgb4_vf_eth_xmit
=================

.. c:function:: netdev_tx_t cxgb4_vf_eth_xmit(struct sk_buff *skb, struct net_device *dev)

    add a packet to an Ethernet TX queue

    :param skb:
        the packet
    :type skb: struct sk_buff \*

    :param dev:
        the egress net device
    :type dev: struct net_device \*

.. _`cxgb4_vf_eth_xmit.description`:

Description
-----------

Add a packet to an SGE Ethernet TX queue.  Runs with softirqs disabled.

.. _`reclaim_completed_tx_imm`:

reclaim_completed_tx_imm
========================

.. c:function:: void reclaim_completed_tx_imm(struct sge_txq *q)

    reclaim completed control-queue Tx descs

    :param q:
        the SGE control Tx queue
    :type q: struct sge_txq \*

.. _`reclaim_completed_tx_imm.description`:

Description
-----------

This is a variant of \ :c:func:`cxgb4_reclaim_completed_tx`\  that is used
for Tx queues that send only immediate data (presently just
the control queues) and thus do not have any sk_buffs to release.

.. _`is_imm`:

is_imm
======

.. c:function:: int is_imm(const struct sk_buff *skb)

    check whether a packet can be sent as immediate data

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

.. _`is_imm.description`:

Description
-----------

Returns true if a packet can be sent as a WR with immediate data.

.. _`ctrlq_check_stop`:

ctrlq_check_stop
================

.. c:function:: void ctrlq_check_stop(struct sge_ctrl_txq *q, struct fw_wr_hdr *wr)

    check if a control queue is full and should stop

    :param q:
        the queue
    :type q: struct sge_ctrl_txq \*

    :param wr:
        most recent WR written to the queue
    :type wr: struct fw_wr_hdr \*

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

.. c:function:: int ctrl_xmit(struct sge_ctrl_txq *q, struct sk_buff *skb)

    send a packet through an SGE control Tx queue

    :param q:
        the control queue
    :type q: struct sge_ctrl_txq \*

    :param skb:
        the packet
    :type skb: struct sk_buff \*

.. _`ctrl_xmit.description`:

Description
-----------

Send a packet through an SGE control Tx queue.  Packets sent through
a control queue must fit entirely as immediate data.

.. _`restart_ctrlq`:

restart_ctrlq
=============

.. c:function:: void restart_ctrlq(unsigned long data)

    restart a suspended control queue

    :param data:
        the control queue to restart
    :type data: unsigned long

.. _`restart_ctrlq.description`:

Description
-----------

Resumes transmission on a suspended Tx control queue.

.. _`t4_mgmt_tx`:

t4_mgmt_tx
==========

.. c:function:: int t4_mgmt_tx(struct adapter *adap, struct sk_buff *skb)

    send a management message

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param skb:
        the packet containing the management message
    :type skb: struct sk_buff \*

.. _`t4_mgmt_tx.description`:

Description
-----------

Send a management message through control queue 0.

.. _`is_ofld_imm`:

is_ofld_imm
===========

.. c:function:: int is_ofld_imm(const struct sk_buff *skb)

    check whether a packet can be sent as immediate data

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

.. _`is_ofld_imm.description`:

Description
-----------

Returns true if a packet can be sent as an offload WR with immediate
data.  We currently use the same limit as for Ethernet packets.

.. _`calc_tx_flits_ofld`:

calc_tx_flits_ofld
==================

.. c:function:: unsigned int calc_tx_flits_ofld(const struct sk_buff *skb)

    calculate # of flits for an offload packet

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

.. _`calc_tx_flits_ofld.description`:

Description
-----------

Returns the number of flits needed for the given offload packet.
These packets are already fully constructed and no additional headers
will be added.

.. _`txq_stop_maperr`:

txq_stop_maperr
===============

.. c:function:: void txq_stop_maperr(struct sge_uld_txq *q)

    stop a Tx queue due to I/O MMU exhaustion

    :param q:
        the queue to stop
    :type q: struct sge_uld_txq \*

.. _`txq_stop_maperr.description`:

Description
-----------

Mark a Tx queue stopped due to I/O MMU exhaustion and resulting
inability to map packets.  A periodic timer attempts to restart
queues so marked.

.. _`ofldtxq_stop`:

ofldtxq_stop
============

.. c:function:: void ofldtxq_stop(struct sge_uld_txq *q, struct fw_wr_hdr *wr)

    stop an offload Tx queue that has become full

    :param q:
        the queue to stop
    :type q: struct sge_uld_txq \*

    :param wr:
        the Work Request causing the queue to become full
    :type wr: struct fw_wr_hdr \*

.. _`ofldtxq_stop.description`:

Description
-----------

Stops an offload Tx queue that has become full and modifies the packet
being written to request a wakeup.

.. _`service_ofldq`:

service_ofldq
=============

.. c:function:: void service_ofldq(struct sge_uld_txq *q)

    service/restart a suspended offload queue

    :param q:
        the offload queue
    :type q: struct sge_uld_txq \*

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

\ :c:func:`service_ofldq`\  can be thought of as a task which opportunistically
uses other threads execution contexts.  We use the Offload Queue
boolean "service_ofldq_running" to make sure that only one instance
is ever running at a time ...

.. _`ofld_xmit`:

ofld_xmit
=========

.. c:function:: int ofld_xmit(struct sge_uld_txq *q, struct sk_buff *skb)

    send a packet through an offload queue

    :param q:
        the Tx offload queue
    :type q: struct sge_uld_txq \*

    :param skb:
        the packet
    :type skb: struct sk_buff \*

.. _`ofld_xmit.description`:

Description
-----------

Send an offload packet through an SGE offload queue.

.. _`restart_ofldq`:

restart_ofldq
=============

.. c:function:: void restart_ofldq(unsigned long data)

    restart a suspended offload queue

    :param data:
        the offload queue to restart
    :type data: unsigned long

.. _`restart_ofldq.description`:

Description
-----------

Resumes transmission on a suspended Tx offload queue.

.. _`skb_txq`:

skb_txq
=======

.. c:function:: unsigned int skb_txq(const struct sk_buff *skb)

    return the Tx queue an offload packet should use

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

.. _`skb_txq.description`:

Description
-----------

Returns the Tx queue an offload packet should use as indicated by bits
1-15 in the packet's queue_mapping.

.. _`is_ctrl_pkt`:

is_ctrl_pkt
===========

.. c:function:: unsigned int is_ctrl_pkt(const struct sk_buff *skb)

    return whether an offload packet is a control packet

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

.. _`is_ctrl_pkt.description`:

Description
-----------

Returns whether an offload packet should use an OFLD or a CTRL
Tx queue as indicated by bit 0 in the packet's queue_mapping.

.. _`t4_ofld_send`:

t4_ofld_send
============

.. c:function:: int t4_ofld_send(struct adapter *adap, struct sk_buff *skb)

    send an offload packet

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param skb:
        the packet
    :type skb: struct sk_buff \*

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

.. c:function:: int cxgb4_ofld_send(struct net_device *dev, struct sk_buff *skb)

    send an offload packet

    :param dev:
        the net device
    :type dev: struct net_device \*

    :param skb:
        the packet
    :type skb: struct sk_buff \*

.. _`cxgb4_ofld_send.description`:

Description
-----------

Sends an offload packet.  This is an exported version of \ ``t4_ofld_send``\ ,
intended for ULDs.

.. _`ofld_xmit_direct`:

ofld_xmit_direct
================

.. c:function:: int ofld_xmit_direct(struct sge_uld_txq *q, const void *src, unsigned int len)

    copy a WR into offload queue

    :param q:
        the Tx offload queue
    :type q: struct sge_uld_txq \*

    :param src:
        location of WR
    :type src: const void \*

    :param len:
        WR length
    :type len: unsigned int

.. _`ofld_xmit_direct.description`:

Description
-----------

Copy an immediate WR into an uncontended SGE offload queue.

.. _`t4_crypto_send`:

t4_crypto_send
==============

.. c:function:: int t4_crypto_send(struct adapter *adap, struct sk_buff *skb)

    send crypto packet

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param skb:
        the packet
    :type skb: struct sk_buff \*

.. _`t4_crypto_send.description`:

Description
-----------

Sends crypto packet.  We use the packet queue_mapping to select the

.. _`t4_crypto_send.appropriate-tx-queue-as-follows`:

appropriate Tx queue as follows
-------------------------------

bit 0 indicates whether the packet
should be sent as regular or control, bits 1-15 select the queue.

.. _`cxgb4_crypto_send`:

cxgb4_crypto_send
=================

.. c:function:: int cxgb4_crypto_send(struct net_device *dev, struct sk_buff *skb)

    send crypto packet

    :param dev:
        the net device
    :type dev: struct net_device \*

    :param skb:
        the packet
    :type skb: struct sk_buff \*

.. _`cxgb4_crypto_send.description`:

Description
-----------

Sends crypto packet.  This is an exported version of \ ``t4_crypto_send``\ ,
intended for ULDs.

.. _`cxgb4_pktgl_to_skb`:

cxgb4_pktgl_to_skb
==================

.. c:function:: struct sk_buff *cxgb4_pktgl_to_skb(const struct pkt_gl *gl, unsigned int skb_len, unsigned int pull_len)

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

.. _`cxgb4_pktgl_to_skb.description`:

Description
-----------

Builds an sk_buff from the given packet gather list.  Returns the
sk_buff or \ ``NULL``\  if sk_buff allocation failed.

.. _`t4_pktgl_free`:

t4_pktgl_free
=============

.. c:function:: void t4_pktgl_free(const struct pkt_gl *gl)

    free a packet gather list

    :param gl:
        the gather list
    :type gl: const struct pkt_gl \*

.. _`t4_pktgl_free.description`:

Description
-----------

Releases the pages of a packet gather list.  We do not own the last
page on the list and do not free it.

.. _`cxgb4_sgetim_to_hwtstamp`:

cxgb4_sgetim_to_hwtstamp
========================

.. c:function:: void cxgb4_sgetim_to_hwtstamp(struct adapter *adap, struct skb_shared_hwtstamps *hwtstamps, u64 sgetstamp)

    convert sge time stamp to hw time stamp

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param hwtstamps:
        time stamp structure to update
    :type hwtstamps: struct skb_shared_hwtstamps \*

    :param sgetstamp:
        60bit iqe timestamp
    :type sgetstamp: u64

.. _`cxgb4_sgetim_to_hwtstamp.description`:

Description
-----------

Every ingress queue entry has the 60-bit timestamp, convert that timestamp
which is in Core Clock ticks into ktime_t and assign it

.. _`t4_systim_to_hwstamp`:

t4_systim_to_hwstamp
====================

.. c:function:: int t4_systim_to_hwstamp(struct adapter *adapter, struct sk_buff *skb)

    read hardware time stamp

    :param adapter:
        *undescribed*
    :type adapter: struct adapter \*

    :param skb:
        the packet
    :type skb: struct sk_buff \*

.. _`t4_systim_to_hwstamp.description`:

Description
-----------

Read Time Stamp from MPS packet and insert in skb which
is forwarded to PTP application

.. _`t4_rx_hststamp`:

t4_rx_hststamp
==============

.. c:function:: int t4_rx_hststamp(struct adapter *adapter, const __be64 *rsp, struct sge_eth_rxq *rxq, struct sk_buff *skb)

    Recv PTP Event Message

    :param adapter:
        *undescribed*
    :type adapter: struct adapter \*

    :param rsp:
        the response queue descriptor holding the RX_PKT message
    :type rsp: const __be64 \*

    :param rxq:
        *undescribed*
    :type rxq: struct sge_eth_rxq \*

    :param skb:
        the packet
    :type skb: struct sk_buff \*

.. _`t4_rx_hststamp.description`:

Description
-----------

PTP enabled and MPS packet, read HW timestamp

.. _`t4_tx_hststamp`:

t4_tx_hststamp
==============

.. c:function:: int t4_tx_hststamp(struct adapter *adapter, struct sk_buff *skb, struct net_device *dev)

    Loopback PTP Transmit Event Message

    :param adapter:
        *undescribed*
    :type adapter: struct adapter \*

    :param skb:
        the packet
    :type skb: struct sk_buff \*

    :param dev:
        the ingress net device
    :type dev: struct net_device \*

.. _`t4_tx_hststamp.description`:

Description
-----------

Read hardware timestamp for the loopback PTP Tx event message

.. _`t4_ethrx_handler`:

t4_ethrx_handler
================

.. c:function:: int t4_ethrx_handler(struct sge_rspq *q, const __be64 *rsp, const struct pkt_gl *si)

    process an ingress ethernet packet

    :param q:
        the response queue that received the packet
    :type q: struct sge_rspq \*

    :param rsp:
        the response queue descriptor holding the RX_PKT message
    :type rsp: const __be64 \*

    :param si:
        the gather list of packet fragments
    :type si: const struct pkt_gl \*

.. _`t4_ethrx_handler.description`:

Description
-----------

Process an ingress ethernet packet and deliver it to the stack.

.. _`restore_rx_bufs`:

restore_rx_bufs
===============

.. c:function:: void restore_rx_bufs(const struct pkt_gl *si, struct sge_fl *q, int frags)

    put back a packet's Rx buffers

    :param si:
        the packet gather list
    :type si: const struct pkt_gl \*

    :param q:
        the SGE free list
    :type q: struct sge_fl \*

    :param frags:
        number of FL buffers to restore
    :type frags: int

.. _`restore_rx_bufs.description`:

Description
-----------

Puts back on an FL the Rx buffers associated with \ ``si``\ .  The buffers
have already been unmapped and are left unmapped, we mark them so to
prevent further unmapping attempts.

This function undoes a series of \ ``unmap_rx_buf``\  calls when we find out
that the current packet can't be processed right away afterall and we
need to come back to it later.  This is a very rare event and there's
no effort to make this particularly efficient.

.. _`is_new_response`:

is_new_response
===============

.. c:function:: bool is_new_response(const struct rsp_ctrl *r, const struct sge_rspq *q)

    check if a response is newly written

    :param r:
        the response descriptor
    :type r: const struct rsp_ctrl \*

    :param q:
        the response queue
    :type q: const struct sge_rspq \*

.. _`is_new_response.description`:

Description
-----------

Returns true if a response descriptor contains a yet unprocessed
response.

.. _`rspq_next`:

rspq_next
=========

.. c:function:: void rspq_next(struct sge_rspq *q)

    advance to the next entry in a response queue

    :param q:
        the queue
    :type q: struct sge_rspq \*

.. _`rspq_next.description`:

Description
-----------

Updates the state of a response queue to advance it to the next entry.

.. _`process_responses`:

process_responses
=================

.. c:function:: int process_responses(struct sge_rspq *q, int budget)

    process responses from an SGE response queue

    :param q:
        the ingress queue to process
    :type q: struct sge_rspq \*

    :param budget:
        how many responses can be processed in this round
    :type budget: int

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

.. c:function:: int napi_rx_handler(struct napi_struct *napi, int budget)

    the NAPI handler for Rx processing

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

.. _`t4_intr_handler`:

t4_intr_handler
===============

.. c:function:: irq_handler_t t4_intr_handler(struct adapter *adap)

    select the top-level interrupt handler

    :param adap:
        the adapter
    :type adap: struct adapter \*

.. _`t4_intr_handler.description`:

Description
-----------

Selects the top-level interrupt handler based on the type of interrupts
(MSI-X, MSI, or INTx).

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

.. _`t4_free_ofld_rxqs`:

t4_free_ofld_rxqs
=================

.. c:function:: void t4_free_ofld_rxqs(struct adapter *adap, int n, struct sge_ofld_rxq *q)

    free a block of consecutive Rx queues

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param n:
        number of queues
    :type n: int

    :param q:
        pointer to first queue
    :type q: struct sge_ofld_rxq \*

.. _`t4_free_ofld_rxqs.description`:

Description
-----------

Release the resources of a consecutive block of offload Rx queues.

.. _`t4_free_sge_resources`:

t4_free_sge_resources
=====================

.. c:function:: void t4_free_sge_resources(struct adapter *adap)

    free SGE resources

    :param adap:
        the adapter
    :type adap: struct adapter \*

.. _`t4_free_sge_resources.description`:

Description
-----------

Frees resources used by the SGE queue sets.

.. _`t4_sge_stop`:

t4_sge_stop
===========

.. c:function:: void t4_sge_stop(struct adapter *adap)

    disable SGE operation

    :param adap:
        the adapter
    :type adap: struct adapter \*

.. _`t4_sge_stop.description`:

Description
-----------

Stop tasklets and timers associated with the DMA engine.  Note that
this is effective only if measures have been taken to disable any HW
events that may restart them.

.. _`t4_sge_init_soft`:

t4_sge_init_soft
================

.. c:function:: int t4_sge_init_soft(struct adapter *adap)

    grab core SGE values needed by SGE code

    :param adap:
        the adapter
    :type adap: struct adapter \*

.. _`t4_sge_init_soft.description`:

Description
-----------

We need to grab the SGE operating parameters that we need to have
in order to do our job and make sure we can live with them.

.. _`t4_sge_init`:

t4_sge_init
===========

.. c:function:: int t4_sge_init(struct adapter *adap)

    initialize SGE

    :param adap:
        the adapter
    :type adap: struct adapter \*

.. _`t4_sge_init.description`:

Description
-----------

Perform low-level SGE code initialization needed every time after a
chip reset.

.. This file was automatic generated / don't edit.

