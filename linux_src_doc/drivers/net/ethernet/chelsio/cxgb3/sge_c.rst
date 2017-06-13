.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb3/sge.c

.. _`refill_rspq`:

refill_rspq
===========

.. c:function:: void refill_rspq(struct adapter *adapter, const struct sge_rspq *q, unsigned int credits)

    replenish an SGE response queue

    :param struct adapter \*adapter:
        the adapter

    :param const struct sge_rspq \*q:
        the response queue to replenish

    :param unsigned int credits:
        how many new responses to make available

.. _`refill_rspq.description`:

Description
-----------

Replenishes a response queue by making the supplied number of responses
available to HW.

.. _`need_skb_unmap`:

need_skb_unmap
==============

.. c:function:: int need_skb_unmap( void)

    does the platform need unmapping of sk_buffs?

    :param  void:
        no arguments

.. _`need_skb_unmap.description`:

Description
-----------

Returns true if the platform needs sk_buff unmapping.  The compiler
optimizes away unnecessary code if this returns true.

.. _`unmap_skb`:

unmap_skb
=========

.. c:function:: void unmap_skb(struct sk_buff *skb, struct sge_txq *q, unsigned int cidx, struct pci_dev *pdev)

    unmap a packet main body and its page fragments

    :param struct sk_buff \*skb:
        the packet

    :param struct sge_txq \*q:
        the Tx queue containing Tx descriptors for the packet

    :param unsigned int cidx:
        index of Tx descriptor

    :param struct pci_dev \*pdev:
        the PCI device

.. _`unmap_skb.description`:

Description
-----------

Unmap the main body of an sk_buff and its page fragments, if any.
Because of the fairly complicated structure of our SGLs and the desire
to conserve space for metadata, the information necessary to unmap an
sk_buff is spread across the sk_buff itself (buffer lengths), the HW Tx
descriptors (the physical addresses of the various data buffers), and
the SW descriptor state (assorted indices).  The send functions
initialize the indices for the first packet descriptor so we can unmap
the buffers held in the first Tx descriptor here, and we have enough
information at this point to set the state for the next Tx descriptor.

Note that it is possible to clean up the first descriptor of a packet
before the send routines have written the next descriptors, but this
race does not cause any problem.  We just end up writing the unmapping
info for the descriptor first.

.. _`free_tx_desc`:

free_tx_desc
============

.. c:function:: void free_tx_desc(struct adapter *adapter, struct sge_txq *q, unsigned int n)

    reclaims Tx descriptors and their buffers

    :param struct adapter \*adapter:
        the adapter

    :param struct sge_txq \*q:
        the Tx queue to reclaim descriptors from

    :param unsigned int n:
        the number of descriptors to reclaim

.. _`free_tx_desc.description`:

Description
-----------

Reclaims Tx descriptors from an SGE Tx queue and frees the associated
Tx buffers.  Called with the Tx queue lock held.

.. _`reclaim_completed_tx`:

reclaim_completed_tx
====================

.. c:function:: unsigned int reclaim_completed_tx(struct adapter *adapter, struct sge_txq *q, unsigned int chunk)

    reclaims completed Tx descriptors

    :param struct adapter \*adapter:
        the adapter

    :param struct sge_txq \*q:
        the Tx queue to reclaim completed descriptors from

    :param unsigned int chunk:
        maximum number of descriptors to reclaim

.. _`reclaim_completed_tx.description`:

Description
-----------

Reclaims Tx descriptors that the SGE has indicated it has processed,
and frees the associated buffers if possible.  Called with the Tx
queue's lock held.

.. _`should_restart_tx`:

should_restart_tx
=================

.. c:function:: int should_restart_tx(const struct sge_txq *q)

    are there enough resources to restart a Tx queue?

    :param const struct sge_txq \*q:
        the Tx queue

.. _`should_restart_tx.description`:

Description
-----------

Checks if there are enough descriptors to restart a suspended Tx queue.

.. _`free_rx_bufs`:

free_rx_bufs
============

.. c:function:: void free_rx_bufs(struct pci_dev *pdev, struct sge_fl *q)

    free the Rx buffers on an SGE free list

    :param struct pci_dev \*pdev:
        the PCI device associated with the adapter

    :param struct sge_fl \*q:
        *undescribed*

.. _`free_rx_bufs.description`:

Description
-----------

Release the buffers on an SGE free-buffer Rx queue.  HW fetching from
this queue should be stopped before calling this function.

.. _`add_one_rx_buf`:

add_one_rx_buf
==============

.. c:function:: int add_one_rx_buf(void *va, unsigned int len, struct rx_desc *d, struct rx_sw_desc *sd, unsigned int gen, struct pci_dev *pdev)

    add a packet buffer to a free-buffer list

    :param void \*va:
        buffer start VA

    :param unsigned int len:
        the buffer length

    :param struct rx_desc \*d:
        the HW Rx descriptor to write

    :param struct rx_sw_desc \*sd:
        the SW Rx descriptor to write

    :param unsigned int gen:
        the generation bit value

    :param struct pci_dev \*pdev:
        the PCI device associated with the adapter

