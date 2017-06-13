.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ufs/ufshci.h

.. _`ufshcd_sg_entry`:

struct ufshcd_sg_entry
======================

.. c:type:: struct ufshcd_sg_entry

    UFSHCI PRD Entry

.. _`ufshcd_sg_entry.definition`:

Definition
----------

.. code-block:: c

    struct ufshcd_sg_entry {
        __le32 base_addr;
        __le32 upper_addr;
        __le32 reserved;
        __le32 size;
    }

.. _`ufshcd_sg_entry.members`:

Members
-------

base_addr
    Lower 32bit physical address DW-0

upper_addr
    Upper 32bit physical address DW-1

reserved
    Reserved for future use DW-2

size
    size of physical segment DW-3

.. _`utp_transfer_cmd_desc`:

struct utp_transfer_cmd_desc
============================

.. c:type:: struct utp_transfer_cmd_desc

    UFS Command Descriptor structure

.. _`utp_transfer_cmd_desc.definition`:

Definition
----------

.. code-block:: c

    struct utp_transfer_cmd_desc {
        u8 command_upiu;
        u8 response_upiu;
        struct ufshcd_sg_entry prd_table;
    }

.. _`utp_transfer_cmd_desc.members`:

Members
-------

command_upiu
    Command UPIU Frame address

response_upiu
    Response UPIU Frame address

prd_table
    Physical Region Descriptor

.. _`request_desc_header`:

struct request_desc_header
==========================

.. c:type:: struct request_desc_header

    Descriptor Header common to both UTRD and UTMRD

.. _`request_desc_header.definition`:

Definition
----------

.. code-block:: c

    struct request_desc_header {
        __le32 dword_0;
        __le32 dword_1;
        __le32 dword_2;
        __le32 dword_3;
    }

.. _`request_desc_header.members`:

Members
-------

dword_0
    *undescribed*

dword_1
    *undescribed*

dword_2
    *undescribed*

dword_3
    *undescribed*

.. _`utp_transfer_req_desc`:

struct utp_transfer_req_desc
============================

.. c:type:: struct utp_transfer_req_desc

    UTRD structure

.. _`utp_transfer_req_desc.definition`:

Definition
----------

.. code-block:: c

    struct utp_transfer_req_desc {
        struct request_desc_header header;
        __le32 command_desc_base_addr_lo;
        __le32 command_desc_base_addr_hi;
        __le16 response_upiu_length;
        __le16 response_upiu_offset;
        __le16 prd_table_length;
        __le16 prd_table_offset;
    }

.. _`utp_transfer_req_desc.members`:

Members
-------

header
    UTRD header DW-0 to DW-3

command_desc_base_addr_lo
    UCD base address low DW-4

command_desc_base_addr_hi
    UCD base address high DW-5

response_upiu_length
    response UPIU length DW-6

response_upiu_offset
    response UPIU offset DW-6

prd_table_length
    Physical region descriptor length DW-7

prd_table_offset
    Physical region descriptor offset DW-7

.. _`utp_task_req_desc`:

struct utp_task_req_desc
========================

.. c:type:: struct utp_task_req_desc

    UTMRD structure

.. _`utp_task_req_desc.definition`:

Definition
----------

.. code-block:: c

    struct utp_task_req_desc {
        struct request_desc_header header;
        __le32 task_req_upiu;
        __le32 task_rsp_upiu;
    }

.. _`utp_task_req_desc.members`:

Members
-------

header
    UTMRD header DW-0 to DW-3

task_req_upiu
    Pointer to task request UPIU DW-4 to DW-11

task_rsp_upiu
    Pointer to task response UPIU DW12 to DW-19

.. This file was automatic generated / don't edit.

