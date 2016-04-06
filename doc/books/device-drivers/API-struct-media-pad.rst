
.. _API-struct-media-pad:

================
struct media_pad
================

*man struct media_pad(9)*

*4.6.0-rc1*

A media pad graph object.


Synopsis
========

.. code-block:: c

    struct media_pad {
      struct media_gobj graph_obj;
      struct media_entity * entity;
      u16 index;
      unsigned long flags;
    };


Members
=======

graph_obj
    Embedded structure containing the media object common data

entity
    Entity this pad belongs to

index
    Pad index in the entity pads array, numbered from 0 to n

flags
    Pad flags, as defined in uapi/media.h (MEDIA_PAD_FL_⋆)
