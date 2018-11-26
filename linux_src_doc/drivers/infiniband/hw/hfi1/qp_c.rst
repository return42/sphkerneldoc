.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/qp.c

.. _`verbs_mtu_enum_to_int`:

verbs_mtu_enum_to_int
=====================

.. c:function:: int verbs_mtu_enum_to_int(struct ib_device *dev, enum ib_mtu mtu)

    "first class citizen".  Instead we hide this here and rely on Verbs ULPs to blindly pass the MTU enum value from the PathRecord to us.

    :param dev:
        *undescribed*
    :type dev: struct ib_device \*

    :param mtu:
        *undescribed*
    :type mtu: enum ib_mtu

.. _`hfi1_setup_wqe`:

hfi1_setup_wqe
==============

.. c:function:: int hfi1_setup_wqe(struct rvt_qp *qp, struct rvt_swqe *wqe, bool *call_send)

    set up the wqe \ ``qp``\  - The qp \ ``wqe``\  - The built wqe \ ``call_send``\  - Determine if the send should be posted or scheduled.

    :param qp:
        *undescribed*
    :type qp: struct rvt_qp \*

    :param wqe:
        *undescribed*
    :type wqe: struct rvt_swqe \*

    :param call_send:
        *undescribed*
    :type call_send: bool \*

.. _`hfi1_setup_wqe.description`:

Description
-----------

Perform setup of the wqe.  This is called
prior to inserting the wqe into the ring but after
the wqe has been setup by RDMAVT. This function
allows the driver the opportunity to perform
validation and additional setup of the wqe.

Returns 0 on success, -EINVAL on failure

.. _`_hfi1_schedule_send`:

\_hfi1_schedule_send
====================

.. c:function:: bool _hfi1_schedule_send(struct rvt_qp *qp)

    schedule progress

    :param qp:
        the QP
    :type qp: struct rvt_qp \*

.. _`_hfi1_schedule_send.description`:

Description
-----------

This schedules qp progress w/o regard to the s_flags.

It is only used in the post send, which doesn't hold
the s_lock.

.. _`hfi1_schedule_send`:

hfi1_schedule_send
==================

.. c:function:: bool hfi1_schedule_send(struct rvt_qp *qp)

    schedule progress

    :param qp:
        the QP
    :type qp: struct rvt_qp \*

.. _`hfi1_schedule_send.description`:

Description
-----------

This schedules qp progress and caller should hold
the s_lock.
\ ``return``\  true if the first leg is scheduled;
false if the first leg is not scheduled.

.. _`qp_to_sdma_engine`:

qp_to_sdma_engine
=================

.. c:function:: struct sdma_engine *qp_to_sdma_engine(struct rvt_qp *qp, u8 sc5)

    map a qp to a send engine

    :param qp:
        the QP
    :type qp: struct rvt_qp \*

    :param sc5:
        the 5 bit sc
    :type sc5: u8

.. _`qp_to_sdma_engine.return`:

Return
------

A send engine for the qp or NULL for SMI type qp.

.. _`qp_iter_print`:

qp_iter_print
=============

.. c:function:: void qp_iter_print(struct seq_file *s, struct rvt_qp_iter *iter)

    print the qp information to seq_file

    :param s:
        the seq_file to emit the qp information on
    :type s: struct seq_file \*

    :param iter:
        the iterator for the qp hash list
    :type iter: struct rvt_qp_iter \*

.. _`hfi1_qp_iter_cb`:

hfi1_qp_iter_cb
===============

.. c:function:: void hfi1_qp_iter_cb(struct rvt_qp *qp, u64 v)

    callback for iterator \ ``qp``\  - the qp \ ``v``\  - the sl in low bits of v

    :param qp:
        *undescribed*
    :type qp: struct rvt_qp \*

    :param v:
        *undescribed*
    :type v: u64

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

    :param ibp:
        the ibport.
    :type ibp: struct hfi1_ibport \*

    :param sl:
        the service level.
    :type sl: u8

.. _`hfi1_error_port_qps.description`:

Description
-----------

This function places all RC/UC qps with a given service level into error
state. It is generally called to force upper lay apps to abandon stale qps
after an sl->sc mapping change.

.. This file was automatic generated / don't edit.

