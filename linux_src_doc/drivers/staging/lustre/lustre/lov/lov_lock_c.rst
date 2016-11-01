.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/lov/lov_lock.c

.. _`lov_lock_sub_init`:

lov_lock_sub_init
=================

.. c:function:: struct lov_lock *lov_lock_sub_init(const struct lu_env *env, const struct cl_object *obj, struct cl_lock *lock)

    locks for a given lov_lock for the first time.

    :param const struct lu_env \*env:
        *undescribed*

    :param const struct cl_object \*obj:
        *undescribed*

    :param struct cl_lock \*lock:
        *undescribed*

.. _`lov_lock_sub_init.description`:

Description
-----------

Goes through all sub-objects of top-object, and creates sub-locks on every
sub-object intersecting with top-lock extent. This is complicated by the
fact that top-lock (that is being created) can be accessed concurrently
through already created sub-locks (possibly shared with other top-locks).

.. _`lov_lock_enqueue`:

lov_lock_enqueue
================

.. c:function:: int lov_lock_enqueue(const struct lu_env *env, const struct cl_lock_slice *slice, struct cl_io *io, struct cl_sync_io *anchor)

    :clo_enqueue() for lov layer. This function is rather subtle, as it enqueues top-lock (i.e., advances top-lock state machine from CLS_QUEUING to CLS_ENQUEUED states) by juggling sub-lock state machines in the face of sub-locks sharing (by multiple top-locks), and concurrent sub-lock cancellations.

    :param const struct lu_env \*env:
        *undescribed*

    :param const struct cl_lock_slice \*slice:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_sync_io \*anchor:
        *undescribed*

.. This file was automatic generated / don't edit.

