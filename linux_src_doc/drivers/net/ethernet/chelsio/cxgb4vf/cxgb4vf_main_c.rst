.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4vf/cxgb4vf_main.c

.. _`set_rxq_intr_params`:

set_rxq_intr_params
===================

.. c:function:: int set_rxq_intr_params(struct adapter *adapter, struct sge_rspq *rspq, unsigned int us, unsigned int cnt)

    set a queue's interrupt holdoff parameters

    :param struct adapter \*adapter:
        the adapter

    :param struct sge_rspq \*rspq:
        the RX response queue

    :param unsigned int us:
        the hold-off time in us, or 0 to disable timer

    :param unsigned int cnt:
        the hold-off packet count, or 0 to disable counter

.. _`set_rxq_intr_params.description`:

Description
-----------

Sets an RX response queue's interrupt hold-off time and packet count.
At least one of the two needs to be enabled for the queue to generate
interrupts.

.. This file was automatic generated / don't edit.

