.. -*- coding: utf-8; mode: rst -*-

====
qp.c
====


.. _`init_qpn_table`:

init_qpn_table
==============

.. c:function:: int init_qpn_table (struct rvt_dev_info *rdi, struct rvt_qpn_table *qpt)

    initialize the QP number table for a device

    :param struct rvt_dev_info \*rdi:

        *undescribed*

    :param struct rvt_qpn_table \*qpt:
        the QPN table



.. _`free_qpn_table`:

free_qpn_table
==============

.. c:function:: void free_qpn_table (struct rvt_qpn_table *qpt)

    free the QP number table for a device

    :param struct rvt_qpn_table \*qpt:
        the QPN table



.. _`rvt_driver_qp_init`:

rvt_driver_qp_init
==================

.. c:function:: int rvt_driver_qp_init (struct rvt_dev_info *rdi)

    Init driver qp resources

    :param struct rvt_dev_info \*rdi:
        rvt dev strucutre



.. _`rvt_driver_qp_init.return`:

Return
------

0 on success



.. _`rvt_free_all_qps`:

rvt_free_all_qps
================

.. c:function:: unsigned rvt_free_all_qps (struct rvt_dev_info *rdi)

    check for QPs still in use

    :param struct rvt_dev_info \*rdi:

        *undescribed*



.. _`rvt_free_all_qps.description`:

Description
-----------

There should not be any QPs still in use.
Free memory for table.



.. _`rvt_qp_exit`:

rvt_qp_exit
===========

.. c:function:: void rvt_qp_exit (struct rvt_dev_info *rdi)

    clean up qps on device exit

    :param struct rvt_dev_info \*rdi:
        rvt dev structure



.. _`rvt_qp_exit.description`:

Description
-----------

Check for qp leaks and free resources.



.. _`alloc_qpn`:

alloc_qpn
=========

.. c:function:: int alloc_qpn (struct rvt_dev_info *rdi, struct rvt_qpn_table *qpt, enum ib_qp_type type, u8 port_num, gfp_t gfp)

    Allocate the next available qpn or zero/one for QP type IB_QPT_SMI/IB_QPT_GSI

    :param struct rvt_dev_info \*rdi:
        rvt device info structure

    :param struct rvt_qpn_table \*qpt:
        queue pair number table pointer

    :param enum ib_qp_type type:

        *undescribed*

    :param u8 port_num:
        IB port number, 1 based, comes from core

    :param gfp_t gfp:

        *undescribed*



.. _`alloc_qpn.return`:

Return
------

The queue pair number



.. _`rvt_clear_mr_refs`:

rvt_clear_mr_refs
=================

.. c:function:: void rvt_clear_mr_refs (struct rvt_qp *qp, int clr_sends)

    Drop help mr refs

    :param struct rvt_qp \*qp:
        rvt qp data structure

    :param int clr_sends:
        If shoudl clear send side or not



.. _`rvt_remove_qp`:

rvt_remove_qp
=============

.. c:function:: void rvt_remove_qp (struct rvt_dev_info *rdi, struct rvt_qp *qp)

    remove qp form table

    :param struct rvt_dev_info \*rdi:
        rvt dev struct

    :param struct rvt_qp \*qp:
        qp to remove



.. _`rvt_remove_qp.description`:

Description
-----------

Remove the QP from the table so it can't be found asynchronously by
the receive routine.



.. _`rvt_reset_qp`:

rvt_reset_qp
============

.. c:function:: void rvt_reset_qp (struct rvt_dev_info *rdi, struct rvt_qp *qp, enum ib_qp_type type)

    initialize the QP state to the reset state

    :param struct rvt_dev_info \*rdi:

        *undescribed*

    :param struct rvt_qp \*qp:
        the QP to reset

    :param enum ib_qp_type type:
        the QP type
        r and s lock are required to be held by the caller



.. _`rvt_create_qp`:

rvt_create_qp
=============

.. c:function:: struct ib_qp *rvt_create_qp (struct ib_pd *ibpd, struct ib_qp_init_attr *init_attr, struct ib_udata *udata)

    create a queue pair for a device

    :param struct ib_pd \*ibpd:
        the protection domain who's device we create the queue pair for

    :param struct ib_qp_init_attr \*init_attr:
        the attributes of the queue pair

    :param struct ib_udata \*udata:
        user data for libibverbs.so



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

