.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/octeon/ethernet-rx.c

.. _`cvm_oct_do_interrupt`:

cvm_oct_do_interrupt
====================

.. c:function:: irqreturn_t cvm_oct_do_interrupt(int cpl, void *dev_id)

    interrupt handler.

    :param int cpl:
        Interrupt number. Unused

    :param void \*dev_id:
        Cookie to identify the device. Unused

.. _`cvm_oct_do_interrupt.description`:

Description
-----------

The interrupt occurs whenever the POW has packets in our group.

.. _`cvm_oct_check_rcv_error`:

cvm_oct_check_rcv_error
=======================

.. c:function:: int cvm_oct_check_rcv_error(cvmx_wqe_t *work)

    process receive errors

    :param cvmx_wqe_t \*work:
        Work queue entry pointing to the packet.

.. _`cvm_oct_check_rcv_error.description`:

Description
-----------

Returns Non-zero if the packet can be dropped, zero otherwise.

.. _`cvm_oct_napi_poll`:

cvm_oct_napi_poll
=================

.. c:function:: int cvm_oct_napi_poll(struct napi_struct *napi, int budget)

    the NAPI poll function.

    :param struct napi_struct \*napi:
        The NAPI instance, or null if called from cvm_oct_poll_controller

    :param int budget:
        Maximum number of packets to receive.

.. _`cvm_oct_napi_poll.description`:

Description
-----------

Returns the number of packets processed.

.. _`cvm_oct_poll_controller`:

cvm_oct_poll_controller
=======================

.. c:function:: void cvm_oct_poll_controller(struct net_device *dev)

    poll for receive packets device.

    :param struct net_device \*dev:
        Device to poll. Unused

.. This file was automatic generated / don't edit.

