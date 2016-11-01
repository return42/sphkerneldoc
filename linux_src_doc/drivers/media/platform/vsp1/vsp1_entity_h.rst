.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/vsp1/vsp1_entity.h

.. _`vsp1_entity_params`:

enum vsp1_entity_params
=======================

.. c:type:: enum vsp1_entity_params

    Entity configuration parameters class \ ``VSP1_ENTITY_PARAMS_INIT``\  - Initial parameters \ ``VSP1_ENTITY_PARAMS_PARTITION``\  - Per-image partition parameters \ ``VSP1_ENTITY_PARAMS_RUNTIME``\  - Runtime-configurable parameters

.. _`vsp1_entity_params.definition`:

Definition
----------

.. code-block:: c

    enum vsp1_entity_params {
        VSP1_ENTITY_PARAMS_INIT,
        VSP1_ENTITY_PARAMS_PARTITION,
        VSP1_ENTITY_PARAMS_RUNTIME
    };

.. _`vsp1_entity_params.constants`:

Constants
---------

VSP1_ENTITY_PARAMS_INIT
    *undescribed*

VSP1_ENTITY_PARAMS_PARTITION
    *undescribed*

VSP1_ENTITY_PARAMS_RUNTIME
    *undescribed*

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
        void (*configure)(struct vsp1_entity *, struct vsp1_pipeline *,struct vsp1_dl_list *, enum vsp1_entity_params);
        unsigned int (*max_width)(struct vsp1_entity *, struct vsp1_pipeline *);
    }

.. _`vsp1_entity_operations.members`:

Members
-------

destroy
    Destroy the entity.

configure
    Setup the hardware based on the entity state (pipeline, formats,
    selection rectangles, ...)

max_width
    Return the max supported width of data that the entity can
    process in a single operation.

.. This file was automatic generated / don't edit.

