.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/dgnc/dgnc_cls.h

.. _`cls_uart_struct`:

struct cls_uart_struct
======================

.. c:type:: struct cls_uart_struct

    Per channel/port Classic UART.

.. _`cls_uart_struct.definition`:

Definition
----------

.. code-block:: c

    struct cls_uart_struct {
        u8 txrx;
        u8 ier;
        u8 isr_fcr;
        u8 lcr;
        u8 mcr;
        u8 lsr;
        u8 msr;
        u8 spr;
    }

.. _`cls_uart_struct.members`:

Members
-------

txrx
    (WR) Holding Register.

ier
    (WR) Interrupt Enable Register.

isr_fcr
    (WR) Interrupt Status Register/Fifo Control Register.

lcr
    (WR) Line Control Register.

mcr
    (WR) Modem Control Register.

lsr
    (WR) Line Status Register.

msr
    (WR) Modem Status Register.

spr
    (WR) Scratch Pad Register.

.. _`cls_uart_struct.description`:

Description
-----------

key - W = read write
- R = read only
- U = unused

.. This file was automatic generated / don't edit.

