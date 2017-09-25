.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/rdmavt_qp.h

.. _`rvt_is_user_qp`:

rvt_is_user_qp
==============

.. c:function:: bool rvt_is_user_qp(struct rvt_qp *qp)

    return if this is user mode QP \ ``qp``\  - the target QP

    :param struct rvt_qp \*qp:
        *undescribed*

.. _`rvt_get_qp`:

rvt_get_qp
==========

.. c:function:: void rvt_get_qp(struct rvt_qp *qp)

    get a QP reference \ ``qp``\  - the QP to hold

    :param struct rvt_qp \*qp:
        *undescribed*

.. _`rvt_put_qp`:

rvt_put_qp
==========

.. c:function:: void rvt_put_qp(struct rvt_qp *qp)

    release a QP reference \ ``qp``\  - the QP to release

    :param struct rvt_qp \*qp:
        *undescribed*

.. _`rvt_put_swqe`:

rvt_put_swqe
============

.. c:function:: void rvt_put_swqe(struct rvt_swqe *wqe)

    drop mr refs held by swqe \ ``wqe``\  - the send wqe

    :param struct rvt_swqe \*wqe:
        *undescribed*

.. _`rvt_put_swqe.description`:

Description
-----------

This drops any mr references held by the swqe

.. _`rvt_qp_wqe_reserve`:

rvt_qp_wqe_reserve
==================

.. c:function:: void rvt_qp_wqe_reserve(struct rvt_qp *qp, struct rvt_swqe *wqe)

    reserve operation \ ``qp``\  - the rvt qp \ ``wqe``\  - the send wqe

    :param struct rvt_qp \*qp:
        *undescribed*

    :param struct rvt_swqe \*wqe:
        *undescribed*

.. _`rvt_qp_wqe_reserve.description`:

Description
-----------

This routine used in post send to record
a wqe relative reserved operation use.

.. _`rvt_qp_wqe_unreserve`:

rvt_qp_wqe_unreserve
====================

.. c:function:: void rvt_qp_wqe_unreserve(struct rvt_qp *qp, struct rvt_swqe *wqe)

    clean reserved operation \ ``qp``\  - the rvt qp \ ``wqe``\  - the send wqe

    :param struct rvt_qp \*qp:
        *undescribed*

    :param struct rvt_swqe \*wqe:
        *undescribed*

.. _`rvt_qp_wqe_unreserve.description`:

Description
-----------

This decrements the reserve use count.

This call MUST precede the change to
s_last to insure that post send sees a stable
s_avail.

An \ :c:func:`smp_mp__after_atomic`\  is used to insure
the compiler does not juggle the order of the s_last
ring index and the decrementing of s_reserved_used.

.. _`rvt_qp_swqe_complete`:

rvt_qp_swqe_complete
====================

.. c:function:: void rvt_qp_swqe_complete(struct rvt_qp *qp, struct rvt_swqe *wqe, enum ib_wc_opcode opcode, enum ib_wc_status status)

    insert send completion \ ``qp``\  - the qp \ ``wqe``\  - the send wqe \ ``status``\  - completion status

    :param struct rvt_qp \*qp:
        *undescribed*

    :param struct rvt_swqe \*wqe:
        *undescribed*

    :param enum ib_wc_opcode opcode:
        *undescribed*

    :param enum ib_wc_status status:
        *undescribed*

.. _`rvt_qp_swqe_complete.description`:

Description
-----------

Insert a send completion into the completion
queue if the qp indicates it should be done.

See IBTA 10.7.3.1 for info on completion
control.

.. _`rvt_compute_aeth`:

rvt_compute_aeth
================

.. c:function:: __be32 rvt_compute_aeth(struct rvt_qp *qp)

    compute the AETH (syndrome + MSN)

    :param struct rvt_qp \*qp:
        the queue pair to compute the AETH for

.. _`rvt_compute_aeth.description`:

Description
-----------

Returns the AETH.

.. _`rvt_get_credit`:

rvt_get_credit
==============

.. c:function:: void rvt_get_credit(struct rvt_qp *qp, u32 aeth)

    flush the send work queue of a QP

    :param struct rvt_qp \*qp:
        the qp who's send work queue to flush

    :param u32 aeth:
        the Acknowledge Extended Transport Header

.. _`rvt_get_credit.description`:

Description
-----------

The QP s_lock should be held.

.. _`rvt_timeout_to_jiffies`:

rvt_timeout_to_jiffies
======================

.. c:function:: unsigned long rvt_timeout_to_jiffies(u8 timeout)

    Convert a ULP timeout input into jiffies \ ``timeout``\  - timeout input(0 - 31).

    :param u8 timeout:
        *undescribed*

.. _`rvt_timeout_to_jiffies.description`:

Description
-----------

Return a timeout value in jiffies.

.. _`rvt_qp_iter`:

struct rvt_qp_iter
==================

.. c:type:: struct rvt_qp_iter

    the iterator for QPs \ ``qp``\  - the current QP

.. _`rvt_qp_iter.definition`:

Definition
----------

.. code-block:: c

    struct rvt_qp_iter {
        struct rvt_qp *qp;
        struct rvt_dev_info *rdi;
        void (*cb)(struct rvt_qp *qp, u64 v);
        u64 v;
        int specials;
        int n;
    }

.. _`rvt_qp_iter.members`:

Members
-------

qp
    *undescribed*

rdi
    *undescribed*

cb
    *undescribed*

v
    *undescribed*

specials
    *undescribed*

n
    *undescribed*

.. _`rvt_qp_iter.description`:

Description
-----------

This structure defines the current iterator
state for sequenced access to all QPs relative
to an rvt_dev_info.

.. This file was automatic generated / don't edit.

