.. -*- coding: utf-8; mode: rst -*-

==============
debugobjects.c
==============

.. _`debug_object_init`:

debug_object_init
=================

.. c:function:: void debug_object_init (void *addr, struct debug_obj_descr *descr)

    debug checks when an object is initialized

    :param void \*addr:
        address of the object

    :param struct debug_obj_descr \*descr:
        pointer to an object specific debug description structure


.. _`debug_object_init_on_stack`:

debug_object_init_on_stack
==========================

.. c:function:: void debug_object_init_on_stack (void *addr, struct debug_obj_descr *descr)

    debug checks when an object on stack is initialized

    :param void \*addr:
        address of the object

    :param struct debug_obj_descr \*descr:
        pointer to an object specific debug description structure


.. _`debug_object_activate`:

debug_object_activate
=====================

.. c:function:: int debug_object_activate (void *addr, struct debug_obj_descr *descr)

    debug checks when an object is activated

    :param void \*addr:
        address of the object

    :param struct debug_obj_descr \*descr:
        pointer to an object specific debug description structure
        Returns 0 for success, -EINVAL for check failed.


.. _`debug_object_deactivate`:

debug_object_deactivate
=======================

.. c:function:: void debug_object_deactivate (void *addr, struct debug_obj_descr *descr)

    debug checks when an object is deactivated

    :param void \*addr:
        address of the object

    :param struct debug_obj_descr \*descr:
        pointer to an object specific debug description structure


.. _`debug_object_destroy`:

debug_object_destroy
====================

.. c:function:: void debug_object_destroy (void *addr, struct debug_obj_descr *descr)

    debug checks when an object is destroyed

    :param void \*addr:
        address of the object

    :param struct debug_obj_descr \*descr:
        pointer to an object specific debug description structure


.. _`debug_object_free`:

debug_object_free
=================

.. c:function:: void debug_object_free (void *addr, struct debug_obj_descr *descr)

    debug checks when an object is freed

    :param void \*addr:
        address of the object

    :param struct debug_obj_descr \*descr:
        pointer to an object specific debug description structure


.. _`debug_object_assert_init`:

debug_object_assert_init
========================

.. c:function:: void debug_object_assert_init (void *addr, struct debug_obj_descr *descr)

    debug checks when object should be init-ed

    :param void \*addr:
        address of the object

    :param struct debug_obj_descr \*descr:
        pointer to an object specific debug description structure


.. _`debug_object_active_state`:

debug_object_active_state
=========================

.. c:function:: void debug_object_active_state (void *addr, struct debug_obj_descr *descr, unsigned int expect, unsigned int next)

    debug checks object usage state machine

    :param void \*addr:
        address of the object

    :param struct debug_obj_descr \*descr:
        pointer to an object specific debug description structure

    :param unsigned int expect:
        expected state

    :param unsigned int next:
        state to move to if expected state is found

