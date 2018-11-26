.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/fsl/dpio/qbman-portal.c

.. _`qbman_swp_init`:

qbman_swp_init
==============

.. c:function:: struct qbman_swp *qbman_swp_init(const struct qbman_swp_desc *d)

    Create a functional object representing the given QBMan portal descriptor.

    :param d:
        the given qbman swp descriptor
    :type d: const struct qbman_swp_desc \*

.. _`qbman_swp_init.description`:

Description
-----------

Return qbman_swp portal for success, NULL if the object cannot
be created.

.. _`qbman_swp_finish`:

qbman_swp_finish
================

.. c:function:: void qbman_swp_finish(struct qbman_swp *p)

    Create and destroy a functional object representing the given QBMan portal descriptor.

    :param p:
        the qbman_swp object to be destroyed
    :type p: struct qbman_swp \*

.. _`qbman_swp_interrupt_read_status`:

qbman_swp_interrupt_read_status
===============================

.. c:function:: u32 qbman_swp_interrupt_read_status(struct qbman_swp *p)

    :param p:
        the given software portal
    :type p: struct qbman_swp \*

.. _`qbman_swp_interrupt_read_status.description`:

Description
-----------

Return the value in the SWP_ISR register.

.. _`qbman_swp_interrupt_clear_status`:

qbman_swp_interrupt_clear_status
================================

.. c:function:: void qbman_swp_interrupt_clear_status(struct qbman_swp *p, u32 mask)

    :param p:
        the given software portal
    :type p: struct qbman_swp \*

    :param mask:
        The mask to clear in SWP_ISR register
    :type mask: u32

.. _`qbman_swp_interrupt_get_trigger`:

qbman_swp_interrupt_get_trigger
===============================

.. c:function:: u32 qbman_swp_interrupt_get_trigger(struct qbman_swp *p)

    read interrupt enable register

    :param p:
        the given software portal
    :type p: struct qbman_swp \*

.. _`qbman_swp_interrupt_get_trigger.description`:

Description
-----------

Return the value in the SWP_IER register.

.. _`qbman_swp_interrupt_set_trigger`:

qbman_swp_interrupt_set_trigger
===============================

.. c:function:: void qbman_swp_interrupt_set_trigger(struct qbman_swp *p, u32 mask)

    enable interrupts for a swp

    :param p:
        the given software portal
    :type p: struct qbman_swp \*

    :param mask:
        The mask of bits to enable in SWP_IER
    :type mask: u32

.. _`qbman_swp_interrupt_get_inhibit`:

qbman_swp_interrupt_get_inhibit
===============================

.. c:function:: int qbman_swp_interrupt_get_inhibit(struct qbman_swp *p)

    read interrupt mask register

    :param p:
        the given software portal object
    :type p: struct qbman_swp \*

.. _`qbman_swp_interrupt_get_inhibit.description`:

Description
-----------

Return the value in the SWP_IIR register.

.. _`qbman_swp_interrupt_set_inhibit`:

qbman_swp_interrupt_set_inhibit
===============================

.. c:function:: void qbman_swp_interrupt_set_inhibit(struct qbman_swp *p, int inhibit)

    write interrupt mask register

    :param p:
        the given software portal object
    :type p: struct qbman_swp \*

    :param inhibit:
        *undescribed*
    :type inhibit: int

.. _`qbman_eq_desc_clear`:

qbman_eq_desc_clear
===================

.. c:function:: void qbman_eq_desc_clear(struct qbman_eq_desc *d)

    Clear the contents of a descriptor to default/starting state.

    :param d:
        *undescribed*
    :type d: struct qbman_eq_desc \*

.. _`qbman_eq_desc_set_no_orp`:

qbman_eq_desc_set_no_orp
========================

.. c:function:: void qbman_eq_desc_set_no_orp(struct qbman_eq_desc *d, int respond_success)

    Set enqueue descriptor without orp

    :param d:
        the enqueue descriptor.
    :type d: struct qbman_eq_desc \*

    :param respond_success:
        *undescribed*
    :type respond_success: int

