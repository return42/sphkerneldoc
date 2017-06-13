.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/filesystems.c

.. _`register_filesystem`:

register_filesystem
===================

.. c:function:: int register_filesystem(struct file_system_type *fs)

    register a new filesystem

    :param struct file_system_type \*fs:
        the file system structure

.. _`register_filesystem.description`:

Description
-----------

     Adds the file system passed to the list of file systems the kernel
     is aware of for mount and other syscalls. Returns 0 on success,
     or a negative errno code on an error.

     The \ :c:type:`struct file_system_type <file_system_type>`\  that is passed is linked into the kernel
     structures and must not be freed until the file system has been
     unregistered.

.. _`unregister_filesystem`:

unregister_filesystem
=====================

.. c:function:: int unregister_filesystem(struct file_system_type *fs)

    unregister a file system

    :param struct file_system_type \*fs:
        filesystem to unregister

.. _`unregister_filesystem.description`:

Description
-----------

     Remove a file system that was previously successfully registered
     with the kernel. An error is returned if the file system is not found.
     Zero is returned on a success.

     Once this function has returned the \ :c:type:`struct file_system_type <file_system_type>`\  structure
     may be freed or reused.

.. This file was automatic generated / don't edit.

