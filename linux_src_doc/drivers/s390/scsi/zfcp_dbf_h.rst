.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_dbf.h

.. _`zfcp_dbf_rec_trigger`:

struct zfcp_dbf_rec_trigger
===========================

.. c:type:: struct zfcp_dbf_rec_trigger

    trace record for triggered recovery action

.. _`zfcp_dbf_rec_trigger.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_dbf_rec_trigger {
        u32 ready;
        u32 running;
        u8 want;
        u8 need;
    }

.. _`zfcp_dbf_rec_trigger.members`:

Members
-------

ready
    number of ready recovery actions

running
    number of running recovery actions

want
    wanted recovery action

need
    needed recovery action

.. _`zfcp_dbf_rec_running`:

struct zfcp_dbf_rec_running
===========================

.. c:type:: struct zfcp_dbf_rec_running

    trace record for running recovery

.. _`zfcp_dbf_rec_running.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_dbf_rec_running {
        u64 fsf_req_id;
        u32 rec_status;
        u16 rec_step;
        u8 rec_action;
        u8 rec_count;
    }

.. _`zfcp_dbf_rec_running.members`:

Members
-------

fsf_req_id
    request id for fsf requests

rec_status
    status of the fsf request

rec_step
    current step of the recovery action

rec_action
    *undescribed*

rec_count
    *undescribed*

.. _`zfcp_dbf_rec_running.rec_count`:

rec_count
---------

recovery counter

.. _`zfcp_dbf_rec_id`:

enum zfcp_dbf_rec_id
====================

.. c:type:: enum zfcp_dbf_rec_id

    recovery trace record id

.. _`zfcp_dbf_rec_id.definition`:

Definition
----------

.. code-block:: c

    enum zfcp_dbf_rec_id {
        ZFCP_DBF_REC_TRIG,
        ZFCP_DBF_REC_RUN
    };

.. _`zfcp_dbf_rec_id.constants`:

Constants
---------

ZFCP_DBF_REC_TRIG
    triggered recovery identifier

ZFCP_DBF_REC_RUN
    running recovery identifier

.. _`zfcp_dbf_rec`:

struct zfcp_dbf_rec
===================

.. c:type:: struct zfcp_dbf_rec

    trace record for error recovery actions

.. _`zfcp_dbf_rec.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_dbf_rec {
        u8 id;
        char tag[ZFCP_DBF_TAG_LEN];
        u64 lun;
        u64 wwpn;
        u32 d_id;
        u32 adapter_status;
        u32 port_status;
        u32 lun_status;
        union {
            struct zfcp_dbf_rec_trigger trig;
            struct zfcp_dbf_rec_running run;
        } u;
    }

.. _`zfcp_dbf_rec.members`:

Members
-------

id
    unique number of recovery record type

tag
    identifier string specifying the location of initiation

lun
    logical unit number

wwpn
    word wide port number

d_id
    destination ID

adapter_status
    current status of the adapter

port_status
    current status of the port

lun_status
    current status of the lun

u
    *undescribed*

u.trig
    structure zfcp_dbf_rec_trigger

u.run
    structure zfcp_dbf_rec_running

.. _`zfcp_dbf_san_id`:

enum zfcp_dbf_san_id
====================

.. c:type:: enum zfcp_dbf_san_id

    SAN trace record identifier

.. _`zfcp_dbf_san_id.definition`:

Definition
----------

.. code-block:: c

    enum zfcp_dbf_san_id {
        ZFCP_DBF_SAN_REQ,
        ZFCP_DBF_SAN_RES,
        ZFCP_DBF_SAN_ELS
    };

.. _`zfcp_dbf_san_id.constants`:

Constants
---------

ZFCP_DBF_SAN_REQ
    request trace record id

ZFCP_DBF_SAN_RES
    response trace record id

ZFCP_DBF_SAN_ELS
    extended link service record id

.. _`zfcp_dbf_hba_res`:

struct zfcp_dbf_hba_res
=======================

.. c:type:: struct zfcp_dbf_hba_res

    trace record for hba responses

.. _`zfcp_dbf_hba_res.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_dbf_hba_res {
        u64 req_issued;
        u32 prot_status;
        u8 prot_status_qual[FSF_PROT_STATUS_QUAL_SIZE];
        u32 fsf_status;
        u8 fsf_status_qual[FSF_STATUS_QUALIFIER_SIZE];
        u32 port_handle;
        u32 lun_handle;
    }

.. _`zfcp_dbf_hba_res.members`:

Members
-------

req_issued
    timestamp when request was issued

prot_status
    protocol status

prot_status_qual
    protocol status qualifier

fsf_status
    fsf status

fsf_status_qual
    fsf status qualifier

port_handle
    *undescribed*

lun_handle
    *undescribed*

.. _`zfcp_dbf_hba_uss`:

struct zfcp_dbf_hba_uss
=======================

.. c:type:: struct zfcp_dbf_hba_uss

    trace record for unsolicited status