.. _`add_one_rx_buf.description`:

Description
-----------

Add a buffer of the given length to the supplied HW and SW Rx
descriptors.

.. _`refill_fl`:

refill_fl
=========

.. c:function:: int refill_fl(struct adapter *adap, struct sge_fl *q, int n, gfp_t gfp)

    refill an SGE free-buffer list

    :param struct adapter \*adap:
        *undescribed*

    :param struct sge_fl \*q:
        the free-list to refill

    :param int n:
        the number of new buffers to allocate

    :param gfp_t gfp:
        the gfp flags for allocating new buffers

.. _`refill_fl.description`:

Description
-----------

(Re)populate an SGE free-buffer list with up to \ ``n``\  new packet buffers,
allocated with the supplied gfp flags.  The caller must assure that
\ ``n``\  does not exceed the queue's capacity.

.. _`recycle_rx_buf`:

recycle_rx_buf
==============

.. c:function:: void recycle_rx_buf(struct adapter *adap, struct sge_fl *q, unsigned int idx)

    recycle a receive buffer

    :param struct adapter \*adap:
        *undescribed*

    :param struct sge_fl \*q:
        the SGE free list

    :param unsigned int idx:
        index of buffer to recycle

.. _`recycle_rx_buf.description`:

Description
-----------

Recycles the specified buffer on the given free list by adding it at
the next available slot on the list.

.. _`alloc_ring`:

alloc_ring
==========

.. c:function:: void *alloc_ring(struct pci_dev *pdev, size_t nelem, size_t elem_size, size_t sw_size, dma_addr_t *phys, void *metadata)

    allocate resources for an SGE descriptor ring

    :param struct pci_dev \*pdev:
        the PCI device

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
of the function), the physical address of the HW ring, and the address
of the SW ring.

.. _`t3_reset_qset`:

t3_reset_qset
=============

.. c:function:: void t3_reset_qset(struct sge_qset *q)

    reset a sge qset

    :param struct sge_qset \*q:
        the queue set

.. _`t3_reset_qset.description`:

Description
-----------

Reset the qset structure.
the NAPI structure is preserved in the event of
the qset's reincarnation, for example during EEH recovery.

.. _`t3_free_qset`:

t3_free_qset
============

.. c:function:: void t3_free_qset(struct adapter *adapter, struct sge_qset *q)

    free the resources of an SGE queue set

    :param struct adapter \*adapter:
        the adapter owning the queue set

    :param struct sge_qset \*q:
        the queue set

.. _`t3_free_qset.description`:

Description
-----------

Release the HW and SW resources associated with an SGE queue set, such
as HW contexts, packet buffers, and descriptor rings.  Traffic to the
queue set must be quiesced prior to calling this.

.. _`init_qset_cntxt`:

init_qset_cntxt
===============

.. c:function:: void init_qset_cntxt(struct sge_qset *qs, unsigned int id)

    initialize an SGE queue set context info

    :param struct sge_qset \*qs:
        the queue set

    :param unsigned int id:
        the queue set id

.. _`init_qset_cntxt.description`:

Description
-----------

Initializes the TIDs and context ids for the queues of a queue set.

.. _`sgl_len`:

sgl_len
=======

.. c:function:: unsigned int sgl_len(unsigned int n)

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

.. c:function:: unsigned int flits_to_desc(unsigned int n)

    returns the num of Tx descriptors for the given flits

    :param unsigned int n:
        the number of flits

.. _`flits_to_desc.description`:

Description
-----------

Calculates the number of Tx descriptors needed for the supplied number
of flits.

.. _`get_packet`:

get_packet
==========

.. c:function:: struct sk_buff *get_packet(struct adapter *adap, struct sge_fl *fl, unsigned int len, unsigned int drop_thres)

    return the next ingress packet buffer from a free list

    :param struct adapter \*adap:
        the adapter that received the packet

    :param struct sge_fl \*fl:
        the SGE free list holding the packet

    :param unsigned int len:
        the packet length including any SGE padding

    :param unsigned int drop_thres:
        # of remaining buffers before we start dropping packets

.. _`get_packet.description`:

Description
-----------

Get the next packet from a free list and complete setup of the
sk_buff.  If the packet is small we make a copy and recycle the
original buffer, otherwise we use the original buffer itself.  If a
positive drop threshold is supplied packets are dropped and their
buffers recycled if (a) the number of remaining buffers is under the
threshold and the packet is too big to copy, or (b) the packet should
be copied but there is no memory for the copy.

.. _`get_packet_pg`:

get_packet_pg
=============

