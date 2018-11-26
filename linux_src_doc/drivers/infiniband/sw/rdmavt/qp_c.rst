.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rdmavt/qp.c

.. _`rvt_wss_init`:

rvt_wss_init
============

.. c:function:: int rvt_wss_init(struct rvt_dev_info *rdi)

    Init wss data structures

    :param rdi:
        *undescribed*
    :type rdi: struct rvt_dev_info \*

.. _`rvt_wss_init.return`:

Return
------

0 on success

.. _`init_qpn_table`:

init_qpn_table
==============

.. c:function:: int init_qpn_table(struct rvt_dev_info *rdi, struct rvt_qpn_table *qpt)

    initialize the QP number table for a device

    :param rdi:
        *undescribed*
    :type rdi: struct rvt_dev_info \*

    :param qpt:
        the QPN table
    :type qpt: struct rvt_qpn_table \*

.. _`free_qpn_table`:

free_qpn_table
==============

.. c:function:: void free_qpn_table(struct rvt_qpn_table *qpt)

    free the QP number table for a device

    :param qpt:
        the QPN table
    :type qpt: struct rvt_qpn_table \*

.. _`rvt_driver_qp_init`:

rvt_driver_qp_init
==================

.. c:function:: int rvt_driver_qp_init(struct rvt_dev_info *rdi)

    Init driver qp resources

    :param rdi:
        rvt dev strucutre
    :type rdi: struct rvt_dev_info \*

.. _`rvt_driver_qp_init.return`:

Return
------

0 on success

.. _`rvt_free_all_qps`:

rvt_free_all_qps
================

.. c:function:: unsigned rvt_free_all_qps(struct rvt_dev_info *rdi)

    check for QPs still in use

    :param rdi:
        rvt device info structure
    :type rdi: struct rvt_dev_info \*

.. _`rvt_free_all_qps.description`:

Description
-----------

There should not be any QPs still in use.
Free memory for table.

.. _`rvt_qp_exit`:

rvt_qp_exit
===========

.. c:function:: void rvt_qp_exit(struct rvt_dev_info *rdi)

    clean up qps on device exit

    :param rdi:
        rvt dev structure
    :type rdi: struct rvt_dev_info \*

.. _`rvt_qp_exit.description`:

Description
-----------

Check for qp leaks and free resources.

.. _`alloc_qpn`:

alloc_qpn
=========

.. c:function:: int alloc_qpn(struct rvt_dev_info *rdi, struct rvt_qpn_table *qpt, enum ib_qp_type type, u8 port_num)

    Allocate the next available qpn or zero/one for QP type IB_QPT_SMI/IB_QPT_GSI

    :param rdi:
        rvt device info structure
    :type rdi: struct rvt_dev_info \*

    :param qpt:
        queue pair number table pointer
    :type qpt: struct rvt_qpn_table \*

    :param type:
        *undescribed*
    :type type: enum ib_qp_type

    :param port_num:
        IB port number, 1 based, comes from core
    :type port_num: u8

.. _`alloc_qpn.return`:

Return
------

The queue pair number

.. _`rvt_clear_mr_refs`:

rvt_clear_mr_refs
=================

.. c:function:: void rvt_clear_mr_refs(struct rvt_qp *qp, int clr_sends)

    Drop help mr refs

    :param qp:
        rvt qp data structure
    :type qp: struct rvt_qp \*

    :param clr_sends:
        If shoudl clear send side or not
    :type clr_sends: int

.. _`rvt_swqe_has_lkey`:

rvt_swqe_has_lkey
=================

.. c:function:: bool rvt_swqe_has_lkey(struct rvt_swqe *wqe, u32 lkey)

    return true if lkey is used by swqe \ ``wqe``\  - the send wqe \ ``lkey``\  - the lkey

    :param wqe:
        *undescribed*
    :type wqe: struct rvt_swqe \*

    :param lkey:
        *undescribed*
    :type lkey: u32

.. _`rvt_swqe_has_lkey.description`:

Description
-----------

Test the swqe for using lkey

.. _`rvt_qp_sends_has_lkey`:

rvt_qp_sends_has_lkey
=====================

