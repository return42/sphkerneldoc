.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/namespace.c

.. _`__mnt_want_write`:

\__mnt_want_write
=================

.. c:function:: int __mnt_want_write(struct vfsmount *m)

    get write access to a mount without freeze protection

    :param m:
        the mount on which to take a write
    :type m: struct vfsmount \*

.. _`__mnt_want_write.description`:

Description
-----------

This tells the low-level filesystem that a write is about to be performed to
it, and makes sure that writes are allowed (mnt it read-write) before
returning success. This operation does not protect against filesystem being
frozen. When the write operation is finished, \__mnt_drop_write() must be
called. This is effectively a refcount.

.. _`mnt_want_write`:

mnt_want_write
==============

.. c:function:: int mnt_want_write(struct vfsmount *m)

    get write access to a mount

    :param m:
        the mount on which to take a write
    :type m: struct vfsmount \*

.. _`mnt_want_write.description`:

Description
-----------

This tells the low-level filesystem that a write is about to be performed to
it, and makes sure that writes are allowed (mount is read-write, filesystem
is not frozen) before returning success.  When the write operation is
finished, \ :c:func:`mnt_drop_write`\  must be called.  This is effectively a refcount.

.. _`mnt_clone_write`:

mnt_clone_write
===============

.. c:function:: int mnt_clone_write(struct vfsmount *mnt)

    get write access to a mount

    :param mnt:
        the mount on which to take a write
    :type mnt: struct vfsmount \*

.. _`mnt_clone_write.description`:

Description
-----------

This is effectively like mnt_want_write, except
it must only be used to take an extra write reference
on a mountpoint that we already know has a write reference
on it. This allows some optimisation.

After finished, mnt_drop_write must be called as usual to
drop the reference.

.. _`__mnt_want_write_file`:

\__mnt_want_write_file
======================

.. c:function:: int __mnt_want_write_file(struct file *file)

    get write access to a file's mount

    :param file:
        the file who's mount on which to take a write
    :type file: struct file \*

.. _`__mnt_want_write_file.description`:

Description
-----------

This is like \__mnt_want_write, but it takes a file and can
do some optimisations if the file is open for write already

.. _`mnt_want_write_file`:

mnt_want_write_file
===================

.. c:function:: int mnt_want_write_file(struct file *file)

    get write access to a file's mount

    :param file:
        the file who's mount on which to take a write
    :type file: struct file \*

.. _`mnt_want_write_file.description`:

Description
-----------

This is like mnt_want_write, but it takes a file and can
do some optimisations if the file is open for write already

.. _`__mnt_drop_write`:

\__mnt_drop_write
=================

.. c:function:: void __mnt_drop_write(struct vfsmount *mnt)

    give up write access to a mount

    :param mnt:
        the mount on which to give up write access
    :type mnt: struct vfsmount \*

.. _`__mnt_drop_write.description`:

Description
-----------

Tells the low-level filesystem that we are done
performing writes to it.  Must be matched with
\__mnt_want_write() call above.

.. _`mnt_drop_write`:

mnt_drop_write
==============

.. c:function:: void mnt_drop_write(struct vfsmount *mnt)

    give up write access to a mount

    :param mnt:
        the mount on which to give up write access
    :type mnt: struct vfsmount \*

.. _`mnt_drop_write.description`:

Description
-----------

Tells the low-level filesystem that we are done performing writes to it and
also allows filesystem to be frozen again.  Must be matched with
\ :c:func:`mnt_want_write`\  call above.

.. _`may_umount_tree`:

may_umount_tree
===============

.. c:function:: int may_umount_tree(struct vfsmount *m)

    check if a mount tree is busy

    :param m:
        *undescribed*
    :type m: struct vfsmount \*

.. _`may_umount_tree.description`:

Description
-----------

This is called to check if a tree of mounts has any
open files, pwds, chroots or sub mounts that are
busy.

.. _`may_umount`:

may_umount
==========

.. c:function:: int may_umount(struct vfsmount *mnt)

    check if a mount point is busy

    :param mnt:
        root of mount
    :type mnt: struct vfsmount \*

.. _`may_umount.description`:

Description
-----------

This is called to check if a mount point has any
open files, pwds, chroots or sub mounts. If the
mount has sub mounts this will return busy
regardless of whether the sub mounts are busy.

Doesn't take quota and stuff into account. IOW, in some cases it will
give false negatives. The main reason why it's here is that we need
a non-destructive way to look for easily umountable filesystems.

.. _`clone_private_mount`:

clone_private_mount
===================

.. c:function:: struct vfsmount *clone_private_mount(const struct path *path)

    create a private clone of a path

    :param path:
        *undescribed*
    :type path: const struct path \*

.. _`clone_private_mount.description`:

Description
-----------

This creates a new vfsmount, which will be the clone of \ ``path``\ .  The new will
not be attached anywhere in the namespace and will be private (i.e. changes
to the originating mount won't be propagated into this).

Release with \ :c:func:`mntput`\ .

.. _`mnt_set_expiry`:

mnt_set_expiry
==============

.. c:function:: void mnt_set_expiry(struct vfsmount *mnt, struct list_head *expiry_list)

    Put a mount on an expiration list

    :param mnt:
        The mount to list.
    :type mnt: struct vfsmount \*

    :param expiry_list:
        The list to add the mount to.
    :type expiry_list: struct list_head \*

.. _`create_mnt_ns`:

create_mnt_ns
=============

.. c:function:: struct mnt_namespace *create_mnt_ns(struct vfsmount *m)

    creates a private namespace and adds a root filesystem

    :param m:
        *undescribed*
    :type m: struct vfsmount \*

.. This file was automatic generated / don't edit.

