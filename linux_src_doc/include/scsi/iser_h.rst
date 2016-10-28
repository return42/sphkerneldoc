.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/scsi/iser.h

.. _`iser_cm_hdr`:

struct iser_cm_hdr
==================

.. c:type:: struct iser_cm_hdr

    iSER CM header (from iSER Annex A12)

.. _`iser_cm_hdr.definition`:

Definition
----------

.. code-block:: c

    struct iser_cm_hdr {
        u8 flags;
        u8 rsvd[3];
    }

.. _`iser_cm_hdr.members`:

Members
-------

flags
    flags support (zbva, send_w_inv)

rsvd
    reserved

.. _`iser_ctrl`:

struct iser_ctrl
================

.. c:type:: struct iser_ctrl

    iSER header of iSCSI control PDU

.. _`iser_ctrl.definition`:

Definition
----------

.. code-block:: c

    struct iser_ctrl {
        u8 flags;
        u8 rsvd[3];
        __be32 write_stag;
        __be64 write_va;
        __be32 read_stag;
        __be64 read_va;
    }

.. _`iser_ctrl.members`:

Members
-------

flags
    opcode and read/write valid bits

rsvd
    reserved

write_stag
    write rkey

write_va
    write virtual address

read_stag
    *undescribed*

read_va
    read virtual address

.. This file was automatic generated / don't edit.