.. c:function:: bool rvt_qp_sends_has_lkey(struct rvt_qp *qp, u32 lkey)

    return true is qp sends use lkey \ ``qp``\  - the rvt_qp \ ``lkey``\  - the lkey

    :param qp:
        *undescribed*
    :type qp: struct rvt_qp \*

    :param lkey:
        *undescribed*
    :type lkey: u32

.. _`rvt_qp_acks_has_lkey`:

rvt_qp_acks_has_lkey
====================

.. c:function:: bool rvt_qp_acks_has_lkey(struct rvt_qp *qp, u32 lkey)

    return true if acks have lkey \ ``qp``\  - the qp \ ``lkey``\  - the lkey

    :param qp:
        *undescribed*
    :type qp: struct rvt_qp \*

    :param lkey:
        *undescribed*
    :type lkey: u32

.. _`rvt_remove_qp`:

rvt_remove_qp
=============

.. c:function:: void rvt_remove_qp(struct rvt_dev_info *rdi, struct rvt_qp *qp)

    remove qp form table

    :param rdi:
        rvt dev struct
    :type rdi: struct rvt_dev_info \*

    :param qp:
        qp to remove
    :type qp: struct rvt_qp \*

.. _`rvt_remove_qp.description`:

Description
-----------

Remove the QP from the table so it can't be found asynchronously by
the receive routine.

.. _`rvt_init_qp`:

rvt_init_qp
===========

.. c:function:: void rvt_init_qp(struct rvt_dev_info *rdi, struct rvt_qp *qp, enum ib_qp_type type)

    initialize the QP state to the reset state

    :param rdi:
        *undescribed*
    :type rdi: struct rvt_dev_info \*

    :param qp:
        the QP to init or reinit
    :type qp: struct rvt_qp \*

    :param type:
        the QP type
    :type type: enum ib_qp_type

.. _`rvt_init_qp.description`:

Description
-----------

This function is called from both \ :c:func:`rvt_create_qp`\  and
\ :c:func:`rvt_reset_qp`\ .   The difference is that the reset
patch the necessary locks to protect against concurent
access.

.. _`rvt_reset_qp`:

rvt_reset_qp
============

.. c:function:: void rvt_reset_qp(struct rvt_dev_info *rdi, struct rvt_qp *qp, enum ib_qp_type type)

    initialize the QP state to the reset state

    :param rdi:
        *undescribed*
    :type rdi: struct rvt_dev_info \*

    :param qp:
        the QP to reset
    :type qp: struct rvt_qp \*

    :param type:
        the QP type
    :type type: enum ib_qp_type

.. _`rvt_reset_qp.description`:

Description
-----------

r_lock, s_hlock, and s_lock are required to be held by the caller

.. _`rvt_create_qp`:

rvt_create_qp
=============

.. c:function:: struct ib_qp *rvt_create_qp(struct ib_pd *ibpd, struct ib_qp_init_attr *init_attr, struct ib_udata *udata)

    create a queue pair for a device

    :param ibpd:
        the protection domain who's device we create the queue pair for
    :type ibpd: struct ib_pd \*

    :param init_attr:
        the attributes of the queue pair
    :type init_attr: struct ib_qp_init_attr \*

    :param udata:
        user data for libibverbs.so
    :type udata: struct ib_udata \*

.. _`rvt_create_qp.description`:

Description
-----------

Queue pair creation is mostly an rvt issue. However, drivers have their own
unique idea of what queue pair numbers mean. For instance there is a reserved
range for PSM.

.. _`rvt_create_qp.return`:

Return
------

the queue pair on success, otherwise returns an errno.

Called by the \ :c:func:`ib_create_qp`\  core verbs function.

.. _`rvt_error_qp`:

rvt_error_qp
============

.. c:function:: int rvt_error_qp(struct rvt_qp *qp, enum ib_wc_status err)

    put a QP into the error state

    :param qp:
        the QP to put into the error state
    :type qp: struct rvt_qp \*

    :param err:
        the receive completion error to signal if a RWQE is active
    :type err: enum ib_wc_status

.. _`rvt_error_qp.description`:

Description
-----------

Flushes both send and receive work queues.

.. _`rvt_error_qp.return`:

Return
------

true if last WQE event should be generated.
The QP r_lock and s_lock should be held and interrupts disabled.
If we are already in error state, just return.

.. _`rvt_modify_qp`:

