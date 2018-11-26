.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/atmel_tclib.c

.. _`atmel_tc_alloc`:

atmel_tc_alloc
==============

.. c:function:: struct atmel_tc *atmel_tc_alloc(unsigned block)

    allocate a specified TC block

    :param block:
        which block to allocate
    :type block: unsigned

.. _`atmel_tc_alloc.description`:

Description
-----------

Caller allocates a block.  If it is available, a pointer to a
pre-initialized struct atmel_tc is returned. The caller can access
the registers directly through the "regs" field.

.. _`atmel_tc_free`:

atmel_tc_free
=============

.. c:function:: void atmel_tc_free(struct atmel_tc *tc)

    release a specified TC block

    :param tc:
        Timer/counter block that was returned by \ :c:func:`atmel_tc_alloc`\ 
    :type tc: struct atmel_tc \*

.. _`atmel_tc_free.description`:

Description
-----------

This reverses the effect of \ :c:func:`atmel_tc_alloc`\ , invalidating the resource
returned by that routine and making the TC available to other drivers.

.. This file was automatic generated / don't edit.

