.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/asm/fcx.h

.. _`tcw`:

struct tcw
==========

.. c:type:: struct tcw

    Transport Control Word (TCW)

.. _`tcw.definition`:

Definition
----------

.. code-block:: c

    struct tcw {
        u32 format:2;
        u32 :6;
        u32 flags:24;
        u32 :8;
        u32 tccbl:6;
        u32 r:1;
        u32 w:1;
        u32 :16;
        u64 output;
        u64 input;
        u64 tsb;
        u64 tccb;
        u32 output_count;
        u32 input_count;
        u32 :32;
        u32 :32;
        u32 :32;
        u32 intrg;
    }

.. _`tcw.members`:

Members
-------

format
    TCW format

flags
    TCW flags

tccbl
    Transport-Command-Control-Block Length

r
    Read Operations

w
    Write Operations

output
    Output-Data Address

input
    Input-Data Address

tsb
    Transport-Status-Block Address

tccb
    Transport-Command-Control-Block Address

output_count
    Output Count

input_count
    Input Count

intrg
    Interrogate TCW Address

.. _`tidaw`:

struct tidaw
============

.. c:type:: struct tidaw

    Transport-Indirect-Addressing Word (TIDAW)

.. _`tidaw.definition`:

Definition
----------

.. code-block:: c

    struct tidaw {
        u32 flags:8;
        u32 :24;
        u32 count;
        u64 addr;
    }

.. _`tidaw.members`:

Members
-------

flags
    TIDAW flags. Can be an arithmetic OR of the following constants:
    \ ``TIDAW_FLAGS_LAST``\ , \ ``TIDAW_FLAGS_SKIP``\ , \ ``TIDAW_FLAGS_DATA_INT``\ ,
    \ ``TIDAW_FLAGS_TTIC``\ , \ ``TIDAW_FLAGS_INSERT_CBC``\ 

count
    Count

addr
    Address

.. _`tsa_iostat`:

struct tsa_iostat
=================

.. c:type:: struct tsa_iostat

    I/O-Status Transport-Status Area (IO-Stat TSA)

.. _`tsa_iostat.definition`:

Definition
----------

.. code-block:: c

    struct tsa_iostat {
        u32 dev_time;
        u32 def_time;
        u32 queue_time;
        u32 dev_busy_time;
        u32 dev_act_time;
        u8 sense[32];
    }

.. _`tsa_iostat.members`:

Members
-------

dev_time
    Device Time

def_time
    Defer Time

queue_time
    Queue Time

dev_busy_time
    Device-Busy Time

dev_act_time
    Device-Active-Only Time

sense
    Sense Data (if present)

.. _`tsa_ddpc`:

struct tsa_ddpc
===============

.. c:type:: struct tsa_ddpc

    Device-Detected-Program-Check Transport-Status Area (DDPC TSA)

.. _`tsa_ddpc.definition`:

Definition
----------

.. code-block:: c

    struct tsa_ddpc {
        u32 :24;
        u32 rc:8;
        u8 rcq[16];
        u8 sense[32];
    }

.. _`tsa_ddpc.members`:

Members
-------

rc
    Reason Code

rcq
    Reason Code Qualifier

sense
    Sense Data (if present)

.. _`tsa_intrg`:

struct tsa_intrg
================

.. c:type:: struct tsa_intrg

    Interrogate Transport-Status Area (Intrg. TSA)

.. _`tsa_intrg.definition`:

Definition
----------

.. code-block:: c

    struct tsa_intrg {
        u32 format:8;
        u32 flags:8;
        u32 cu_state:8;
        u32 dev_state:8;
        u32 op_state:8;
        u32 :24;
        u8 sd_info[12];
        u32 dl_id;
        u8 dd_data[28];
    }

.. _`tsa_intrg.members`:

Members
-------

format
    Format

flags
    Flags. Can be an arithmetic OR of the following constants:
    \ ``TSA_INTRG_FLAGS_CU_STATE_VALID``\ , \ ``TSA_INTRG_FLAGS_DEV_STATE_VALID``\ ,
    \ ``TSA_INTRG_FLAGS_OP_STATE_VALID``\ 

cu_state
    Controle-Unit State

dev_state
    Device State

op_state
    Operation State

sd_info
    State-Dependent Information

dl_id
    Device-Level Identifier

dd_data
    Device-Dependent Data

.. _`tsb`:

struct tsb
==========

.. c:type:: struct tsb

    Transport-Status Block (TSB)

.. _`tsb.definition`:

Definition
----------

.. code-block:: c

    struct tsb {
        u32 length:8;
        u32 flags:8;
        u32 dcw_offset:16;
        u32 count;
        u32 :32;
        union {
            struct tsa_iostat iostat;
            struct tsa_ddpc ddpc;
            struct tsa_intrg intrg;
        } __attribute__ ((packed)) tsa;
    }

