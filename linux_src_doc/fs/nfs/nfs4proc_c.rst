.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/nfs4proc.c

.. _`nfs41_check_expired_locks`:

nfs41_check_expired_locks
=========================

.. c:function:: int nfs41_check_expired_locks(struct nfs4_state *state)

    possibly free a lock stateid

    :param state:
        NFSv4 state for an inode
    :type state: struct nfs4_state \*

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

    :param state:
        NFSv4 state for an inode
    :type state: struct nfs4_state \*

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

    :param server:
        initialized nfs_server handle
    :type server: struct nfs_server \*

    :param fhandle:
        we fill in the pseudo-fs root file handle
    :type fhandle: struct nfs_fh \*

    :param info:
        we fill in an FSINFO struct
    :type info: struct nfs_fsinfo \*

    :param auth_probe:
        probe the auth flavours
    :type auth_probe: bool

.. _`nfs4_proc_get_rootfh.description`:

Description
-----------

Returns zero on success, or a negative errno.

.. _`nfs4_proc_setclientid`:

nfs4_proc_setclientid
=====================

.. c:function:: int nfs4_proc_setclientid(struct nfs_client *clp, u32 program, unsigned short port, struct rpc_cred *cred, struct nfs4_setclientid_res *res)

    Negotiate client ID

    :param clp:
        state data structure
    :type clp: struct nfs_client \*

    :param program:
        RPC program for NFSv4 callback service
    :type program: u32

    :param port:
        IP port number for NFS4 callback service
    :type port: unsigned short

    :param cred:
        RPC credential to use for this call
    :type cred: struct rpc_cred \*

    :param res:
        where to place the result
    :type res: struct nfs4_setclientid_res \*

.. _`nfs4_proc_setclientid.description`:

Description
-----------

Returns zero, a negative errno, or a negative NFS4ERR status code.

.. _`nfs4_proc_setclientid_confirm`:

nfs4_proc_setclientid_confirm
=============================

.. c:function:: int nfs4_proc_setclientid_confirm(struct nfs_client *clp, struct nfs4_setclientid_res *arg, struct rpc_cred *cred)

    Confirm client ID

    :param clp:
        state data structure
    :type clp: struct nfs_client \*

    :param arg:
        *undescribed*
    :type arg: struct nfs4_setclientid_res \*

    :param cred:
        RPC credential to use for this call
    :type cred: struct rpc_cred \*

.. _`nfs4_proc_setclientid_confirm.description`:

Description
-----------

Returns zero, a negative errno, or a negative NFS4ERR status code.

.. _`nfs4_proc_get_locations`:

nfs4_proc_get_locations
=======================

.. c:function:: int nfs4_proc_get_locations(struct inode *inode, struct nfs4_fs_locations *locations, struct page *page, struct rpc_cred *cred)

    discover locations for a migrated FSID

    :param inode:
        inode on FSID that is migrating
    :type inode: struct inode \*

    :param locations:
        result of query
    :type locations: struct nfs4_fs_locations \*

    :param page:
        buffer
    :type page: struct page \*

    :param cred:
        credential to use for this operation
    :type cred: struct rpc_cred \*

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

    :param inode:
        inode on FSID to check
    :type inode: struct inode \*

    :param cred:
        credential to use for this operation
    :type cred: struct rpc_cred \*

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

    :param dir:
        *undescribed*
    :type dir: struct inode \*

    :param name:
        *undescribed*
    :type name: const struct qstr \*

    :param flavors:
        *undescribed*
    :type flavors: struct nfs4_secinfo_flavors \*

    :param use_integrity:
        *undescribed*
    :type use_integrity: bool

.. _`nfs4_test_session_trunk`:

nfs4_test_session_trunk
=======================

.. c:function:: int nfs4_test_session_trunk(struct rpc_clnt *clnt, struct rpc_xprt *xprt, void *data)

    :param clnt:
        struct rpc_clnt to get new transport
    :type clnt: struct rpc_clnt \*

    :param xprt:
        the rpc_xprt to test
    :type xprt: struct rpc_xprt \*

    :param data:
        call data for \_nfs4_proc_exchange_id.
    :type data: void \*

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

    :param server:
        *undescribed*
    :type server: struct nfs_server \*

    :param fhandle:
        *undescribed*
    :type fhandle: struct nfs_fh \*

    :param info:
        *undescribed*
    :type info: struct nfs_fsinfo \*

    :param flavors:
        *undescribed*
    :type flavors: struct nfs4_secinfo_flavors \*

    :param use_integrity:
        *undescribed*
    :type use_integrity: bool

.. _`nfs41_test_stateid`:

nfs41_test_stateid
==================

.. c:function:: int nfs41_test_stateid(struct nfs_server *server, nfs4_stateid *stateid, struct rpc_cred *cred)

    perform a TEST_STATEID operation

    :param server:
        server / transport on which to perform the operation
    :type server: struct nfs_server \*

    :param stateid:
        state ID to test
    :type stateid: nfs4_stateid \*

    :param cred:
        credential
    :type cred: struct rpc_cred \*

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

    :param server:
        server / transport on which to perform the operation
    :type server: struct nfs_server \*

    :param stateid:
        state ID to release
    :type stateid: const nfs4_stateid \*

    :param cred:
        credential
    :type cred: struct rpc_cred \*

    :param privileged:
        *undescribed*
    :type privileged: bool

.. _`nfs41_free_stateid.note`:

Note
----

this function is always asynchronous.

.. This file was automatic generated / don't edit.