.. _`qbman_eq_desc_set_fq`:

qbman_eq_desc_set_fq
====================

.. c:function:: void qbman_eq_desc_set_fq(struct qbman_eq_desc *d, u32 fqid)

    set the FQ for the enqueue command

    :param d:
        the enqueue descriptor
    :type d: struct qbman_eq_desc \*

    :param fqid:
        the id of the frame queue to be enqueued
    :type fqid: u32

.. _`qbman_eq_desc_set_qd`:

qbman_eq_desc_set_qd
====================

.. c:function:: void qbman_eq_desc_set_qd(struct qbman_eq_desc *d, u32 qdid, u32 qd_bin, u32 qd_prio)

    Set Queuing Destination for the enqueue command

    :param d:
        the enqueue descriptor
    :type d: struct qbman_eq_desc \*

    :param qdid:
        the id of the queuing destination to be enqueued
    :type qdid: u32

    :param qd_bin:
        the queuing destination bin
    :type qd_bin: u32

    :param qd_prio:
        the queuing destination priority
    :type qd_prio: u32

.. _`qbman_swp_enqueue`:

qbman_swp_enqueue
=================

.. c:function:: int qbman_swp_enqueue(struct qbman_swp *s, const struct qbman_eq_desc *d, const struct dpaa2_fd *fd)

    Issue an enqueue command

    :param s:
        the software portal used for enqueue
    :type s: struct qbman_swp \*

    :param d:
        the enqueue descriptor
    :type d: const struct qbman_eq_desc \*

    :param fd:
        the frame descriptor to be enqueued
    :type fd: const struct dpaa2_fd \*

.. _`qbman_swp_enqueue.description`:

Description
-----------

Please note that 'fd' should only be NULL if the "action" of the
descriptor is "orp_hole" or "orp_nesn".

Return 0 for successful enqueue, -EBUSY if the EQCR is not ready.

.. _`qbman_swp_push_get`:

qbman_swp_push_get
==================

.. c:function:: void qbman_swp_push_get(struct qbman_swp *s, u8 channel_idx, int *enabled)

    Get the push dequeue setup

    :param s:
        *undescribed*
    :type s: struct qbman_swp \*

    :param channel_idx:
        the channel index to query
    :type channel_idx: u8

    :param enabled:
        returned boolean to show whether the push dequeue is enabled
        for the given channel
    :type enabled: int \*

.. _`qbman_swp_push_set`:

qbman_swp_push_set
==================

.. c:function:: void qbman_swp_push_set(struct qbman_swp *s, u8 channel_idx, int enable)

    Enable or disable push dequeue

    :param s:
        *undescribed*
    :type s: struct qbman_swp \*

    :param channel_idx:
        the channel index (0 to 15)
    :type channel_idx: u8

    :param enable:
        enable or disable push dequeue
    :type enable: int

.. _`qbman_pull_desc_clear`:

qbman_pull_desc_clear
=====================

.. c:function:: void qbman_pull_desc_clear(struct qbman_pull_desc *d)

    Clear the contents of a descriptor to default/starting state

    :param d:
        the pull dequeue descriptor to be cleared
    :type d: struct qbman_pull_desc \*

.. _`qbman_pull_desc_set_storage`:

qbman_pull_desc_set_storage
===========================

.. c:function:: void qbman_pull_desc_set_storage(struct qbman_pull_desc *d, struct dpaa2_dq *storage, dma_addr_t storage_phys, int stash)

    Set the pull dequeue storage

    :param d:
        the pull dequeue descriptor to be set
    :type d: struct qbman_pull_desc \*

    :param storage:
        the pointer of the memory to store the dequeue result
    :type storage: struct dpaa2_dq \*

    :param storage_phys:
        the physical address of the storage memory
    :type storage_phys: dma_addr_t

    :param stash:
        to indicate whether write allocate is enabled
    :type stash: int

