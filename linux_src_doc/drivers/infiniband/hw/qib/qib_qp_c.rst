.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_qp.c

.. _`qib_free_all_qps`:

qib_free_all_qps
================

.. c:function:: unsigned qib_free_all_qps(struct rvt_dev_info *rdi)

    check for QPs still in use

    :param rdi:
        *undescribed*
    :type rdi: struct rvt_dev_info \*

.. _`qib_check_send_wqe`:

qib_check_send_wqe
==================

.. c:function:: int qib_check_send_wqe(struct rvt_qp *qp, struct rvt_swqe *wqe, bool *call_send)

    validate wr/wqe \ ``qp``\  - The qp \ ``wqe``\  - The built wqe \ ``call_send``\  - Determine if the send should be posted or scheduled

    :param qp:
        *undescribed*
    :type qp: struct rvt_qp \*

    :param wqe:
        *undescribed*
    :type wqe: struct rvt_swqe \*

    :param call_send:
        *undescribed*
    :type call_send: bool \*

.. _`qib_check_send_wqe.description`:

Description
-----------

Returns 0 on success, -EINVAL on failure

.. _`qib_qp_iter_print`:

qib_qp_iter_print
=================

.. c:function:: void qib_qp_iter_print(struct seq_file *s, struct rvt_qp_iter *iter)

    print information to seq_file \ ``s``\  - the seq_file \ ``iter``\  - the iterator

    :param s:
        *undescribed*
    :type s: struct seq_file \*

    :param iter:
        *undescribed*
    :type iter: struct rvt_qp_iter \*

.. This file was automatic generated / don't edit.

