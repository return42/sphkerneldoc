
.. _API-struct-bdb-header:

=================
struct bdb_header
=================

*man struct bdb_header(9)*

*4.6.0-rc1*

BDB Header structure


Synopsis
========

.. code-block:: c

    struct bdb_header {
      u8 signature[16];
      u16 version;
      u16 header_size;
      u16 bdb_size;
    };


Members
=======

signature[16]
    BDB signature “BIOS_DATA_BLOCK”

version
    Version of the data block definitions

header_size
    Size of this structure

bdb_size
    Size of BDB (BDB Header and data blocks)