.. _`zfcp_dbf_hba_uss.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_dbf_hba_uss {
        u32 status_type;
        u32 status_subtype;
        u32 d_id;
        u64 lun;
        u64 queue_designator;
    }

.. _`zfcp_dbf_hba_uss.members`:

Members
-------

status_type
    type of unsolicited status

status_subtype
    subtype of unsolicited status

d_id
    destination ID

lun
    logical unit number

queue_designator
    queue designator

.. _`zfcp_dbf_hba_id`:

enum zfcp_dbf_hba_id
====================

.. c:type:: enum zfcp_dbf_hba_id

    HBA trace record identifier

.. _`zfcp_dbf_hba_id.definition`:

Definition
----------

.. code-block:: c

    enum zfcp_dbf_hba_id {
        ZFCP_DBF_HBA_RES,
        ZFCP_DBF_HBA_USS,
        ZFCP_DBF_HBA_BIT,
        ZFCP_DBF_HBA_BASIC
    };

.. _`zfcp_dbf_hba_id.constants`:

Constants
---------

ZFCP_DBF_HBA_RES
    response trace record

ZFCP_DBF_HBA_USS
    unsolicited status trace record

ZFCP_DBF_HBA_BIT
    bit error trace record

ZFCP_DBF_HBA_BASIC
    *undescribed*

.. _`zfcp_dbf_hba`:

struct zfcp_dbf_hba
===================

.. c:type:: struct zfcp_dbf_hba

    common trace record for HBA records

.. _`zfcp_dbf_hba.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_dbf_hba {
        u8 id;
        char tag[ZFCP_DBF_TAG_LEN];
        u64 fsf_req_id;
        u32 fsf_req_status;
        u32 fsf_cmd;
        u32 fsf_seq_no;
        u16 pl_len;
        union {
            struct zfcp_dbf_hba_res res;
            struct zfcp_dbf_hba_uss uss;
            struct fsf_bit_error_payload be;
        } u;
    }

.. _`zfcp_dbf_hba.members`:

Members
-------

id
    unique number of recovery record type

tag
    identifier string specifying the location of initiation

fsf_req_id
    request id for fsf requests

fsf_req_status
    status of fsf request

fsf_cmd
    fsf command

fsf_seq_no
    fsf sequence number

pl_len
    length of payload stored as zfcp_dbf_pay

u
    record type specific data

.. _`zfcp_dbf_scsi_id`:

enum zfcp_dbf_scsi_id
=====================

.. c:type:: enum zfcp_dbf_scsi_id

    scsi trace record identifier

.. _`zfcp_dbf_scsi_id.definition`:

Definition
----------

.. code-block:: c

    enum zfcp_dbf_scsi_id {
        ZFCP_DBF_SCSI_CMND
    };

.. _`zfcp_dbf_scsi_id.constants`:

Constants
---------

ZFCP_DBF_SCSI_CMND
    scsi command trace record

.. _`zfcp_dbf_scsi`:

struct zfcp_dbf_scsi
====================

.. c:type:: struct zfcp_dbf_scsi

    common trace record for SCSI records

.. _`zfcp_dbf_scsi.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_dbf_scsi {
        u8 id;
        char tag[ZFCP_DBF_TAG_LEN];
        u32 scsi_id;
        u32 scsi_lun;
        u32 scsi_result;
        u8 scsi_retries;
        u8 scsi_allowed;
        u8 fcp_rsp_info;
    #define ZFCP_DBF_SCSI_OPCODE 16
        u8 scsi_opcode[ZFCP_DBF_SCSI_OPCODE];
        u64 fsf_req_id;
        u64 host_scribble;
        u16 pl_len;
        struct fcp_resp_with_ext fcp_rsp;
        u32 scsi_lun_64_hi;
    }

.. _`zfcp_dbf_scsi.members`:

Members
-------

id
    unique number of recovery record type

tag
    identifier string specifying the location of initiation

scsi_id
    scsi device id

scsi_lun
    scsi device logical unit number, low part of 64 bit, old 32 bit

scsi_result
    scsi result

scsi_retries
    current retry number of scsi request

scsi_allowed
    allowed retries

fcp_rsp_info
    FCP response info code

scsi_opcode
    scsi opcode

fsf_req_id
    request id of fsf request

host_scribble
    LLD specific data attached to SCSI request

pl_len
    length of payload stored as zfcp_dbf_pay

fcp_rsp
    response for FCP request

scsi_lun_64_hi
    scsi device logical unit number, high part of 64 bit

.. _`zfcp_dbf_pay`:

struct zfcp_dbf_pay
===================

.. c:type:: struct zfcp_dbf_pay

    trace record for unformatted payload information

.. _`zfcp_dbf_pay.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_dbf_pay {
        u8 counter;
        char area[ZFCP_DBF_TAG_LEN];
        u64 fsf_req_id;
    #define ZFCP_DBF_PAY_MAX_REC 0x100
        char data[ZFCP_DBF_PAY_MAX_REC];
    }

.. _`zfcp_dbf_pay.members`:

Members
-------

