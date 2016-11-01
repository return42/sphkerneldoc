.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/rdmavt_qp.h

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

.. This file was automatic generated / don't edit.

