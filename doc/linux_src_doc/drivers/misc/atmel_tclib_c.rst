.. -*- coding: utf-8; mode: rst -*-

=============
atmel_tclib.c
=============


.. _`atmel_tc_alloc`:

atmel_tc_alloc
==============

.. c:function:: struct atmel_tc *atmel_tc_alloc (unsigned block)

    allocate a specified TC block

    :param unsigned block:
        which block to allocate



.. _`atmel_tc_alloc.description`:

Description
-----------

Caller allocates a block.  If it is available, a pointer to a
pre-initialized struct atmel_tc is returned. The caller can access
the registers directly through the "regs" field.



.. _`atmel_tc_free`:

atmel_tc_free
=============

.. c:function:: void atmel_tc_free (struct atmel_tc *tc)

    release a specified TC block

    :param struct atmel_tc \*tc:
        Timer/counter block that was returned by :c:func:`atmel_tc_alloc`



.. _`atmel_tc_free.description`:

Description
-----------

This reverses the effect of :c:func:`atmel_tc_alloc`, invalidating the resource
returned by that routine and making the TC available to other drivers.

