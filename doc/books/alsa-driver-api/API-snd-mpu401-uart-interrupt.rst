
.. _API-snd-mpu401-uart-interrupt:

=========================
snd_mpu401_uart_interrupt
=========================

*man snd_mpu401_uart_interrupt(9)*

*4.6.0-rc1*

generic MPU401-UART interrupt handler


Synopsis
========

.. c:function:: irqreturn_t snd_mpu401_uart_interrupt( int irq, void * dev_id )

Arguments
=========

``irq``
    the irq number

``dev_id``
    mpu401 instance


Description
===========

Processes the interrupt for MPU401-UART i/o.


Return
======

``IRQ_HANDLED`` if the interrupt was handled. ``IRQ_NONE`` otherwise.
