.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ldlm/ldlm_extent.c

.. _`debug_subsystem`:

DEBUG_SUBSYSTEM
===============

.. c:function::  DEBUG_SUBSYSTEM()

.. _`debug_subsystem.description`:

Description
-----------

EXTENT lock type is for locking a contiguous range of values, represented
by 64-bit starting and ending offsets (inclusive). There are several extent
lock modes, some of which may be mutually incompatible. Extent locks are
considered incompatible if their modes are incompatible and their extents
intersect.  See the lock mode compatibility matrix in lustre_dlm.h.

.. This file was automatic generated / don't edit.