.. _`qbman_pull_desc_set_storage.description`:

Description
-----------

If not called, or if called with 'storage' as NULL, the result pull dequeues
will produce results to DQRR. If 'storage' is non-NULL, then results are
produced to the given memory location (using the DMA address which
the caller provides in 'storage_phys'), and 'stash' controls whether or not
those writes to main-memory express a cache-warming attribute.

.. _`qbman_pull_desc_set_numframes`:

qbman_pull_desc_set_numframes
=============================

.. c:function:: void qbman_pull_desc_set_numframes(struct qbman_pull_desc *d, u8 numframes)

    Set the number of frames to be dequeued

    :param d:
        the pull dequeue descriptor to be set
    :type d: struct qbman_pull_desc \*

    :param numframes:
        number of frames to be set, must be between 1 and 16, inclusive
    :type numframes: u8

.. _`qbman_pull_desc_set_fq`:

qbman_pull_desc_set_fq
======================

.. c:function:: void qbman_pull_desc_set_fq(struct qbman_pull_desc *d, u32 fqid)

    Set fqid from which the dequeue command dequeues

    :param d:
        *undescribed*
    :type d: struct qbman_pull_desc \*

    :param fqid:
        the frame queue index of the given FQ
    :type fqid: u32

.. _`qbman_pull_desc_set_wq`:

qbman_pull_desc_set_wq
======================

.. c:function:: void qbman_pull_desc_set_wq(struct qbman_pull_desc *d, u32 wqid, enum qbman_pull_type_e dct)

    Set wqid from which the dequeue command dequeues

    :param d:
        *undescribed*
    :type d: struct qbman_pull_desc \*

    :param wqid:
        composed of channel id and wqid within the channel
    :type wqid: u32

    :param dct:
        the dequeue command type
    :type dct: enum qbman_pull_type_e

.. _`qbman_pull_desc_set_channel`:

qbman_pull_desc_set_channel
===========================

.. c:function:: void qbman_pull_desc_set_channel(struct qbman_pull_desc *d, u32 chid, enum qbman_pull_type_e dct)

    Set channelid from which the dequeue command dequeues

    :param d:
        *undescribed*
    :type d: struct qbman_pull_desc \*

    :param chid:
        the channel id to be dequeued
    :type chid: u32

    :param dct:
        the dequeue command type
    :type dct: enum qbman_pull_type_e

.. _`qbman_swp_pull`:

qbman_swp_pull
==============

.. c:function:: int qbman_swp_pull(struct qbman_swp *s, struct qbman_pull_desc *d)

    Issue the pull dequeue command

    :param s:
        the software portal object
    :type s: struct qbman_swp \*

    :param d:
        the software portal descriptor which has been configured with
        the set of qbman_pull_desc_set\_\*() calls
    :type d: struct qbman_pull_desc \*

.. _`qbman_swp_pull.description`:

Description
-----------

Return 0 for success, and -EBUSY if the software portal is not ready
to do pull dequeue.

.. _`qbman_swp_dqrr_next`:

qbman_swp_dqrr_next
===================

.. c:function:: const struct dpaa2_dq *qbman_swp_dqrr_next(struct qbman_swp *s)

    Get an valid DQRR entry

    :param s:
        the software portal object
    :type s: struct qbman_swp \*

.. _`qbman_swp_dqrr_next.description`:

Description
-----------

Return NULL if there are no unconsumed DQRR entries. Return a DQRR entry
only once, so repeated calls can return a sequence of DQRR entries, without
requiring they be consumed immediately or in any particular order.

.. _`qbman_swp_dqrr_consume`:

qbman_swp_dqrr_consume
======================

