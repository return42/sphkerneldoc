.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/ttm/ttm_memory.h

.. _`ttm_mem_shrink`:

struct ttm_mem_shrink
=====================

.. c:type:: struct ttm_mem_shrink

    callback to shrink TTM memory usage.

.. _`ttm_mem_shrink.definition`:

Definition
----------

.. code-block:: c

    struct ttm_mem_shrink {
        int (*do_shrink)(struct ttm_mem_shrink *);
    }

.. _`ttm_mem_shrink.members`:

Members
-------

do_shrink
    The callback function.

.. _`ttm_mem_shrink.description`:

Description
-----------

Arguments to the do_shrink functions are intended to be passed using
inheritance. That is, the argument class derives from struct ttm_mem_shrink,
and can be accessed using \ :c:func:`container_of`\ .

.. _`ttm_mem_init_shrink`:

ttm_mem_init_shrink
===================

.. c:function:: void ttm_mem_init_shrink(struct ttm_mem_shrink *shrink, int (*func)(struct ttm_mem_shrink *))

    initialize a struct ttm_mem_shrink object

    :param struct ttm_mem_shrink \*shrink:
        The object to initialize.

    :param int (\*func)(struct ttm_mem_shrink \*):
        The callback function.

.. _`ttm_mem_register_shrink`:

ttm_mem_register_shrink
=======================

.. c:function:: int ttm_mem_register_shrink(struct ttm_mem_global *glob, struct ttm_mem_shrink *shrink)

    register a struct ttm_mem_shrink object.

    :param struct ttm_mem_global \*glob:
        The struct ttm_mem_global object to register with.

    :param struct ttm_mem_shrink \*shrink:
        An initialized struct ttm_mem_shrink object to register.

.. _`ttm_mem_register_shrink.return`:

Return
------

-EBUSY: There's already a callback registered. (May change).

.. _`ttm_mem_unregister_shrink`:

ttm_mem_unregister_shrink
=========================

.. c:function:: void ttm_mem_unregister_shrink(struct ttm_mem_global *glob, struct ttm_mem_shrink *shrink)

    unregister a struct ttm_mem_shrink object.

    :param struct ttm_mem_global \*glob:
        The struct ttm_mem_global object to unregister from.

    :param struct ttm_mem_shrink \*shrink:
        A previously registert struct ttm_mem_shrink object.

.. This file was automatic generated / don't edit.

