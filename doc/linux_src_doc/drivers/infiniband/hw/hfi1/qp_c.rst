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

.. _`hfi1_compute_aeth`:

hfi1_compute_aeth
=================

.. c:function:: __be32 hfi1_compute_aeth(struct rvt_qp *qp)

    compute the AETH (syndrome + MSN)

    :param struct rvt_qp \*qp:
        the queue pair to compute the AETH for

.. _`hfi1_compute_aeth.description`:

Description
-----------

Returns the AETH.

.. _`_hfi1_schedule_send`:

_hfi1_schedule_send
===================

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

.. _`hfi1_get_credit`:

hfi1_get_credit
===============

.. c:function:: void hfi1_get_credit(struct rvt_qp *qp, u32 aeth)

    flush the send work queue of a QP

    :param struct rvt_qp \*qp:
        the qp who's send work queue to flush

    :param u32 aeth:
        the Acknowledge Extended Transport Header

.. _`hfi1_get_credit.description`:

Description
-----------

The QP s_lock should be held.

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

