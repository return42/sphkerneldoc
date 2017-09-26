.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ufs/ufs.h

.. _`utp_upiu_header`:

struct utp_upiu_header
======================

.. c:type:: struct utp_upiu_header

    UPIU header structure

.. _`utp_upiu_header.definition`:

Definition
----------

.. code-block:: c

    struct utp_upiu_header {
        __be32 dword_0;
        __be32 dword_1;
        __be32 dword_2;
    }

.. _`utp_upiu_header.members`:

Members
-------

dword_0
    UPIU header DW-0

dword_1
    UPIU header DW-1

dword_2
    UPIU header DW-2

.. _`utp_upiu_cmd`:

struct utp_upiu_cmd
===================

.. c:type:: struct utp_upiu_cmd

    Command UPIU structure

.. _`utp_upiu_cmd.definition`:

Definition
----------

.. code-block:: c

    struct utp_upiu_cmd {
        __be32 exp_data_transfer_len;
        u8 cdb[MAX_CDB_SIZE];
    }

.. _`utp_upiu_cmd.members`:

Members
-------

exp_data_transfer_len
    *undescribed*

cdb
    Command Descriptor Block CDB DW-4 to DW-7

.. _`utp_upiu_query`:

struct utp_upiu_query
=====================

.. c:type:: struct utp_upiu_query

    upiu request buffer structure for query request.

.. _`utp_upiu_query.definition`:

Definition
----------

.. code-block:: c

    struct utp_upiu_query {
        u8 opcode;
        u8 idn;
        u8 index;
        u8 selector;
        __be16 reserved_osf;
        __be16 length;
        __be32 value;
        __be32 reserved[2];
    }

.. _`utp_upiu_query.members`:

Members
-------

opcode
    command to perform B-0

idn
    a value that indicates the particular type of data B-1

index
    Index to further identify data B-2

selector
    Index to further identify data B-3

reserved_osf
    spec reserved field B-4,5

length
    number of descriptor bytes to read/write B-6,7

value
    Attribute value to be written DW-5

reserved
    spec reserved DW-6,7

.. _`utp_upiu_req`:

struct utp_upiu_req
===================

.. c:type:: struct utp_upiu_req

    general upiu request structure

.. _`utp_upiu_req.definition`:

Definition
----------

.. code-block:: c

    struct utp_upiu_req {
        struct utp_upiu_header header;
        union {
            struct utp_upiu_cmd sc;
            struct utp_upiu_query qr;
        } ;
    }

.. _`utp_upiu_req.members`:

Members
-------

header
    UPIU header structure DW-0 to DW-2

{unnamed_union}
    anonymous

sc
    fields structure for scsi command DW-3 to DW-7

qr
    fields structure for query request DW-3 to DW-7

.. _`utp_cmd_rsp`:

struct utp_cmd_rsp
==================

.. c:type:: struct utp_cmd_rsp

    Response UPIU structure

.. _`utp_cmd_rsp.definition`:

Definition
----------

.. code-block:: c

    struct utp_cmd_rsp {
        __be32 residual_transfer_count;
        __be32 reserved[4];
        __be16 sense_data_len;
        u8 sense_data[RESPONSE_UPIU_SENSE_DATA_LENGTH];
    }

.. _`utp_cmd_rsp.members`:

Members
-------

residual_transfer_count
    Residual transfer count DW-3

reserved
    Reserved double words DW-4 to DW-7

sense_data_len
    Sense data length DW-8 U16

sense_data
    Sense data field DW-8 to DW-12

.. _`utp_upiu_rsp`:

struct utp_upiu_rsp
===================

.. c:type:: struct utp_upiu_rsp

    general upiu response structure

.. _`utp_upiu_rsp.definition`:

Definition
----------

.. code-block:: c

    struct utp_upiu_rsp {
        struct utp_upiu_header header;
        union {
            struct utp_cmd_rsp sr;
            struct utp_upiu_query qr;
        } ;
    }

.. _`utp_upiu_rsp.members`:

Members
-------

header
    UPIU header structure DW-0 to DW-2

{unnamed_union}
    anonymous

sr
    fields structure for scsi command DW-3 to DW-12

qr
    fields structure for query request DW-3 to DW-7

.. _`utp_upiu_task_req`:

struct utp_upiu_task_req
========================

.. c:type:: struct utp_upiu_task_req

    Task request UPIU structure \ ``header``\  - UPIU header structure DW0 to DW-2

.. _`utp_upiu_task_req.definition`:

Definition
----------

.. code-block:: c

    struct utp_upiu_task_req {
        struct utp_upiu_header header;
        __be32 input_param1;
        __be32 input_param2;
        __be32 input_param3;
        __be32 reserved[2];
    }

.. _`utp_upiu_task_req.members`:

Members
-------

header
    *undescribed*

input_param1
    Input parameter 1 DW-3

input_param2
    Input parameter 2 DW-4

input_param3
    Input parameter 3 DW-5

reserved
    Reserved double words DW-6 to DW-7

.. _`utp_upiu_task_rsp`:

struct utp_upiu_task_rsp
========================

.. c:type:: struct utp_upiu_task_rsp

    Task Management Response UPIU structure

.. _`utp_upiu_task_rsp.definition`:

Definition
----------

.. code-block:: c

    struct utp_upiu_task_rsp {
        struct utp_upiu_header header;
        __be32 output_param1;
        __be32 output_param2;
        __be32 reserved[3];
    }

.. _`utp_upiu_task_rsp.members`:

Members
-------

header
    UPIU header structure DW0-DW-2

output_param1
    Ouput parameter 1 DW3

output_param2
    Output parameter 2 DW4

reserved
    Reserved double words DW-5 to DW-7

.. _`ufs_query_req`:

struct ufs_query_req
====================

.. c:type:: struct ufs_query_req

    parameters for building a query request

.. _`ufs_query_req.definition`:

Definition
----------

.. code-block:: c

    struct ufs_query_req {
        u8 query_func;
        struct utp_upiu_query upiu_req;
    }

.. _`ufs_query_req.members`:

Members
-------

query_func
    UPIU header query function

upiu_req
    the query request data

.. _`ufs_query_res`:

struct ufs_query_res
====================

.. c:type:: struct ufs_query_res

    UPIU QUERY

.. _`ufs_query_res.definition`:

Definition
----------

.. code-block:: c

    struct ufs_query_res {
        u8 response;
        struct utp_upiu_query upiu_res;
    }

.. _`ufs_query_res.members`:

Members
-------

response
    device response code

upiu_res
    query response data

.. This file was automatic generated / don't edit.

