.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/obdclass/cl_lock.c

.. _`cl_lock_slice_add`:

cl_lock_slice_add
=================

.. c:function:: void cl_lock_slice_add(struct cl_lock *lock, struct cl_lock_slice *slice, struct cl_object *obj, const struct cl_lock_operations *ops)

    :param struct cl_lock \*lock:
        *undescribed*

    :param struct cl_lock_slice \*slice:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param const struct cl_lock_operations \*ops:
        *undescribed*

.. _`cl_lock_slice_add.description`:

Description
-----------

This is called by cl_object_operations::\ :c:func:`coo_lock_init`\  methods to add a
per-layer state to the lock. New state is added at the end of
cl_lock::cll_layers list, that is, it is at the bottom of the stack.

\see \ :c:func:`cl_req_slice_add`\ , \ :c:func:`cl_page_slice_add`\ , \ :c:func:`cl_io_slice_add`\ 

.. _`cl_lock_at`:

cl_lock_at
==========

.. c:function:: const struct cl_lock_slice *cl_lock_at(const struct cl_lock *lock, const struct lu_device_type *dtype)

    device stack.

    :param const struct cl_lock \*lock:
        *undescribed*

    :param const struct lu_device_type \*dtype:
        *undescribed*

.. _`cl_lock_at.description`:

Description
-----------

\see \ :c:func:`cl_page_at`\ 

.. _`cl_lock_enqueue`:

cl_lock_enqueue
===============

.. c:function:: int cl_lock_enqueue(const struct lu_env *env, struct cl_io *io, struct cl_lock *lock, struct cl_sync_io *anchor)

    \param anchor: if we need to wait for resources before getting the lock, use \ ``anchor``\  for the purpose. \retval 0  enqueue successfully \retval <0 error code

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_lock \*lock:
        *undescribed*

    :param struct cl_sync_io \*anchor:
        *undescribed*

.. _`cl_lock_request`:

cl_lock_request
===============

.. c:function:: int cl_lock_request(const struct lu_env *env, struct cl_io *io, struct cl_lock *lock)

    level entry point of cl_lock interface that finds existing or enqueues new lock matching given description.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_lock \*lock:
        *undescribed*

.. _`cl_lock_release`:

cl_lock_release
===============

.. c:function:: void cl_lock_release(const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_lock \*lock:
        *undescribed*

.. _`cl_lock_descr_print`:

cl_lock_descr_print
===================

.. c:function:: void cl_lock_descr_print(const struct lu_env *env, void *cookie, lu_printer_t printer, const struct cl_lock_descr *descr)

    :param const struct lu_env \*env:
        *undescribed*

    :param void \*cookie:
        *undescribed*

    :param lu_printer_t printer:
        *undescribed*

    :param const struct cl_lock_descr \*descr:
        *undescribed*

.. _`cl_lock_print`:

cl_lock_print
=============

.. c:function:: void cl_lock_print(const struct lu_env *env, void *cookie, lu_printer_t printer, const struct cl_lock *lock)

    :param const struct lu_env \*env:
        *undescribed*

    :param void \*cookie:
        *undescribed*

    :param lu_printer_t printer:
        *undescribed*

    :param const struct cl_lock \*lock:
        *undescribed*

.. This file was automatic generated / don't edit.