.. c:function:: struct sk_buff *get_packet_pg(struct adapter *adap, struct sge_fl *fl, struct sge_rspq *q, unsigned int len, unsigned int drop_thres)

    return the next ingress packet buffer from a free list

    :param struct adapter \*adap:
        the adapter that received the packet

    :param struct sge_fl \*fl:
        the SGE free list holding the packet

    :param struct sge_rspq \*q:
        *undescribed*

    :param unsigned int len:
        the packet length including any SGE padding

    :param unsigned int drop_thres:
        # of remaining buffers before we start dropping packets

.. _`get_packet_pg.description`:

Description
-----------

Get the next packet from a free list populated with page chunks.
If the packet is small we make a copy and recycle the original buffer,
otherwise we attach the original buffer as a page fragment to a fresh
sk_buff.  If a positive drop threshold is supplied packets are dropped
and their buffers recycled if (a) the number of remaining buffers is
under the threshold and the packet is too big to copy, or (b) there's
no system memory.

.. _`get_packet_pg.note`:

Note
----

this function is similar to \ ``get_packet``\  but deals with Rx buffers
that are page chunks rather than sk_buffs.

.. _`get_imm_packet`:

get_imm_packet
==============

.. c:function:: struct sk_buff *get_imm_packet(const struct rsp_desc *resp)

    return the next ingress packet buffer from a response

    :param const struct rsp_desc \*resp:
        the response descriptor containing the packet data

.. _`get_imm_packet.description`:

Description
-----------

Return a packet containing the immediate data of the given response.

.. _`calc_tx_descs`:

calc_tx_descs
=============

.. c:function:: unsigned int calc_tx_descs(const struct sk_buff *skb)

    calculate the number of Tx descriptors for a packet

    :param const struct sk_buff \*skb:
        the packet

.. _`calc_tx_descs.description`:

Description
-----------

Returns the number of Tx descriptors needed for the given Ethernet
packet.  Ethernet packets require addition of WR and CPL headers.

.. _`make_sgl`:

make_sgl
========

.. c:function:: unsigned int make_sgl(const struct sk_buff *skb, struct sg_ent *sgp, unsigned char *start, unsigned int len, struct pci_dev *pdev)

    populate a scatter/gather list for a packet

    :param const struct sk_buff \*skb:
        the packet

    :param struct sg_ent \*sgp:
        the SGL to populate

    :param unsigned char \*start:
        start address of skb main body data to include in the SGL

    :param unsigned int len:
        length of skb main body data to include in the SGL

    :param struct pci_dev \*pdev:
        the PCI device

.. _`make_sgl.description`:

Description
-----------

Generates a scatter/gather list for the buffers that make up a packet
and returns the SGL size in 8-byte words.  The caller must size the SGL
appropriately.

.. _`check_ring_tx_db`:

check_ring_tx_db
================

.. c:function:: void check_ring_tx_db(struct adapter *adap, struct sge_txq *q)

    check and potentially ring a Tx queue's doorbell

    :param struct adapter \*adap:
        the adapter

    :param struct sge_txq \*q:
        the Tx queue

.. _`check_ring_tx_db.description`:

Description
-----------

Ring the doorbel if a Tx queue is asleep.  There is a natural race,
where the HW is going to sleep just after we checked, however,
then the interrupt handler will detect the outstanding TX packet
and ring the doorbell for us.

When GTS is disabled we unconditionally ring the doorbell.

.. _`write_wr_hdr_sgl`:

write_wr_hdr_sgl
================

.. c:function:: void write_wr_hdr_sgl(unsigned int ndesc, struct sk_buff *skb, struct tx_desc *d, unsigned int pidx, const struct sge_txq *q, const struct sg_ent *sgl, unsigned int flits, unsigned int sgl_flits, unsigned int gen, __be32 wr_hi, __be32 wr_lo)

    write a WR header and, optionally, SGL

    :param unsigned int ndesc:
        number of Tx descriptors spanned by the SGL

    :param struct sk_buff \*skb:
        the packet corresponding to the WR

    :param struct tx_desc \*d:
        first Tx descriptor to be written

    :param unsigned int pidx:
        index of above descriptors

    :param const struct sge_txq \*q:
        the SGE Tx queue

    :param const struct sg_ent \*sgl:
        the SGL

    :param unsigned int flits:
        number of flits to the start of the SGL in the first descriptor

    :param unsigned int sgl_flits:
        the SGL size in flits

    :param unsigned int gen:
        the Tx descriptor generation

    :param __be32 wr_hi:
        top 32 bits of WR header based on WR type (big endian)

    :param __be32 wr_lo:
        low 32 bits of WR header based on WR type (big endian)

.. _`write_wr_hdr_sgl.description`:

Description
-----------

Write a work request header and an associated SGL.  If the SGL is
small enough to fit into one Tx descriptor it has already been written
and we just need to write the WR header.  Otherwise we distribute the
SGL across the number of descriptors it spans.

.. _`write_tx_pkt_wr`:

write_tx_pkt_wr
===============

