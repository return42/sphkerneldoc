.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/ppc4xx/adma.c

.. _`ppc440spe_desc_init_interrupt`:

ppc440spe_desc_init_interrupt
=============================

.. c:function:: void ppc440spe_desc_init_interrupt(struct ppc440spe_adma_desc_slot *desc, struct ppc440spe_adma_chan *chan)

    initialize the descriptor for INTERRUPT pseudo operation

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

.. _`ppc440spe_desc_init_null_xor`:

ppc440spe_desc_init_null_xor
============================

.. c:function:: void ppc440spe_desc_init_null_xor(struct ppc440spe_adma_desc_slot *desc)

    initialize the descriptor for NULL XOR pseudo operation

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

.. _`ppc440spe_desc_init_xor`:

ppc440spe_desc_init_xor
=======================

.. c:function:: void ppc440spe_desc_init_xor(struct ppc440spe_adma_desc_slot *desc, int src_cnt, unsigned long flags)

    initialize the descriptor for XOR operation

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param src_cnt:
        *undescribed*
    :type src_cnt: int

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`ppc440spe_desc_init_dma2pq`:

ppc440spe_desc_init_dma2pq
==========================

.. c:function:: void ppc440spe_desc_init_dma2pq(struct ppc440spe_adma_desc_slot *desc, int dst_cnt, int src_cnt, unsigned long flags)

    initialize the descriptor for PQ operation in DMA2 controller

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param dst_cnt:
        *undescribed*
    :type dst_cnt: int

    :param src_cnt:
        *undescribed*
    :type src_cnt: int

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`ppc440spe_desc_init_dma01pq`:

ppc440spe_desc_init_dma01pq
===========================

.. c:function:: void ppc440spe_desc_init_dma01pq(struct ppc440spe_adma_desc_slot *desc, int dst_cnt, int src_cnt, unsigned long flags, unsigned long op)

    initialize the descriptors for PQ operation with DMA0/1

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param dst_cnt:
        *undescribed*
    :type dst_cnt: int

    :param src_cnt:
        *undescribed*
    :type src_cnt: int

    :param flags:
        *undescribed*
    :type flags: unsigned long

    :param op:
        *undescribed*
    :type op: unsigned long

.. _`ppc440spe_desc_init_dma01pqzero_sum`:

ppc440spe_desc_init_dma01pqzero_sum
===================================

.. c:function:: void ppc440spe_desc_init_dma01pqzero_sum(struct ppc440spe_adma_desc_slot *desc, int dst_cnt, int src_cnt)

    initialize the descriptor for PQ_ZERO_SUM operation

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param dst_cnt:
        *undescribed*
    :type dst_cnt: int

    :param src_cnt:
        *undescribed*
    :type src_cnt: int

.. _`ppc440spe_desc_init_memcpy`:

ppc440spe_desc_init_memcpy
==========================

.. c:function:: void ppc440spe_desc_init_memcpy(struct ppc440spe_adma_desc_slot *desc, unsigned long flags)

    initialize the descriptor for MEMCPY operation

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`ppc440spe_desc_set_src_addr`:

ppc440spe_desc_set_src_addr
===========================

.. c:function:: void ppc440spe_desc_set_src_addr(struct ppc440spe_adma_desc_slot *desc, struct ppc440spe_adma_chan *chan, int src_idx, dma_addr_t addrh, dma_addr_t addrl)

    set source address into the descriptor

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

    :param src_idx:
        *undescribed*
    :type src_idx: int

    :param addrh:
        *undescribed*
    :type addrh: dma_addr_t

    :param addrl:
        *undescribed*
    :type addrl: dma_addr_t

.. _`ppc440spe_desc_set_src_mult`:

ppc440spe_desc_set_src_mult
===========================

.. c:function:: void ppc440spe_desc_set_src_mult(struct ppc440spe_adma_desc_slot *desc, struct ppc440spe_adma_chan *chan, u32 mult_index, int sg_index, unsigned char mult_value)

    set source address mult into the descriptor

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

    :param mult_index:
        *undescribed*
    :type mult_index: u32

    :param sg_index:
        *undescribed*
    :type sg_index: int

    :param mult_value:
        *undescribed*
    :type mult_value: unsigned char

.. _`ppc440spe_desc_set_dest_addr`:

ppc440spe_desc_set_dest_addr
============================

