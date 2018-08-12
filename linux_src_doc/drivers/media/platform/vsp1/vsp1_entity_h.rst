.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/vsp1/vsp1_entity.h

.. _`vsp1_entity_operations`:

struct vsp1_entity_operations
=============================

.. c:type:: struct vsp1_entity_operations

    Entity operations

.. _`vsp1_entity_operations.definition`:

Definition
----------

.. code-block:: c

    struct vsp1_entity_operations {
        void (*destroy)(struct vsp1_entity *);
        void (*configure_stream)(struct vsp1_entity *, struct vsp1_pipeline *, struct vsp1_dl_body *);
        void (*configure_frame)(struct vsp1_entity *, struct vsp1_pipeline *, struct vsp1_dl_list *, struct vsp1_dl_body *);
        void (*configure_partition)(struct vsp1_entity *,struct vsp1_pipeline *,struct vsp1_dl_list *, struct vsp1_dl_body *);
        unsigned int (*max_width)(struct vsp1_entity *, struct vsp1_pipeline *);
        void (*partition)(struct vsp1_entity *, struct vsp1_pipeline *,struct vsp1_partition *, unsigned int, struct vsp1_partition_window *);
    }

.. _`vsp1_entity_operations.members`:

Members
-------

destroy
    Destroy the entity.

configure_stream
    Setup the hardware parameters for the stream which do
    not vary between frames (pipeline, formats).

configure_frame
    Configure the runtime parameters for each frame.

configure_partition
    Configure partition specific parameters.

max_width
    Return the max supported width of data that the entity can
    process in a single operation.

partition
    Process the partition construction based on this entity's
    configuration.

.. This file was automatic generated / don't edit.