.. c:function:: void write_tx_pkt_wr(struct adapter *adap, struct sk_buff *skb, const struct port_info *pi, unsigned int pidx, unsigned int gen, struct sge_txq *q, unsigned int ndesc, unsigned int compl)

    write a TX_PKT work request

    :param struct adapter \*adap:
        the adapter

    :param struct sk_buff \*skb:
        the packet to send

    :param const struct port_info \*pi:
        the egress interface

    :param unsigned int pidx:
        index of the first Tx descriptor to write

    :param unsigned int gen:
        the generation value to use

    :param struct sge_txq \*q:
        the Tx queue

    :param unsigned int ndesc:
        number of descriptors the packet will occupy

    :param unsigned int compl:
        the value of the COMPL bit to use

.. _`write_tx_pkt_wr.description`:

Description
-----------

Generate a TX_PKT work request to send the supplied packet.

.. _`t3_eth_xmit`:

t3_eth_xmit
===========

.. c:function:: netdev_tx_t t3_eth_xmit(struct sk_buff *skb, struct net_device *dev)

    add a packet to the Ethernet Tx queue

    :param struct sk_buff \*skb:
        the packet

    :param struct net_device \*dev:
        the egress net device

.. _`t3_eth_xmit.description`:

Description
-----------

Add a packet to an SGE Tx queue.  Runs with softirqs disabled.

.. _`write_imm`:

write_imm
=========

.. c:function:: void write_imm(struct tx_desc *d, struct sk_buff *skb, unsigned int len, unsigned int gen)

    write a packet into a Tx descriptor as immediate data

    :param struct tx_desc \*d:
        the Tx descriptor to write

    :param struct sk_buff \*skb:
        the packet

    :param unsigned int len:
        the length of packet data to write as immediate data

    :param unsigned int gen:
        the generation bit value to write

.. _`write_imm.description`:

Description
-----------

Writes a packet as immediate data into a Tx descriptor.  The packet
contains a work request at its beginning.  We must write the packet
carefully so the SGE doesn't read it accidentally before it's written
in its entirety.

.. _`check_desc_avail`:

check_desc_avail
================

.. c:function:: int check_desc_avail(struct adapter *adap, struct sge_txq *q, struct sk_buff *skb, unsigned int ndesc, unsigned int qid)

    check descriptor availability on a send queue

    :param struct adapter \*adap:
        the adapter

    :param struct sge_txq \*q:
        the send queue

    :param struct sk_buff \*skb:
        the packet needing the descriptors

    :param unsigned int ndesc:
        the number of Tx descriptors needed

    :param unsigned int qid:
        the Tx queue number in its queue set (TXQ_OFLD or TXQ_CTRL)

.. _`check_desc_avail.description`:

Description
-----------

Checks if the requested number of Tx descriptors is available on an
SGE send queue.  If the queue is already suspended or not enough
descriptors are available the packet is queued for later transmission.
Must be called with the Tx queue locked.

Returns 0 if enough descriptors are available, 1 if there aren't
enough descriptors and the packet has been queued, and 2 if the caller
needs to retry because there weren't enough descriptors at the
beginning of the call but some freed up in the mean time.

.. _`reclaim_completed_tx_imm`:

reclaim_completed_tx_imm
========================

.. c:function:: void reclaim_completed_tx_imm(struct sge_txq *q)

    reclaim completed control-queue Tx descs

    :param struct sge_txq \*q:
        the SGE control Tx queue

.. _`reclaim_completed_tx_imm.description`:

Description
-----------

This is a variant of \ :c:func:`reclaim_completed_tx`\  that is used for Tx queues
that send only immediate data (presently just the control queues) and
thus do not have any sk_buffs to release.

.. _`ctrl_xmit`:

ctrl_xmit
=========

.. c:function:: int ctrl_xmit(struct adapter *adap, struct sge_txq *q, struct sk_buff *skb)

    send a packet through an SGE control Tx queue

    :param struct adapter \*adap:
        the adapter

    :param struct sge_txq \*q:
        the control queue

    :param struct sk_buff \*skb:
        the packet

.. _`ctrl_xmit.description`:

Description
-----------

Send a packet through an SGE control Tx queue.  Packets sent through
a control queue must fit entirely as immediate data in a single Tx
descriptor and have no page fragments.

.. _`restart_ctrlq`:

restart_ctrlq
=============

.. c:function:: void restart_ctrlq(unsigned long data)

    restart a suspended control queue

    :param unsigned long data:
        *undescribed*

.. _`restart_ctrlq.description`:

Description
-----------

Resumes transmission on a suspended Tx control queue.

.. _`deferred_unmap_destructor`:

deferred_unmap_destructor
=========================

.. c:function:: void deferred_unmap_destructor(struct sk_buff *skb)

    unmap a packet when it is freed

    :param struct sk_buff \*skb:
        the packet

.. _`deferred_unmap_destructor.description`:

Description
-----------

This is the packet destructor used for Tx packets that need to remain
mapped until they are freed rather than until their Tx descriptors are
freed.

