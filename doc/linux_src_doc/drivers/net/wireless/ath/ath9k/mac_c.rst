.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath9k/mac.c

.. _`ath9k_hw_updatetxtriglevel`:

ath9k_hw_updatetxtriglevel
==========================

.. c:function:: bool ath9k_hw_updatetxtriglevel(struct ath_hw *ah, bool bIncTrigLevel)

    adjusts the frame trigger level

    :param struct ath_hw \*ah:
        atheros hardware struct

    :param bool bIncTrigLevel:
        whether or not the frame trigger level should be updated

.. _`ath9k_hw_updatetxtriglevel.description`:

Description
-----------

The frame trigger level specifies the minimum number of bytes,
in units of 64 bytes, that must be DMA'ed into the PCU TX FIFO
before the PCU will initiate sending the frame on the air. This can
mean we initiate transmit before a full frame is on the PCU TX FIFO.
Resets to 0x1 (meaning 64 bytes or a full frame, whichever occurs
first)

Caution must be taken to ensure to set the frame trigger level based
on the DMA request size. For example if the DMA request size is set to
128 bytes the trigger level cannot exceed 6 \* 64 = 384. This is because
there need to be enough space in the tx FIFO for the requested transfer
size. Hence the tx FIFO will stop with 512 - 128 = 384 bytes. If we set
the threshold to a value beyond 6, then the transmit will hang.

Current dual   stream devices have a PCU TX FIFO size of 8 KB.
Current single stream devices have a PCU TX FIFO size of 4 KB, however,
there is a hardware issue which forces us to use 2 KB instead so the
frame trigger level must not exceed 2 KB for these chipsets.

.. This file was automatic generated / don't edit.

