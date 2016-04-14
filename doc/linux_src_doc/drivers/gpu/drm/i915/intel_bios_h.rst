.. -*- coding: utf-8; mode: rst -*-

============
intel_bios.h
============

.. _`vbt_header`:

struct vbt_header
=================

.. c:type:: struct vbt_header

    VBT Header structure



Definition
----------

.. code-block:: c

  struct vbt_header {
    u8 signature[20];
    u16 version;
    u16 header_size;
    u16 vbt_size;
    u8 vbt_checksum;
    u8 reserved0;
    u32 bdb_offset;
    u32 aim_offset[4];
  };



Members
-------

:``signature[20]``:
    VBT signature, always starts with "$VBT"

:``version``:
    Version of this structure

:``header_size``:
    Size of this structure

:``vbt_size``:
    Size of VBT (VBT Header, BDB Header and data blocks)

:``vbt_checksum``:
    Checksum

:``reserved0``:
    Reserved

:``bdb_offset``:
    Offset of :c:type:`struct bdb_header <bdb_header>` from beginning of VBT

:``aim_offset[4]``:
    Offsets of add-in data blocks from beginning of VBT



.. _`bdb_header`:

struct bdb_header
=================

.. c:type:: struct bdb_header

    BDB Header structure



Definition
----------

.. code-block:: c

  struct bdb_header {
    u8 signature[16];
    u16 version;
    u16 header_size;
    u16 bdb_size;
  };



Members
-------

:``signature[16]``:
    BDB signature "BIOS_DATA_BLOCK"

:``version``:
    Version of the data block definitions

:``header_size``:
    Size of this structure

:``bdb_size``:
    Size of BDB (BDB Header and data blocks)


