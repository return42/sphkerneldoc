.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/rpmh-rsc.c

.. _`rpmh_rsc_invalidate`:

rpmh_rsc_invalidate
===================

.. c:function:: int rpmh_rsc_invalidate(struct rsc_drv *drv)

    Invalidate sleep and wake TCSes

    :param drv:
        the RSC controller
    :type drv: struct rsc_drv \*

.. _`tcs_tx_done`:

tcs_tx_done
===========

.. c:function:: irqreturn_t tcs_tx_done(int irq, void *p)

    TX Done interrupt handler

    :param irq:
        *undescribed*
    :type irq: int

    :param p:
        *undescribed*
    :type p: void \*

.. _`rpmh_rsc_send_data`:

rpmh_rsc_send_data
==================

.. c:function:: int rpmh_rsc_send_data(struct rsc_drv *drv, const struct tcs_request *msg)

    Validate the incoming message and write to the appropriate TCS block.

    :param drv:
        the controller
    :type drv: struct rsc_drv \*

    :param msg:
        the data to be sent
    :type msg: const struct tcs_request \*

.. _`rpmh_rsc_send_data.return`:

Return
------

0 on success, -EINVAL on error.

.. _`rpmh_rsc_send_data.note`:

Note
----

This call blocks until a valid data is written to the TCS.

.. _`rpmh_rsc_write_ctrl_data`:

rpmh_rsc_write_ctrl_data
========================

.. c:function:: int rpmh_rsc_write_ctrl_data(struct rsc_drv *drv, const struct tcs_request *msg)

    Write request to the controller

    :param drv:
        the controller
    :type drv: struct rsc_drv \*

    :param msg:
        the data to be written to the controller
    :type msg: const struct tcs_request \*

.. _`rpmh_rsc_write_ctrl_data.description`:

Description
-----------

There is no response returned for writing the request to the controller.

.. This file was automatic generated / don't edit.

