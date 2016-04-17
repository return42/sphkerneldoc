.. -*- coding: utf-8; mode: rst -*-

========
switch.c
========


.. _`stop_spu_isolate`:

stop_spu_isolate
================

.. c:function:: void stop_spu_isolate (struct spu *spu)

    :param struct spu \*spu:

        *undescribed*



.. _`stop_spu_isolate.description`:

Description
-----------

Check SPU run-control state and force isolated
exit function as necessary.



.. _`spu_save`:

spu_save
========

.. c:function:: int spu_save (struct spu_state *prev, struct spu *spu)

    SPU context save, with locking.

    :param struct spu_state \*prev:
        pointer to SPU context save area, to be saved.

    :param struct spu \*spu:
        pointer to SPU iomem structure.



.. _`spu_save.description`:

Description
-----------

Acquire locks, perform the save operation then return.



.. _`spu_restore`:

spu_restore
===========

.. c:function:: int spu_restore (struct spu_state *new, struct spu *spu)

    SPU context restore, with harvest and locking.

    :param struct spu_state \*new:
        pointer to SPU context save area, to be restored.

    :param struct spu \*spu:
        pointer to SPU iomem structure.



.. _`spu_restore.description`:

Description
-----------

Perform harvest + restore, as we may not be coming
from a previous successful save operation, and the
hardware state is unknown.



.. _`spu_init_csa`:

spu_init_csa
============

.. c:function:: int spu_init_csa (struct spu_state *csa)

    allocate and initialize an SPU context save area.

    :param struct spu_state \*csa:

        *undescribed*



.. _`spu_init_csa.description`:

Description
-----------


Allocate and initialize the contents of an SPU context save area.
This includes enabling address translation, interrupt masks, etc.,
as appropriate for the given OS environment.

Note that storage for the 'lscsa' is allocated separately,
as it is by far the largest of the context save regions,
and may need to be pinned or otherwise specially aligned.

