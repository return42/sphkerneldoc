.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/nitrox/nitrox_isr.c

.. _`nps_pkt_slc_isr`:

nps_pkt_slc_isr
===============

.. c:function:: irqreturn_t nps_pkt_slc_isr(int irq, void *data)

    IRQ handler for NPS solicit port

    :param int irq:
        irq number

    :param void \*data:
        argument

.. _`clear_nps_core_int_active`:

clear_nps_core_int_active
=========================

.. c:function:: void clear_nps_core_int_active(struct nitrox_device *ndev)

    clear NPS_CORE_INT_ACTIVE interrupts

    :param struct nitrox_device \*ndev:
        NITROX device

.. _`nitrox_pf_cleanup_isr`:

nitrox_pf_cleanup_isr
=====================

.. c:function:: void nitrox_pf_cleanup_isr(struct nitrox_device *ndev)

    Cleanup PF MSI-X and IRQ

    :param struct nitrox_device \*ndev:
        NITROX device

.. _`nitrox_pf_init_isr`:

nitrox_pf_init_isr
==================

.. c:function:: int nitrox_pf_init_isr(struct nitrox_device *ndev)

    Initialize PF MSI-X vectors and IRQ

    :param struct nitrox_device \*ndev:
        NITROX device

.. _`nitrox_pf_init_isr.return`:

Return
------

0 on success, a negative value on failure.

.. This file was automatic generated / don't edit.

