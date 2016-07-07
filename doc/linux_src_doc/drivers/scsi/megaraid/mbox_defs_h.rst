.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/megaraid/mbox_defs.h

.. _`max_notify_size`:

MAX_NOTIFY_SIZE
===============

.. c:function::  MAX_NOTIFY_SIZE()

    enquiry for device information

.. _`private_bios_data`:

struct private_bios_data
========================

.. c:type:: struct private_bios_data

    bios private data for boot devices

.. _`private_bios_data.definition`:

Definition
----------

.. code-block:: c

    struct private_bios_data {
        uint8_t geometry:4;
        uint8_t unused:4;
        uint8_t boot_drv;
        uint8_t rsvd[12];
        uint16_t cksum;
    }

.. _`private_bios_data.members`:

Members
-------

geometry
    bits 0-3 - BIOS geometry, 0x0001 - 1GB, 0x0010 - 2GB,
    0x1000 - 8GB, Others values are invalid

unused
    bits 4-7 are unused

boot_drv
    logical drive set as boot drive, 0..7 - for 8LD cards,
    0..39 - for 40LD cards

cksum
    0-(sum of first 13 bytes of this structure)

.. This file was automatic generated / don't edit.

