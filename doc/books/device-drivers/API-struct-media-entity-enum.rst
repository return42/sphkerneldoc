
.. _API-struct-media-entity-enum:

========================
struct media_entity_enum
========================

*man struct media_entity_enum(9)*

*4.6.0-rc1*

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
    Bit map in which each bit represents one entity at struct media_entity->internal_idx.

idx_max
    Number of bits in bmap
