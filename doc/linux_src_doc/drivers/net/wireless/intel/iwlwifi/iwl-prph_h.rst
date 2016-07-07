.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-prph.h

.. _`scd_mem_lower_bound`:

SCD_MEM_LOWER_BOUND
===================

.. c:function::  SCD_MEM_LOWER_BOUND()

.. _`scd_mem_lower_bound.description`:

Description
-----------

The Tx Scheduler selects the next frame to be transmitted, choosing TFDs
(Transmit Frame Descriptors) from up to 16 circular Tx queues resident in
host DRAM.  It steers each frame's Tx command (which contains the frame
data) into one of up to 7 prioritized Tx DMA FIFO channels within the
device.  A queue maps to only one (selectable by driver) Tx DMA channel,
but one DMA channel may take input from several queues.

Tx DMA FIFOs have dedicated purposes.

For 5000 series and up, they are used differently
(cf. iwl5000_default_queue_to_tx_fifo in iwl-5000.c):

0 -- EDCA BK (background) frames, lowest priority
1 -- EDCA BE (best effort) frames, normal priority
2 -- EDCA VI (video) frames, higher priority
3 -- EDCA VO (voice) and management frames, highest priority
4 -- unused
5 -- unused
6 -- unused
7 -- Commands

Driver should normally map queues 0-6 to Tx DMA/FIFO channels 0-6.
In addition, driver can map the remaining queues to Tx DMA/FIFO
channels 0-3 to support 11n aggregation via EDCA DMA channels.

.. _`scd_mem_lower_bound.the-driver-sets-up-each-queue-to-work-in-one-of-two-modes`:

The driver sets up each queue to work in one of two modes
---------------------------------------------------------


1)  Scheduler-Ack, in which the scheduler automatically supports a
block-ack (BA) window of up to 64 TFDs.  In this mode, each queue
contains TFDs for a unique combination of Recipient Address (RA)
and Traffic Identifier (TID), that is, traffic of a given
Quality-Of-Service (QOS) priority, destined for a single station.

In scheduler-ack mode, the scheduler keeps track of the Tx status of
each frame within the BA window, including whether it's been transmitted,
and whether it's been acknowledged by the receiving station.  The device
automatically processes block-acks received from the receiving STA,
and reschedules un-acked frames to be retransmitted (successful
Tx completion may end up being out-of-order).

The driver must maintain the queue's Byte Count table in host DRAM
for this mode.
This mode does not support fragmentation.

2)  FIFO (a.k.a. non-Scheduler-ACK), in which each TFD is processed in order.
The device may automatically retry Tx, but will retry only one frame
at a time, until receiving ACK from receiving station, or reaching
retry limit and giving up.

The command queue (#4/#9) must use this mode!
This mode does not require use of the Byte Count table in host DRAM.

.. _`scd_mem_lower_bound.driver-controls-scheduler-operation-via-3-means`:

Driver controls scheduler operation via 3 means
-----------------------------------------------

1)  Scheduler registers
2)  Shared scheduler data base in internal SRAM
3)  Shared data in host DRAM

.. _`scd_mem_lower_bound.initialization`:

Initialization
--------------


When loading, driver should allocate memory for:
1)  16 TFD circular buffers, each with space for (typically) 256 TFDs.
2)  16 Byte Count circular buffers in 16 KBytes contiguous memory
(1024 bytes for each queue).

After receiving "Alive" response from uCode, driver must initialize
the scheduler (especially for queue #4/#9, the command queue, otherwise
the driver can't issue commands!):

.. _`scd_win_size`:

SCD_WIN_SIZE
============

.. c:function::  SCD_WIN_SIZE()

    can keep track of at one time when creating block-ack chains of frames. Note that "64" matches the number of ack bits in a block-ack packet.

.. This file was automatic generated / don't edit.

