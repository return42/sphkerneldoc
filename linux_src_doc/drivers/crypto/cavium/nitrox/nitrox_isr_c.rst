.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/nitrox/nitrox_isr.c

.. _`nr_ring_vectors`:

NR_RING_VECTORS
===============

.. c:function::  NR_RING_VECTORS()

    - NPS packet ring, AQMQ ring and ZQMQ ring

.. _`nps_pkt_slc_isr`:

nps_pkt_slc_isr
===============

.. c:function:: irqreturn_t nps_pkt_slc_isr(int irq, void *data)

    IRQ handler for NPS solicit port

    :param irq:
        irq number
    :type irq: int

    :param data:
        argument
    :type data: void \*

.. _`nps_core_int_isr`:

nps_core_int_isr
================

.. c:function:: irqreturn_t nps_core_int_isr(int irq, void *data)

    interrupt handler for NITROX errors and mailbox communication

    :param irq:
        *undescribed*
    :type irq: int

    :param data:
        *undescribed*
    :type data: void \*

.. This file was automatic generated / don't edit.

