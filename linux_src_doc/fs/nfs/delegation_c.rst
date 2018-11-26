.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/delegation.c

.. _`nfs_mark_delegation_referenced`:

nfs_mark_delegation_referenced
==============================

.. c:function:: void nfs_mark_delegation_referenced(struct nfs_delegation *delegation)

    set delegation's REFERENCED flag

    :param delegation:
        delegation to process
    :type delegation: struct nfs_delegation \*

.. _`nfs4_have_delegation`:

nfs4_have_delegation
====================

.. c:function:: int nfs4_have_delegation(struct inode *inode, fmode_t flags)

    check if inode has a delegation, mark it NFS_DELEGATION_REFERENCED if there is one.

    :param inode:
        inode to check
    :type inode: struct inode \*

    :param flags:
        delegation types to check for
    :type flags: fmode_t

.. _`nfs4_have_delegation.description`:

Description
-----------

Returns one if inode has the indicated delegation, otherwise zero.

.. _`nfs_inode_reclaim_delegation`:

nfs_inode_reclaim_delegation
============================

.. c:function:: void nfs_inode_reclaim_delegation(struct inode *inode, struct rpc_cred *cred, fmode_t type, const nfs4_stateid *stateid, unsigned long pagemod_limit)

    process a delegation reclaim request

    :param inode:
        inode to process
    :type inode: struct inode \*

    :param cred:
        credential to use for request
    :type cred: struct rpc_cred \*

    :param type:
        delegation type
    :type type: fmode_t

    :param stateid:
        delegation stateid
    :type stateid: const nfs4_stateid \*

    :param pagemod_limit:
        write delegation "space_limit"
    :type pagemod_limit: unsigned long

.. _`nfs_inode_set_delegation`:

nfs_inode_set_delegation
========================

.. c:function:: int nfs_inode_set_delegation(struct inode *inode, struct rpc_cred *cred, fmode_t type, const nfs4_stateid *stateid, unsigned long pagemod_limit)

    set up a delegation on an inode

    :param inode:
        inode to which delegation applies
    :type inode: struct inode \*

    :param cred:
        cred to use for subsequent delegation processing
    :type cred: struct rpc_cred \*

    :param type:
        delegation type
    :type type: fmode_t

    :param stateid:
        delegation stateid
    :type stateid: const nfs4_stateid \*

    :param pagemod_limit:
        write delegation "space_limit"
    :type pagemod_limit: unsigned long

.. _`nfs_inode_set_delegation.description`:

Description
-----------

Returns zero on success, or a negative errno value.

.. _`nfs_client_return_marked_delegations`:

nfs_client_return_marked_delegations
====================================

.. c:function:: int nfs_client_return_marked_delegations(struct nfs_client *clp)

    return previously marked delegations

    :param clp:
        nfs_client to process
    :type clp: struct nfs_client \*

.. _`nfs_client_return_marked_delegations.description`:

Description
-----------

Note that this function is designed to be called by the state
manager thread. For this reason, it cannot flush the dirty data,
since that could deadlock in case of a state recovery error.

Returns zero on success, or a negative errno value.

.. _`nfs_inode_return_delegation_noreclaim`:

nfs_inode_return_delegation_noreclaim
=====================================

.. c:function:: void nfs_inode_return_delegation_noreclaim(struct inode *inode)

    return delegation, don't reclaim opens

    :param inode:
        inode to process
    :type inode: struct inode \*

.. _`nfs_inode_return_delegation_noreclaim.description`:

Description
-----------

Does not protect against delegation reclaims, therefore really only safe
to be called from \ :c:func:`nfs4_clear_inode`\ .

.. _`nfs4_inode_return_delegation`:

nfs4_inode_return_delegation
============================

.. c:function:: int nfs4_inode_return_delegation(struct inode *inode)

    synchronously return a delegation

    :param inode:
        inode to process
    :type inode: struct inode \*

.. _`nfs4_inode_return_delegation.description`:

Description
-----------

This routine will always flush any dirty data to disk on the
assumption that if we need to return the delegation, then
we should stop caching.

Returns zero on success, or a negative errno value.

.. _`nfs4_inode_make_writeable`:

nfs4_inode_make_writeable
=========================

.. c:function:: int nfs4_inode_make_writeable(struct inode *inode)

    :param inode:
        pointer to inode
    :type inode: struct inode \*

.. _`nfs4_inode_make_writeable.description`:

Description
-----------

Make the inode writeable by returning the delegation if necessary

Returns zero on success, or a negative errno value.

.. _`nfs_expire_all_delegations`:

nfs_expire_all_delegations
==========================

.. c:function:: void nfs_expire_all_delegations(struct nfs_client *clp)

    :param clp:
        client to process
    :type clp: struct nfs_client \*

.. _`nfs_server_return_all_delegations`:

nfs_server_return_all_delegations
=================================

.. c:function:: void nfs_server_return_all_delegations(struct nfs_server *server)

    return delegations for one superblock

    :param server:
        *undescribed*
    :type server: struct nfs_server \*

.. _`nfs_expire_unused_delegation_types`:

nfs_expire_unused_delegation_types
==================================

.. c:function:: void nfs_expire_unused_delegation_types(struct nfs_client *clp, fmode_t flags)

    :param clp:
        client to process
    :type clp: struct nfs_client \*

    :param flags:
        delegation types to expire
    :type flags: fmode_t

