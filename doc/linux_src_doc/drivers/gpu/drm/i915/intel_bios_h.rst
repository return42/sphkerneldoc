.. -*- coding: utf-8; mode: rst -*-

============
intel_bios.h
============



.. _xref_struct_vbt_header:

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

:``u8 signature[20]``:
    VBT signature, always starts with "$VBT"

:``u16 version``:
    Version of this structure

:``u16 header_size``:
    Size of this structure

:``u16 vbt_size``:
    Size of VBT (VBT Header, BDB Header and data blocks)

:``u8 vbt_checksum``:
    Checksum

:``u8 reserved0``:
    Reserved

:``u32 bdb_offset``:
    Offset of :c:type:`struct bdb_header <bdb_header>` from beginning of VBT

:``u32 aim_offset[4]``:
    Offsets of add-in data blocks from beginning of VBT





.. _xref_struct_bdb_header:

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

:``u8 signature[16]``:
    BDB signature "BIOS_DATA_BLOCK"

:``u16 version``:
    Version of the data block definitions

:``u16 header_size``:
    Size of this structure

:``u16 bdb_size``:
    Size of BDB (BDB Header and data blocks)



