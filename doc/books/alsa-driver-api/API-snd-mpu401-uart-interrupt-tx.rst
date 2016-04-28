.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-mpu401-uart-interrupt-tx:

============================
snd_mpu401_uart_interrupt_tx
============================

*man snd_mpu401_uart_interrupt_tx(9)*

*4.6.0-rc5*

generic MPU401-UART transmit irq handler


Synopsis
========

.. c:function:: irqreturn_t snd_mpu401_uart_interrupt_tx( int irq, void * dev_id )

Arguments
=========

``irq``
    the irq number

``dev_id``
    mpu401 instance


Description
===========

Processes the interrupt for MPU401-UART output.


Return
======

``IRQ_HANDLED`` if the interrupt was handled. ``IRQ_NONE`` otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
