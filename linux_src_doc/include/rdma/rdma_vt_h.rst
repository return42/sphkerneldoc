.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/rdma_vt.h

.. _`rvt_lookup_qpn`:

rvt_lookup_qpn
==============

.. c:function:: struct rvt_qp *rvt_lookup_qpn(struct rvt_dev_info *rdi, struct rvt_ibport *rvp, u32 qpn)

    return the QP with the given QPN

    :param struct rvt_dev_info \*rdi:
        *undescribed*

    :param struct rvt_ibport \*rvp:
        *undescribed*

    :param u32 qpn:
        the QP number to look up

.. _`rvt_lookup_qpn.description`:

Description
-----------

The caller must hold the \ :c:func:`rcu_read_lock`\ , and keep the lock until
the returned qp is no longer in use.

.. _`rvt_mod_retry_timer`:

rvt_mod_retry_timer
===================

.. c:function:: void rvt_mod_retry_timer(struct rvt_qp *qp)

    mod a retry timer \ ``qp``\  - the QP Modify a potentially already running retry timer

    :param struct rvt_qp \*qp:
        *undescribed*

.. This file was automatic generated / don't edit.

