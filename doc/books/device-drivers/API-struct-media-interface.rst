
.. _API-struct-media-interface:

======================
struct media_interface
======================

*man struct media_interface(9)*

*4.6.0-rc1*

A media interface graph object.


Synopsis
========

.. code-block:: c

    struct media_interface {
      struct media_gobj graph_obj;
      struct list_head links;
      u32 type;
      u32 flags;
    };


Members
=======

graph_obj
    embedded graph object

links
    List of links pointing to graph entities

type
    Type of the interface as defined in the uapi/media/media.h header, e. g. MEDIA_INTF_T_⋆

flags
    Interface flags as defined in uapi/media/media.h
