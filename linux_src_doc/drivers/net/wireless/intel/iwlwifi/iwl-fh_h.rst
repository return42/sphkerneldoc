.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-fh.h

.. _`fh_mem_lower_bound`:

FH_MEM_LOWER_BOUND
==================

.. c:function::  FH_MEM_LOWER_BOUND()

    Addresses are offsets from device's PCI hardware base address.

.. _`fh_kw_mem_addr_reg`:

FH_KW_MEM_ADDR_REG
==================

.. c:function::  FH_KW_MEM_ADDR_REG()

    Warm (KW) buffer base address.

.. _`fh_kw_mem_addr_reg.description`:

Description
-----------

Driver must allocate a 4KByte buffer that is for keeping the
host DRAM powered on (via dummy accesses to DRAM) to maintain low-latency
DRAM access when doing Txing or Rxing.  The dummy accesses prevent host
from going into a power-savings mode that would cause higher DRAM latency,
and possible data over/under-runs, before all Tx/Rx is complete.

Driver loads FH_KW_MEM_ADDR_REG with the physical address (bits 35:4)
of the buffer, which must be 4K aligned.  Once this is set up, the device
automatically invokes keep-warm accesses when normal accesses might not
be sufficient to maintain fast DRAM response.

.. _`fh_kw_mem_addr_reg.bit-fields`:

Bit fields
----------

31-0:  Keep-warm buffer physical base address [35:4], must be 4K aligned

.. _`fh_mem_cbbc_0_15_lower_bound`:

FH_MEM_CBBC_0_15_LOWER_BOUND
============================

.. c:function::  FH_MEM_CBBC_0_15_LOWER_BOUND()

.. _`fh_mem_cbbc_0_15_lower_bound.description`:

Description
-----------

Device has 16 base pointer registers, one for each of 16 host-DRAM-resident
circular buffers (CBs/queues) containing Transmit Frame Descriptors (TFDs)
(see struct iwl_tfd_frame).  These 16 pointer registers are offset by 0x04
bytes from one another.  Each TFD circular buffer in DRAM must be 256-byte
aligned (address bits 0-7 must be 0).
Later devices have 20 (5000 series) or 30 (higher) queues, but the registers
for them are in different places.

.. _`fh_mem_cbbc_0_15_lower_bound.bit-fields-in-each-pointer-register`:

Bit fields in each pointer register
-----------------------------------

27-0: TFD CB physical base address [35:8], must be 256-byte aligned

.. _`fh_mem_rscsr_lower_bound`:

FH_MEM_RSCSR_LOWER_BOUND
========================

.. c:function::  FH_MEM_RSCSR_LOWER_BOUND()

.. _`fh_mem_rscsr_lower_bound.description`:

Description
-----------

These registers provide handshake between driver and device for the Rx queue
(this queue handles \*all\* command responses, notifications, Rx data, etc.
sent from uCode to host driver).  Unlike Tx, there is only one Rx
queue, and only one Rx DMA/FIFO channel.  Also unlike Tx, which can
concatenate up to 20 DRAM buffers to form a Tx frame, each Receive Buffer
Descriptor (RBD) points to only one Rx Buffer (RB); there is a 1:1
mapping between RBDs and RBs.

Driver must allocate host DRAM memory for the following, and set the

.. _`fh_mem_rscsr_lower_bound.physical-address-of-each-into-device-registers`:

physical address of each into device registers
----------------------------------------------


1)  Receive Buffer Descriptor (RBD) circular buffer (CB), typically with 256
entries (although any power of 2, up to 4096, is selectable by driver).
Each entry (1 dword) points to a receive buffer (RB) of consistent size
(typically 4K, although 8K or 16K are also selectable by driver).
Driver sets up RB size and number of RBDs in the CB via Rx config
register FH_MEM_RCSR_CHNL0_CONFIG_REG.

.. _`fh_mem_rscsr_lower_bound.bit-fields-within-one-rbd`:

Bit fields within one RBD
-------------------------

27-0:  Receive Buffer physical address bits [35:8], 256-byte aligned

Driver sets physical address [35:8] of base of RBD circular buffer
into FH_RSCSR_CHNL0_RBDCB_BASE_REG [27:0].

2)  Rx status buffer, 8 bytes, in which uCode indicates which Rx Buffers
(RBs) have been filled, via a "write pointer", actually the index of
the RB's corresponding RBD within the circular buffer.  Driver sets
physical address [35:4] into FH_RSCSR_CHNL0_STTS_WPTR_REG [31:0].

