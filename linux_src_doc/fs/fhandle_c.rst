.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fhandle.c

.. _`sys_name_to_handle_at`:

sys_name_to_handle_at
=====================

.. c:function:: long sys_name_to_handle_at(int dfd, const char __user *name, struct file_handle __user *handle, int __user *mnt_id, int flag)

    convert name to handle

    :param int dfd:
        directory relative to which name is interpreted if not absolute

    :param const char __user \*name:
        name that should be converted to handle.

    :param struct file_handle __user \*handle:
        resulting file handle

    :param int __user \*mnt_id:
        mount id of the file system containing the file

    :param int flag:
        flag value to indicate whether to follow symlink or not

.. _`sys_name_to_handle_at.description`:

Description
-----------

\ ``handle``\ ->handle_size indicate the space available to store the
variable part of the file handle in bytes. If there is not
enough space, the field is updated to return the minimum
value required.

.. _`sys_open_by_handle_at`:

sys_open_by_handle_at
=====================

.. c:function:: long sys_open_by_handle_at(int mountdirfd, struct file_handle __user *handle, int flags)

    Open the file handle

    :param int mountdirfd:
        directory file descriptor

    :param struct file_handle __user \*handle:
        file handle to be opened

    :param int flags:
        *undescribed*

.. _`sys_open_by_handle_at.description`:

Description
-----------

\ ``mountdirfd``\  indicate the directory file descriptor
of the mount point. file handle is decoded relative
to the vfsmount pointed by the \ ``mountdirfd``\ . \ ``flags``\ 
value is same as the open(2) flags.

.. This file was automatic generated / don't edit.