.. _`write_ofld_wr`:

write_ofld_wr
=============

.. c:function:: void write_ofld_wr(struct adapter *adap, struct sk_buff *skb, struct sge_txq *q, unsigned int pidx, unsigned int gen, unsigned int ndesc)

    write an offload work request

    :param struct adapter \*adap:
        the adapter

    :param struct sk_buff \*skb:
        the packet to send

    :param struct sge_txq \*q:
        the Tx queue

    :param unsigned int pidx:
        index of the first Tx descriptor to write

    :param unsigned int gen:
        the generation value to use

    :param unsigned int ndesc:
        number of descriptors the packet will occupy

.. _`write_ofld_wr.description`:

Description
-----------

Write an offload work request to send the supplied packet.  The packet
data already carry the work request with most fields populated.

.. _`calc_tx_descs_ofld`:

calc_tx_descs_ofld
==================

.. c:function:: unsigned int calc_tx_descs_ofld(const struct sk_buff *skb)

    calculate # of Tx descriptors for an offload packet

    :param const struct sk_buff \*skb:
        the packet

.. _`calc_tx_descs_ofld.description`:

Description
-----------

Returns the number of Tx descriptors needed for the given offload
packet.  These packets are already fully constructed.

.. _`ofld_xmit`:

ofld_xmit
=========

.. c:function:: int ofld_xmit(struct adapter *adap, struct sge_txq *q, struct sk_buff *skb)

    send a packet through an offload queue

    :param struct adapter \*adap:
        the adapter

    :param struct sge_txq \*q:
        the Tx offload queue

    :param struct sk_buff \*skb:
        the packet

.. _`ofld_xmit.description`:

Description
-----------

Send an offload packet through an SGE offload queue.

.. _`restart_offloadq`:

restart_offloadq
================

.. c:function:: void restart_offloadq(unsigned long data)

    restart a suspended offload queue

    :param unsigned long data:
        *undescribed*

.. _`restart_offloadq.description`:

Description
-----------

Resumes transmission on a suspended Tx offload queue.

.. _`queue_set`:

queue_set
=========

.. c:function:: int queue_set(const struct sk_buff *skb)

    return the queue set a packet should use

    :param const struct sk_buff \*skb:
        the packet

.. _`queue_set.description`:

Description
-----------

Maps a packet to the SGE queue set it should use.  The desired queue
set is carried in bits 1-3 in the packet's priority.

.. _`is_ctrl_pkt`:

is_ctrl_pkt
===========

.. c:function:: int is_ctrl_pkt(const struct sk_buff *skb)

    return whether an offload packet is a control packet

    :param const struct sk_buff \*skb:
        the packet

.. _`is_ctrl_pkt.description`:

Description
-----------

Determines whether an offload packet should use an OFLD or a CTRL
Tx queue.  This is indicated by bit 0 in the packet's priority.

.. _`t3_offload_tx`:

t3_offload_tx
=============

.. c:function:: int t3_offload_tx(struct t3cdev *tdev, struct sk_buff *skb)

    send an offload packet

    :param struct t3cdev \*tdev:
        the offload device to send to

    :param struct sk_buff \*skb:
        the packet

.. _`t3_offload_tx.description`:

Description
-----------

Sends an offload packet.  We use the packet priority to select the

.. _`t3_offload_tx.appropriate-tx-queue-as-follows`:

appropriate Tx queue as follows
-------------------------------

bit 0 indicates whether the packet
should be sent as regular or control, bits 1-3 select the queue set.

.. _`offload_enqueue`:

offload_enqueue
===============

.. c:function:: void offload_enqueue(struct sge_rspq *q, struct sk_buff *skb)

    add an offload packet to an SGE offload receive queue

    :param struct sge_rspq \*q:
        the SGE response queue

    :param struct sk_buff \*skb:
        the packet

.. _`offload_enqueue.description`:

Description
-----------

Add a new offload packet to an SGE response queue's offload packet
queue.  If the packet is the first on the queue it schedules the RX
softirq to process the queue.

.. _`deliver_partial_bundle`:

deliver_partial_bundle
======================

.. c:function:: void deliver_partial_bundle(struct t3cdev *tdev, struct sge_rspq *q, struct sk_buff  *skbs, int n)

    deliver a (partial) bundle of Rx offload pkts

    :param struct t3cdev \*tdev:
        the offload device that will be receiving the packets

    :param struct sge_rspq \*q:
        the SGE response queue that assembled the bundle

    :param struct sk_buff  \*skbs:
        the partial bundle

    :param int n:
        the number of packets in the bundle

.. _`deliver_partial_bundle.description`:

Description
-----------

Delivers a (partial) bundle of Rx offload packets to an offload device.

.. _`ofld_poll`:

ofld_poll
=========

.. c:function:: int ofld_poll(struct napi_struct *napi, int budget)

    NAPI handler for offload packets in interrupt mode

    :param struct napi_struct \*napi:
        *undescribed*

    :param int budget:
        polling budget

