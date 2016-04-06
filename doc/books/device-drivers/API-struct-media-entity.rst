
.. _API-struct-media-entity:

===================
struct media_entity
===================

*man struct media_entity(9)*

*4.6.0-rc1*

A media entity graph object.


Synopsis
========

.. code-block:: c

    struct media_entity {
      struct media_gobj graph_obj;
      const char * name;
      u32 function;
      unsigned long flags;
      u16 num_pads;
      u16 num_links;
      u16 num_backlinks;
      int internal_idx;
      struct media_pad * pads;
      struct list_head links;
      const struct media_entity_operations * ops;
      int stream_count;
      int use_count;
      struct media_pipeline * pipe;
      union info;
    };


Members
=======

graph_obj
    Embedded structure containing the media object common data.

name
    Entity name.

function
    Entity main function, as defined in uapi/media.h (MEDIA_ENT_F_⋆)

flags
    Entity flags, as defined in uapi/media.h (MEDIA_ENT_FL_⋆)

num_pads
    Number of sink and source pads.

num_links
    Total number of links, forward and back, enabled and disabled.

num_backlinks
    Number of backlinks

internal_idx
    An unique internal entity specific number. The numbers are re-used if entities are unregistered or registered again.

pads
    Pads array with the size defined by ``num_pads``.

links
    List of data links.

ops
    Entity operations.

stream_count
    Stream count for the entity.

use_count
    Use count for the entity.

pipe
    Pipeline this entity belongs to.

info
    Union with devnode information. Kept just for backward compatibility.


NOTE
====

``stream_count`` and ``use_count`` reference counts must never be negative, but are signed integers on purpose: a simple WARN_ON(<0) check can be used to detect reference count
bugs that would make them negative.
