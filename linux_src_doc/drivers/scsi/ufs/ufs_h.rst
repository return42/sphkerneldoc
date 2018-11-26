.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ufs/ufs.h

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

.. _`ufs_is_valid_unit_desc_lun`:

ufs_is_valid_unit_desc_lun
==========================

.. c:function:: bool ufs_is_valid_unit_desc_lun(u8 lun)

    checks if the given LUN has a unit descriptor

    :param lun:
        LU number to check
    :type lun: u8

.. This file was automatic generated / don't edit.

