.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_fc.h

.. _`zfcp_fc_event`:

struct zfcp_fc_event
====================

.. c:type:: struct zfcp_fc_event

    FC HBAAPI event for internal queueing from irq context

.. _`zfcp_fc_event.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_fc_event {
        enum fc_host_event_code code;
        u32 data;
        struct list_head list;
    }

.. _`zfcp_fc_event.members`:

Members
-------

code
    Event code

data
    Event data

list
    list_head for zfcp_fc_events list

.. _`zfcp_fc_events`:

struct zfcp_fc_events
=====================

.. c:type:: struct zfcp_fc_events

    Infrastructure for posting FC events from irq context

.. _`zfcp_fc_events.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_fc_events {
        struct list_head list;
        spinlock_t list_lock;
        struct work_struct work;
    }

.. _`zfcp_fc_events.members`:

Members
-------

list
    List for queueing of events from irq context to workqueue

list_lock
    Lock for event list

work
    work_struct for forwarding events in workqueue

.. _`zfcp_fc_gid_pn_req`:

struct zfcp_fc_gid_pn_req
=========================

.. c:type:: struct zfcp_fc_gid_pn_req

    container for ct header plus gid_pn request

.. _`zfcp_fc_gid_pn_req.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_fc_gid_pn_req {
        struct fc_ct_hdr ct_hdr;
        struct fc_ns_gid_pn gid_pn;
    }

.. _`zfcp_fc_gid_pn_req.members`:

Members
-------

ct_hdr
    FC GS common transport header

gid_pn
    GID_PN request

.. _`zfcp_fc_gid_pn_rsp`:

struct zfcp_fc_gid_pn_rsp
=========================

.. c:type:: struct zfcp_fc_gid_pn_rsp

    container for ct header plus gid_pn response

.. _`zfcp_fc_gid_pn_rsp.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_fc_gid_pn_rsp {
        struct fc_ct_hdr ct_hdr;
        struct fc_gid_pn_resp gid_pn;
    }

.. _`zfcp_fc_gid_pn_rsp.members`:

Members
-------

ct_hdr
    FC GS common transport header

gid_pn
    GID_PN response

.. _`zfcp_fc_gpn_ft_req`:

struct zfcp_fc_gpn_ft_req
=========================

.. c:type:: struct zfcp_fc_gpn_ft_req

    container for ct header plus gpn_ft request

.. _`zfcp_fc_gpn_ft_req.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_fc_gpn_ft_req {
        struct fc_ct_hdr ct_hdr;
        struct fc_ns_gid_ft gpn_ft;
    }

.. _`zfcp_fc_gpn_ft_req.members`:

Members
-------

ct_hdr
    FC GS common transport header

gpn_ft
    GPN_FT request

.. _`zfcp_fc_gspn_req`:

struct zfcp_fc_gspn_req
=======================

.. c:type:: struct zfcp_fc_gspn_req

    container for ct header plus GSPN_ID request

.. _`zfcp_fc_gspn_req.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_fc_gspn_req {
        struct fc_ct_hdr ct_hdr;
        struct fc_gid_pn_resp gspn;
    }

.. _`zfcp_fc_gspn_req.members`:

Members
-------

ct_hdr
    FC GS common transport header

gspn
    GSPN_ID request

.. _`zfcp_fc_gspn_rsp`:

struct zfcp_fc_gspn_rsp
=======================

.. c:type:: struct zfcp_fc_gspn_rsp

    container for ct header plus GSPN_ID response

.. _`zfcp_fc_gspn_rsp.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_fc_gspn_rsp {
        struct fc_ct_hdr ct_hdr;
        struct fc_gspn_resp gspn;
        char name[FC_SYMBOLIC_NAME_SIZE];
    }

.. _`zfcp_fc_gspn_rsp.members`:

Members
-------

ct_hdr
    FC GS common transport header

gspn
    GSPN_ID response

name
    The name string of the GSPN_ID response

.. _`zfcp_fc_rspn_req`:

struct zfcp_fc_rspn_req
=======================

.. c:type:: struct zfcp_fc_rspn_req

    container for ct header plus RSPN_ID request

.. _`zfcp_fc_rspn_req.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_fc_rspn_req {
        struct fc_ct_hdr ct_hdr;
        struct fc_ns_rspn rspn;
        char name[FC_SYMBOLIC_NAME_SIZE];
    }

.. _`zfcp_fc_rspn_req.members`:

Members
-------

ct_hdr
    FC GS common transport header

rspn
    RSPN_ID request

name
    The name string of the RSPN_ID request

.. _`zfcp_fc_req`:

struct zfcp_fc_req
==================

.. c:type:: struct zfcp_fc_req

    Container for FC ELS and CT requests sent from zfcp

