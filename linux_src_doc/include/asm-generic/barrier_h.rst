.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/barrier.h

.. _`smp_acquire__after_ctrl_dep`:

smp_acquire__after_ctrl_dep
===========================

.. c:function::  smp_acquire__after_ctrl_dep( void)

    Provide ACQUIRE ordering after a control dependency

    :param  void:
        no arguments

.. _`smp_acquire__after_ctrl_dep.description`:

Description
-----------

A control dependency provides a LOAD->STORE order, the additional RMB
provides LOAD->LOAD order, together they provide LOAD->{LOAD,STORE} order,
aka. (load)-ACQUIRE.

Architectures that do not do load speculation can have this be \ :c:func:`barrier`\ .

.. _`smp_cond_load_acquire`:

smp_cond_load_acquire
=====================

.. c:function::  smp_cond_load_acquire( ptr,  cond_expr)

    (Spin) wait for cond with ACQUIRE ordering

    :param  ptr:
        pointer to the variable to wait on

    :param  cond_expr:
        *undescribed*

.. _`smp_cond_load_acquire.description`:

Description
-----------

Equivalent to using \ :c:func:`smp_load_acquire`\  on the condition variable but employs
the control dependency of the wait to reduce the barrier on many platforms.

Due to C lacking lambda expressions we load the value of \*ptr into a
pre-named variable \ ``VAL``\  to be used in \ ``cond``\ .

.. This file was automatic generated / don't edit.