Bit fields in lower dword of Rx status buffer (upper dword not used

.. _`fh_mem_rscsr_lower_bound.by-driver`:

by driver
---------

31-12:  Not used by driver
11- 0:  Index of last filled Rx buffer descriptor
(device writes, driver reads this value)

As the driver prepares Receive Buffers (RBs) for device to fill, driver must
enter pointers to these RBs into contiguous RBD circular buffer entries,
and update the device's "write" index register,
FH_RSCSR_CHNL0_RBDCB_WPTR_REG.

This "write" index corresponds to the \*next\* RBD that the driver will make
available, i.e. one RBD past the tail of the ready-to-fill RBDs within
the circular buffer.  This value should initially be 0 (before preparing any
RBs), should be 8 after preparing the first 8 RBs (for example), and must
wrap back to 0 at the end of the circular buffer (but don't wrap before
"read" index has advanced past 1!  See below).

.. _`fh_mem_rscsr_lower_bound.note`:

NOTE
----

DEVICE EXPECTS THE WRITE INDEX TO BE INCREMENTED IN MULTIPLES OF 8.

As the device fills RBs (referenced from contiguous RBDs within the circular
buffer), it updates the Rx status buffer in host DRAM, 2) described above,
to tell the driver the index of the latest filled RBD.  The driver must
read this "read" index from DRAM after receiving an Rx interrupt from device

The driver must also internally keep track of a third index, which is the
next RBD to process.  When receiving an Rx interrupt, driver should process
all filled but unprocessed RBs up to, but not including, the RB
corresponding to the "read" index.  For example, if "read" index becomes "1",
driver may process the RB pointed to by RBD 0.  Depending on volume of
traffic, there may be many RBs to process.

If read index == write index, device thinks there is no room to put new data.
Due to this, the maximum number of filled RBs is 255, instead of 256.  To
be safe, make sure that there is a gap of at least 2 RBDs between "write"
and "read" indexes; that is, make sure that there are no more than 254
buffers waiting to be filled.

.. _`fh_rscsr_chnl0_stts_wptr_reg`:

FH_RSCSR_CHNL0_STTS_WPTR_REG
============================

.. c:function::  FH_RSCSR_CHNL0_STTS_WPTR_REG()

    byte Rx Status buffer.

.. _`fh_rscsr_chnl0_stts_wptr_reg.bit-fields`:

Bit fields
----------

31-0: Rx status buffer physical base address [35:4], must 16-byte aligned.

.. _`fh_rscsr_chnl0_rbdcb_base_reg`:

FH_RSCSR_CHNL0_RBDCB_BASE_REG
=============================

.. c:function::  FH_RSCSR_CHNL0_RBDCB_BASE_REG()

.. _`fh_rscsr_chnl0_rbdcb_base_reg.bit-fields`:

Bit fields
----------

27-0:  RBD CD physical base address [35:8], must be 256-byte aligned.

.. _`fh_rscsr_chnl0_rbdcb_wptr_reg`:

FH_RSCSR_CHNL0_RBDCB_WPTR_REG
=============================

.. c:function::  FH_RSCSR_CHNL0_RBDCB_WPTR_REG()

.. _`fh_rscsr_chnl0_rbdcb_wptr_reg.bit-fields`:

Bit fields
----------

11-0:  Index of driver's most recent prepared-to-be-filled RBD, + 1.
NOTE:  For 256-entry circular buffer, use only bits [7:0].

.. _`fh_mem_rcsr_lower_bound`:

FH_MEM_RCSR_LOWER_BOUND
=======================

.. c:function::  FH_MEM_RCSR_LOWER_BOUND()

    Rx Config Reg for channel 0 (only channel used)

.. _`fh_mem_rcsr_lower_bound.description`:

Description
-----------

Driver must initialize FH_MEM_RCSR_CHNL0_CONFIG_REG as follows for
normal operation (see bit fields).

Clearing FH_MEM_RCSR_CHNL0_CONFIG_REG to 0 turns off Rx DMA.
Driver should poll FH_MEM_RSSR_RX_STATUS_REG for
FH_RSSR_CHNL0_RX_STATUS_CHNL_IDLE (bit 24) before continuing.

.. _`fh_mem_rcsr_lower_bound.bit-fields`:

Bit fields
----------

31-30: Rx DMA channel enable: '00' off/pause, '01' pause at end of frame,
'10' operate normally
29-24: reserved
23-20: # RBDs in circular buffer = 2^value; use "8" for 256 RBDs (normal),
min "5" for 32 RBDs, max "12" for 4096 RBDs.
19-18: reserved
17-16: size of each receive buffer; '00' 4K (normal), '01' 8K,
'10' 12K, '11' 16K.
15-14: reserved
13-12: IRQ destination; '00' none, '01' host driver (normal operation)
11- 4: timeout for closing Rx buffer and interrupting host (units 32 usec)
typical value 0x10 (about 1/2 msec)
3- 0: reserved

