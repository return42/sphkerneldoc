.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/nfs4proc.c

.. _`nfs41_check_expired_locks`:

nfs41_check_expired_locks
=========================

.. c:function:: int nfs41_check_expired_locks(struct nfs4_state *state)

    possibly free a lock stateid

    :param struct nfs4_state \*state:
        NFSv4 state for an inode

.. _`nfs41_check_expired_locks.description`:

Description
-----------

Returns NFS_OK if recovery for this stateid is now finished.
Otherwise a negative NFS4ERR value is returned.

.. _`nfs41_check_open_stateid`:

nfs41_check_open_stateid
========================

.. c:function:: int nfs41_check_open_stateid(struct nfs4_state *state)

    possibly free an open stateid

    :param struct nfs4_state \*state:
        NFSv4 state for an inode

.. _`nfs41_check_open_stateid.description`:

Description
-----------

Returns NFS_OK if recovery for this stateid is now finished.
Otherwise a negative NFS4ERR value is returned.

.. _`nfs4_proc_get_rootfh`:

nfs4_proc_get_rootfh
====================

.. c:function:: int nfs4_proc_get_rootfh(struct nfs_server *server, struct nfs_fh *fhandle, struct nfs_fsinfo *info, bool auth_probe)

    get file handle for server's pseudoroot

    :param struct nfs_server \*server:
        initialized nfs_server handle

    :param struct nfs_fh \*fhandle:
        we fill in the pseudo-fs root file handle

    :param struct nfs_fsinfo \*info:
        we fill in an FSINFO struct

    :param bool auth_probe:
        probe the auth flavours

.. _`nfs4_proc_get_rootfh.description`:

Description
-----------

Returns zero on success, or a negative errno.

.. _`nfs4_proc_setclientid`:

nfs4_proc_setclientid
=====================

.. c:function:: int nfs4_proc_setclientid(struct nfs_client *clp, u32 program, unsigned short port, struct rpc_cred *cred, struct nfs4_setclientid_res *res)

    Negotiate client ID

    :param struct nfs_client \*clp:
        state data structure

    :param u32 program:
        RPC program for NFSv4 callback service

    :param unsigned short port:
        IP port number for NFS4 callback service

    :param struct rpc_cred \*cred:
        RPC credential to use for this call

    :param struct nfs4_setclientid_res \*res:
        where to place the result

.. _`nfs4_proc_setclientid.description`:

Description
-----------

Returns zero, a negative errno, or a negative NFS4ERR status code.

.. _`nfs4_proc_setclientid_confirm`:

nfs4_proc_setclientid_confirm
=============================

.. c:function:: int nfs4_proc_setclientid_confirm(struct nfs_client *clp, struct nfs4_setclientid_res *arg, struct rpc_cred *cred)

    Confirm client ID

    :param struct nfs_client \*clp:
        state data structure

    :param struct nfs4_setclientid_res \*arg:
        *undescribed*

    :param struct rpc_cred \*cred:
        RPC credential to use for this call

.. _`nfs4_proc_setclientid_confirm.description`:

Description
-----------

Returns zero, a negative errno, or a negative NFS4ERR status code.

.. _`nfs4_proc_get_locations`:

nfs4_proc_get_locations
=======================

.. c:function:: int nfs4_proc_get_locations(struct inode *inode, struct nfs4_fs_locations *locations, struct page *page, struct rpc_cred *cred)

    discover locations for a migrated FSID

    :param struct inode \*inode:
        inode on FSID that is migrating

    :param struct nfs4_fs_locations \*locations:
        result of query

    :param struct page \*page:
        buffer

    :param struct rpc_cred \*cred:
        credential to use for this operation

.. _`nfs4_proc_get_locations.description`:

Description
-----------

Returns NFS4_OK on success, a negative NFS4ERR status code if the
operation failed, or a negative errno if a local error occurred.

On success, "locations" is filled in, but if the server has
no locations information, NFS_ATTR_FATTR_V4_LOCATIONS is not
asserted.

-NFS4ERR_LEASE_MOVED is returned if the server still has leases
from this client that require migration recovery.

.. _`nfs4_proc_fsid_present`:

nfs4_proc_fsid_present
======================

