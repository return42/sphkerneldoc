.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-mpc52xx.c

.. _`mpc52xx_spi_fsm_process`:

mpc52xx_spi_fsm_process
=======================

.. c:function:: void mpc52xx_spi_fsm_process(int irq, struct mpc52xx_spi *ms)

    Finite State Machine iteration function

    :param irq:
        irq number that triggered the FSM or 0 for polling
    :type irq: int

    :param ms:
        pointer to mpc52xx_spi driver data
    :type ms: struct mpc52xx_spi \*

.. _`mpc52xx_spi_irq`:

mpc52xx_spi_irq
===============

.. c:function:: irqreturn_t mpc52xx_spi_irq(int irq, void *_ms)

    IRQ handler

    :param irq:
        *undescribed*
    :type irq: int

    :param _ms:
        *undescribed*
    :type _ms: void \*

.. _`mpc52xx_spi_wq`:

mpc52xx_spi_wq
==============

.. c:function:: void mpc52xx_spi_wq(struct work_struct *work)

    Workqueue function for polling the state machine

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. This file was automatic generated / don't edit.