.. _`zfcp_fc_req.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_fc_req {
        struct zfcp_fsf_ct_els ct_els;
        struct scatterlist sg_req;
        struct scatterlist sg_rsp;
        union {
            struct {
                struct fc_els_adisc req;
                struct fc_els_adisc rsp;
            } adisc;
            struct {
                struct zfcp_fc_gid_pn_req req;
                struct zfcp_fc_gid_pn_rsp rsp;
            } gid_pn;
            struct {
                struct scatterlist sg_rsp2[ZFCP_FC_GPN_FT_NUM_BUFS - 1];
                struct zfcp_fc_gpn_ft_req req;
            } gpn_ft;
            struct {
                struct zfcp_fc_gspn_req req;
                struct zfcp_fc_gspn_rsp rsp;
            } gspn;
            struct {
                struct zfcp_fc_rspn_req req;
                struct fc_ct_hdr rsp;
            } rspn;
        } u;
    }

.. _`zfcp_fc_req.members`:

Members
-------

ct_els
    data required for issuing fsf command

sg_req
    scatterlist entry for request data

sg_rsp
    scatterlist entry for response data

u
    request specific data

.. _`zfcp_fc_wka_status`:

enum zfcp_fc_wka_status
=======================

.. c:type:: enum zfcp_fc_wka_status

    FC WKA port status in zfcp

.. _`zfcp_fc_wka_status.definition`:

Definition
----------

.. code-block:: c

    enum zfcp_fc_wka_status {
        ZFCP_FC_WKA_PORT_OFFLINE,
        ZFCP_FC_WKA_PORT_CLOSING,
        ZFCP_FC_WKA_PORT_OPENING,
        ZFCP_FC_WKA_PORT_ONLINE
    };

.. _`zfcp_fc_wka_status.constants`:

Constants
---------

ZFCP_FC_WKA_PORT_OFFLINE
    Port is closed and not in use

ZFCP_FC_WKA_PORT_CLOSING
    The FSF "close port" request is pending

ZFCP_FC_WKA_PORT_OPENING
    The FSF "open port" request is pending

ZFCP_FC_WKA_PORT_ONLINE
    The port is open and the port handle is valid

.. _`zfcp_fc_wka_port`:

struct zfcp_fc_wka_port
=======================

.. c:type:: struct zfcp_fc_wka_port

    representation of well-known-address (WKA) FC port

.. _`zfcp_fc_wka_port.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_fc_wka_port {
        struct zfcp_adapter *adapter;
        wait_queue_head_t completion_wq;
        enum zfcp_fc_wka_status status;
        atomic_t refcount;
        u32 d_id;
        u32 handle;
        struct mutex mutex;
        struct delayed_work work;
    }

.. _`zfcp_fc_wka_port.members`:

Members
-------

adapter
    Pointer to adapter structure this WKA port belongs to

completion_wq
    Wait for completion of open/close command

status
    Current status of WKA port

refcount
    Reference count to keep port open as long as it is in use

d_id
    FC destination id or well-known-address

handle
    FSF handle for the open WKA port

mutex
    Mutex used during opening/closing state changes

work
    For delaying the closing of the WKA port

.. _`zfcp_fc_wka_ports`:

struct zfcp_fc_wka_ports
========================

.. c:type:: struct zfcp_fc_wka_ports

    Data structures for FC generic services

.. _`zfcp_fc_wka_ports.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_fc_wka_ports {
        struct zfcp_fc_wka_port ms;
        struct zfcp_fc_wka_port ts;
        struct zfcp_fc_wka_port ds;
        struct zfcp_fc_wka_port as;
    }

.. _`zfcp_fc_wka_ports.members`:

Members
-------

ms
    FC Management service

ts
    FC time service

ds
    FC directory service

as
    FC alias service

.. _`zfcp_fc_scsi_to_fcp`:

zfcp_fc_scsi_to_fcp
===================

.. c:function:: void zfcp_fc_scsi_to_fcp(struct fcp_cmnd *fcp, struct scsi_cmnd *scsi, u8 tm_flags)

    setup FCP command with data from scsi_cmnd

    :param struct fcp_cmnd \*fcp:
        fcp_cmnd to setup

    :param struct scsi_cmnd \*scsi:
        scsi_cmnd where to get LUN, task attributes/flags and CDB

    :param u8 tm_flags:
        *undescribed*

.. _`zfcp_fc_eval_fcp_rsp`:

zfcp_fc_eval_fcp_rsp
====================

.. c:function:: void zfcp_fc_eval_fcp_rsp(struct fcp_resp_with_ext *fcp_rsp, struct scsi_cmnd *scsi)

    evaluate FCP RSP IU and update scsi_cmnd accordingly

    :param struct fcp_resp_with_ext \*fcp_rsp:
        FCP RSP IU to evaluate

    :param struct scsi_cmnd \*scsi:
        SCSI command where to update status and sense buffer

.. This file was automatic generated / don't edit.

