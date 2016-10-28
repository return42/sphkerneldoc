.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ldlm/ldlm_inodebits.c

.. _`debug_subsystem`:

DEBUG_SUBSYSTEM
===============

.. c:function::  DEBUG_SUBSYSTEM()

.. _`debug_subsystem.description`:

Description
-----------

IBITS lock type contains a bit mask determining various properties of an
object. The meanings of specific bits are specific to the caller and are
opaque to LDLM code.

Locks with intersecting bitmasks and conflicting lock modes (e.g.  LCK_PW)
are considered conflicting.  See the lock mode compatibility matrix
in lustre_dlm.h.

.. This file was automatic generated / don't edit.