.. c:function:: void ppc440spe_desc_set_dest_addr(struct ppc440spe_adma_desc_slot *desc, struct ppc440spe_adma_chan *chan, dma_addr_t addrh, dma_addr_t addrl, u32 dst_idx)

    set destination address into the descriptor

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

    :param addrh:
        *undescribed*
    :type addrh: dma_addr_t

    :param addrl:
        *undescribed*
    :type addrl: dma_addr_t

    :param dst_idx:
        *undescribed*
    :type dst_idx: u32

.. _`ppc440spe_desc_set_byte_count`:

ppc440spe_desc_set_byte_count
=============================

.. c:function:: void ppc440spe_desc_set_byte_count(struct ppc440spe_adma_desc_slot *desc, struct ppc440spe_adma_chan *chan, u32 byte_count)

    set number of data bytes involved into the operation

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

    :param byte_count:
        *undescribed*
    :type byte_count: u32

.. _`ppc440spe_desc_set_rxor_block_size`:

ppc440spe_desc_set_rxor_block_size
==================================

.. c:function:: void ppc440spe_desc_set_rxor_block_size(u32 byte_count)

    set RXOR block size

    :param byte_count:
        *undescribed*
    :type byte_count: u32

.. _`ppc440spe_desc_set_dcheck`:

ppc440spe_desc_set_dcheck
=========================

.. c:function:: void ppc440spe_desc_set_dcheck(struct ppc440spe_adma_desc_slot *desc, struct ppc440spe_adma_chan *chan, u8 *qword)

    set CHECK pattern

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

    :param qword:
        *undescribed*
    :type qword: u8 \*

.. _`ppc440spe_xor_set_link`:

ppc440spe_xor_set_link
======================

.. c:function:: void ppc440spe_xor_set_link(struct ppc440spe_adma_desc_slot *prev_desc, struct ppc440spe_adma_desc_slot *next_desc)

    set link address in xor CB

    :param prev_desc:
        *undescribed*
    :type prev_desc: struct ppc440spe_adma_desc_slot \*

    :param next_desc:
        *undescribed*
    :type next_desc: struct ppc440spe_adma_desc_slot \*

.. _`ppc440spe_desc_set_link`:

ppc440spe_desc_set_link
=======================

.. c:function:: void ppc440spe_desc_set_link(struct ppc440spe_adma_chan *chan, struct ppc440spe_adma_desc_slot *prev_desc, struct ppc440spe_adma_desc_slot *next_desc)

    set the address of descriptor following this descriptor in chain

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

    :param prev_desc:
        *undescribed*
    :type prev_desc: struct ppc440spe_adma_desc_slot \*

    :param next_desc:
        *undescribed*
    :type next_desc: struct ppc440spe_adma_desc_slot \*

.. _`ppc440spe_desc_get_link`:

ppc440spe_desc_get_link
=======================

.. c:function:: u32 ppc440spe_desc_get_link(struct ppc440spe_adma_desc_slot *desc, struct ppc440spe_adma_chan *chan)

    get the address of the descriptor that follows this one

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

.. _`ppc440spe_desc_is_aligned`:

ppc440spe_desc_is_aligned
=========================

.. c:function:: int ppc440spe_desc_is_aligned(struct ppc440spe_adma_desc_slot *desc, int num_slots)

    check alignment

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param num_slots:
        *undescribed*
    :type num_slots: int

.. _`ppc440spe_chan_xor_slot_count`:

ppc440spe_chan_xor_slot_count
=============================

.. c:function:: int ppc440spe_chan_xor_slot_count(size_t len, int src_cnt, int *slots_per_op)

    get the number of slots necessary for XOR operation

    :param len:
        *undescribed*
    :type len: size_t

    :param src_cnt:
        *undescribed*
    :type src_cnt: int

    :param slots_per_op:
        *undescribed*
    :type slots_per_op: int \*

.. _`ppc440spe_dma2_pq_slot_count`:

ppc440spe_dma2_pq_slot_count
============================

.. c:function:: int ppc440spe_dma2_pq_slot_count(dma_addr_t *srcs, int src_cnt, size_t len)

    get the number of slots necessary for DMA2 PQ operation

    :param srcs:
        *undescribed*
    :type srcs: dma_addr_t \*

    :param src_cnt:
        *undescribed*
    :type src_cnt: int

    :param len:
        *undescribed*
    :type len: size_t

