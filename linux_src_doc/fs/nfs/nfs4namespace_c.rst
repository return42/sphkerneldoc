.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/nfs4namespace.c

.. _`nfs_find_best_sec`:

nfs_find_best_sec
=================

.. c:function:: struct rpc_clnt *nfs_find_best_sec(struct rpc_clnt *clnt, struct nfs_server *server, struct nfs4_secinfo_flavors *flavors)

    Find a security mechanism supported locally

    :param clnt:
        *undescribed*
    :type clnt: struct rpc_clnt \*

    :param server:
        NFS server struct
    :type server: struct nfs_server \*

    :param flavors:
        List of security tuples returned by SECINFO procedure
    :type flavors: struct nfs4_secinfo_flavors \*

.. _`nfs_find_best_sec.description`:

Description
-----------

Return an rpc client that uses the first security mechanism in
"flavors" that is locally supported.  The "flavors" array
is searched in the order returned from the server, per RFC 3530
recommendation and each flavor is checked for membership in the
sec= mount option list if it exists.

Return -EPERM if no matching flavor is found in the array.

Please call \ :c:func:`rpc_shutdown_client`\  when you are done with this rpc client.

.. _`nfs4_negotiate_security`:

nfs4_negotiate_security
=======================

.. c:function:: struct rpc_clnt *nfs4_negotiate_security(struct rpc_clnt *clnt, struct inode *inode, const struct qstr *name)

    in response to an NFS4ERR_WRONGSEC on lookup, return an rpc_clnt that uses the best available security flavor with respect to the secinfo flavor list and the sec= mount options.

    :param clnt:
        RPC client to clone
    :type clnt: struct rpc_clnt \*

    :param inode:
        directory inode
    :type inode: struct inode \*

    :param name:
        lookup name
    :type name: const struct qstr \*

.. _`nfs4_negotiate_security.description`:

Description
-----------

Please call \ :c:func:`rpc_shutdown_client`\  when you are done with this rpc client.

.. _`nfs_follow_referral`:

nfs_follow_referral
===================

.. c:function:: struct vfsmount *nfs_follow_referral(struct dentry *dentry, const struct nfs4_fs_locations *locations)

    set up mountpoint when hitting a referral on moved error \ ``dentry``\  - parent directory \ ``locations``\  - array of NFSv4 server location information

    :param dentry:
        *undescribed*
    :type dentry: struct dentry \*

    :param locations:
        *undescribed*
    :type locations: const struct nfs4_fs_locations \*

.. _`nfs4_replace_transport`:

nfs4_replace_transport
======================

.. c:function:: int nfs4_replace_transport(struct nfs_server *server, const struct nfs4_fs_locations *locations)

    set up transport to destination server

    :param server:
        export being migrated
    :type server: struct nfs_server \*

    :param locations:
        fs_locations array
    :type locations: const struct nfs4_fs_locations \*

.. _`nfs4_replace_transport.description`:

Description
-----------

Returns zero on success, or a negative errno value.

The client tries all the entries in the "locations" array, in the
order returned by the server, until one works or the end of the
array is reached.

.. This file was automatic generated / don't edit.

