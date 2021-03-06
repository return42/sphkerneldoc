.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/octeon/ethernet-rx.c

.. _`cvm_oct_do_interrupt`:

cvm_oct_do_interrupt
====================

.. c:function:: irqreturn_t cvm_oct_do_interrupt(int irq, void *napi_id)

    interrupt handler.

    :param irq:
        Interrupt number.
    :type irq: int

    :param napi_id:
        Cookie to identify the NAPI instance.
    :type napi_id: void \*

.. _`cvm_oct_do_interrupt.description`:

Description
-----------

The interrupt occurs whenever the POW has packets in our group.

.. _`cvm_oct_check_rcv_error`:

cvm_oct_check_rcv_error
=======================

.. c:function:: int cvm_oct_check_rcv_error(cvmx_wqe_t *work)

    process receive errors

    :param work:
        Work queue entry pointing to the packet.
    :type work: cvmx_wqe_t \*

.. _`cvm_oct_check_rcv_error.description`:

Description
-----------

Returns Non-zero if the packet can be dropped, zero otherwise.

.. _`cvm_oct_napi_poll`:

cvm_oct_napi_poll
=================

.. c:function:: int cvm_oct_napi_poll(struct napi_struct *napi, int budget)

    the NAPI poll function.

    :param napi:
        The NAPI instance.
    :type napi: struct napi_struct \*

    :param budget:
        Maximum number of packets to receive.
    :type budget: int

.. _`cvm_oct_napi_poll.description`:

Description
-----------

Returns the number of packets processed.

.. _`cvm_oct_poll_controller`:

cvm_oct_poll_controller
=======================

.. c:function:: void cvm_oct_poll_controller(struct net_device *dev)

    poll for receive packets device.

    :param dev:
        Device to poll. Unused
    :type dev: struct net_device \*

.. This file was automatic generated / don't edit.