.. _`ofld_poll.description`:

Description
-----------

The NAPI handler for offload packets when a response queue is serviced
by the hard interrupt handler, i.e., when it's operating in non-polling
mode.  Creates small packet batches and sends them through the offload
receive handler.  Batches need to be of modest size as we do prefetches
on the packets in each.

.. _`rx_offload`:

rx_offload
==========

.. c:function:: int rx_offload(struct t3cdev *tdev, struct sge_rspq *rq, struct sk_buff *skb, struct sk_buff  *rx_gather, unsigned int gather_idx)

    process a received offload packet

    :param struct t3cdev \*tdev:
        the offload device receiving the packet

    :param struct sge_rspq \*rq:
        the response queue that received the packet

    :param struct sk_buff \*skb:
        the packet

    :param struct sk_buff  \*rx_gather:
        a gather list of packets if we are building a bundle

    :param unsigned int gather_idx:
        index of the next available slot in the bundle

.. _`rx_offload.description`:

Description
-----------

Process an ingress offload pakcet and add it to the offload ingress
queue.  Returns the index of the next available slot in the bundle.

.. _`restart_tx`:

restart_tx
==========

.. c:function:: void restart_tx(struct sge_qset *qs)

    check whether to restart suspended Tx queues

    :param struct sge_qset \*qs:
        the queue set to resume

.. _`restart_tx.description`:

Description
-----------

Restarts suspended Tx queues of an SGE queue set if they have enough
free resources to resume operation.

.. _`cxgb3_arp_process`:

cxgb3_arp_process
=================

.. c:function:: void cxgb3_arp_process(struct port_info *pi, struct sk_buff *skb)

    process an ARP request probing a private IP address

    :param struct port_info \*pi:
        *undescribed*

    :param struct sk_buff \*skb:
        the skbuff containing the ARP request

.. _`cxgb3_arp_process.description`:

Description
-----------

Check if the ARP request is probing the private IP address
dedicated to iSCSI, generate an ARP reply if so.

.. _`rx_eth`:

rx_eth
======

.. c:function:: void rx_eth(struct adapter *adap, struct sge_rspq *rq, struct sk_buff *skb, int pad, int lro)

    process an ingress ethernet packet

    :param struct adapter \*adap:
        the adapter

    :param struct sge_rspq \*rq:
        the response queue that received the packet

    :param struct sk_buff \*skb:
        the packet

    :param int pad:
        amount of padding at the start of the buffer

    :param int lro:
        *undescribed*

.. _`rx_eth.description`:

Description
-----------

Process an ingress ethernet pakcet and deliver it to the stack.
The padding is 2 if the packet was delivered in an Rx buffer and 0
if it was immediate data in a response.

.. _`lro_add_page`:

lro_add_page
============

.. c:function:: void lro_add_page(struct adapter *adap, struct sge_qset *qs, struct sge_fl *fl, int len, int complete)

    add a page chunk to an LRO session

    :param struct adapter \*adap:
        the adapter

    :param struct sge_qset \*qs:
        the associated queue set

    :param struct sge_fl \*fl:
        the free list containing the page chunk to add

    :param int len:
        packet length

    :param int complete:
        Indicates the last fragment of a frame

.. _`lro_add_page.description`:

Description
-----------

Add a received packet contained in a page chunk to an existing LRO
session.

.. _`handle_rsp_cntrl_info`:

handle_rsp_cntrl_info
=====================

.. c:function:: void handle_rsp_cntrl_info(struct sge_qset *qs, u32 flags)

    handles control information in a response

    :param struct sge_qset \*qs:
        the queue set corresponding to the response

    :param u32 flags:
        the response control flags

.. _`handle_rsp_cntrl_info.description`:

Description
-----------

Handles the control information of an SGE response, such as GTS
indications and completion credits for the queue set's Tx queues.
HW coalesces credits, we don't do any extra SW coalescing.

.. _`check_ring_db`:

check_ring_db
=============

.. c:function:: void check_ring_db(struct adapter *adap, struct sge_qset *qs, unsigned int sleeping)

    check if we need to ring any doorbells

    :param struct adapter \*adap:
        *undescribed*

    :param struct sge_qset \*qs:
        the queue set whose Tx queues are to be examined

    :param unsigned int sleeping:
        indicates which Tx queue sent GTS

.. _`check_ring_db.description`:

Description
-----------

Checks if some of a queue set's Tx queues need to ring their doorbells
to resume transmission after idling while they still have unprocessed
descriptors.

.. _`is_new_response`:

is_new_response
===============

.. c:function:: int is_new_response(const struct rsp_desc *r, const struct sge_rspq *q)

    check if a response is newly written

    :param const struct rsp_desc \*r:
        the response descriptor

    :param const struct sge_rspq \*q:
        the response queue

.. _`is_new_response.description`:

Description
-----------

Returns true if a response descriptor contains a yet unprocessed
response.

