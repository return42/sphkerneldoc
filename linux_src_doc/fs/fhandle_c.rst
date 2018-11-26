.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fhandle.c

.. _`sys_name_to_handle_at`:

sys_name_to_handle_at
=====================

.. c:function:: long sys_name_to_handle_at(int dfd, const char __user *name, struct file_handle __user *handle, int __user *mnt_id, int flag)

    convert name to handle

    :param dfd:
        directory relative to which name is interpreted if not absolute
    :type dfd: int

    :param name:
        name that should be converted to handle.
    :type name: const char __user \*

    :param handle:
        resulting file handle
    :type handle: struct file_handle __user \*

    :param mnt_id:
        mount id of the file system containing the file
    :type mnt_id: int __user \*

    :param flag:
        flag value to indicate whether to follow symlink or not
    :type flag: int

.. _`sys_name_to_handle_at.description`:

Description
-----------

\ ``handle->handle_size``\  indicate the space available to store the
variable part of the file handle in bytes. If there is not
enough space, the field is updated to return the minimum
value required.

.. _`sys_open_by_handle_at`:

sys_open_by_handle_at
=====================

.. c:function:: long sys_open_by_handle_at(int mountdirfd, struct file_handle __user *handle, int flags)

    Open the file handle

    :param mountdirfd:
        directory file descriptor
    :type mountdirfd: int

    :param handle:
        file handle to be opened
    :type handle: struct file_handle __user \*

    :param flags:
        *undescribed*
    :type flags: int

.. _`sys_open_by_handle_at.description`:

Description
-----------

\ ``mountdirfd``\  indicate the directory file descriptor
of the mount point. file handle is decoded relative
to the vfsmount pointed by the \ ``mountdirfd``\ . \ ``flags``\ 
value is same as the open(2) flags.

.. This file was automatic generated / don't edit.

