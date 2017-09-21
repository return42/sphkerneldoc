.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/debug.h

.. _`iwl_debug_cmds`:

enum iwl_debug_cmds
===================

.. c:type:: enum iwl_debug_cmds

    debug commands

.. _`iwl_debug_cmds.definition`:

Definition
----------

.. code-block:: c

    enum iwl_debug_cmds {
        LMAC_RD_WR,
        UMAC_RD_WR,
        MFU_ASSERT_DUMP_NTF
    };

.. _`iwl_debug_cmds.constants`:

Constants
---------

LMAC_RD_WR
    LMAC memory read/write, using \ :c:type:`struct iwl_dbg_mem_access_cmd <iwl_dbg_mem_access_cmd>`\  and
    \ :c:type:`struct iwl_dbg_mem_access_rsp <iwl_dbg_mem_access_rsp>`\ 

UMAC_RD_WR
    UMAC memory read/write, using \ :c:type:`struct iwl_dbg_mem_access_cmd <iwl_dbg_mem_access_cmd>`\  and
    \ :c:type:`struct iwl_dbg_mem_access_rsp <iwl_dbg_mem_access_rsp>`\ 

MFU_ASSERT_DUMP_NTF
    &struct iwl_mfu_assert_dump_notif

.. _`iwl_error_resp`:

struct iwl_error_resp
=====================

.. c:type:: struct iwl_error_resp

    FW error indication ( REPLY_ERROR = 0x2 )

.. _`iwl_error_resp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_error_resp {
        __le32 error_type;
        u8 cmd_id;
        u8 reserved1;
        __le16 bad_cmd_seq_num;
        __le32 error_service;
        __le64 timestamp;
    }

.. _`iwl_error_resp.members`:

Members
-------

error_type
    one of FW_ERR\_\*

cmd_id
    the command ID for which the error occurred

reserved1
    reserved

bad_cmd_seq_num
    sequence number of the erroneous command

error_service
    which service created the error, applicable only if
    error_type = 2, otherwise 0

timestamp
    TSF in usecs.

.. _`iwl_shared_mem_cfg_v2`:

struct iwl_shared_mem_cfg_v2
============================

.. c:type:: struct iwl_shared_mem_cfg_v2

    Shared memory configuration information

.. _`iwl_shared_mem_cfg_v2.definition`:

Definition
----------

.. code-block:: c

    struct iwl_shared_mem_cfg_v2 {
        __le32 shared_mem_addr;
        __le32 shared_mem_size;
        __le32 sample_buff_addr;
        __le32 sample_buff_size;
        __le32 txfifo_addr;
        __le32 txfifo_size;
        __le32 rxfifo_size;
        __le32 page_buff_addr;
        __le32 page_buff_size;
        __le32 rxfifo_addr;
        __le32 internal_txfifo_addr;
        __le32 internal_txfifo_size;
    }

.. _`iwl_shared_mem_cfg_v2.members`:

Members
-------

shared_mem_addr
    shared memory addr (pre 8000 HW set to 0x0 as MARBH is not
    accessible)

shared_mem_size
    shared memory size

sample_buff_addr
    internal sample (mon/adc) buff addr (pre 8000 HW set to
    0x0 as accessible only via DBGM RDAT)

sample_buff_size
    internal sample buff size

txfifo_addr
    start addr of TXF0 (excluding the context table 0.5KB), (pre
    8000 HW set to 0x0 as not accessible)

txfifo_size
    size of TXF0 ... TXF7

rxfifo_size
    RXF1, RXF2 sizes. If there is no RXF2, it'll have a value of 0

page_buff_addr
    used by UMAC and performance debug (page miss analysis),
    when paging is not supported this should be 0

page_buff_size
    size of \ ``page_buff_addr``\ 

rxfifo_addr
    Start address of rxFifo

internal_txfifo_addr
    start address of internalFifo

internal_txfifo_size
    internal fifos' size

.. _`iwl_shared_mem_cfg_v2.note`:

NOTE
----

on firmware that don't have IWL_UCODE_TLV_CAPA_EXTEND_SHARED_MEM_CFG
set, the last 3 members don't exist.

.. _`iwl_shared_mem_lmac_cfg`:

struct iwl_shared_mem_lmac_cfg
==============================

.. c:type:: struct iwl_shared_mem_lmac_cfg

    LMAC shared memory configuration

.. _`iwl_shared_mem_lmac_cfg.definition`:

Definition
----------

.. code-block:: c

    struct iwl_shared_mem_lmac_cfg {
        __le32 txfifo_addr;
        __le32 txfifo_size;
        __le32 rxfifo1_addr;
        __le32 rxfifo1_size;
    }

.. _`iwl_shared_mem_lmac_cfg.members`:

Members
-------

txfifo_addr
    start addr of TXF0 (excluding the context table 0.5KB)

txfifo_size
    size of TX FIFOs

rxfifo1_addr
    RXF1 addr

rxfifo1_size
    RXF1 size

.. _`iwl_shared_mem_cfg`:

struct iwl_shared_mem_cfg
=========================

.. c:type:: struct iwl_shared_mem_cfg

    Shared memory configuration information

.. _`iwl_shared_mem_cfg.definition`:

Definition
----------

.. code-block:: c

    struct iwl_shared_mem_cfg {
        __le32 shared_mem_addr;
        __le32 shared_mem_size;
        __le32 sample_buff_addr;
        __le32 sample_buff_size;
        __le32 rxfifo2_addr;
        __le32 rxfifo2_size;
        __le32 page_buff_addr;
        __le32 page_buff_size;
        __le32 lmac_num;
        struct iwl_shared_mem_lmac_cfg lmac_smem;
    }

.. _`iwl_shared_mem_cfg.members`:

Members
-------

shared_mem_addr
    shared memory address

shared_mem_size
    shared memory size

sample_buff_addr
    internal sample (mon/adc) buff addr

sample_buff_size
    internal sample buff size

rxfifo2_addr
    start addr of RXF2

rxfifo2_size
    size of RXF2

page_buff_addr
    used by UMAC and performance debug (page miss analysis),
    when paging is not supported this should be 0

page_buff_size
    size of \ ``page_buff_addr``\ 

lmac_num
    number of LMACs (1 or 2)

lmac_smem
    per - LMAC smem data

.. _`iwl_mfuart_load_notif`:

struct iwl_mfuart_load_notif
============================

.. c:type:: struct iwl_mfuart_load_notif

    mfuart image version & status ( MFUART_LOAD_NOTIFICATION = 0xb1 )

.. _`iwl_mfuart_load_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mfuart_load_notif {
        __le32 installed_ver;
        __le32 external_ver;
        __le32 status;
        __le32 duration;
        __le32 image_size;
    }

