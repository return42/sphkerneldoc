
.. _API-struct-media-entity-graph:

=========================
struct media_entity_graph
=========================

*man struct media_entity_graph(9)*

*4.6.0-rc1*

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
    Graph traversal stack; the stack contains information on the path the media entities to be walked and the links through which they were reached.

ent_enum
    Visited entities

top
    The top of the stack
