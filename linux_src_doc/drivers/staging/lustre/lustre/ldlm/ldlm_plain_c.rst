.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ldlm/ldlm_plain.c

.. _`debug_subsystem`:

DEBUG_SUBSYSTEM
===============

.. c:function::  DEBUG_SUBSYSTEM()

.. _`debug_subsystem.description`:

Description
-----------

PLAIN locks are the simplest form of LDLM locking, and are used when
there only needs to be a single lock on a resource. This avoids some
of the complexity of EXTENT and IBITS lock types, but doesn't allow
different "parts" of a resource to be locked concurrently.  Example
use cases for PLAIN locks include locking of MGS configuration logs
and (as of Lustre 2.4) quota records.

.. This file was automatic generated / don't edit.

