.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/lcommon_cl.c

.. _`define_mutex`:

DEFINE_MUTEX
============

.. c:function::  DEFINE_MUTEX( cl_inode_fini_guard)

    pressure, when environments cannot be allocated.

    :param  cl_inode_fini_guard:
        *undescribed*

.. _`cl_file_inode_init`:

cl_file_inode_init
==================

.. c:function:: int cl_file_inode_init(struct inode *inode, struct lustre_md *md)

    meta-data arrives from the server.

    :param struct inode \*inode:
        *undescribed*

    :param struct lustre_md \*md:
        *undescribed*

.. _`cl_file_inode_init.description`:

Description
-----------

\param inode regular file inode
\param md    new file metadata from MDS
- allocates cl_object if necessary,
- updated layout, if object was already here.

.. _`cl_object_put_last`:

cl_object_put_last
==================

.. c:function:: void cl_object_put_last(struct lu_env *env, struct cl_object *obj)

    the last one, which will lead to the object be destroyed immediately. Must be called after \ :c:func:`cl_object_kill`\  against this object.

    :param struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

.. _`cl_object_put_last.the-reason-we-want-to-do-this-is`:

The reason we want to do this is
--------------------------------

destroying top object will wait for sub
objects being destroyed first, so we can't let bottom layer (e.g. from ASTs)
to initiate top object destroying which may deadlock. See bz22520.

.. _`cl_fid_build_ino`:

cl_fid_build_ino
================

.. c:function:: __u64 cl_fid_build_ino(const struct lu_fid *fid, int api32)

    :param const struct lu_fid \*fid:
        *undescribed*

    :param int api32:
        *undescribed*

.. _`cl_fid_build_gen`:

cl_fid_build_gen
================

.. c:function:: __u32 cl_fid_build_gen(const struct lu_fid *fid)

    bit inode number then return a non-zero generation to distinguish them.

    :param const struct lu_fid \*fid:
        *undescribed*

.. This file was automatic generated / don't edit.