.. c:function:: int nfs4_proc_fsid_present(struct inode *inode, struct rpc_cred *cred)

    Is this FSID present or absent on server?

    :param struct inode \*inode:
        inode on FSID to check

    :param struct rpc_cred \*cred:
        credential to use for this operation

.. _`nfs4_proc_fsid_present.description`:

Description
-----------

Server indicates whether the FSID is present, moved, or not
recognized.  This operation is necessary to clear a LEASE_MOVED
condition for this client ID.

Returns NFS4_OK if the FSID is present on this server,
-NFS4ERR_MOVED if the FSID is no longer present, a negative
NFS4ERR code if some error occurred on the server, or a
negative errno if a local failure occurred.

.. _`_nfs4_proc_secinfo`:

\_nfs4_proc_secinfo
===================

.. c:function:: int _nfs4_proc_secinfo(struct inode *dir, const struct qstr *name, struct nfs4_secinfo_flavors *flavors, bool use_integrity)

    cl_rpcclient is using krb5i/p, use the integrity protected cl_rpcclient and the machine credential as per RFC3530bis and RFC5661 Security Considerations sections. Otherwise, just use the user cred with the filesystem's rpc_client.

    :param struct inode \*dir:
        *undescribed*

    :param const struct qstr \*name:
        *undescribed*

    :param struct nfs4_secinfo_flavors \*flavors:
        *undescribed*

    :param bool use_integrity:
        *undescribed*

.. _`nfs4_test_session_trunk`:

nfs4_test_session_trunk
=======================

.. c:function:: int nfs4_test_session_trunk(struct rpc_clnt *clnt, struct rpc_xprt *xprt, void *data)

    :param struct rpc_clnt \*clnt:
        struct rpc_clnt to get new transport

    :param struct rpc_xprt \*xprt:
        the rpc_xprt to test

    :param void \*data:
        call data for \_nfs4_proc_exchange_id.

.. _`nfs4_test_session_trunk.description`:

Description
-----------

This is an \ :c:func:`add_xprt_test`\  test function called from
rpc_clnt_setup_test_and_add_xprt.

The rpc_xprt_switch is referrenced by rpc_clnt_setup_test_and_add_xprt
and is dereferrenced in nfs4_exchange_id_release

Upon success, add the new transport to the rpc_clnt

.. _`_nfs41_proc_secinfo_no_name`:

\_nfs41_proc_secinfo_no_name
============================

.. c:function:: int _nfs41_proc_secinfo_no_name(struct nfs_server *server, struct nfs_fh *fhandle, struct nfs_fsinfo *info, struct nfs4_secinfo_flavors *flavors, bool use_integrity)

    possible) as per RFC3530bis and RFC5661 Security Considerations sections

    :param struct nfs_server \*server:
        *undescribed*

    :param struct nfs_fh \*fhandle:
        *undescribed*

    :param struct nfs_fsinfo \*info:
        *undescribed*

    :param struct nfs4_secinfo_flavors \*flavors:
        *undescribed*

    :param bool use_integrity:
        *undescribed*

.. _`nfs41_test_stateid`:

nfs41_test_stateid
==================

.. c:function:: int nfs41_test_stateid(struct nfs_server *server, nfs4_stateid *stateid, struct rpc_cred *cred)

    perform a TEST_STATEID operation

    :param struct nfs_server \*server:
        server / transport on which to perform the operation

    :param nfs4_stateid \*stateid:
        state ID to test

    :param struct rpc_cred \*cred:
        credential

.. _`nfs41_test_stateid.description`:

Description
-----------

Returns NFS_OK if the server recognizes that "stateid" is valid.
Otherwise a negative NFS4ERR value is returned if the operation
failed or the state ID is not currently valid.

.. _`nfs41_free_stateid`:

nfs41_free_stateid
==================

.. c:function:: int nfs41_free_stateid(struct nfs_server *server, const nfs4_stateid *stateid, struct rpc_cred *cred, bool privileged)

    perform a FREE_STATEID operation

    :param struct nfs_server \*server:
        server / transport on which to perform the operation

    :param const nfs4_stateid \*stateid:
        state ID to release

    :param struct rpc_cred \*cred:
        credential

    :param bool privileged:
        *undescribed*

.. _`nfs41_free_stateid.note`:

Note
----

this function is always asynchronous.

.. This file was automatic generated / don't edit.

