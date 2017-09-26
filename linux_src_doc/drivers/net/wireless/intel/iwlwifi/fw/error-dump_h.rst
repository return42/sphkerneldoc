.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/error-dump.h

.. _`iwl_fw_error_dump_type`:

enum iwl_fw_error_dump_type
===========================

.. c:type:: enum iwl_fw_error_dump_type

    types of data in the dump file

.. _`iwl_fw_error_dump_type.definition`:

Definition
----------

.. code-block:: c

    enum iwl_fw_error_dump_type {
        IWL_FW_ERROR_DUMP_CSR,
        IWL_FW_ERROR_DUMP_RXF,
        IWL_FW_ERROR_DUMP_TXCMD,
        IWL_FW_ERROR_DUMP_DEV_FW_INFO,
        IWL_FW_ERROR_DUMP_FW_MONITOR,
        IWL_FW_ERROR_DUMP_PRPH,
        IWL_FW_ERROR_DUMP_TXF,
        IWL_FW_ERROR_DUMP_FH_REGS,
        IWL_FW_ERROR_DUMP_MEM,
        IWL_FW_ERROR_DUMP_ERROR_INFO,
        IWL_FW_ERROR_DUMP_RB,
        IWL_FW_ERROR_DUMP_PAGING,
        IWL_FW_ERROR_DUMP_RADIO_REG,
        IWL_FW_ERROR_DUMP_INTERNAL_TXF,
        IWL_FW_ERROR_DUMP_EXTERNAL,
        IWL_FW_ERROR_DUMP_MEM_CFG,
        IWL_FW_ERROR_DUMP_MAX
    };

.. _`iwl_fw_error_dump_type.constants`:

Constants
---------

IWL_FW_ERROR_DUMP_CSR
    Control Status Registers - from offset 0

IWL_FW_ERROR_DUMP_RXF
    *undescribed*

IWL_FW_ERROR_DUMP_TXCMD
    last TX command data, structured as
    \ :c:type:`struct iwl_fw_error_dump_txcmd <iwl_fw_error_dump_txcmd>`\  packets

IWL_FW_ERROR_DUMP_DEV_FW_INFO
    struct \ ``iwl_fw_error_dump_info``\ 
    info on the device / firmware.

IWL_FW_ERROR_DUMP_FW_MONITOR
    firmware monitor

IWL_FW_ERROR_DUMP_PRPH
    range of periphery registers - there can be several
    sections like this in a single file.

IWL_FW_ERROR_DUMP_TXF
    *undescribed*

IWL_FW_ERROR_DUMP_FH_REGS
    range of FH registers

IWL_FW_ERROR_DUMP_MEM
    chunk of memory

IWL_FW_ERROR_DUMP_ERROR_INFO
    description of what triggered this dump.
    Structured as \ :c:type:`struct iwl_fw_error_dump_trigger_desc <iwl_fw_error_dump_trigger_desc>`\ .

IWL_FW_ERROR_DUMP_RB
    the content of an RB structured as
    \ :c:type:`struct iwl_fw_error_dump_rb <iwl_fw_error_dump_rb>`\ 

IWL_FW_ERROR_DUMP_PAGING
    *undescribed*

IWL_FW_ERROR_DUMP_RADIO_REG
    Dump the radio registers.

IWL_FW_ERROR_DUMP_INTERNAL_TXF
    *undescribed*

IWL_FW_ERROR_DUMP_EXTERNAL
    used only by external code utilities, and
    for that reason is not in use in any other place in the Linux Wi-Fi
    stack.

IWL_FW_ERROR_DUMP_MEM_CFG
    the addresses and sizes of fifos in the smem,
    which we get from the fw after ALIVE. The content is structured as
    \ :c:type:`struct iwl_fw_error_dump_smem_cfg <iwl_fw_error_dump_smem_cfg>`\ .

IWL_FW_ERROR_DUMP_MAX
    *undescribed*