.. c:function:: void qbman_swp_dqrr_consume(struct qbman_swp *s, const struct dpaa2_dq *dq)

    Consume DQRR entries previously returned from \ :c:func:`qbman_swp_dqrr_next`\ .

    :param s:
        the software portal object
    :type s: struct qbman_swp \*

    :param dq:
        the DQRR entry to be consumed
    :type dq: const struct dpaa2_dq \*

.. _`qbman_result_has_new_result`:

qbman_result_has_new_result
===========================

.. c:function:: int qbman_result_has_new_result(struct qbman_swp *s, const struct dpaa2_dq *dq)

    Check and get the dequeue response from the dq storage memory set in pull dequeue command

    :param s:
        the software portal object
    :type s: struct qbman_swp \*

    :param dq:
        the dequeue result read from the memory
    :type dq: const struct dpaa2_dq \*

.. _`qbman_result_has_new_result.description`:

Description
-----------

Return 1 for getting a valid dequeue result, or 0 for not getting a valid
dequeue result.

Only used for user-provided storage of dequeue results, not DQRR. For
efficiency purposes, the driver will perform any required endianness
conversion to ensure that the user's dequeue result storage is in host-endian
format. As such, once the user has called \ :c:func:`qbman_result_has_new_result`\  and
been returned a valid dequeue result, they should not call it again on
the same memory location (except of course if another dequeue command has
been executed to produce a new result to that location).

.. _`qbman_release_desc_clear`:

qbman_release_desc_clear
========================

.. c:function:: void qbman_release_desc_clear(struct qbman_release_desc *d)

    Clear the contents of a descriptor to default/starting state.

    :param d:
        *undescribed*
    :type d: struct qbman_release_desc \*

.. _`qbman_release_desc_set_bpid`:

qbman_release_desc_set_bpid
===========================

.. c:function:: void qbman_release_desc_set_bpid(struct qbman_release_desc *d, u16 bpid)

    Set the ID of the buffer pool to release to

    :param d:
        *undescribed*
    :type d: struct qbman_release_desc \*

    :param bpid:
        *undescribed*
    :type bpid: u16

.. _`qbman_release_desc_set_rcdi`:

qbman_release_desc_set_rcdi
===========================

.. c:function:: void qbman_release_desc_set_rcdi(struct qbman_release_desc *d, int enable)

    Determines whether or not the portal's RCDI interrupt source should be asserted after the release command is completed.

    :param d:
        *undescribed*
    :type d: struct qbman_release_desc \*

    :param enable:
        *undescribed*
    :type enable: int

.. _`qbman_swp_release`:

qbman_swp_release
=================

.. c:function:: int qbman_swp_release(struct qbman_swp *s, const struct qbman_release_desc *d, const u64 *buffers, unsigned int num_buffers)

    Issue a buffer release command

    :param s:
        the software portal object
    :type s: struct qbman_swp \*

    :param d:
        the release descriptor
    :type d: const struct qbman_release_desc \*

    :param buffers:
        a pointer pointing to the buffer address to be released
    :type buffers: const u64 \*

    :param num_buffers:
        number of buffers to be released,  must be less than 8
    :type num_buffers: unsigned int

.. _`qbman_swp_release.description`:

Description
-----------

Return 0 for success, -EBUSY if the release command ring is not ready.

.. _`qbman_swp_acquire`:

qbman_swp_acquire
=================

.. c:function:: int qbman_swp_acquire(struct qbman_swp *s, u16 bpid, u64 *buffers, unsigned int num_buffers)

    Issue a buffer acquire command

    :param s:
        the software portal object
    :type s: struct qbman_swp \*

    :param bpid:
        the buffer pool index
    :type bpid: u16

    :param buffers:
        a pointer pointing to the acquired buffer addresses
    :type buffers: u64 \*

    :param num_buffers:
        number of buffers to be acquired, must be less than 8
    :type num_buffers: unsigned int

.. _`qbman_swp_acquire.description`:

Description
-----------

Return 0 for success, or negative error code if the acquire command
fails.

.. This file was automatic generated / don't edit.

