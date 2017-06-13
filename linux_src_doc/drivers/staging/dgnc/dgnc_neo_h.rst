.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/dgnc/dgnc_neo.h

.. _`neo_uart_struct`:

struct neo_uart_struct
======================

.. c:type:: struct neo_uart_struct

    Per channel/port NEO UART structure

.. _`neo_uart_struct.definition`:

Definition
----------

.. code-block:: c

    struct neo_uart_struct {
        u8 txrx;
        u8 ier;
        u8 isr_fcr;
        u8 lcr;
        u8 mcr;
        u8 lsr;
        u8 msr;
        u8 spr;
        u8 fctr;
        u8 efr;
        u8 tfifo;
        u8 rfifo;
        u8 xoffchar1;
        u8 xoffchar2;
        u8 xonchar1;
        u8 xonchar2;
        u8 reserved1;
        u8 txrxburst;
        u8 reserved2;
        u8 rxburst_with_errors;
    }

.. _`neo_uart_struct.members`:

Members
-------

txrx
    (RW) Holding Register.

ier
    (RW) Interrupt Enable Register.

isr_fcr
    (RW) Interrupt Status Reg/Fifo Control Register.

lcr
    (RW) Line Control Register.

mcr
    (RW) Modem Control Register.

lsr
    (RW) Line Status Register.

msr
    (RW) Modem Status Register.

spr
    (RW) Scratch Pad Register.

fctr
    (RW) Feature Control Register.

efr
    (RW) Enhanced Function Register.

tfifo
    (RW) Transmit FIFO Register.

rfifo
    (RW) Receive  FIFO Register.

xoffchar1
    (RW) XOff Character 1 Register.

xoffchar2
    (RW) XOff Character 2 Register.

xonchar1
    (RW) Xon Character 1 Register.

xonchar2
    (RW) XOn Character 2 Register.

reserved1
    (U) Reserved by Exar.

txrxburst
    (RW)  64 bytes of RX/TX FIFO Data.

reserved2
    (U) Reserved by Exar.

rxburst_with_errors
    (R) bytes of RX FIFO Data + LSR.

.. _`neo_uart_struct.description`:

Description
-----------

key - W = read write
- R = read only
- U = unused

.. This file was automatic generated / don't edit.