.. _`fh_mem_rssr_lower_bound`:

FH_MEM_RSSR_LOWER_BOUND
=======================

.. c:function::  FH_MEM_RSSR_LOWER_BOUND()

.. _`fh_mem_rssr_lower_bound.description`:

Description
-----------

After stopping Rx DMA channel (writing 0 to
FH_MEM_RCSR_CHNL0_CONFIG_REG), driver must poll
FH_MEM_RSSR_RX_STATUS_REG until Rx channel is idle.

.. _`fh_mem_rssr_lower_bound.bit-fields`:

Bit fields
----------

24:  1 = Channel 0 is idle

FH_MEM_RSSR_SHARED_CTRL_REG and FH_MEM_RSSR_RX_ENABLE_ERR_IRQ2DRV
contain default values that should not be altered by the driver.

.. _`rfh_gen_status`:

RFH_GEN_STATUS
==============

.. c:function::  RFH_GEN_STATUS()

.. _`rfh_gen_status.bit-29`:

Bit 29
------

RBD_FETCH_IDLE
This status flag is set by the RFH when there is no active RBD fetch from
DRAM.
Once the RFH RBD controller starts fetching (or when there is a pending
RBD read response from DRAM), this flag is immediately turned off.

.. _`rfh_gen_status.bit-30`:

Bit 30
------

SRAM_DMA_IDLE
This status flag is set by the RFH when there is no active transaction from
SRAM to DRAM.
Once the SRAM to DRAM DMA is active, this flag is immediately turned off.

.. _`rfh_gen_status.bit-31`:

Bit 31
------

RXF_DMA_IDLE
This status flag is set by the RFH when there is no active transaction from
RXF to DRAM.
Once the RXF-to-DRAM DMA is active, this flag is immediately turned off.

.. _`fh_tcsr_lower_bound`:

FH_TCSR_LOWER_BOUND
===================

.. c:function::  FH_TCSR_LOWER_BOUND()

.. _`fh_tcsr_lower_bound.description`:

Description
-----------

Device has one configuration register for each of 8 Tx DMA/FIFO channels
supported in hardware (don't confuse these with the 16 Tx queues in DRAM,
which feed the DMA/FIFO channels); config regs are separated by 0x20 bytes.

To use a Tx DMA channel, driver must initialize its
FH_TCSR_CHNL_TX_CONFIG_REG(chnl) with:

FH_TCSR_TX_CONFIG_REG_VAL_DMA_CHNL_ENABLE \|
FH_TCSR_TX_CONFIG_REG_VAL_DMA_CREDIT_ENABLE_VAL

All other bits should be 0.

.. _`fh_tcsr_lower_bound.bit-fields`:

Bit fields
----------

31-30: Tx DMA channel enable: '00' off/pause, '01' pause at end of frame,
'10' operate normally
29- 4: Reserved, set to "0"
3: Enable internal DMA requests (1, normal operation), disable (0)
2- 0: Reserved, set to "0"

.. _`fh_tssr_lower_bound`:

FH_TSSR_LOWER_BOUND
===================

.. c:function::  FH_TSSR_LOWER_BOUND()

.. _`fh_tssr_lower_bound.description`:

Description
-----------