.. _`tsb.members`:

Members
-------

length
    Length

flags
    Flags. Can be an arithmetic OR of the following constants:
    \ ``TSB_FLAGS_DCW_OFFSET_VALID``\ , \ ``TSB_FLAGS_COUNT_VALID``\ , \ ``TSB_FLAGS_CACHE_MISS``\ ,
    \ ``TSB_FLAGS_TIME_VALID``\ 

dcw_offset
    DCW Offset

count
    Count

tsa
    Transport-Status-Area

.. _`dcw_intrg_data`:

struct dcw_intrg_data
=====================

.. c:type:: struct dcw_intrg_data

    Interrogate DCW data

.. _`dcw_intrg_data.definition`:

Definition
----------

.. code-block:: c

    struct dcw_intrg_data {
        u32 format:8;
        u32 rc:8;
        u32 rcq:8;
        u32 lpm:8;
        u32 pam:8;
        u32 pim:8;
        u32 timeout:16;
        u32 flags:8;
        u32 :24;
        u32 :32;
        u64 time;
        u64 prog_id;
        u8 prog_data[0];
    }

.. _`dcw_intrg_data.members`:

Members
-------

format
    Format. Should be \ ``DCW_INTRG_FORMAT_DEFAULT``\ 

rc
    Reason Code. Can be one of \ ``DCW_INTRG_RC_UNSPECIFIED``\ ,
    \ ``DCW_INTRG_RC_TIMEOUT``\ 

rcq
    Reason Code Qualifier: Can be one of \ ``DCW_INTRG_RCQ_UNSPECIFIED``\ ,
    \ ``DCW_INTRG_RCQ_PRIMARY``\ , \ ``DCW_INTRG_RCQ_SECONDARY``\ 

lpm
    Logical-Path Mask

pam
    Path-Available Mask

pim
    Path-Installed Mask

timeout
    Timeout

flags
    Flags. Can be an arithmetic OR of \ ``DCW_INTRG_FLAGS_MPM``\ ,
    \ ``DCW_INTRG_FLAGS_PPR``\ , \ ``DCW_INTRG_FLAGS_CRIT``\ 

time
    Time

prog_id
    Program Identifier

prog_data
    Program-Dependent Data

.. _`dcw`:

struct dcw
==========

.. c:type:: struct dcw

    Device-Command Word (DCW)

.. _`dcw.definition`:

Definition
----------

.. code-block:: c

    struct dcw {
        u32 cmd:8;
        u32 flags:8;
        u32 :8;
        u32 cd_count:8;
        u32 count;
        u8 cd[0];
    }

.. _`dcw.members`:

Members
-------

cmd
    Command Code. Can be one of \ ``DCW_CMD_WRITE``\ , \ ``DCW_CMD_READ``\ ,
    \ ``DCW_CMD_CONTROL``\ , \ ``DCW_CMD_SENSE``\ , \ ``DCW_CMD_SENSE_ID``\ , \ ``DCW_CMD_INTRG``\ 

flags
    Flags. Can be an arithmetic OR of \ ``DCW_FLAGS_CC``\ 

cd_count
    Control-Data Count

count
    Count

cd
    Control Data

.. _`tccb_tcah`:

struct tccb_tcah
================

.. c:type:: struct tccb_tcah

    Transport-Command-Area Header (TCAH)

.. _`tccb_tcah.definition`:

Definition
----------

.. code-block:: c

    struct tccb_tcah {
        u32 format:8;
        u32 :24;
        u32 :24;
        u32 tcal:8;
        u32 sac:16;
        u32 :8;
        u32 prio:8;
        u32 :32;
    }

.. _`tccb_tcah.members`:

Members
-------

format
    Format. Should be \ ``TCCB_FORMAT_DEFAULT``\ 

tcal
    Transport-Command-Area Length

sac
    Service-Action Code. Can be one of \ ``TCCB_SAC_DEFAULT``\ , \ ``TCCB_SAC_INTRG``\ 

prio
    Priority

.. _`tccb_tcat`:

struct tccb_tcat
================

.. c:type:: struct tccb_tcat

    Transport-Command-Area Trailer (TCAT)

.. _`tccb_tcat.definition`:

Definition
----------

.. code-block:: c

    struct tccb_tcat {
        u32 :32;
        u32 count;
    }

.. _`tccb_tcat.members`:

Members
-------

count
    Transport Count

.. _`tccb`:

struct tccb
===========

.. c:type:: struct tccb

    (partial) Transport-Command-Control Block (TCCB)

.. _`tccb.definition`:

Definition
----------

.. code-block:: c

    struct tccb {
        struct tccb_tcah tcah;
        u8 tca[0];
    }

.. _`tccb.members`:

Members
-------

tcah
    TCAH

tca
    Transport-Command Area

.. This file was automatic generated / don't edit.

