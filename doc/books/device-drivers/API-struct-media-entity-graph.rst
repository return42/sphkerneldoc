.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-media-entity-graph:

=========================
struct media_entity_graph
=========================

*man struct media_entity_graph(9)*

*4.6.0-rc5*

Media graph traversal state


Synopsis
========

.. code-block:: c

    struct media_entity_graph {
      struct stack[MEDIA_ENTITY_ENUM_MAX_DEPTH];
      struct media_entity_enum ent_enum;
      int top;
    };


Members
=======

stack[MEDIA_ENTITY_ENUM_MAX_DEPTH]
    Graph traversal stack; the stack contains information on the path
    the media entities to be walked and the links through which they
    were reached.

ent_enum
    Visited entities

top
    The top of the stack


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
