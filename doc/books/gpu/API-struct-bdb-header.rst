.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-bdb-header:

=================
struct bdb_header
=================

*man struct bdb_header(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