rvt_modify_qp
=============

.. c:function:: int rvt_modify_qp(struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_udata *udata)

    modify the attributes of a queue pair

    :param ibqp:
        the queue pair who's attributes we're modifying
    :type ibqp: struct ib_qp \*

    :param attr:
        the new attributes
    :type attr: struct ib_qp_attr \*

    :param attr_mask:
        the mask of attributes to modify
    :type attr_mask: int

    :param udata:
        user data for libibverbs.so
    :type udata: struct ib_udata \*

.. _`rvt_modify_qp.return`:

Return
------

0 on success, otherwise returns an errno.

.. _`rvt_destroy_qp`:

rvt_destroy_qp
==============

.. c:function:: int rvt_destroy_qp(struct ib_qp *ibqp)

    destroy a queue pair

    :param ibqp:
        the queue pair to destroy
    :type ibqp: struct ib_qp \*

.. _`rvt_destroy_qp.description`:

Description
-----------

Note that this can be called while the QP is actively sending or
receiving!

.. _`rvt_destroy_qp.return`:

Return
------

0 on success.

.. _`rvt_query_qp`:

rvt_query_qp
============

.. c:function:: int rvt_query_qp(struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_qp_init_attr *init_attr)

    query an ipbq

    :param ibqp:
        IB qp to query
    :type ibqp: struct ib_qp \*

    :param attr:
        attr struct to fill in
    :type attr: struct ib_qp_attr \*

    :param attr_mask:
        attr mask ignored
    :type attr_mask: int

    :param init_attr:
        struct to fill in
    :type init_attr: struct ib_qp_init_attr \*

.. _`rvt_query_qp.return`:

Return
------

always 0

.. _`rvt_post_recv`:

rvt_post_recv
=============

.. c:function:: int rvt_post_recv(struct ib_qp *ibqp, const struct ib_recv_wr *wr, const struct ib_recv_wr **bad_wr)

    post a receive on a QP

    :param ibqp:
        the QP to post the receive on
    :type ibqp: struct ib_qp \*

    :param wr:
        the WR to post
    :type wr: const struct ib_recv_wr \*

    :param bad_wr:
        the first bad WR is put here
    :type bad_wr: const struct ib_recv_wr \*\*

.. _`rvt_post_recv.description`:

Description
-----------

This may be called from interrupt context.

.. _`rvt_post_recv.return`:

Return
------

0 on success otherwise errno

.. _`rvt_qp_valid_operation`:

rvt_qp_valid_operation
======================

.. c:function:: int rvt_qp_valid_operation(struct rvt_qp *qp, const struct rvt_operation_params *post_parms, const struct ib_send_wr *wr)

    validate post send wr request \ ``qp``\  - the qp \ ``post``\ -parms - the post send table for the driver \ ``wr``\  - the work request

    :param qp:
        *undescribed*
    :type qp: struct rvt_qp \*

    :param post_parms:
        *undescribed*
    :type post_parms: const struct rvt_operation_params \*

    :param wr:
        *undescribed*
    :type wr: const struct ib_send_wr \*

.. _`rvt_qp_valid_operation.description`:

Description
-----------

The routine validates the operation based on the
validation table an returns the length of the operation
which can extend beyond the ib_send_bw.  Operation
dependent flags key atomic operation validation.

There is an exception for UD qps that validates the pd and
overrides the length to include the additional UD specific
length.

Returns a negative error or the length of the work request
for building the swqe.

.. _`rvt_qp_is_avail`:

rvt_qp_is_avail
===============

.. c:function:: int rvt_qp_is_avail(struct rvt_qp *qp, struct rvt_dev_info *rdi, bool reserved_op)

    determine queue capacity

    :param qp:
        the qp
    :type qp: struct rvt_qp \*

    :param rdi:
        the rdmavt device
    :type rdi: struct rvt_dev_info \*

    :param reserved_op:
        is reserved operation
    :type reserved_op: bool

.. _`rvt_qp_is_avail.description`:

Description
-----------

This assumes the s_hlock is held but the s_last
qp variable is uncontrolled.

For non reserved operations, the qp->s_avail
may be changed.

The return value is zero or a -ENOMEM.

.. _`rvt_post_one_wr`:

rvt_post_one_wr
===============

