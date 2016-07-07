.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/mount_clnt.c

.. _`nfs_mount`:

nfs_mount
=========

.. c:function:: int nfs_mount(struct nfs_mount_request *info)

    Obtain an NFS file handle for the given host and path

    :param struct nfs_mount_request \*info:
        pointer to mount request arguments

.. _`nfs_mount.description`:

Description
-----------

Uses default timeout parameters specified by underlying transport. On
successful return, the auth_flavs list and auth_flav_len will be populated
with the list from the server or a faked-up list if the server didn't
provide one.

.. _`nfs_umount`:

nfs_umount
==========

.. c:function:: void nfs_umount(const struct nfs_mount_request *info)

    Notify a server that we have unmounted this export

    :param const struct nfs_mount_request \*info:
        pointer to umount request arguments

.. _`nfs_umount.description`:

Description
-----------

MOUNTPROC_UMNT is advisory, so we set a short timeout, and always
use UDP.

.. This file was automatic generated / don't edit.