.. _`ppc440spe_adma_device_clear_eot_status`:

ppc440spe_adma_device_clear_eot_status
======================================

.. c:function:: void ppc440spe_adma_device_clear_eot_status(struct ppc440spe_adma_chan *chan)

    interrupt ack to XOR or DMA engine

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

.. _`ppc440spe_chan_is_busy`:

ppc440spe_chan_is_busy
======================

.. c:function:: int ppc440spe_chan_is_busy(struct ppc440spe_adma_chan *chan)

    get the channel status

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

.. _`ppc440spe_chan_set_first_xor_descriptor`:

ppc440spe_chan_set_first_xor_descriptor
=======================================

.. c:function:: void ppc440spe_chan_set_first_xor_descriptor(struct ppc440spe_adma_chan *chan, struct ppc440spe_adma_desc_slot *next_desc)

    init XORcore chain

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

    :param next_desc:
        *undescribed*
    :type next_desc: struct ppc440spe_adma_desc_slot \*

.. _`ppc440spe_dma_put_desc`:

ppc440spe_dma_put_desc
======================

.. c:function:: void ppc440spe_dma_put_desc(struct ppc440spe_adma_chan *chan, struct ppc440spe_adma_desc_slot *desc)

    put DMA0,1 descriptor to FIFO. called with irqs disabled

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

.. _`ppc440spe_chan_append`:

ppc440spe_chan_append
=====================

.. c:function:: void ppc440spe_chan_append(struct ppc440spe_adma_chan *chan)

    update the h/w chain in the channel

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

.. _`ppc440spe_chan_get_current_descriptor`:

ppc440spe_chan_get_current_descriptor
=====================================

.. c:function:: u32 ppc440spe_chan_get_current_descriptor(struct ppc440spe_adma_chan *chan)

    get the currently executed descriptor

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

.. _`ppc440spe_chan_run`:

ppc440spe_chan_run
==================

.. c:function:: void ppc440spe_chan_run(struct ppc440spe_adma_chan *chan)

    enable the channel

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

.. _`ppc440spe_can_rxor`:

ppc440spe_can_rxor
==================

.. c:function:: int ppc440spe_can_rxor(struct page **srcs, int src_cnt, size_t len)

    check if the operands may be processed with RXOR

    :param srcs:
        *undescribed*
    :type srcs: struct page \*\*

    :param src_cnt:
        *undescribed*
    :type src_cnt: int

    :param len:
        *undescribed*
    :type len: size_t

.. _`ppc440spe_adma_estimate`:

ppc440spe_adma_estimate
=======================

.. c:function:: int ppc440spe_adma_estimate(struct dma_chan *chan, enum dma_transaction_type cap, struct page **dst_lst, int dst_cnt, struct page **src_lst, int src_cnt, size_t src_sz)

    estimate the efficiency of processing the operation given on this channel. It's assumed that 'chan' is capable to process 'cap' type of operation.

    :param chan:
        channel to use
    :type chan: struct dma_chan \*

    :param cap:
        type of transaction
    :type cap: enum dma_transaction_type

    :param dst_lst:
        array of destination pointers
    :type dst_lst: struct page \*\*

    :param dst_cnt:
        number of destination operands
    :type dst_cnt: int

    :param src_lst:
        array of source pointers
    :type src_lst: struct page \*\*

    :param src_cnt:
        number of source operands
    :type src_cnt: int

    :param src_sz:
        size of each source operand
    :type src_sz: size_t

.. _`ppc440spe_get_group_entry`:

ppc440spe_get_group_entry
=========================

.. c:function:: struct ppc440spe_adma_desc_slot *ppc440spe_get_group_entry(struct ppc440spe_adma_desc_slot *tdesc, u32 entry_idx)

    get group entry with index idx

    :param tdesc:
        is the last allocated slot in the group.
    :type tdesc: struct ppc440spe_adma_desc_slot \*

    :param entry_idx:
        *undescribed*
    :type entry_idx: u32

.. _`ppc440spe_adma_free_slots`:

ppc440spe_adma_free_slots
=========================

.. c:function:: void ppc440spe_adma_free_slots(struct ppc440spe_adma_desc_slot *slot, struct ppc440spe_adma_chan *chan)

    flags descriptor slots for reuse

    :param slot:
        Slot to free
        Caller must hold \ :c:type:`ppc440spe_chan->lock <ppc440spe_chan>`\  while calling this function
    :type slot: struct ppc440spe_adma_desc_slot \*

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

