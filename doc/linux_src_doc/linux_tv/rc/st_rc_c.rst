.. -*- coding: utf-8; mode: rst -*-

=======
st_rc.c
=======



.. _xref_IRB_RX_INTS:

IRB_RX_INTS
===========

.. c:function:: IRB_RX_INTS ()

    \\\gt; bit 3; Enable overrun IRQ 1 -\\\gt; bit 2; Enable last symbol IRQ 1 -\\\gt; bit 1: Enable RX interrupt 1 -\\\gt; bit 0;




.. _xref_st_rc_rx_interrupt:

st_rc_rx_interrupt
==================

.. c:function:: irqreturn_t st_rc_rx_interrupt (int irq, void * data)

     output and standard definition used by LIRC (and most of the world!)

    :param int irq:

        _undescribed_

    :param void * data:

        _undescribed_



Description
-----------



          mark                                     mark
     |-IRB_RX_ON-|                            |-IRB_RX_ON-|
     ___  ___  ___                            ___  ___  ___             _
     | |  | |  | |                            | |  | |  | |             |
     | |  | |  | |         space 0            | |  | |  | |   space 1   |
_____| |__| |__| |____________________________| |__| |__| |_____________|


     |--------------- IRB_RX_SYS -------------|------ IRB_RX_SYS -------|


     |------------- encoding bit 0 -----------|---- encoding bit 1 -----|


ST hardware returns mark (IRB_RX_ON) and total symbol time (IRB_RX_SYS), so
convert to standard mark/space we have to calculate space=(IRB_RX_SYS-mark)
The mark time represents the amount of time the carrier (usually 36-40kHz)
is detected.The above examples shows Pulse Width Modulation encoding where
bit 0 is represented by space>mark.


