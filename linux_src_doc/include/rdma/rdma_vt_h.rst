.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/rdma_vt.h

.. _`rvt_set_ibdev_name`:

rvt_set_ibdev_name
==================

.. c:function:: void rvt_set_ibdev_name(struct rvt_dev_info *rdi, const char *fmt, const char *name, const int unit)

    Craft an IB device name from client info

    :param rdi:
        pointer to the client rvt_dev_info structure
    :type rdi: struct rvt_dev_info \*

    :param fmt:
        *undescribed*
    :type fmt: const char \*

    :param name:
        client specific name
    :type name: const char \*

    :param unit:
        client specific unit number.
    :type unit: const int

.. _`rvt_get_ibdev_name`:

rvt_get_ibdev_name
==================

.. c:function:: const char *rvt_get_ibdev_name(const struct rvt_dev_info *rdi)

    return the IB name

    :param rdi:
        rdmavt device
    :type rdi: const struct rvt_dev_info \*

.. _`rvt_get_ibdev_name.description`:

Description
-----------

Return the registered name of the device.

.. _`rvt_lookup_qpn`:

rvt_lookup_qpn
==============

.. c:function:: struct rvt_qp *rvt_lookup_qpn(struct rvt_dev_info *rdi, struct rvt_ibport *rvp, u32 qpn)

    return the QP with the given QPN

    :param rdi:
        *undescribed*
    :type rdi: struct rvt_dev_info \*

    :param rvp:
        *undescribed*
    :type rvp: struct rvt_ibport \*

    :param qpn:
        the QP number to look up
    :type qpn: u32

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

    :param qp:
        *undescribed*
    :type qp: struct rvt_qp \*

.. This file was automatic generated / don't edit.

