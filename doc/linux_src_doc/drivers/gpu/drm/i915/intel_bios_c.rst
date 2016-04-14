.. -*- coding: utf-8; mode: rst -*-

============
intel_bios.c
============

.. _`video-bios-table--vbt-`:

Video BIOS Table (VBT)
======================

The Video BIOS Table, or VBT, provides platform and board specific
configuration information to the driver that is not discoverable or available
through other means. The configuration is mostly related to display
hardware. The VBT is available via the ACPI OpRegion or, on older systems, in
the PCI ROM.

The VBT consists of a VBT Header (defined as :c:type:`struct vbt_header <vbt_header>`), a BDB
Header (:c:type:`struct bdb_header <bdb_header>`), and a number of BIOS Data Blocks (BDB) that
contain the actual configuration information. The VBT Header, and thus the
VBT, begins with "$VBT" signature. The VBT Header contains the offset of the
BDB Header. The data blocks are concatenated after the BDB Header. The data
blocks have a 1-byte Block ID, 2-byte Block Size, and Block Size bytes of
data. (Block 53, the MIPI Sequence Block is an exception.)

The driver parses the VBT during load. The relevant information is stored in
driver private data for ease of use, and the actual VBT is not read after
that.


.. _`intel_bios_is_valid_vbt`:

intel_bios_is_valid_vbt
=======================

.. c:function:: bool intel_bios_is_valid_vbt (const void *buf, size_t size)

    does the given buffer contain a valid VBT

    :param const void \*buf:
        pointer to a buffer to validate

    :param size_t size:
        size of the buffer


.. _`intel_bios_is_valid_vbt.description`:

Description
-----------

Returns true on valid VBT.


.. _`intel_bios_init`:

intel_bios_init
===============

.. c:function:: int intel_bios_init (struct drm_i915_private *dev_priv)

    find VBT and initialize settings from the BIOS

    :param struct drm_i915_private \*dev_priv:
        i915 device instance


.. _`intel_bios_init.description`:

Description
-----------

Loads the Video BIOS and checks that the VBT exists.  Sets scratch registers
to appropriate values.

Returns 0 on success, nonzero on failure.

