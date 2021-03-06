.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/cell/spufs/switch.c

.. _`stop_spu_isolate`:

stop_spu_isolate
================

.. c:function:: void stop_spu_isolate(struct spu *spu)

    Check SPU run-control state and force isolated exit function as necessary.

    :param spu:
        *undescribed*
    :type spu: struct spu \*

.. _`spu_save`:

spu_save
========

.. c:function:: int spu_save(struct spu_state *prev, struct spu *spu)

    SPU context save, with locking.

    :param prev:
        pointer to SPU context save area, to be saved.
    :type prev: struct spu_state \*

    :param spu:
        pointer to SPU iomem structure.
    :type spu: struct spu \*

.. _`spu_save.description`:

Description
-----------

Acquire locks, perform the save operation then return.

.. _`spu_restore`:

spu_restore
===========

.. c:function:: int spu_restore(struct spu_state *new, struct spu *spu)

    SPU context restore, with harvest and locking.

    :param new:
        pointer to SPU context save area, to be restored.
    :type new: struct spu_state \*

    :param spu:
        pointer to SPU iomem structure.
    :type spu: struct spu \*

.. _`spu_restore.description`:

Description
-----------

Perform harvest + restore, as we may not be coming
from a previous successful save operation, and the
hardware state is unknown.

.. _`spu_init_csa`:

spu_init_csa
============

.. c:function:: int spu_init_csa(struct spu_state *csa)

    allocate and initialize an SPU context save area.

    :param csa:
        *undescribed*
    :type csa: struct spu_state \*

.. _`spu_init_csa.description`:

Description
-----------

Allocate and initialize the contents of an SPU context save area.
This includes enabling address translation, interrupt masks, etc.,
as appropriate for the given OS environment.

Note that storage for the 'lscsa' is allocated separately,
as it is by far the largest of the context save regions,
and may need to be pinned or otherwise specially aligned.

.. This file was automatic generated / don't edit.