.. c:function:: int rvt_post_one_wr(struct rvt_qp *qp, const struct ib_send_wr *wr, bool *call_send)

    post one RC, UC, or UD send work request

    :param qp:
        the QP to post on
    :type qp: struct rvt_qp \*

    :param wr:
        the work request to send
    :type wr: const struct ib_send_wr \*

    :param call_send:
        *undescribed*
    :type call_send: bool \*

.. _`rvt_post_send`:

rvt_post_send
=============

.. c:function:: int rvt_post_send(struct ib_qp *ibqp, const struct ib_send_wr *wr, const struct ib_send_wr **bad_wr)

    post a send on a QP

    :param ibqp:
        the QP to post the send on
    :type ibqp: struct ib_qp \*

    :param wr:
        the list of work requests to post
    :type wr: const struct ib_send_wr \*

    :param bad_wr:
        the first bad WR is put here
    :type bad_wr: const struct ib_send_wr \*\*

.. _`rvt_post_send.description`:

Description
-----------

This may be called from interrupt context.

.. _`rvt_post_send.return`:

Return
------

0 on success else errno

.. _`rvt_post_srq_recv`:

rvt_post_srq_recv
=================

.. c:function:: int rvt_post_srq_recv(struct ib_srq *ibsrq, const struct ib_recv_wr *wr, const struct ib_recv_wr **bad_wr)

    post a receive on a shared receive queue

    :param ibsrq:
        the SRQ to post the receive on
    :type ibsrq: struct ib_srq \*

    :param wr:
        the list of work requests to post
    :type wr: const struct ib_recv_wr \*

    :param bad_wr:
        A pointer to the first WR to cause a problem is put here
    :type bad_wr: const struct ib_recv_wr \*\*

.. _`rvt_post_srq_recv.description`:

Description
-----------

This may be called from interrupt context.

.. _`rvt_post_srq_recv.return`:

Return
------

0 on success else errno

.. _`rvt_get_rwqe`:

rvt_get_rwqe
============

.. c:function:: int rvt_get_rwqe(struct rvt_qp *qp, bool wr_id_only)

    copy the next RWQE into the QP's RWQE

    :param qp:
        the QP
    :type qp: struct rvt_qp \*

    :param wr_id_only:
        update qp->r_wr_id only, not qp->r_sge
    :type wr_id_only: bool

.. _`rvt_get_rwqe.description`:

Description
-----------

Return -1 if there is a local error, 0 if no RWQE is available,
otherwise return 1.

Can be called from interrupt level.

.. _`rvt_comm_est`:

rvt_comm_est
============

.. c:function:: void rvt_comm_est(struct rvt_qp *qp)

    handle trap with QP established

    :param qp:
        the QP
    :type qp: struct rvt_qp \*

.. _`rvt_add_rnr_timer`:

rvt_add_rnr_timer
=================

.. c:function:: void rvt_add_rnr_timer(struct rvt_qp *qp, u32 aeth)

    add/start an rnr timer \ ``qp``\  - the QP \ ``aeth``\  - aeth of RNR timeout, simulated aeth for loopback add an rnr timer on the QP

    :param qp:
        *undescribed*
    :type qp: struct rvt_qp \*

    :param aeth:
        *undescribed*
    :type aeth: u32

.. _`rvt_stop_rc_timers`:

rvt_stop_rc_timers
==================

.. c:function:: void rvt_stop_rc_timers(struct rvt_qp *qp)

    stop all timers \ ``qp``\  - the QP stop any pending timers

    :param qp:
        *undescribed*
    :type qp: struct rvt_qp \*

.. _`rvt_stop_rnr_timer`:

rvt_stop_rnr_timer
==================

.. c:function:: void rvt_stop_rnr_timer(struct rvt_qp *qp)

    stop an rnr timer \ ``qp``\  - the QP

    :param qp:
        *undescribed*
    :type qp: struct rvt_qp \*

.. _`rvt_stop_rnr_timer.description`:

Description
-----------

stop an rnr timer and return if the timer
had been pending.

.. _`rvt_del_timers_sync`:

rvt_del_timers_sync
===================

.. c:function:: void rvt_del_timers_sync(struct rvt_qp *qp)

    wait for any timeout routines to exit \ ``qp``\  - the QP

    :param qp:
        *undescribed*
    :type qp: struct rvt_qp \*