.. _`process_responses`:

process_responses
=================

.. c:function:: int process_responses(struct adapter *adap, struct sge_qset *qs, int budget)

    process responses from an SGE response queue

    :param struct adapter \*adap:
        the adapter

    :param struct sge_qset \*qs:
        the queue set to which the response queue belongs

    :param int budget:
        how many responses can be processed in this round

.. _`process_responses.description`:

Description
-----------

Process responses from an SGE response queue up to the supplied budget.
Responses include received packets as well as credits and other events
for the queues that belong to the response queue's queue set.
A negative budget is effectively unlimited.

Additionally choose the interrupt holdoff time for the next interrupt
on this queue.  If the system is under memory shortage use a fairly
long delay to help recovery.

.. _`napi_rx_handler`:

napi_rx_handler
===============

.. c:function:: int napi_rx_handler(struct napi_struct *napi, int budget)

    the NAPI handler for Rx processing

    :param struct napi_struct \*napi:
        the napi instance

    :param int budget:
        how many packets we can process in this round

.. _`napi_rx_handler.description`:

Description
-----------

Handler for new data events when using NAPI.

.. _`process_pure_responses`:

process_pure_responses
======================

.. c:function:: int process_pure_responses(struct adapter *adap, struct sge_qset *qs, struct rsp_desc *r)

    process pure responses from a response queue

    :param struct adapter \*adap:
        the adapter

    :param struct sge_qset \*qs:
        the queue set owning the response queue

    :param struct rsp_desc \*r:
        the first pure response to process

.. _`process_pure_responses.description`:

Description
-----------

A simpler version of \ :c:func:`process_responses`\  that handles only pure (i.e.,
non data-carrying) responses.  Such respones are too light-weight to
justify calling a softirq under NAPI, so we handle them specially in
the interrupt handler.  The function is called with a pointer to a
response, which the caller must ensure is a valid pure response.

Returns 1 if it encounters a valid data-carrying response, 0 otherwise.

.. _`handle_responses`:

handle_responses
================

.. c:function:: int handle_responses(struct adapter *adap, struct sge_rspq *q)

    decide what to do with new responses in NAPI mode

    :param struct adapter \*adap:
        the adapter

    :param struct sge_rspq \*q:
        the response queue

.. _`handle_responses.description`:

Description
-----------

This is used by the NAPI interrupt handlers to decide what to do with
new SGE responses.  If there are no new responses it returns -1.  If
there are new responses and they are pure (i.e., non-data carrying)
it handles them straight in hard interrupt context as they are very
cheap and don't deliver any packets.  Finally, if there are any data
signaling responses it schedules the NAPI handler.  Returns 1 if it
schedules NAPI, 0 if all new responses were pure.

The caller must ascertain NAPI is not already running.

.. _`t3_intr_handler`:

t3_intr_handler
===============

.. c:function:: irq_handler_t t3_intr_handler(struct adapter *adap, int polling)

    select the top-level interrupt handler

    :param struct adapter \*adap:
        the adapter

    :param int polling:
        whether using NAPI to service response queues

.. _`t3_intr_handler.description`:

Description
-----------

Selects the top-level interrupt handler based on the type of interrupts
(MSI-X, MSI, or legacy) and whether NAPI will be used to service the
response queues.

.. _`t3_sge_err_intr_handler`:

t3_sge_err_intr_handler
=======================

.. c:function:: void t3_sge_err_intr_handler(struct adapter *adapter)

    SGE async event interrupt handler

    :param struct adapter \*adapter:
        the adapter

.. _`t3_sge_err_intr_handler.description`:

Description
-----------

Interrupt handler for SGE asynchronous (non-data) events.

.. _`sge_timer_tx`:

sge_timer_tx
============

.. c:function:: void sge_timer_tx(unsigned long data)

    perform periodic maintenance of an SGE qset

    :param unsigned long data:
        the SGE queue set to maintain

.. _`sge_timer_tx.description`:

Description
-----------

Runs periodically from a timer to perform maintenance of an SGE queue
set.  It performs two tasks:

Cleans up any completed Tx descriptors that may still be pending.
Normal descriptor cleanup happens when new packets are added to a Tx
queue so this timer is relatively infrequent and does any cleanup only
if the Tx queue has not seen any new packets in a while.  We make a
best effort attempt to reclaim descriptors, in that we don't wait
around if we cannot get a queue's lock (which most likely is because
someone else is queueing new packets and so will also handle the clean
up).  Since control queues use immediate data exclusively we don't
bother cleaning them up here.

.. _`sge_timer_rx`:

sge_timer_rx
============

.. c:function:: void sge_timer_rx(unsigned long data)

    perform periodic maintenance of an SGE qset

    :param unsigned long data:
        the SGE queue set to maintain

.. _`sge_timer_rx.description`:

Description
-----------