.. _`iwl_fw_error_dump_data`:

struct iwl_fw_error_dump_data
=============================

.. c:type:: struct iwl_fw_error_dump_data

    data for one type

.. _`iwl_fw_error_dump_data.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_error_dump_data {
        __le32 type;
        __le32 len;
        __u8 data[];
    }

.. _`iwl_fw_error_dump_data.members`:

Members
-------

type
    &enum iwl_fw_error_dump_type

len
    the length starting from \ ``data``\ 

data
    the data itself

.. _`iwl_fw_error_dump_file`:

struct iwl_fw_error_dump_file
=============================

.. c:type:: struct iwl_fw_error_dump_file

    the layout of the header of the file

.. _`iwl_fw_error_dump_file.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_error_dump_file {
        __le32 barker;
        __le32 file_len;
        u8 data[0];
    }

.. _`iwl_fw_error_dump_file.members`:

Members
-------

barker
    must be \ ``IWL_FW_ERROR_DUMP_BARKER``\ 

file_len
    the length of all the file starting from \ ``barker``\ 

data
    array of \ :c:type:`struct iwl_fw_error_dump_data <iwl_fw_error_dump_data>`\ 

.. _`iwl_fw_error_dump_txcmd`:

struct iwl_fw_error_dump_txcmd
==============================

.. c:type:: struct iwl_fw_error_dump_txcmd

    TX command data

.. _`iwl_fw_error_dump_txcmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_error_dump_txcmd {
        __le32 cmdlen;
        __le32 caplen;
        u8 data[];
    }

.. _`iwl_fw_error_dump_txcmd.members`:

Members
-------

cmdlen
    original length of command

caplen
    captured length of command (may be less)

data
    captured command data, \ ``caplen``\  bytes

.. _`iwl_fw_error_dump_fifo`:

struct iwl_fw_error_dump_fifo
=============================

.. c:type:: struct iwl_fw_error_dump_fifo

    RX/TX FIFO data

.. _`iwl_fw_error_dump_fifo.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_error_dump_fifo {
        __le32 fifo_num;
        __le32 available_bytes;
        __le32 wr_ptr;
        __le32 rd_ptr;
        __le32 fence_ptr;
        __le32 fence_mode;
        u8 data[];
    }

.. _`iwl_fw_error_dump_fifo.members`:

Members
-------

fifo_num
    number of FIFO (starting from 0)

available_bytes
    num of bytes available in FIFO (may be less than FIFO size)

wr_ptr
    position of write pointer

rd_ptr
    position of read pointer

fence_ptr
    position of fence pointer

fence_mode
    the current mode of the fence (before locking) -
    0=follow RD pointer ; 1 = freeze

data
    all of the FIFO's data

.. _`iwl_fw_error_dump_info`:

struct iwl_fw_error_dump_info
=============================

.. c:type:: struct iwl_fw_error_dump_info

    info on the device / firmware

.. _`iwl_fw_error_dump_info.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_error_dump_info {
        __le32 device_family;
        __le32 hw_step;
        u8 fw_human_readable[FW_VER_HUMAN_READABLE_SZ];
        u8 dev_human_readable[64];
        u8 bus_human_readable[8];
    }

.. _`iwl_fw_error_dump_info.members`:

Members
-------

device_family
    the family of the device (7 / 8)

hw_step
    the step of the device

fw_human_readable
    human readable FW version

dev_human_readable
    name of the device

bus_human_readable
    name of the bus used

.. _`iwl_fw_error_dump_fw_mon`:

struct iwl_fw_error_dump_fw_mon
===============================

.. c:type:: struct iwl_fw_error_dump_fw_mon

    FW monitor data

.. _`iwl_fw_error_dump_fw_mon.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_error_dump_fw_mon {
        __le32 fw_mon_wr_ptr;
        __le32 fw_mon_base_ptr;
        __le32 fw_mon_cycle_cnt;
        __le32 reserved[3];
        u8 data[];
    }