.. _`iwl_mfuart_load_notif.members`:

Members
-------

installed_ver
    installed image version

external_ver
    external image version

status
    MFUART loading status

duration
    MFUART loading time

image_size
    MFUART image size in bytes

.. _`iwl_mfu_assert_dump_notif`:

struct iwl_mfu_assert_dump_notif
================================

.. c:type:: struct iwl_mfu_assert_dump_notif

    mfuart dump logs ( MFU_ASSERT_DUMP_NTF = 0xfe )

.. _`iwl_mfu_assert_dump_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mfu_assert_dump_notif {
        __le32 assert_id;
        __le32 curr_reset_num;
        __le16 index_num;
        __le16 parts_num;
        __le32 data_size;
        __le32 data;
    }

.. _`iwl_mfu_assert_dump_notif.members`:

Members
-------

assert_id
    mfuart assert id that cause the notif

curr_reset_num
    number of asserts since uptime

index_num
    current chunk id

parts_num
    total number of chunks

data_size
    number of data bytes sent

data
    data buffer

.. _`iwl_mvm_marker_id`:

enum iwl_mvm_marker_id
======================

.. c:type:: enum iwl_mvm_marker_id

    marker ids

.. _`iwl_mvm_marker_id.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_marker_id {
        MARKER_ID_TX_FRAME_LATENCY
    };

.. _`iwl_mvm_marker_id.constants`:

Constants
---------

MARKER_ID_TX_FRAME_LATENCY
    TX latency marker

.. _`iwl_mvm_marker_id.description`:

Description
-----------

The ids for different type of markers to insert into the usniffer logs

.. _`iwl_mvm_marker`:

struct iwl_mvm_marker
=====================

.. c:type:: struct iwl_mvm_marker

    mark info into the usniffer logs

.. _`iwl_mvm_marker.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_marker {
        u8 dw_len;
        u8 marker_id;
        __le16 reserved;
        __le64 timestamp;
        __le32 metadata;
    }

.. _`iwl_mvm_marker.members`:

Members
-------

dw_len
    The amount of dwords following this byte including this byte.

marker_id
    A unique marker id (iwl_mvm_marker_id).

reserved
    reserved.

timestamp
    in milliseconds since 1970-01-01 00:00:00 UTC

metadata
    additional meta data that will be written to the unsiffer log

.. _`iwl_mvm_marker.description`:

Description
-----------

(MARKER_CMD = 0xcb)

Mark the UTC time stamp into the usniffer logs together with additional
metadata, so the usniffer output can be parsed.
In the command response the ucode will return the GP2 time.

.. _`iwl_dbg_mem_access_cmd`:

struct iwl_dbg_mem_access_cmd
=============================

.. c:type:: struct iwl_dbg_mem_access_cmd

    Request the device to read/write memory

.. _`iwl_dbg_mem_access_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dbg_mem_access_cmd {
        __le32 op;
        __le32 addr;
        __le32 len;
        __le32 data;
    }

.. _`iwl_dbg_mem_access_cmd.members`:

Members
-------

op
    DEBUG_MEM_OP\_\*

addr
    address to read/write from/to

len
    in dwords, to read/write

data
    for write opeations, contains the source buffer

.. _`iwl_dbg_mem_access_rsp`:

struct iwl_dbg_mem_access_rsp
=============================

.. c:type:: struct iwl_dbg_mem_access_rsp

    Response to debug mem commands

.. _`iwl_dbg_mem_access_rsp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dbg_mem_access_rsp {
        __le32 status;
        __le32 len;
        __le32 data;
    }

.. _`iwl_dbg_mem_access_rsp.members`:

Members
-------

status
    DEBUG_MEM_STATUS\_\*

len
    read dwords (0 for write operations)

data
    contains the read DWs

.. This file was automatic generated / don't edit.

