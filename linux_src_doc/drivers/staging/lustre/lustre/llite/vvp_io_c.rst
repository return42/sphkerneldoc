.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/vvp_io.c

.. _`cl_is_normalio`:

cl_is_normalio
==============

.. c:function:: int cl_is_normalio(const struct lu_env *env, const struct cl_io *io)

    :param const struct lu_env \*env:
        *undescribed*

    :param const struct cl_io \*io:
        *undescribed*

.. _`can_populate_pages`:

can_populate_pages
==================

.. c:function:: bool can_populate_pages(const struct lu_env *env, struct cl_io *io, struct inode *inode)

    To avoid populating pages to a wrong stripe, we have to verify the correctness of layout. It works because swapping layout processes have to acquire group lock.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct inode \*inode:
        *undescribed*

.. _`vvp_prep_size`:

vvp_prep_size
=============

.. c:function:: int vvp_prep_size(const struct lu_env *env, struct cl_object *obj, struct cl_io *io, loff_t start, size_t count, int *exceed)

    >i_size), when position at the offset \a pos is accessed. File size can be arbitrary stale on a Lustre client, but client at least knows KMS. If accessed area is inside [0, KMS], set file size to KMS, otherwise glimpse file size.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param loff_t start:
        *undescribed*

    :param size_t count:
        *undescribed*

    :param int \*exceed:
        *undescribed*

.. _`vvp_prep_size.locking`:

Locking
-------

cl_isize_lock is used to serialize changes to inode size and to
protect consistency between inode size and cl_object
attributes. \ :c:func:`cl_object_size_lock`\  protects consistency between cl_attr's of
top-object and sub-objects.

.. _`vvp_io_setattr_lock`:

vvp_io_setattr_lock
===================

.. c:function:: int vvp_io_setattr_lock(const struct lu_env *env, const struct cl_io_slice *ios)

    :\ :c:func:`vio_lock`\  method for CIT_SETATTR io.

    :param const struct lu_env \*env:
        *undescribed*

    :param const struct cl_io_slice \*ios:
        *undescribed*

.. _`vvp_io_setattr_lock.description`:

Description
-----------

Handles "lockless io" mode when extent locking is done by server.

.. This file was automatic generated / don't edit.

