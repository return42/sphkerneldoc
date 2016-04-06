
.. _API-struct-media-entity-operations:

==============================
struct media_entity_operations
==============================

*man struct media_entity_operations(9)*

*4.6.0-rc1*

Media entity operations


Synopsis
========

.. code-block:: c

    struct media_entity_operations {
      int (* link_setup) (struct media_entity *entity,const struct media_pad *local,const struct media_pad *remote, u32 flags);
      int (* link_validate) (struct media_link *link);
    };


Members
=======

link_setup
    Notify the entity of link changes. The operation can return an error, in which case link setup will be cancelled. Optional.

link_validate
    Return whether a link is valid from the entity point of view. The ``media_entity_pipeline_start`` function validates all links by calling this operation. Optional.
