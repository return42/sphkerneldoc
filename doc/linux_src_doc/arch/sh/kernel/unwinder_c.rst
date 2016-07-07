.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/kernel/unwinder.c

.. _`select_unwinder`:

select_unwinder
===============

.. c:function:: struct unwinder *select_unwinder( void)

    Select the best registered stack unwinder.

    :param  void:
        no arguments

.. _`select_unwinder.description`:

Description
-----------

Private function. Must hold unwinder_lock when called.

Select the stack unwinder with the best rating. This is useful for
setting up curr_unwinder.

.. _`unwinder_register`:

unwinder_register
=================

.. c:function:: int unwinder_register(struct unwinder *u)

    Used to install new stack unwinder

    :param struct unwinder \*u:
        unwinder to be registered

.. _`unwinder_register.description`:

Description
-----------

Install the new stack unwinder on the unwinder list, which is sorted
by rating.

Returns -EBUSY if registration fails, zero otherwise.

.. This file was automatic generated / don't edit.