After stopping Tx DMA channel (writing 0 to
FH_TCSR_CHNL_TX_CONFIG_REG(chnl)), driver must poll
FH_TSSR_TX_STATUS_REG until selected Tx channel is idle
(channel's buffers empty \| no pending requests).

.. _`fh_tssr_lower_bound.bit-fields`:

Bit fields
----------

31-24:  1 = Channel buffers empty (channel 7:0)
23-16:  1 = No pending requests (channel 7:0)

.. _`fh_tssr_tx_error_reg`:

FH_TSSR_TX_ERROR_REG
====================

.. c:function::  FH_TSSR_TX_ERROR_REG()

    31:  Indicates an address error when accessed to internal memory uCode/driver must write "1" in order to clear this flag 30:  Indicates that Host did not send the expected number of dwords to FH uCode/driver must write "1" in order to clear this flag 16-9:Each status bit is for one channel. Indicates that an (Error) ActDMA command was received from the scheduler while the TRB was already full with previous command uCode/driver must write "1" in order to clear this flag 7-0: Each status bit indicates a channel's TxCredit error. When an error bit is set, it indicates that the FH has received a full indication from the RTC TxFIFO and the current value of the TxCredit counter was not equal to zero. This mean that the credit mechanism was not synchronized to the TxFIFO status uCode/driver must write "1" in order to clear this flag

.. _`iwl_rb_status`:

struct iwl_rb_status
====================

.. c:type:: struct iwl_rb_status

    reserve buffer status host memory mapped FH registers

.. _`iwl_rb_status.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rb_status {
        __le16 closed_rb_num;
        __le16 closed_fr_num;
        __le16 finished_rb_num;
        __le16 finished_fr_nam;
        __le32 __unused;
    }

.. _`iwl_rb_status.members`:

Members
-------

closed_rb_num
    11] - Indicates the index of the RB which was closed

closed_fr_num
    11] - Indicates the index of the RX Frame which was closed

finished_rb_num
    11] - Indicates the index of the current RB
    in which the last frame was written to

finished_fr_nam
    *undescribed*

\__unused
    *undescribed*

.. _`iwl_tfd_tb_hi_n_len`:

enum iwl_tfd_tb_hi_n_len
========================

.. c:type:: enum iwl_tfd_tb_hi_n_len

    TB hi_n_len bits

.. _`iwl_tfd_tb_hi_n_len.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tfd_tb_hi_n_len {
        TB_HI_N_LEN_ADDR_HI_MSK,
        TB_HI_N_LEN_LEN_MSK
    };

.. _`iwl_tfd_tb_hi_n_len.constants`:

Constants
---------

TB_HI_N_LEN_ADDR_HI_MSK
    high 4 bits (to make it 36) of DMA address

TB_HI_N_LEN_LEN_MSK
    length of the TB

.. _`iwl_tfd_tb`:

struct iwl_tfd_tb
=================

.. c:type:: struct iwl_tfd_tb


.. _`iwl_tfd_tb.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tfd_tb {
        __le32 lo;
        __le16 hi_n_len;
    }

.. _`iwl_tfd_tb.members`:

Members
-------

lo
    low [31:0] portion of the dma address of TX buffer
    every even is unaligned on 16 bit boundary

hi_n_len
    \ :c:type:`enum iwl_tfd_tb_hi_n_len <iwl_tfd_tb_hi_n_len>`\ 

.. _`iwl_tfd_tb.description`:

Description
-----------

This structure contains dma address and length of transmission address

.. _`iwl_tfh_tb`:

struct iwl_tfh_tb
=================

.. c:type:: struct iwl_tfh_tb


.. _`iwl_tfh_tb.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tfh_tb {
        __le16 tb_len;
        __le64 addr;
    }

.. _`iwl_tfh_tb.members`:

Members
-------

tb_len
    *undescribed*

addr
    *undescribed*

.. _`iwl_tfh_tb.description`:

Description
-----------

This structure contains dma address and length of transmission address

\ ``tb_len``\  length of the tx buffer
\ ``addr``\  64 bits dma address

.. _`iwl_tfh_tfd`:

struct iwl_tfh_tfd
==================

.. c:type:: struct iwl_tfh_tfd

    Transmit Frame Descriptor (TFD) \ ````\  num_tbs 0-4 number of active tbs 5 -15   reserved \ ````\  tbs[25]    transmit frame buffer descriptors \ ````\  \__pad      padding

.. _`iwl_tfh_tfd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tfh_tfd {
        __le16 num_tbs;
        struct iwl_tfh_tb tbs[IWL_TFH_NUM_TBS];
        __le32 __pad;
    }

.. _`iwl_tfh_tfd.members`:

Members
-------

num_tbs
    *undescribed*

tbs
    *undescribed*

\__pad
    *undescribed*

.. _`iwlagn_scd_bc_tbl`:

struct iwlagn_scd_bc_tbl
========================

.. c:type:: struct iwlagn_scd_bc_tbl

    base physical address provided by SCD_DRAM_BASE_ADDR

.. _`iwlagn_scd_bc_tbl.definition`:

Definition
----------

.. code-block:: c

    struct iwlagn_scd_bc_tbl {
        __le16 tfd_offset[TFD_QUEUE_BC_SIZE];
    }

.. _`iwlagn_scd_bc_tbl.members`:

Members
-------

tfd_offset
    *undescribed*

.. _`iwlagn_scd_bc_tbl.for-devices-up-to-22000`:

For devices up to 22000
-----------------------

\ ``tfd_offset``\   0-12 - tx command byte count
12-16 - station index

.. _`iwlagn_scd_bc_tbl.for-22000-and-on`:

For 22000 and on
----------------

\ ``tfd_offset``\   0-12 - tx command byte count
12-13 - number of 64 byte chunks
14-16 - reserved

.. This file was automatic generated / don't edit.