.. _`nfs_expire_unreferenced_delegations`:

nfs_expire_unreferenced_delegations
===================================

.. c:function:: void nfs_expire_unreferenced_delegations(struct nfs_client *clp)

    Eliminate unused delegations

    :param clp:
        nfs_client to process
    :type clp: struct nfs_client \*

.. _`nfs_async_inode_return_delegation`:

nfs_async_inode_return_delegation
=================================

.. c:function:: int nfs_async_inode_return_delegation(struct inode *inode, const nfs4_stateid *stateid)

    asynchronously return a delegation

    :param inode:
        inode to process
    :type inode: struct inode \*

    :param stateid:
        state ID information
    :type stateid: const nfs4_stateid \*

.. _`nfs_async_inode_return_delegation.description`:

Description
-----------

Returns zero on success, or a negative errno value.

.. _`nfs_delegation_find_inode`:

nfs_delegation_find_inode
=========================

.. c:function:: struct inode *nfs_delegation_find_inode(struct nfs_client *clp, const struct nfs_fh *fhandle)

    retrieve the inode associated with a delegation

    :param clp:
        client state handle
    :type clp: struct nfs_client \*

    :param fhandle:
        filehandle from a delegation recall
    :type fhandle: const struct nfs_fh \*

.. _`nfs_delegation_find_inode.description`:

Description
-----------

Returns pointer to inode matching "fhandle," or NULL if a matching inode
cannot be found.

.. _`nfs_delegation_mark_reclaim`:

nfs_delegation_mark_reclaim
===========================

.. c:function:: void nfs_delegation_mark_reclaim(struct nfs_client *clp)

    mark all delegations as needing to be reclaimed

    :param clp:
        nfs_client to process
    :type clp: struct nfs_client \*

.. _`nfs_delegation_reap_unclaimed`:

nfs_delegation_reap_unclaimed
=============================

.. c:function:: void nfs_delegation_reap_unclaimed(struct nfs_client *clp)

    reap unclaimed delegations after reboot recovery is done

    :param clp:
        nfs_client to process
    :type clp: struct nfs_client \*

.. _`nfs_mark_test_expired_all_delegations`:

nfs_mark_test_expired_all_delegations
=====================================

.. c:function:: void nfs_mark_test_expired_all_delegations(struct nfs_client *clp)

    mark all delegations for testing

    :param clp:
        nfs_client to process
    :type clp: struct nfs_client \*

.. _`nfs_mark_test_expired_all_delegations.description`:

Description
-----------

Iterates through all the delegations associated with this server and
marks them as needing to be checked for validity.

.. _`nfs_reap_expired_delegations`:

nfs_reap_expired_delegations
============================

.. c:function:: void nfs_reap_expired_delegations(struct nfs_client *clp)

    reap expired delegations

    :param clp:
        nfs_client to process
    :type clp: struct nfs_client \*

.. _`nfs_reap_expired_delegations.description`:

Description
-----------

Iterates through all the delegations associated with this server and
checks if they have may have been revoked. This function is usually
expected to be called in cases where the server may have lost its
lease.

.. _`nfs_delegations_present`:

nfs_delegations_present
=======================

.. c:function:: int nfs_delegations_present(struct nfs_client *clp)

    check for existence of delegations

    :param clp:
        client state handle
    :type clp: struct nfs_client \*

.. _`nfs_delegations_present.description`:

Description
-----------

Returns one if there are any nfs_delegation structures attached
to this nfs_client.

.. _`nfs4_refresh_delegation_stateid`:

nfs4_refresh_delegation_stateid
===============================

.. c:function:: bool nfs4_refresh_delegation_stateid(nfs4_stateid *dst, struct inode *inode)

    Update delegation stateid seqid

    :param dst:
        stateid to refresh
    :type dst: nfs4_stateid \*

    :param inode:
        inode to check
    :type inode: struct inode \*

.. _`nfs4_refresh_delegation_stateid.description`:

Description
-----------

Returns "true" and updates "dst->seqid" \* if inode had a delegation
that matches our delegation stateid. Otherwise "false" is returned.

.. _`nfs4_copy_delegation_stateid`:

nfs4_copy_delegation_stateid
============================

.. c:function:: bool nfs4_copy_delegation_stateid(struct inode *inode, fmode_t flags, nfs4_stateid *dst, struct rpc_cred **cred)

    Copy inode's state ID information

    :param inode:
        inode to check
    :type inode: struct inode \*

    :param flags:
        delegation type requirement
    :type flags: fmode_t

    :param dst:
        stateid data structure to fill in
    :type dst: nfs4_stateid \*

    :param cred:
        optional argument to retrieve credential
    :type cred: struct rpc_cred \*\*

.. _`nfs4_copy_delegation_stateid.description`:

Description
-----------

Returns "true" and fills in "dst->data" \* if inode had a delegation,
otherwise "false" is returned.

.. _`nfs4_delegation_flush_on_close`:

nfs4_delegation_flush_on_close
==============================

.. c:function:: bool nfs4_delegation_flush_on_close(const struct inode *inode)

    Check if we must flush file on close

    :param inode:
        inode to check
    :type inode: const struct inode \*

.. _`nfs4_delegation_flush_on_close.description`:

Description
-----------

This function checks the number of outstanding writes to the file
against the delegation 'space_limit' field to see if
the spec requires us to flush the file on close.

.. This file was automatic generated / don't edit.