.. _`iwl_fw_error_dump_fw_mon.members`:

Members
-------

fw_mon_wr_ptr
    the position of the write pointer in the cyclic buffer

fw_mon_base_ptr
    base pointer of the data

fw_mon_cycle_cnt
    number of wraparounds

reserved
    for future use

data
    captured data

.. _`iwl_fw_error_dump_smem_cfg`:

struct iwl_fw_error_dump_smem_cfg
=================================

.. c:type:: struct iwl_fw_error_dump_smem_cfg

    Dump SMEM configuration This must follow \ :c:type:`struct iwl_fwrt_shared_mem_cfg <iwl_fwrt_shared_mem_cfg>`\ .

.. _`iwl_fw_error_dump_smem_cfg.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_error_dump_smem_cfg {
        __le32 num_lmacs;
        __le32 num_txfifo_entries;
        struct {
            __le32 txfifo_size[TX_FIFO_MAX_NUM];
            __le32 rxfifo1_size;
        } lmac[MAX_NUM_LMAC];
        __le32 rxfifo2_size;
        __le32 internal_txfifo_addr;
        __le32 internal_txfifo_size[TX_FIFO_INTERNAL_MAX_NUM];
    }

.. _`iwl_fw_error_dump_smem_cfg.members`:

Members
-------

num_lmacs
    number of lmacs

num_txfifo_entries
    number of tx fifos

lmac
    sizes of lmacs txfifos and rxfifo1

txfifo_size
    *undescribed*

rxfifo1_size
    *undescribed*

rxfifo2_size
    size of rxfifo2

internal_txfifo_addr
    address of internal tx fifo

internal_txfifo_size
    size of internal tx fifo

.. _`iwl_fw_error_dump_prph`:

struct iwl_fw_error_dump_prph
=============================

.. c:type:: struct iwl_fw_error_dump_prph

    periphery registers data

.. _`iwl_fw_error_dump_prph.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_error_dump_prph {
        __le32 prph_start;
        __le32 data[];
    }

.. _`iwl_fw_error_dump_prph.members`:

Members
-------

prph_start
    address of the first register in this chunk

data
    the content of the registers

.. _`iwl_fw_error_dump_mem`:

struct iwl_fw_error_dump_mem
============================

.. c:type:: struct iwl_fw_error_dump_mem

    chunk of memory

.. _`iwl_fw_error_dump_mem.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_error_dump_mem {
        __le32 type;
        __le32 offset;
        u8 data[];
    }

.. _`iwl_fw_error_dump_mem.members`:

Members
-------

type
    &enum iwl_fw_error_dump_mem_type

offset
    the offset from which the memory was read

data
    the content of the memory

.. _`iwl_fw_error_dump_rb`:

struct iwl_fw_error_dump_rb
===========================

.. c:type:: struct iwl_fw_error_dump_rb

    content of an Receive Buffer

.. _`iwl_fw_error_dump_rb.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_error_dump_rb {
        __le32 index;
        __le32 rxq;
        __le32 reserved;
        u8 data[];
    }

.. _`iwl_fw_error_dump_rb.members`:

Members
-------

index
    the index of the Receive Buffer in the Rx queue

rxq
    the RB's Rx queue

reserved
    *undescribed*

data
    the content of the Receive Buffer

.. _`iwl_fw_error_dump_paging`:

struct iwl_fw_error_dump_paging
===============================

.. c:type:: struct iwl_fw_error_dump_paging

    content of the UMAC's image page block on DRAM

