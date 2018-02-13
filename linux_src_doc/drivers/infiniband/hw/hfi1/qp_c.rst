.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/qp.c

.. _`verbs_mtu_enum_to_int`:

verbs_mtu_enum_to_int
=====================

.. c:function:: int verbs_mtu_enum_to_int(struct ib_device *dev, enum ib_mtu mtu)

    "first class citizen".  Instead we hide this here and rely on Verbs ULPs to blindly pass the MTU enum value from the PathRecord to us.

    :param struct ib_device \*dev:
        *undescribed*

    :param enum ib_mtu mtu:
        *undescribed*

.. _`hfi1_check_send_wqe`:

hfi1_check_send_wqe
===================

.. c:function:: int hfi1_check_send_wqe(struct rvt_qp *qp, struct rvt_swqe *wqe)

    validate wqe \ ``qp``\  - The qp \ ``wqe``\  - The built wqe

    :param struct rvt_qp \*qp:
        *undescribed*

    :param struct rvt_swqe \*wqe:
        *undescribed*

.. _`hfi1_check_send_wqe.description`:

Description
-----------

validate wqe.  This is called
prior to inserting the wqe into
the ring but after the wqe has been
setup.

Returns 0 on success, -EINVAL on failure

.. _`_hfi1_schedule_send`:

\_hfi1_schedule_send
====================

.. c:function:: void _hfi1_schedule_send(struct rvt_qp *qp)

    schedule progress

    :param struct rvt_qp \*qp:
        the QP

.. _`_hfi1_schedule_send.description`:

Description
-----------

This schedules qp progress w/o regard to the s_flags.

It is only used in the post send, which doesn't hold
the s_lock.

.. _`hfi1_schedule_send`:

hfi1_schedule_send
==================

.. c:function:: void hfi1_schedule_send(struct rvt_qp *qp)

    schedule progress

    :param struct rvt_qp \*qp:
        the QP

.. _`hfi1_schedule_send.description`:

Description
-----------

This schedules qp progress and caller should hold
the s_lock.

.. _`qp_iter_print`:

qp_iter_print
=============

.. c:function:: void qp_iter_print(struct seq_file *s, struct rvt_qp_iter *iter)

    print the qp information to seq_file

    :param struct seq_file \*s:
        the seq_file to emit the qp information on

    :param struct rvt_qp_iter \*iter:
        the iterator for the qp hash list

.. _`hfi1_qp_iter_cb`:

hfi1_qp_iter_cb
===============

.. c:function:: void hfi1_qp_iter_cb(struct rvt_qp *qp, u64 v)

    callback for iterator \ ``qp``\  - the qp \ ``v``\  - the sl in low bits of v

    :param struct rvt_qp \*qp:
        *undescribed*

    :param u64 v:
        *undescribed*

.. _`hfi1_qp_iter_cb.description`:

Description
-----------

This is called from the iterator callback to work
on an individual qp.

.. _`hfi1_error_port_qps`:

hfi1_error_port_qps
===================

.. c:function:: void hfi1_error_port_qps(struct hfi1_ibport *ibp, u8 sl)

    put a port's RC/UC qps into error state

    :param struct hfi1_ibport \*ibp:
        the ibport.

    :param u8 sl:
        the service level.

.. _`hfi1_error_port_qps.description`:

Description
-----------

This function places all RC/UC qps with a given service level into error
state. It is generally called to force upper lay apps to abandon stale qps
after an sl->sc mapping change.

.. This file was automatic generated / don't edit.

