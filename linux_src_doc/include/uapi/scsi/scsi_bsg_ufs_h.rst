.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/scsi/scsi_bsg_ufs.h

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
        __u8 opcode;
        __u8 idn;
        __u8 index;
        __u8 selector;
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
        __u8 cdb[UFS_CDB_SIZE];
    }

.. _`utp_upiu_cmd.members`:

Members
-------

exp_data_transfer_len
    *undescribed*

cdb
    Command Descriptor Block CDB DW-4 to DW-7

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
            struct utp_upiu_query tr;
            struct utp_upiu_query uc;
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

tr
    *undescribed*

uc
    *undescribed*

.. This file was automatic generated / don't edit.

