.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mn10300/include/asm/mmu_context.h

.. _`allocate_mmu_context`:

allocate_mmu_context
====================

.. c:function:: unsigned long allocate_mmu_context(struct mm_struct *mm)

    Allocate storage for the arch-specific MMU data

    :param struct mm_struct \*mm:
        The userspace VM context being set up

.. _`destroy_context`:

destroy_context
===============

.. c:function::  destroy_context( mm)

    Destroy mm context information

    :param  mm:
        The MM being destroyed.

.. _`destroy_context.description`:

Description
-----------

Destroy context related info for an mm_struct that is about to be put to
rest

.. _`switch_mm`:

switch_mm
=========

.. c:function:: void switch_mm(struct mm_struct *prev, struct mm_struct *next, struct task_struct *tsk)

    Change between userspace virtual memory contexts

    :param struct mm_struct \*prev:
        The outgoing MM context.

    :param struct mm_struct \*next:
        The incoming MM context.

    :param struct task_struct \*tsk:
        The incoming task.

.. This file was automatic generated / don't edit.