counter
    ascending record number

area
    area this record is originated from

fsf_req_id
    request id of fsf request

data
    unformatted data

.. _`zfcp_dbf`:

struct zfcp_dbf
===============

.. c:type:: struct zfcp_dbf

    main dbf trace structure

.. _`zfcp_dbf.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_dbf {
        debug_info_t *pay;
        debug_info_t *rec;
        debug_info_t *hba;
        debug_info_t *san;
        debug_info_t *scsi;
        spinlock_t pay_lock;
        spinlock_t rec_lock;
        spinlock_t hba_lock;
        spinlock_t san_lock;
        spinlock_t scsi_lock;
        struct zfcp_dbf_pay pay_buf;
        struct zfcp_dbf_rec rec_buf;
        struct zfcp_dbf_hba hba_buf;
        struct zfcp_dbf_san san_buf;
        struct zfcp_dbf_scsi scsi_buf;
    }

.. _`zfcp_dbf.members`:

Members
-------

pay
    reference to payload trace area

rec
    reference to recovery trace area

hba
    reference to hba trace area

san
    reference to san trace area

scsi
    reference to scsi trace area

pay_lock
    lock protecting payload trace buffer

rec_lock
    lock protecting recovery trace buffer

hba_lock
    lock protecting hba trace buffer

san_lock
    lock protecting san trace buffer

scsi_lock
    lock protecting scsi trace buffer

pay_buf
    pre-allocated buffer for payload

rec_buf
    pre-allocated buffer for recovery

hba_buf
    pre-allocated buffer for hba

san_buf
    pre-allocated buffer for san

scsi_buf
    pre-allocated buffer for scsi

.. _`zfcp_dbf_hba_fsf_resp_suppress`:

zfcp_dbf_hba_fsf_resp_suppress
==============================

.. c:function:: bool zfcp_dbf_hba_fsf_resp_suppress(struct zfcp_fsf_req *req)

    true if we should not trace by default

    :param struct zfcp_fsf_req \*req:
        request that has been completed

.. _`zfcp_dbf_hba_fsf_resp_suppress.description`:

Description
-----------

Returns true if FCP response with only benign residual under count.

.. _`zfcp_dbf_hba_fsf_response`:

zfcp_dbf_hba_fsf_response
=========================

.. c:function:: void zfcp_dbf_hba_fsf_response(struct zfcp_fsf_req *req)

    trace event for request completion

    :param struct zfcp_fsf_req \*req:
        request that has been completed

.. _`zfcp_dbf_scsi_result`:

zfcp_dbf_scsi_result
====================

.. c:function:: void zfcp_dbf_scsi_result(struct scsi_cmnd *scmd, struct zfcp_fsf_req *req)

    trace event for SCSI command completion

    :param struct scsi_cmnd \*scmd:
        SCSI command pointer

    :param struct zfcp_fsf_req \*req:
        FSF request used to issue SCSI command

.. _`zfcp_dbf_scsi_fail_send`:

zfcp_dbf_scsi_fail_send
=======================

.. c:function:: void zfcp_dbf_scsi_fail_send(struct scsi_cmnd *scmd)

    trace event for failure to send SCSI command

    :param struct scsi_cmnd \*scmd:
        SCSI command pointer

.. _`zfcp_dbf_scsi_abort`:

zfcp_dbf_scsi_abort
===================

.. c:function:: void zfcp_dbf_scsi_abort(char *tag, struct scsi_cmnd *scmd, struct zfcp_fsf_req *fsf_req)

    trace event for SCSI command abort

    :param char \*tag:
        tag indicating success or failure of abort operation

    :param struct scsi_cmnd \*scmd:
        SCSI command to be aborted

    :param struct zfcp_fsf_req \*fsf_req:
        request containing abort (might be NULL)

.. _`zfcp_dbf_scsi_devreset`:

zfcp_dbf_scsi_devreset
======================

.. c:function:: void zfcp_dbf_scsi_devreset(char *tag, struct scsi_cmnd *scmnd, u8 flag, struct zfcp_fsf_req *fsf_req)

    trace event for Logical Unit or Target Reset

    :param char \*tag:
        tag indicating success or failure of reset operation

    :param struct scsi_cmnd \*scmnd:
        SCSI command which caused this error recovery

    :param u8 flag:
        indicates type of reset (Target Reset, Logical Unit Reset)

    :param struct zfcp_fsf_req \*fsf_req:
        *undescribed*

.. _`zfcp_dbf_scsi_nullcmnd`:

zfcp_dbf_scsi_nullcmnd
======================

.. c:function:: void zfcp_dbf_scsi_nullcmnd(struct scsi_cmnd *scmnd, struct zfcp_fsf_req *fsf_req)

    trace NULLify of SCSI command in dev/tgt-reset.

    :param struct scsi_cmnd \*scmnd:
        SCSI command that was NULLified.

    :param struct zfcp_fsf_req \*fsf_req:
        request that owned \ ``scmnd``\ .

.. This file was automatic generated / don't edit.

