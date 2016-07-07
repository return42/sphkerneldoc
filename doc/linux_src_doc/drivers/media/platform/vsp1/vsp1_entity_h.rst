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
        void (* destroy) (struct vsp1_entity *);
        void (* set_memory) (struct vsp1_entity *, struct vsp1_dl_list *dl);
        void (* configure) (struct vsp1_entity *, struct vsp1_pipeline *,struct vsp1_dl_list *);
    }

.. _`vsp1_entity_operations.members`:

Members
-------

destroy
    Destroy the entity.

set_memory
    Setup memory buffer access. This operation applies the settings
    stored in the rwpf mem field to the display list. Valid for RPF
    and WPF only.

configure
    Setup the hardware based on the entity state (pipeline, formats,
    selection rectangles, ...)

.. This file was automatic generated / don't edit.

