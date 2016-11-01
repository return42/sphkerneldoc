.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/ttm/ttm_placement.h

.. _`ttm_place`:

struct ttm_place
================

.. c:type:: struct ttm_place


.. _`ttm_place.definition`:

Definition
----------

.. code-block:: c

    struct ttm_place {
        unsigned fpfn;
        unsigned lpfn;
        uint32_t flags;
    }

.. _`ttm_place.members`:

Members
-------

fpfn
    first valid page frame number to put the object

lpfn
    last valid page frame number to put the object

flags
    memory domain and caching flags for the object

.. _`ttm_place.description`:

Description
-----------

Structure indicating a possible place to put an object.

.. _`ttm_placement`:

struct ttm_placement
====================

.. c:type:: struct ttm_placement


.. _`ttm_placement.definition`:

Definition
----------

.. code-block:: c

    struct ttm_placement {
        unsigned num_placement;
        const struct ttm_place *placement;
        unsigned num_busy_placement;
        const struct ttm_place *busy_placement;
    }

.. _`ttm_placement.members`:

Members
-------

num_placement
    number of preferred placements

placement
    preferred placements

num_busy_placement
    number of preferred placements when need to evict buffer

busy_placement
    preferred placements when need to evict buffer

.. _`ttm_placement.description`:

Description
-----------

Structure indicating the placement you request for an object.

.. This file was automatic generated / don't edit.

