.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-media-entity-enum:

========================
struct media_entity_enum
========================

*man struct media_entity_enum(9)*

*4.6.0-rc5*

An enumeration of media entities.


Synopsis
========

.. code-block:: c

    struct media_entity_enum {
      unsigned long * bmap;
      int idx_max;
    };


Members
=======

bmap
    Bit map in which each bit represents one entity at struct
    media_entity->internal_idx.

idx_max
    Number of bits in bmap


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
