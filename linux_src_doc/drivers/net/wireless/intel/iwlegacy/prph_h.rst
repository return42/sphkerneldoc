.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlegacy/prph.h

.. _`bsm_wr_ctrl_reg_bit_start`:

BSM_WR_CTRL_REG_BIT_START
=========================

.. c:function::  BSM_WR_CTRL_REG_BIT_START()

.. _`bsm_wr_ctrl_reg_bit_start.description`:

Description
-----------

The Bootstrap State Machine (BSM) stores a short bootstrap uCode program
in special SRAM that does not power down when the embedded control
processor is sleeping (e.g. for periodic power-saving shutdowns of radio).

When powering back up after sleeps (or during initial uCode load), the BSM
internally loads the short bootstrap program from the special SRAM into the
embedded processor's instruction SRAM, and starts the processor so it runs
the bootstrap program.

This bootstrap program loads (via PCI busmaster DMA) instructions and data
images for a uCode program from host DRAM locations.  The host driver
indicates DRAM locations and sizes for instruction and data images via the
four BSM_DRAM\_\* registers.  Once the bootstrap program loads the new program,
the new program starts automatically.

The uCode used for open-source drivers includes two programs:

1)  Initialization -- performs hardware calibration and sets up some
internal data, then notifies host via "initialize alive" notification
(struct il_init_alive_resp) that it has completed all of its work.
After signal from host, it then loads and starts the runtime program.
The initialization program must be used when initially setting up the
NIC after loading the driver.

2)  Runtime/Protocol -- performs all normal runtime operations.  This
notifies host via "alive" notification (struct il_alive_resp) that it
is ready to be used.

When initializing the NIC, the host driver does the following procedure:

1)  Load bootstrap program (instructions only, no data image for bootstrap)
into bootstrap memory.  Use dword writes starting at BSM_SRAM_LOWER_BOUND

2)  Point (via BSM_DRAM\_\*) to the "initialize" uCode data and instruction
images in host DRAM.

3)  Set up BSM to copy from BSM SRAM into uCode instruction SRAM when asked:
BSM_WR_MEM_SRC_REG = 0
BSM_WR_MEM_DST_REG = RTC_INST_LOWER_BOUND
BSM_WR_MEM_DWCOUNT_REG = # dwords in bootstrap instruction image

4)  Load bootstrap into instruction SRAM:
BSM_WR_CTRL_REG = BSM_WR_CTRL_REG_BIT_START

5)  Wait for load completion:
Poll BSM_WR_CTRL_REG for BSM_WR_CTRL_REG_BIT_START = 0

6)  Enable future boot loads whenever NIC's power management triggers it:
BSM_WR_CTRL_REG = BSM_WR_CTRL_REG_BIT_START_EN

7)  Start the NIC by removing all reset bits:
CSR_RESET = 0

The bootstrap uCode (already in instruction SRAM) loads initialization
uCode.  Initialization uCode performs data initialization, sends
"initialize alive" notification to host, and waits for a signal from
host to load runtime code.

4)  Point (via BSM_DRAM\_\*) to the "runtime" uCode data and instruction
images in host DRAM.  The last register loaded must be the instruction
byte count register ("1" in MSbit tells initialization uCode to load
the runtime uCode):
BSM_DRAM_INST_BYTECOUNT_REG = byte count \| BSM_DRAM_INST_LOAD

5)  Wait for "alive" notification, then issue normal runtime commands.

Data caching during power-downs:

Just before the embedded controller powers down (e.g for automatic
power-saving modes, or for RFKILL), uCode stores (via PCI busmaster DMA)
a current snapshot of the embedded processor's data SRAM into host DRAM.
This caches the data while the embedded processor's memory is powered down.
Location and size are controlled by BSM_DRAM_DATA\_\* registers.

.. _`bsm_wr_ctrl_reg_bit_start.note`:

NOTE
----

Instruction SRAM does not need to be saved, since that doesn't
change during operation; the original image (from uCode distribution
file) can be used for reload.

When powering back up, the BSM loads the bootstrap program.  Bootstrap looks
at the BSM_DRAM\_\* registers, which now point to the runtime instruction
image and the cached (modified) runtime data (\*not\* the initialization
uCode).  Bootstrap reloads these runtime images into SRAM, and restarts the
uCode from where it left off before the power-down.

Initialization uCode does \*not\* run as part of the save/restore
procedure.

This save/restore method is mostly for autonomous power management during
normal operation (result of C_POWER_TBL).  Platform suspend/resume and
RFKILL should use complete restarts (with total re-initialization) of uCode,
allowing total shutdown (including BSM memory).

