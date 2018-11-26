.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/debugobjects.c

.. _`debug_object_init`:

debug_object_init
=================

.. c:function:: void debug_object_init(void *addr, struct debug_obj_descr *descr)

    debug checks when an object is initialized

    :param addr:
        address of the object
    :type addr: void \*

    :param descr:
        pointer to an object specific debug description structure
    :type descr: struct debug_obj_descr \*

.. _`debug_object_init_on_stack`:

debug_object_init_on_stack
==========================

.. c:function:: void debug_object_init_on_stack(void *addr, struct debug_obj_descr *descr)

    debug checks when an object on stack is initialized

    :param addr:
        address of the object
    :type addr: void \*

    :param descr:
        pointer to an object specific debug description structure
    :type descr: struct debug_obj_descr \*

.. _`debug_object_activate`:

debug_object_activate
=====================

.. c:function:: int debug_object_activate(void *addr, struct debug_obj_descr *descr)

    debug checks when an object is activated

    :param addr:
        address of the object
    :type addr: void \*

    :param descr:
        pointer to an object specific debug description structure
        Returns 0 for success, -EINVAL for check failed.
    :type descr: struct debug_obj_descr \*

.. _`debug_object_deactivate`:

debug_object_deactivate
=======================

.. c:function:: void debug_object_deactivate(void *addr, struct debug_obj_descr *descr)

    debug checks when an object is deactivated

    :param addr:
        address of the object
    :type addr: void \*

    :param descr:
        pointer to an object specific debug description structure
    :type descr: struct debug_obj_descr \*

.. _`debug_object_destroy`:

debug_object_destroy
====================

.. c:function:: void debug_object_destroy(void *addr, struct debug_obj_descr *descr)

    debug checks when an object is destroyed

    :param addr:
        address of the object
    :type addr: void \*

    :param descr:
        pointer to an object specific debug description structure
    :type descr: struct debug_obj_descr \*

.. _`debug_object_free`:

debug_object_free
=================

.. c:function:: void debug_object_free(void *addr, struct debug_obj_descr *descr)

    debug checks when an object is freed

    :param addr:
        address of the object
    :type addr: void \*

    :param descr:
        pointer to an object specific debug description structure
    :type descr: struct debug_obj_descr \*

.. _`debug_object_assert_init`:

debug_object_assert_init
========================

.. c:function:: void debug_object_assert_init(void *addr, struct debug_obj_descr *descr)

    debug checks when object should be init-ed

    :param addr:
        address of the object
    :type addr: void \*

    :param descr:
        pointer to an object specific debug description structure
    :type descr: struct debug_obj_descr \*

.. _`debug_object_active_state`:

debug_object_active_state
=========================

.. c:function:: void debug_object_active_state(void *addr, struct debug_obj_descr *descr, unsigned int expect, unsigned int next)

    debug checks object usage state machine

    :param addr:
        address of the object
    :type addr: void \*

    :param descr:
        pointer to an object specific debug description structure
    :type descr: struct debug_obj_descr \*

    :param expect:
        expected state
    :type expect: unsigned int

    :param next:
        state to move to if expected state is found
    :type next: unsigned int

.. This file was automatic generated / don't edit.