.. _`iwl_fw_error_dump_paging.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_error_dump_paging {
        __le32 index;
        __le32 reserved;
        u8 data[];
    }

.. _`iwl_fw_error_dump_paging.members`:

Members
-------

index
    the index of the page block

reserved
    *undescribed*

data
    the content of the page block

.. _`iwl_fw_error_next_data`:

iwl_fw_error_next_data
======================

.. c:function:: struct iwl_fw_error_dump_data *iwl_fw_error_next_data(struct iwl_fw_error_dump_data *data)

    advance fw error dump data pointer

    :param struct iwl_fw_error_dump_data \*data:
        previous data block

.. _`iwl_fw_error_next_data.return`:

Return
------

next data block

.. _`iwl_fw_dbg_trigger`:

enum iwl_fw_dbg_trigger
=======================

.. c:type:: enum iwl_fw_dbg_trigger

    triggers available

.. _`iwl_fw_dbg_trigger.definition`:

Definition
----------

.. code-block:: c

    enum iwl_fw_dbg_trigger {
        FW_DBG_TRIGGER_INVALID,
        FW_DBG_TRIGGER_USER,
        FW_DBG_TRIGGER_FW_ASSERT,
        FW_DBG_TRIGGER_MISSED_BEACONS,
        FW_DBG_TRIGGER_CHANNEL_SWITCH,
        FW_DBG_TRIGGER_FW_NOTIF,
        FW_DBG_TRIGGER_MLME,
        FW_DBG_TRIGGER_STATS,
        FW_DBG_TRIGGER_RSSI,
        FW_DBG_TRIGGER_TXQ_TIMERS,
        FW_DBG_TRIGGER_TIME_EVENT,
        FW_DBG_TRIGGER_BA,
        FW_DBG_TRIGGER_TX_LATENCY,
        FW_DBG_TRIGGER_TDLS,
        FW_DBG_TRIGGER_TX_STATUS,
        FW_DBG_TRIGGER_MAX
    };

.. _`iwl_fw_dbg_trigger.constants`:

Constants
---------

FW_DBG_TRIGGER_INVALID
    *undescribed*

FW_DBG_TRIGGER_USER
    trigger log collection by user
    This should not be defined as a trigger to the driver, but a value the
    driver should set to indicate that the trigger was initiated by the
    user.

FW_DBG_TRIGGER_FW_ASSERT
    trigger log collection when the firmware asserts

FW_DBG_TRIGGER_MISSED_BEACONS
    trigger log collection when beacons are
    missed.

FW_DBG_TRIGGER_CHANNEL_SWITCH
    trigger log collection upon channel switch.

FW_DBG_TRIGGER_FW_NOTIF
    trigger log collection when the firmware sends a
    command response or a notification.

FW_DBG_TRIGGER_MLME
    trigger log collection upon MLME event.

FW_DBG_TRIGGER_STATS
    trigger log collection upon statistics threshold.

FW_DBG_TRIGGER_RSSI
    trigger log collection when the rssi of the beacon
    goes below a threshold.

FW_DBG_TRIGGER_TXQ_TIMERS
    configures the timers for the Tx queue hang
    detection.

FW_DBG_TRIGGER_TIME_EVENT
    trigger log collection upon time events related
    events.

FW_DBG_TRIGGER_BA
    trigger log collection upon BlockAck related events.

FW_DBG_TRIGGER_TX_LATENCY
    *undescribed*

FW_DBG_TRIGGER_TDLS
    *undescribed*

FW_DBG_TRIGGER_TX_STATUS
    trigger log collection upon tx status when
    the firmware sends a tx reply.

FW_DBG_TRIGGER_MAX
    *undescribed*

.. _`iwl_fw_error_dump_trigger_desc`:

struct iwl_fw_error_dump_trigger_desc
=====================================

.. c:type:: struct iwl_fw_error_dump_trigger_desc

    describes the trigger condition

.. _`iwl_fw_error_dump_trigger_desc.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_error_dump_trigger_desc {
        __le32 type;
        u8 data[];
    }

.. _`iwl_fw_error_dump_trigger_desc.members`:

Members
-------

type
    &enum iwl_fw_dbg_trigger

data
    raw data about what happened

.. This file was automatic generated / don't edit.

