.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/namespace.c

.. _`nfs_do_submount`:

nfs_do_submount
===============

.. c:function:: struct vfsmount *nfs_do_submount(struct dentry *dentry, struct nfs_fh *fh, struct nfs_fattr *fattr, rpc_authflavor_t authflavor)

    set up mountpoint when crossing a filesystem boundary \ ``dentry``\  - parent directory \ ``fh``\  - filehandle for new root dentry \ ``fattr``\  - attributes for new root inode \ ``authflavor``\  - security flavor to use when performing the mount

    :param struct dentry \*dentry:
        *undescribed*

    :param struct nfs_fh \*fh:
        *undescribed*

    :param struct nfs_fattr \*fattr:
        *undescribed*

    :param rpc_authflavor_t authflavor:
        *undescribed*

.. This file was automatic generated / don't edit.