a) Replenishes Rx queues that have run out due to memory shortage.
Normally new Rx buffers are added when existing ones are consumed but
when out of memory a queue can become empty.  We try to add only a few
buffers here, the queue will be replenished fully as these new buffers
are used up if memory shortage has subsided.

b) Return coalesced response queue credits in case a response queue is
starved.

.. _`t3_update_qset_coalesce`:

t3_update_qset_coalesce
=======================

.. c:function:: void t3_update_qset_coalesce(struct sge_qset *qs, const struct qset_params *p)

    update coalescing settings for a queue set

    :param struct sge_qset \*qs:
        the SGE queue set

    :param const struct qset_params \*p:
        new queue set parameters

.. _`t3_update_qset_coalesce.description`:

Description
-----------

Update the coalescing settings for an SGE queue set.  Nothing is done
if the queue set is not initialized yet.

.. _`t3_sge_alloc_qset`:

t3_sge_alloc_qset
=================

.. c:function:: int t3_sge_alloc_qset(struct adapter *adapter, unsigned int id, int nports, int irq_vec_idx, const struct qset_params *p, int ntxq, struct net_device *dev, struct netdev_queue *netdevq)

    initialize an SGE queue set

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int id:
        the queue set id

    :param int nports:
        how many Ethernet ports will be using this queue set

    :param int irq_vec_idx:
        the IRQ vector index for response queue interrupts

    :param const struct qset_params \*p:
        configuration parameters for this queue set

    :param int ntxq:
        number of Tx queues for the queue set

    :param struct net_device \*dev:
        *undescribed*

    :param struct netdev_queue \*netdevq:
        net device TX queue associated with this queue set

.. _`t3_sge_alloc_qset.description`:

Description
-----------

Allocate resources and initialize an SGE queue set.  A queue set
comprises a response queue, two Rx free-buffer queues, and up to 3
Tx queues.  The Tx queues are assigned roles in the order Ethernet
queue, offload queue, and control queue.

.. _`t3_start_sge_timers`:

t3_start_sge_timers
===================

.. c:function:: void t3_start_sge_timers(struct adapter *adap)

    start SGE timer call backs

    :param struct adapter \*adap:
        the adapter

.. _`t3_start_sge_timers.description`:

Description
-----------

Starts each SGE queue set's timer call back

.. _`t3_stop_sge_timers`:

t3_stop_sge_timers
==================

.. c:function:: void t3_stop_sge_timers(struct adapter *adap)

    stop SGE timer call backs

    :param struct adapter \*adap:
        the adapter

.. _`t3_stop_sge_timers.description`:

Description
-----------

Stops each SGE queue set's timer call back

.. _`t3_free_sge_resources`:

t3_free_sge_resources
=====================

.. c:function:: void t3_free_sge_resources(struct adapter *adap)

    free SGE resources

    :param struct adapter \*adap:
        the adapter

.. _`t3_free_sge_resources.description`:

Description
-----------

Frees resources used by the SGE queue sets.

.. _`t3_sge_start`:

t3_sge_start
============

.. c:function:: void t3_sge_start(struct adapter *adap)

    enable SGE

    :param struct adapter \*adap:
        the adapter

.. _`t3_sge_start.description`:

Description
-----------

Enables the SGE for DMAs.  This is the last step in starting packet
transfers.

.. _`t3_sge_stop`:

t3_sge_stop
===========

.. c:function:: void t3_sge_stop(struct adapter *adap)

    disable SGE operation

    :param struct adapter \*adap:
        the adapter

.. _`t3_sge_stop.description`:

Description
-----------

Disables the DMA engine.  This can be called in emeregencies (e.g.,
from error interrupts) or from normal process context.  In the latter
case it also disables any pending queue restart tasklets.  Note that
if it is called in interrupt context it cannot disable the restart
tasklets as it cannot wait, however the tasklets will have no effect
since the doorbells are disabled and the driver will call this again
later from process context, at which time the tasklets will be stopped
if they are still running.

.. _`t3_sge_init`:

t3_sge_init
===========

.. c:function:: void t3_sge_init(struct adapter *adap, struct sge_params *p)

    initialize SGE

    :param struct adapter \*adap:
        the adapter

    :param struct sge_params \*p:
        the SGE parameters

.. _`t3_sge_init.description`:

Description
-----------

Performs SGE initialization needed every time after a chip reset.
We do not initialize any of the queue sets here, instead the driver
top-level must request those individually.  We also do not enable DMA
here, that should be done after the queues have been set up.

.. _`t3_sge_prep`:

t3_sge_prep
===========

.. c:function:: void t3_sge_prep(struct adapter *adap, struct sge_params *p)

    one-time SGE initialization

    :param struct adapter \*adap:
        the associated adapter

    :param struct sge_params \*p:
        SGE parameters

.. _`t3_sge_prep.description`:

Description
-----------

Performs one-time initialization of SGE SW state.  Includes determining
defaults for the assorted SGE parameters, which admins can change until
they are used to initialize the SGE.

.. This file was automatic generated / don't edit.