Note that, during normal operation, the host DRAM that held the initial
startup data for the runtime code is now being used as a backup data cache
for modified data!  If you need to completely re-initialize the NIC, make
sure that you use the runtime data image from the uCode distribution file,
not the modified/saved runtime data.  You may want to store a separate
"clean" runtime data image in DRAM to avoid disk reads of distribution file.

.. _`scd_win_size`:

SCD_WIN_SIZE
============

.. c:function::  SCD_WIN_SIZE()

.. _`scd_win_size.description`:

Description
-----------

The Tx Scheduler selects the next frame to be transmitted, choosing TFDs
(Transmit Frame Descriptors) from up to 16 circular Tx queues resident in
host DRAM.  It steers each frame's Tx command (which contains the frame
data) into one of up to 7 prioritized Tx DMA FIFO channels within the
device.  A queue maps to only one (selectable by driver) Tx DMA channel,
but one DMA channel may take input from several queues.

Tx DMA FIFOs have dedicated purposes.  For 4965, they are used as follows
(cf. default_queue_to_tx_fifo in 4965.c):

0 -- EDCA BK (background) frames, lowest priority
1 -- EDCA BE (best effort) frames, normal priority
2 -- EDCA VI (video) frames, higher priority
3 -- EDCA VO (voice) and management frames, highest priority
4 -- Commands (e.g. RXON, etc.)
5 -- unused (HCCA)
6 -- unused (HCCA)
7 -- not used by driver (device-internal only)


Driver should normally map queues 0-6 to Tx DMA/FIFO channels 0-6.
In addition, driver can map the remaining queues to Tx DMA/FIFO
channels 0-3 to support 11n aggregation via EDCA DMA channels.

.. _`scd_win_size.the-driver-sets-up-each-queue-to-work-in-one-of-two-modes`:

The driver sets up each queue to work in one of two modes
---------------------------------------------------------


1)  Scheduler-Ack, in which the scheduler automatically supports a
block-ack (BA) win of up to 64 TFDs.  In this mode, each queue
contains TFDs for a unique combination of Recipient Address (RA)
and Traffic Identifier (TID), that is, traffic of a given
Quality-Of-Service (QOS) priority, destined for a single station.

In scheduler-ack mode, the scheduler keeps track of the Tx status of
each frame within the BA win, including whether it's been transmitted,
and whether it's been acknowledged by the receiving station.  The device
automatically processes block-acks received from the receiving STA,
and reschedules un-acked frames to be retransmitted (successful
Tx completion may end up being out-of-order).

The driver must maintain the queue's Byte Count table in host DRAM
(struct il4965_sched_queue_byte_cnt_tbl) for this mode.
This mode does not support fragmentation.

2)  FIFO (a.k.a. non-Scheduler-ACK), in which each TFD is processed in order.
The device may automatically retry Tx, but will retry only one frame
at a time, until receiving ACK from receiving station, or reaching
retry limit and giving up.

The command queue (#4/#9) must use this mode!
This mode does not require use of the Byte Count table in host DRAM.

.. _`scd_win_size.driver-controls-scheduler-operation-via-3-means`:

Driver controls scheduler operation via 3 means
-----------------------------------------------

1)  Scheduler registers
2)  Shared scheduler data base in internal 4956 SRAM
3)  Shared data in host DRAM

.. _`scd_win_size.initialization`:

Initialization
--------------


When loading, driver should allocate memory for:
1)  16 TFD circular buffers, each with space for (typically) 256 TFDs.
2)  16 Byte Count circular buffers in 16 KBytes contiguous memory
(1024 bytes for each queue).

After receiving "Alive" response from uCode, driver must initialize
the scheduler (especially for queue #4/#9, the command queue, otherwise
the driver can't issue commands!):

.. _`il49_scd_context_data_offset`:

IL49_SCD_CONTEXT_DATA_OFFSET
============================

.. c:function::  IL49_SCD_CONTEXT_DATA_OFFSET()

.. _`il49_scd_context_data_offset.description`:

Description
-----------

Driver should clear and initialize the following areas after receiving
"Alive" response from 4965 uCode, i.e. after initial
uCode load, or after a uCode load done for error recovery:

SCD_CONTEXT_DATA_OFFSET (size 128 bytes)
SCD_TX_STTS_BITMAP_OFFSET (size 256 bytes)
SCD_TRANSLATE_TBL_OFFSET (size 32 bytes)

Driver accesses SRAM via HBUS_TARG_MEM\_\* registers.
Driver reads base address of this scheduler area from SCD_SRAM_BASE_ADDR.
All OFFSET values must be added to this base address.

.. This file was automatic generated / don't edit.

