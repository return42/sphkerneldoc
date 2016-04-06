
.. _API-struct-media-link:

=================
struct media_link
=================

*man struct media_link(9)*

*4.6.0-rc1*

A link object part of a media graph.


Synopsis
========

.. code-block:: c

    struct media_link {
      struct media_gobj graph_obj;
      struct list_head list;
      union {unnamed_union};
      struct media_link * reverse;
      unsigned long flags;
      bool is_backlink;
    };


Members
=======

graph_obj
    Embedded structure containing the media object common data

list
    Linked list associated with an entity or an interface that owns the link.

{unnamed_union}
    anonymous

reverse
    Pointer to the link for the reverse direction of a pad to pad link.

flags
    Link flags, as defined in uapi/media.h (MEDIA_LNK_FL_⋆)

is_backlink
    Indicate if the link is a backlink.