.. _`ppc440spe_adma_run_tx_complete_actions`:

ppc440spe_adma_run_tx_complete_actions
======================================

.. c:function:: dma_cookie_t ppc440spe_adma_run_tx_complete_actions(struct ppc440spe_adma_desc_slot *desc, struct ppc440spe_adma_chan *chan, dma_cookie_t cookie)

    call functions to be called upon completion

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

    :param cookie:
        *undescribed*
    :type cookie: dma_cookie_t

.. _`ppc440spe_adma_clean_slot`:

ppc440spe_adma_clean_slot
=========================

.. c:function:: int ppc440spe_adma_clean_slot(struct ppc440spe_adma_desc_slot *desc, struct ppc440spe_adma_chan *chan)

    clean up CDB slot (if ack is set)

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

.. _`__ppc440spe_adma_slot_cleanup`:

\__ppc440spe_adma_slot_cleanup
==============================

.. c:function:: void __ppc440spe_adma_slot_cleanup(struct ppc440spe_adma_chan *chan)

    this is the common clean-up routine which runs through the channel CDBs list until reach the descriptor currently processed. When routine determines that all CDBs of group are completed then corresponding callbacks (if any) are called and slots are freed.

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

.. _`ppc440spe_adma_tasklet`:

ppc440spe_adma_tasklet
======================

.. c:function:: void ppc440spe_adma_tasklet(unsigned long data)

    clean up watch-dog initiator

    :param data:
        *undescribed*
    :type data: unsigned long

.. _`ppc440spe_adma_slot_cleanup`:

ppc440spe_adma_slot_cleanup
===========================

.. c:function:: void ppc440spe_adma_slot_cleanup(struct ppc440spe_adma_chan *chan)

    clean up scheduled initiator

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

.. _`ppc440spe_adma_alloc_slots`:

ppc440spe_adma_alloc_slots
==========================

.. c:function:: struct ppc440spe_adma_desc_slot *ppc440spe_adma_alloc_slots(struct ppc440spe_adma_chan *chan, int num_slots, int slots_per_op)

    allocate free slots (if any)

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

    :param num_slots:
        *undescribed*
    :type num_slots: int

    :param slots_per_op:
        *undescribed*
    :type slots_per_op: int

.. _`ppc440spe_adma_alloc_chan_resources`:

ppc440spe_adma_alloc_chan_resources
===================================

.. c:function:: int ppc440spe_adma_alloc_chan_resources(struct dma_chan *chan)

    allocate pools for CDB slots

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

.. _`ppc440spe_rxor_set_region`:

ppc440spe_rxor_set_region
=========================

.. c:function:: void ppc440spe_rxor_set_region(struct ppc440spe_adma_desc_slot *desc, u8 xor_arg_no, u32 mask)

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param xor_arg_no:
        *undescribed*
    :type xor_arg_no: u8

    :param mask:
        *undescribed*
    :type mask: u32

.. _`ppc440spe_rxor_set_src`:

ppc440spe_rxor_set_src
======================

.. c:function:: void ppc440spe_rxor_set_src(struct ppc440spe_adma_desc_slot *desc, u8 xor_arg_no, dma_addr_t addr)

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param xor_arg_no:
        *undescribed*
    :type xor_arg_no: u8

    :param addr:
        *undescribed*
    :type addr: dma_addr_t

.. _`ppc440spe_rxor_set_mult`:

ppc440spe_rxor_set_mult
=======================

.. c:function:: void ppc440spe_rxor_set_mult(struct ppc440spe_adma_desc_slot *desc, u8 xor_arg_no, u8 idx, u8 mult)

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param xor_arg_no:
        *undescribed*
    :type xor_arg_no: u8

    :param idx:
        *undescribed*
    :type idx: u8

    :param mult:
        *undescribed*
    :type mult: u8

.. _`ppc440spe_adma_check_threshold`:

ppc440spe_adma_check_threshold
==============================

.. c:function:: void ppc440spe_adma_check_threshold(struct ppc440spe_adma_chan *chan)

    append CDBs to h/w chain if threshold has been achieved

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

.. _`ppc440spe_adma_tx_submit`:

ppc440spe_adma_tx_submit
========================

