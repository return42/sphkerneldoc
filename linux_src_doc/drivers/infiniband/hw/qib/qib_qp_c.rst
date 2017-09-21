.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_qp.c

.. _`qib_free_all_qps`:

qib_free_all_qps
================

.. c:function:: unsigned qib_free_all_qps(struct rvt_dev_info *rdi)

    check for QPs still in use

    :param struct rvt_dev_info \*rdi:
        *undescribed*

.. _`qib_check_send_wqe`:

qib_check_send_wqe
==================

.. c:function:: int qib_check_send_wqe(struct rvt_qp *qp, struct rvt_swqe *wqe)

    validate wr/wqe \ ``qp``\  - The qp \ ``wqe``\  - The built wqe

    :param struct rvt_qp \*qp:
        *undescribed*

    :param struct rvt_swqe \*wqe:
        *undescribed*

.. _`qib_check_send_wqe.description`:

Description
-----------

validate wr/wqe.  This is called
prior to inserting the wqe into
the ring but after the wqe has been
setup.

Returns 1 to force direct progress, 0 otherwise, -EINVAL on failure

.. _`qib_qp_iter_print`:

qib_qp_iter_print
=================

.. c:function:: void qib_qp_iter_print(struct seq_file *s, struct rvt_qp_iter *iter)

    print information to seq_file \ ``s``\  - the seq_file \ ``iter``\  - the iterator

    :param struct seq_file \*s:
        *undescribed*

    :param struct rvt_qp_iter \*iter:
        *undescribed*

.. This file was automatic generated / don't edit.

