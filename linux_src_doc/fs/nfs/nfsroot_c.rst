.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/nfsroot.c

.. _`nfs_root_data`:

nfs_root_data
=============

.. c:function:: int nfs_root_data(char **root_device, char **root_data)

    Return prepared 'data' for NFSROOT mount

    :param root_device:
        OUT: address of string containing NFSROOT device
    :type root_device: char \*\*

    :param root_data:
        OUT: address of string containing NFSROOT mount options
    :type root_data: char \*\*

.. _`nfs_root_data.description`:

Description
-----------

Returns zero and sets \ ``root_device``\  and \ ``root_data``\  if successful,
otherwise -1 is returned.

.. This file was automatic generated / don't edit.

