.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/namespace.c

.. _`nfs_do_submount`:

nfs_do_submount
===============

.. c:function:: struct vfsmount *nfs_do_submount(struct dentry *dentry, struct nfs_fh *fh, struct nfs_fattr *fattr, rpc_authflavor_t authflavor)

    set up mountpoint when crossing a filesystem boundary \ ``dentry``\  - parent directory \ ``fh``\  - filehandle for new root dentry \ ``fattr``\  - attributes for new root inode \ ``authflavor``\  - security flavor to use when performing the mount

    :param dentry:
        *undescribed*
    :type dentry: struct dentry \*

    :param fh:
        *undescribed*
    :type fh: struct nfs_fh \*

    :param fattr:
        *undescribed*
    :type fattr: struct nfs_fattr \*

    :param authflavor:
        *undescribed*
    :type authflavor: rpc_authflavor_t

.. This file was automatic generated / don't edit.

