.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/megaraid/mbox_defs.h

.. _`mbox64_t`:

typedef mbox64_t
================

.. c:type:: typedef mbox64_t

    64-bit extension for the mailbox

.. _`mbox64_t.description`:

Description
-----------

This is the extension of the 32-bit mailbox to be able to perform DMA
beyond 4GB address range.

.. _`mraid_passthru_t`:

typedef mraid_passthru_t
========================

.. c:type:: typedef mraid_passthru_t

    passthru structure to issue commands to physical devices

.. _`mraid_epassthru_t`:

typedef mraid_epassthru_t
=========================

.. c:type:: typedef mraid_epassthru_t

    passthru structure to issue commands to physical devices

.. _`mraid_pinfo_t`:

typedef mraid_pinfo_t
=====================

.. c:type:: typedef mraid_pinfo_t

    product info, static information about the controller

.. _`mraid_pinfo_t.description`:

Description
-----------

This structures holds the information about the controller which is not
expected to change dynamically.

.. _`mraid_pinfo_t.the-current-value-of-config-signature-is-0x00282008`:

The current value of config signature is 0x00282008
---------------------------------------------------

0x28 = MAX_LOGICAL_DRIVES,
0x20 = Number of stripes and
0x08 = Number of spans

.. _`mraid_notify_t`:

typedef mraid_notify_t
======================

.. c:type:: typedef mraid_notify_t

    the notification structure

.. _`max_notify_size`:

MAX_NOTIFY_SIZE
===============

.. c:function::  MAX_NOTIFY_SIZE()

    enquiry for device information

.. _`mraid_adapinfo_t`:

typedef mraid_adapinfo_t
========================

.. c:type:: typedef mraid_adapinfo_t

    information about the adapter

.. _`mraid_ldrv_info_t`:

typedef mraid_ldrv_info_t
=========================

.. c:type:: typedef mraid_ldrv_info_t

    information about the logical drives

.. _`mraid_pdrv_info_t`:

typedef mraid_pdrv_info_t
=========================

.. c:type:: typedef mraid_pdrv_info_t

    information about the physical drives

.. _`mraid_inquiry_t`:

typedef mraid_inquiry_t
=======================

.. c:type:: typedef mraid_inquiry_t

    RAID inquiry, mailbox command 0x05

.. _`mraid_extinq_t`:

typedef mraid_extinq_t
======================

.. c:type:: typedef mraid_extinq_t

    RAID extended inquiry, mailbox command 0x04

.. _`adap_device_t`:

typedef adap_device_t
=====================

.. c:type:: typedef adap_device_t

    device information

.. _`adap_span_40ld_t`:

typedef adap_span_40ld_t
========================

.. c:type:: typedef adap_span_40ld_t

    40LD span

.. _`adap_span_8ld_t`:

typedef adap_span_8ld_t
=======================

.. c:type:: typedef adap_span_8ld_t

    8LD span

.. _`logdrv_param_t`:

typedef logdrv_param_t
======================

.. c:type:: typedef logdrv_param_t

    logical drives parameters

.. _`logdrv_40ld_t`:

typedef logdrv_40ld_t
=====================

.. c:type:: typedef logdrv_40ld_t

    logical drive definition for 40LD controllers

.. _`logdrv_8ld_span8_t`:

typedef logdrv_8ld_span8_t
==========================

.. c:type:: typedef logdrv_8ld_span8_t

    logical drive definition for 8LD controllers

.. _`logdrv_8ld_span8_t.description`:

Description
-----------

8-LD logical drive with up to 8 spans

.. _`logdrv_8ld_span4_t`:

typedef logdrv_8ld_span4_t
==========================

.. c:type:: typedef logdrv_8ld_span4_t

    logical drive definition for 8LD controllers

.. _`logdrv_8ld_span4_t.description`:

Description
-----------

8-LD logical drive with up to 4 spans

.. _`phys_drive_t`:

typedef phys_drive_t
====================

.. c:type:: typedef phys_drive_t

    physical device information

.. _`disk_array_40ld_t`:

typedef disk_array_40ld_t
=========================

.. c:type:: typedef disk_array_40ld_t

    disk array for 40LD controllers

.. _`disk_array_8ld_span8_t`:

typedef disk_array_8ld_span8_t
==============================

.. c:type:: typedef disk_array_8ld_span8_t

    disk array for 8LD controllers

.. _`disk_array_8ld_span8_t.description`:

Description
-----------

Disk array for 8LD logical drives with up to 8 spans

.. _`disk_array_8ld_span4_t`:

typedef disk_array_8ld_span4_t
==============================

.. c:type:: typedef disk_array_8ld_span4_t

    disk array for 8LD controllers

.. _`disk_array_8ld_span4_t.description`:

Description
-----------

Disk array for 8LD logical drives with up to 4 spans

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
        uint8_t geometry :4;
        uint8_t unused :4;
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

rsvd
    *undescribed*

cksum
    0-(sum of first 13 bytes of this structure)

.. _`mbox_sgl64`:

typedef mbox_sgl64
==================

.. c:type:: typedef mbox_sgl64

    64-bit scatter list for mailbox based controllers

.. _`mbox_sgl32`:

typedef mbox_sgl32
==================

.. c:type:: typedef mbox_sgl32

    32-bit scatter list for mailbox based controllers

.. This file was automatic generated / don't edit.

