.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-mpc52xx.c

.. _`mpc52xx_spi_fsm_process`:

mpc52xx_spi_fsm_process
=======================

.. c:function:: void mpc52xx_spi_fsm_process(int irq, struct mpc52xx_spi *ms)

    Finite State Machine iteration function

    :param int irq:
        irq number that triggered the FSM or 0 for polling

    :param struct mpc52xx_spi \*ms:
        pointer to mpc52xx_spi driver data

.. _`mpc52xx_spi_irq`:

mpc52xx_spi_irq
===============

.. c:function:: irqreturn_t mpc52xx_spi_irq(int irq, void *_ms)

    IRQ handler

    :param int irq:
        *undescribed*

    :param void \*_ms:
        *undescribed*

.. _`mpc52xx_spi_wq`:

mpc52xx_spi_wq
==============

.. c:function:: void mpc52xx_spi_wq(struct work_struct *work)

    Workqueue function for polling the state machine

    :param struct work_struct \*work:
        *undescribed*

.. This file was automatic generated / don't edit.