Called by the :c:func:`ib_create_qp` core verbs function.



.. _`rvt_error_qp`:

rvt_error_qp
============

.. c:function:: int rvt_error_qp (struct rvt_qp *qp, enum ib_wc_status err)

    put a QP into the error state

    :param struct rvt_qp \*qp:
        the QP to put into the error state

    :param enum ib_wc_status err:
        the receive completion error to signal if a RWQE is active



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

.. c:function:: int rvt_modify_qp (struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_udata *udata)

    modify the attributes of a queue pair

    :param struct ib_qp \*ibqp:
        the queue pair who's attributes we're modifying

    :param struct ib_qp_attr \*attr:
        the new attributes

    :param int attr_mask:
        the mask of attributes to modify

    :param struct ib_udata \*udata:
        user data for libibverbs.so



.. _`rvt_modify_qp.return`:

Return
------

0 on success, otherwise returns an errno.



.. _`rvt_destroy_qp`:

rvt_destroy_qp
==============

.. c:function:: int rvt_destroy_qp (struct ib_qp *ibqp)

    destroy a queue pair

    :param struct ib_qp \*ibqp:
        the queue pair to destroy



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

.. c:function:: int rvt_query_qp (struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_qp_init_attr *init_attr)

    query an ipbq

    :param struct ib_qp \*ibqp:
        IB qp to query

    :param struct ib_qp_attr \*attr:
        attr struct to fill in

    :param int attr_mask:
        attr mask ignored

    :param struct ib_qp_init_attr \*init_attr:
        struct to fill in



.. _`rvt_query_qp.return`:

Return
------

always 0



.. _`rvt_post_recv`:

rvt_post_recv
=============

.. c:function:: int rvt_post_recv (struct ib_qp *ibqp, struct ib_recv_wr *wr, struct ib_recv_wr **bad_wr)

    post a receive on a QP

    :param struct ib_qp \*ibqp:
        the QP to post the receive on

    :param struct ib_recv_wr \*wr:
        the WR to post

    :param struct ib_recv_wr \*\*bad_wr:
        the first bad WR is put here



.. _`rvt_post_recv.description`:

Description
-----------

This may be called from interrupt context.



.. _`rvt_post_recv.return`:

Return
------

0 on success otherwise errno



.. _`qp_get_savail`:

qp_get_savail
=============

.. c:function:: u32 qp_get_savail (struct rvt_qp *qp)

    return number of avail send entries

    :param struct rvt_qp \*qp:

        *undescribed*



.. _`qp_get_savail.description`:

Description
-----------


``qp`` - the qp

This assumes the s_hlock is held but the s_last
qp variable is uncontrolled.



.. _`rvt_post_one_wr`:

rvt_post_one_wr
===============

.. c:function:: int rvt_post_one_wr (struct rvt_qp *qp, struct ib_send_wr *wr, int *call_send)

    post one RC, UC, or UD send work request

    :param struct rvt_qp \*qp:
        the QP to post on

    :param struct ib_send_wr \*wr:
        the work request to send

    :param int \*call_send:

        *undescribed*



.. _`rvt_post_send`:

rvt_post_send
=============

.. c:function:: int rvt_post_send (struct ib_qp *ibqp, struct ib_send_wr *wr, struct ib_send_wr **bad_wr)

    post a send on a QP

    :param struct ib_qp \*ibqp:
        the QP to post the send on

    :param struct ib_send_wr \*wr:
        the list of work requests to post

    :param struct ib_send_wr \*\*bad_wr:
        the first bad WR is put here



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

.. c:function:: int rvt_post_srq_recv (struct ib_srq *ibsrq, struct ib_recv_wr *wr, struct ib_recv_wr **bad_wr)

    post a receive on a shared receive queue

    :param struct ib_srq \*ibsrq:
        the SRQ to post the receive on

    :param struct ib_recv_wr \*wr:
        the list of work requests to post

    :param struct ib_recv_wr \*\*bad_wr:
        A pointer to the first WR to cause a problem is put here



.. _`rvt_post_srq_recv.description`:

Description
-----------

This may be called from interrupt context.



.. _`rvt_post_srq_recv.return`:

Return
------

0 on success else errno