.. _`rvt_rc_timeout`:

rvt_rc_timeout
==============

.. c:function:: void rvt_rc_timeout(struct timer_list *t)

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`rvt_qp_iter_init`:

rvt_qp_iter_init
================

.. c:function:: struct rvt_qp_iter *rvt_qp_iter_init(struct rvt_dev_info *rdi, u64 v, void (*cb)(struct rvt_qp *qp, u64 v))

    initial for QP iteration

    :param rdi:
        rvt devinfo
    :type rdi: struct rvt_dev_info \*

    :param v:
        u64 value
    :type v: u64

    :param void (\*cb)(struct rvt_qp \*qp, u64 v):
        *undescribed*

.. _`rvt_qp_iter_init.description`:

Description
-----------

This returns an iterator suitable for iterating QPs
in the system.

The \ ``cb``\  is a user defined callback and \ ``v``\  is a 64
bit value passed to and relevant for processing in the
\ ``cb``\ .  An example use case would be to alter QP processing
based on criteria not part of the rvt_qp.

Use cases that require memory allocation to succeed
must preallocate appropriately.

.. _`rvt_qp_iter_init.return`:

Return
------

a pointer to an rvt_qp_iter or NULL

.. _`rvt_qp_iter_next`:

rvt_qp_iter_next
================

.. c:function:: int rvt_qp_iter_next(struct rvt_qp_iter *iter)

    return the next QP in iter \ ``iter``\  - the iterator

    :param iter:
        *undescribed*
    :type iter: struct rvt_qp_iter \*

.. _`rvt_qp_iter_next.description`:

Description
-----------

Fine grained QP iterator suitable for use
with debugfs seq_file mechanisms.

Updates iter->qp with the current QP when the return
value is 0.

.. _`rvt_qp_iter_next.return`:

Return
------

0 - iter->qp is valid 1 - no more QPs

.. _`rvt_qp_iter`:

rvt_qp_iter
===========

.. c:function:: void rvt_qp_iter(struct rvt_dev_info *rdi, u64 v, void (*cb)(struct rvt_qp *qp, u64 v))

    iterate all QPs \ ``rdi``\  - rvt devinfo \ ``v``\  - a 64 bit value \ ``cb``\  - a callback

    :param rdi:
        *undescribed*
    :type rdi: struct rvt_dev_info \*

    :param v:
        *undescribed*
    :type v: u64

    :param void (\*cb)(struct rvt_qp \*qp, u64 v):
        *undescribed*

.. _`rvt_qp_iter.description`:

Description
-----------

This provides a way for iterating all QPs.

The \ ``cb``\  is a user defined callback and \ ``v``\  is a 64
bit value passed to and relevant for processing in the
cb.  An example use case would be to alter QP processing
based on criteria not part of the rvt_qp.

The code has an internal iterator to simplify
non seq_file use cases.

.. _`rvt_copy_sge`:

rvt_copy_sge
============

.. c:function:: void rvt_copy_sge(struct rvt_qp *qp, struct rvt_sge_state *ss, void *data, u32 length, bool release, bool copy_last)

    copy data to SGE memory

    :param qp:
        associated QP
    :type qp: struct rvt_qp \*

    :param ss:
        the SGE state
    :type ss: struct rvt_sge_state \*

    :param data:
        the data to copy
    :type data: void \*

    :param length:
        the length of the data
    :type length: u32

    :param release:
        boolean to release MR
    :type release: bool

    :param copy_last:
        do a separate copy of the last 8 bytes
    :type copy_last: bool

.. _`rvt_ruc_loopback`:

rvt_ruc_loopback
================

.. c:function:: void rvt_ruc_loopback(struct rvt_qp *sqp)

    handle UC and RC loopback requests

    :param sqp:
        the sending QP
    :type sqp: struct rvt_qp \*

.. _`rvt_ruc_loopback.description`:

Description
-----------

This is called from \ :c:func:`rvt_do_send`\  to forward a WQE addressed to the same HFI
Note that although we are single threaded due to the send engine, we still
have to protect against \ :c:func:`post_send`\ .  We don't have to worry about
receive interrupts since this is a connected protocol and all packets
will pass through here.

.. This file was automatic generated / don't edit.

