
.. _API-struct-vbt-header:

=================
struct vbt_header
=================

*man struct vbt_header(9)*

*4.6.0-rc1*

VBT Header structure


Synopsis
========

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
=======

signature[20]
    VBT signature, always starts with “$VBT”

version
    Version of this structure

header_size
    Size of this structure

vbt_size
    Size of VBT (VBT Header, BDB Header and data blocks)

vbt_checksum
    Checksum

reserved0
    Reserved

bdb_offset
    Offset of ``struct bdb_header`` from beginning of VBT

aim_offset[4]
    Offsets of add-in data blocks from beginning of VBT