.. c:function:: dma_cookie_t ppc440spe_adma_tx_submit(struct dma_async_tx_descriptor *tx)

    submit new descriptor group to the channel (it's not necessary that descriptors will be submitted to the h/w chains too right now)

    :param tx:
        *undescribed*
    :type tx: struct dma_async_tx_descriptor \*

.. _`ppc440spe_adma_prep_dma_interrupt`:

ppc440spe_adma_prep_dma_interrupt
=================================

.. c:function:: struct dma_async_tx_descriptor *ppc440spe_adma_prep_dma_interrupt(struct dma_chan *chan, unsigned long flags)

    prepare CDB for a pseudo DMA operation

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`ppc440spe_adma_prep_dma_memcpy`:

ppc440spe_adma_prep_dma_memcpy
==============================

.. c:function:: struct dma_async_tx_descriptor *ppc440spe_adma_prep_dma_memcpy(struct dma_chan *chan, dma_addr_t dma_dest, dma_addr_t dma_src, size_t len, unsigned long flags)

    prepare CDB for a MEMCPY operation

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

    :param dma_dest:
        *undescribed*
    :type dma_dest: dma_addr_t

    :param dma_src:
        *undescribed*
    :type dma_src: dma_addr_t

    :param len:
        *undescribed*
    :type len: size_t

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`ppc440spe_adma_prep_dma_xor`:

ppc440spe_adma_prep_dma_xor
===========================

.. c:function:: struct dma_async_tx_descriptor *ppc440spe_adma_prep_dma_xor(struct dma_chan *chan, dma_addr_t dma_dest, dma_addr_t *dma_src, u32 src_cnt, size_t len, unsigned long flags)

    prepare CDB for a XOR operation

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

    :param dma_dest:
        *undescribed*
    :type dma_dest: dma_addr_t

    :param dma_src:
        *undescribed*
    :type dma_src: dma_addr_t \*

    :param src_cnt:
        *undescribed*
    :type src_cnt: u32

    :param len:
        *undescribed*
    :type len: size_t

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`ppc440spe_adma_init_dma2rxor_slot`:

ppc440spe_adma_init_dma2rxor_slot
=================================

.. c:function:: void ppc440spe_adma_init_dma2rxor_slot(struct ppc440spe_adma_desc_slot *desc, dma_addr_t *src, int src_cnt)

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param src:
        *undescribed*
    :type src: dma_addr_t \*

    :param src_cnt:
        *undescribed*
    :type src_cnt: int

.. _`ppc440spe_dma01_prep_mult`:

ppc440spe_dma01_prep_mult
=========================

.. c:function:: struct ppc440spe_adma_desc_slot *ppc440spe_dma01_prep_mult(struct ppc440spe_adma_chan *ppc440spe_chan, dma_addr_t *dst, int dst_cnt, dma_addr_t *src, int src_cnt, const unsigned char *scf, size_t len, unsigned long flags)

    for Q operation where destination is also the source

    :param ppc440spe_chan:
        *undescribed*
    :type ppc440spe_chan: struct ppc440spe_adma_chan \*

    :param dst:
        *undescribed*
    :type dst: dma_addr_t \*

    :param dst_cnt:
        *undescribed*
    :type dst_cnt: int

    :param src:
        *undescribed*
    :type src: dma_addr_t \*

    :param src_cnt:
        *undescribed*
    :type src_cnt: int

    :param scf:
        *undescribed*
    :type scf: const unsigned char \*

    :param len:
        *undescribed*
    :type len: size_t

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`ppc440spe_dma01_prep_sum_product`:

ppc440spe_dma01_prep_sum_product
================================

.. c:function:: struct ppc440spe_adma_desc_slot *ppc440spe_dma01_prep_sum_product(struct ppc440spe_adma_chan *ppc440spe_chan, dma_addr_t *dst, dma_addr_t *src, int src_cnt, const unsigned char *scf, size_t len, unsigned long flags)

    Dx = A\*(P+Pxy) + B\*(Q+Qxy) operation where destination is also the source.

    :param ppc440spe_chan:
        *undescribed*
    :type ppc440spe_chan: struct ppc440spe_adma_chan \*

    :param dst:
        *undescribed*
    :type dst: dma_addr_t \*

    :param src:
        *undescribed*
    :type src: dma_addr_t \*

    :param src_cnt:
        *undescribed*
    :type src_cnt: int

    :param scf:
        *undescribed*
    :type scf: const unsigned char \*

    :param len:
        *undescribed*
    :type len: size_t

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`ppc440spe_adma_prep_dma_pq`:

ppc440spe_adma_prep_dma_pq
==========================

.. c:function:: struct dma_async_tx_descriptor *ppc440spe_adma_prep_dma_pq(struct dma_chan *chan, dma_addr_t *dst, dma_addr_t *src, unsigned int src_cnt, const unsigned char *scf, size_t len, unsigned long flags)

    prepare CDB (group) for a GF-XOR operation

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

    :param dst:
        *undescribed*
    :type dst: dma_addr_t \*

    :param src:
        *undescribed*
    :type src: dma_addr_t \*

    :param src_cnt:
        *undescribed*
    :type src_cnt: unsigned int

    :param scf:
        *undescribed*
    :type scf: const unsigned char \*

    :param len:
        *undescribed*
    :type len: size_t

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`ppc440spe_adma_prep_dma_pqzero_sum`:

ppc440spe_adma_prep_dma_pqzero_sum
==================================

.. c:function:: struct dma_async_tx_descriptor *ppc440spe_adma_prep_dma_pqzero_sum(struct dma_chan *chan, dma_addr_t *pq, dma_addr_t *src, unsigned int src_cnt, const unsigned char *scf, size_t len, enum sum_check_flags *pqres, unsigned long flags)

    prepare CDB group for a PQ_ZERO_SUM operation

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

    :param pq:
        *undescribed*
    :type pq: dma_addr_t \*

    :param src:
        *undescribed*
    :type src: dma_addr_t \*

    :param src_cnt:
        *undescribed*
    :type src_cnt: unsigned int

    :param scf:
        *undescribed*
    :type scf: const unsigned char \*

    :param len:
        *undescribed*
    :type len: size_t

    :param pqres:
        *undescribed*
    :type pqres: enum sum_check_flags \*

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`ppc440spe_adma_prep_dma_xor_zero_sum`:

ppc440spe_adma_prep_dma_xor_zero_sum
====================================

.. c:function:: struct dma_async_tx_descriptor *ppc440spe_adma_prep_dma_xor_zero_sum(struct dma_chan *chan, dma_addr_t *src, unsigned int src_cnt, size_t len, enum sum_check_flags *result, unsigned long flags)

    prepare CDB group for XOR ZERO_SUM operation

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

    :param src:
        *undescribed*
    :type src: dma_addr_t \*

    :param src_cnt:
        *undescribed*
    :type src_cnt: unsigned int

    :param len:
        *undescribed*
    :type len: size_t

    :param result:
        *undescribed*
    :type result: enum sum_check_flags \*

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`ppc440spe_adma_set_dest`:

ppc440spe_adma_set_dest
=======================

.. c:function:: void ppc440spe_adma_set_dest(struct ppc440spe_adma_desc_slot *sw_desc, dma_addr_t addr, int index)

    set destination address into descriptor

    :param sw_desc:
        *undescribed*
    :type sw_desc: struct ppc440spe_adma_desc_slot \*

    :param addr:
        *undescribed*
    :type addr: dma_addr_t

    :param index:
        *undescribed*
    :type index: int

.. _`ppc440spe_adma_pq_set_dest`:

ppc440spe_adma_pq_set_dest
==========================

.. c:function:: void ppc440spe_adma_pq_set_dest(struct ppc440spe_adma_desc_slot *sw_desc, dma_addr_t *addrs, unsigned long flags)

    set destination address into descriptor for the PQXOR operation

    :param sw_desc:
        *undescribed*
    :type sw_desc: struct ppc440spe_adma_desc_slot \*

    :param addrs:
        *undescribed*
    :type addrs: dma_addr_t \*

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`ppc440spe_adma_pqzero_sum_set_dest`:

ppc440spe_adma_pqzero_sum_set_dest
==================================

.. c:function:: void ppc440spe_adma_pqzero_sum_set_dest(struct ppc440spe_adma_desc_slot *sw_desc, dma_addr_t paddr, dma_addr_t qaddr)

    set destination address into descriptor for the PQ_ZERO_SUM operation

    :param sw_desc:
        *undescribed*
    :type sw_desc: struct ppc440spe_adma_desc_slot \*

    :param paddr:
        *undescribed*
    :type paddr: dma_addr_t

    :param qaddr:
        *undescribed*
    :type qaddr: dma_addr_t

.. _`ppc440spe_desc_set_xor_src_cnt`:

ppc440spe_desc_set_xor_src_cnt
==============================

.. c:function:: void ppc440spe_desc_set_xor_src_cnt(struct ppc440spe_adma_desc_slot *desc, int src_cnt)

    set source count into descriptor

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param src_cnt:
        *undescribed*
    :type src_cnt: int

.. _`ppc440spe_adma_pq_set_src`:

ppc440spe_adma_pq_set_src
=========================

.. c:function:: void ppc440spe_adma_pq_set_src(struct ppc440spe_adma_desc_slot *sw_desc, dma_addr_t addr, int index)

    set source address into descriptor

    :param sw_desc:
        *undescribed*
    :type sw_desc: struct ppc440spe_adma_desc_slot \*

    :param addr:
        *undescribed*
    :type addr: dma_addr_t

    :param index:
        *undescribed*
    :type index: int

.. _`ppc440spe_adma_memcpy_xor_set_src`:

ppc440spe_adma_memcpy_xor_set_src
=================================

.. c:function:: void ppc440spe_adma_memcpy_xor_set_src(struct ppc440spe_adma_desc_slot *sw_desc, dma_addr_t addr, int index)

    set source address into descriptor

    :param sw_desc:
        *undescribed*
    :type sw_desc: struct ppc440spe_adma_desc_slot \*

    :param addr:
        *undescribed*
    :type addr: dma_addr_t

    :param index:
        *undescribed*
    :type index: int

.. _`ppc440spe_adma_dma2rxor_inc_addr`:

ppc440spe_adma_dma2rxor_inc_addr
================================

.. c:function:: void ppc440spe_adma_dma2rxor_inc_addr(struct ppc440spe_adma_desc_slot *desc, struct ppc440spe_rxor *cursor, int index, int src_cnt)

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param cursor:
        *undescribed*
    :type cursor: struct ppc440spe_rxor \*

    :param index:
        *undescribed*
    :type index: int

    :param src_cnt:
        *undescribed*
    :type src_cnt: int

.. _`ppc440spe_adma_dma2rxor_prep_src`:

ppc440spe_adma_dma2rxor_prep_src
================================

.. c:function:: int ppc440spe_adma_dma2rxor_prep_src(struct ppc440spe_adma_desc_slot *hdesc, struct ppc440spe_rxor *cursor, int index, int src_cnt, u32 addr)

    setup RXOR types in DMA2 CDB

    :param hdesc:
        *undescribed*
    :type hdesc: struct ppc440spe_adma_desc_slot \*

    :param cursor:
        *undescribed*
    :type cursor: struct ppc440spe_rxor \*

    :param index:
        *undescribed*
    :type index: int

    :param src_cnt:
        *undescribed*
    :type src_cnt: int

    :param addr:
        *undescribed*
    :type addr: u32

.. _`ppc440spe_adma_dma2rxor_set_src`:

ppc440spe_adma_dma2rxor_set_src
===============================

.. c:function:: void ppc440spe_adma_dma2rxor_set_src(struct ppc440spe_adma_desc_slot *desc, int index, dma_addr_t addr)

    set RXOR source address; it's assumed that \ :c:func:`ppc440spe_adma_dma2rxor_prep_src`\  has already done prior this call

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param index:
        *undescribed*
    :type index: int

    :param addr:
        *undescribed*
    :type addr: dma_addr_t

.. _`ppc440spe_adma_dma2rxor_set_mult`:

ppc440spe_adma_dma2rxor_set_mult
================================

.. c:function:: void ppc440spe_adma_dma2rxor_set_mult(struct ppc440spe_adma_desc_slot *desc, int index, u8 mult)

    set RXOR multipliers; it's assumed that \ :c:func:`ppc440spe_adma_dma2rxor_prep_src`\  has already done prior this call

    :param desc:
        *undescribed*
    :type desc: struct ppc440spe_adma_desc_slot \*

    :param index:
        *undescribed*
    :type index: int

    :param mult:
        *undescribed*
    :type mult: u8

.. _`ppc440spe_init_rxor_cursor`:

ppc440spe_init_rxor_cursor
==========================

.. c:function:: void ppc440spe_init_rxor_cursor(struct ppc440spe_rxor *cursor)

    :param cursor:
        *undescribed*
    :type cursor: struct ppc440spe_rxor \*

.. _`ppc440spe_adma_pq_set_src_mult`:

ppc440spe_adma_pq_set_src_mult
==============================

.. c:function:: void ppc440spe_adma_pq_set_src_mult(struct ppc440spe_adma_desc_slot *sw_desc, unsigned char mult, int index, int dst_pos)

    set multiplication coefficient into descriptor for the PQXOR operation

    :param sw_desc:
        *undescribed*
    :type sw_desc: struct ppc440spe_adma_desc_slot \*

    :param mult:
        *undescribed*
    :type mult: unsigned char

    :param index:
        *undescribed*
    :type index: int

    :param dst_pos:
        *undescribed*
    :type dst_pos: int

.. _`ppc440spe_adma_free_chan_resources`:

ppc440spe_adma_free_chan_resources
==================================

.. c:function:: void ppc440spe_adma_free_chan_resources(struct dma_chan *chan)

    free the resources allocated

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

.. _`ppc440spe_adma_tx_status`:

ppc440spe_adma_tx_status
========================

.. c:function:: enum dma_status ppc440spe_adma_tx_status(struct dma_chan *chan, dma_cookie_t cookie, struct dma_tx_state *txstate)

    poll the status of an ADMA transaction

    :param chan:
        ADMA channel handle
    :type chan: struct dma_chan \*

    :param cookie:
        ADMA transaction identifier
    :type cookie: dma_cookie_t

    :param txstate:
        a holder for the current state of the channel
    :type txstate: struct dma_tx_state \*

.. _`ppc440spe_adma_eot_handler`:

ppc440spe_adma_eot_handler
==========================

.. c:function:: irqreturn_t ppc440spe_adma_eot_handler(int irq, void *data)

    end of transfer interrupt handler

    :param irq:
        *undescribed*
    :type irq: int

    :param data:
        *undescribed*
    :type data: void \*

.. _`ppc440spe_adma_err_handler`:

ppc440spe_adma_err_handler
==========================

.. c:function:: irqreturn_t ppc440spe_adma_err_handler(int irq, void *data)

    DMA error interrupt handler; do the same things as a eot handler

    :param irq:
        *undescribed*
    :type irq: int

    :param data:
        *undescribed*
    :type data: void \*

.. _`ppc440spe_test_callback`:

ppc440spe_test_callback
=======================

.. c:function:: void ppc440spe_test_callback(void *unused)

    called when test operation has been done

    :param unused:
        *undescribed*
    :type unused: void \*

.. _`ppc440spe_adma_issue_pending`:

ppc440spe_adma_issue_pending
============================

.. c:function:: void ppc440spe_adma_issue_pending(struct dma_chan *chan)

    flush all pending descriptors to h/w

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

.. _`ppc440spe_chan_start_null_xor`:

ppc440spe_chan_start_null_xor
=============================

.. c:function:: void ppc440spe_chan_start_null_xor(struct ppc440spe_adma_chan *chan)

    initiate the first XOR operation (DMA engines use FIFOs (as opposite to chains used in XOR) so this is a XOR specific operation)

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

.. _`ppc440spe_test_raid6`:

ppc440spe_test_raid6
====================

.. c:function:: int ppc440spe_test_raid6(struct ppc440spe_adma_chan *chan)

    test are RAID-6 capabilities enabled successfully. For this we just perform one WXOR operation with the same source and destination addresses, the GF-multiplier is 1; so if RAID-6 capabilities are enabled then we'll get src/dst filled with zero.

    :param chan:
        *undescribed*
    :type chan: struct ppc440spe_adma_chan \*

.. _`ppc440spe_adma_probe`:

ppc440spe_adma_probe
====================

.. c:function:: int ppc440spe_adma_probe(struct platform_device *ofdev)

    probe the asynch device

    :param ofdev:
        *undescribed*
    :type ofdev: struct platform_device \*

.. _`ppc440spe_adma_remove`:

ppc440spe_adma_remove
=====================

.. c:function:: int ppc440spe_adma_remove(struct platform_device *ofdev)

    remove the asynch device

    :param ofdev:
        *undescribed*
    :type ofdev: struct platform_device \*

.. This file was automatic generated / don't edit.

