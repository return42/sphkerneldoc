.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/lov/lov_io.c

.. _`lov_io_submit`:

lov_io_submit
=============

.. c:function:: int lov_io_submit(const struct lu_env *env, const struct cl_io_slice *ios, enum cl_req_type crt, struct cl_2queue *queue)

    :cio_submit() method. It takes a list of pages in \a queue, splits it into per-stripe sub-lists, invokes \ :c:func:`cl_io_submit`\  on underlying devices to submit sub-lists, and then splices everything back.

    :param const struct lu_env \*env:
        *undescribed*

    :param const struct cl_io_slice \*ios:
        *undescribed*

    :param enum cl_req_type crt:
        *undescribed*

    :param struct cl_2queue \*queue:
        *undescribed*

.. _`lov_io_submit.major-complication-of-this-function-is-a-need-to-handle-memory-cleansing`:

Major complication of this function is a need to handle memory cleansing
------------------------------------------------------------------------

\ :c:func:`cl_io_submit`\  is called to write out pages as a part of VM memory
reclamation, and hence it may not fail due to memory shortages (system
dead-locks otherwise). To deal with this, some resources (sub-lists,
sub-environment, etc.) are allocated per-device on "startup" (i.e., in a
not-memory cleansing context), and in case of memory shortage, these
pre-allocated resources are used by \ :c:func:`lov_io_submit`\  under
lov_device::ld_mutex mutex.

.. This file was automatic generated / don't edit.

