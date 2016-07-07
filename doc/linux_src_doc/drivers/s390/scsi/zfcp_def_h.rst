.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_def.h

.. _`zfcp_unit`:

struct zfcp_unit
================

.. c:type:: struct zfcp_unit

    LUN configured via zfcp sysfs

.. _`zfcp_unit.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_unit {
        struct device dev;
        struct list_head list;
        struct zfcp_port *port;
        u64 fcp_lun;
        struct work_struct scsi_work;
    }

.. _`zfcp_unit.members`:

Members
-------

dev
    struct device for sysfs representation and reference counting

list
    entry in LUN/unit list per zfcp_port

port
    reference to zfcp_port where this LUN is configured

fcp_lun
    64 bit LUN value

scsi_work
    for running scsi_scan_target

.. _`zfcp_unit.description`:

Description
-----------

This is the representation of a LUN that has been configured for
usage. The main data here is the 64 bit LUN value, data for
running I/O and recovery is in struct zfcp_scsi_dev.

.. _`zfcp_scsi_dev`:

struct zfcp_scsi_dev
====================

.. c:type:: struct zfcp_scsi_dev

    zfcp data per SCSI device

.. _`zfcp_scsi_dev.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_scsi_dev {
        atomic_t status;
        u32 lun_handle;
        struct zfcp_erp_action erp_action;
        atomic_t erp_counter;
        struct zfcp_latencies latencies;
        struct zfcp_port *port;
    }

.. _`zfcp_scsi_dev.members`:

Members
-------

status
    zfcp internal status flags

lun_handle
    handle from "open lun" for issuing FSF requests

erp_action
    zfcp erp data for opening and recovering this LUN

erp_counter
    zfcp erp counter for this LUN

latencies
    FSF channel and fabric latencies

port
    zfcp_port where this LUN belongs to

.. _`sdev_to_zfcp`:

sdev_to_zfcp
============

.. c:function:: struct zfcp_scsi_dev *sdev_to_zfcp(struct scsi_device *sdev)

    Access zfcp LUN data for SCSI device

    :param struct scsi_device \*sdev:
        scsi_device where to get the zfcp_scsi_dev pointer

.. _`zfcp_scsi_dev_lun`:

zfcp_scsi_dev_lun
=================

.. c:function:: u64 zfcp_scsi_dev_lun(struct scsi_device *sdev)

    Return SCSI device LUN as 64 bit FCP LUN

    :param struct scsi_device \*sdev:
        SCSI device where to get the LUN from

.. _`zfcp_fsf_req`:

struct zfcp_fsf_req
===================

.. c:type:: struct zfcp_fsf_req

    basic FSF request structure

.. _`zfcp_fsf_req.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_fsf_req {
        struct list_head list;
        unsigned long req_id;
        struct zfcp_adapter *adapter;
        struct zfcp_qdio_req qdio_req;
        struct completion completion;
        u32 status;
        u32 fsf_command;
        struct fsf_qtcb *qtcb;
        u32 seq_no;
        void *data;
        struct timer_list timer;
        struct zfcp_erp_action *erp_action;
        mempool_t *pool;
        unsigned long long issued;
        void (* handler) (struct zfcp_fsf_req *);
    }

.. _`zfcp_fsf_req.members`:

Members
-------

list
    list of FSF requests

req_id
    unique request ID

adapter
    adapter this request belongs to

qdio_req
    qdio queue related values

completion
    used to signal the completion of the request

status
    status of the request

fsf_command
    FSF command issued

qtcb
    associated QTCB

seq_no
    sequence number of this request

data
    private data

timer
    timer data of this request

erp_action
    reference to erp action if request issued on behalf of ERP

pool
    reference to memory pool if used for this request

issued
    time when request was send (STCK)

handler
    handler which should be called to process response

.. This file was automatic generated / don't edit.

