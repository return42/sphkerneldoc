.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/inode.c

.. _`nfs_compat_user_ino64`:

nfs_compat_user_ino64
=====================

.. c:function:: u64 nfs_compat_user_ino64(u64 fileid)

    returns the user-visible inode number

    :param u64 fileid:
        64-bit fileid

.. _`nfs_compat_user_ino64.description`:

Description
-----------

This function returns a 32-bit inode number if the boot parameter
nfs.enable_ino64 is zero.

.. _`nfs_sync_mapping`:

nfs_sync_mapping
================

.. c:function:: int nfs_sync_mapping(struct address_space *mapping)

    helper to flush all mmapped dirty data to disk

    :param struct address_space \*mapping:
        *undescribed*

.. _`nfs_vmtruncate`:

nfs_vmtruncate
==============

.. c:function:: int nfs_vmtruncate(struct inode *inode, loff_t offset)

    unmap mappings "freed" by \ :c:func:`truncate`\  syscall

    :param struct inode \*inode:
        inode of the file used

    :param loff_t offset:
        file offset to start truncating

.. _`nfs_vmtruncate.description`:

Description
-----------

This is a copy of the common vmtruncate, but with the locking
corrected to take into account the fact that NFS requires
inode->i_size to be updated under the inode->i_lock.

.. _`nfs_vmtruncate.note`:

Note
----

must be called with inode->i_lock held!

.. _`nfs_setattr_update_inode`:

nfs_setattr_update_inode
========================

.. c:function:: void nfs_setattr_update_inode(struct inode *inode, struct iattr *attr, struct nfs_fattr *fattr)

    Update inode metadata after a setattr call.

    :param struct inode \*inode:
        pointer to struct inode

    :param struct iattr \*attr:
        pointer to struct iattr

    :param struct nfs_fattr \*fattr:
        *undescribed*

.. _`nfs_setattr_update_inode.note`:

Note
----

we do this in the \*proc.c in order to ensure that
it works for things like exclusive creates too.

.. _`nfs_close_context`:

nfs_close_context
=================

.. c:function:: void nfs_close_context(struct nfs_open_context *ctx, int is_sync)

    Common \ :c:func:`close_context`\  routine NFSv2/v3

    :param struct nfs_open_context \*ctx:
        pointer to context

    :param int is_sync:
        is this a synchronous close

.. _`nfs_close_context.description`:

Description
-----------

Ensure that the attributes are up to date if we're mounted
with close-to-open semantics and we have cached data that will
need to be revalidated on open.

.. _`nfs_revalidate_inode`:

nfs_revalidate_inode
====================

.. c:function:: int nfs_revalidate_inode(struct nfs_server *server, struct inode *inode)

    Revalidate the inode attributes \ ``server``\  - pointer to nfs_server struct \ ``inode``\  - pointer to inode struct

    :param struct nfs_server \*server:
        *undescribed*

    :param struct inode \*inode:
        *undescribed*

.. _`nfs_revalidate_inode.description`:

Description
-----------

Updates inode attribute information by retrieving the data from the server.

.. _`__nfs_revalidate_mapping`:

__nfs_revalidate_mapping
========================

.. c:function:: int __nfs_revalidate_mapping(struct inode *inode, struct address_space *mapping, bool may_lock)

    Revalidate the pagecache \ ``inode``\  - pointer to host inode \ ``mapping``\  - pointer to mapping \ ``may_lock``\  - take inode->i_mutex?

    :param struct inode \*inode:
        *undescribed*

    :param struct address_space \*mapping:
        *undescribed*

    :param bool may_lock:
        *undescribed*

.. _`nfs_revalidate_mapping`:

nfs_revalidate_mapping
======================

.. c:function:: int nfs_revalidate_mapping(struct inode *inode, struct address_space *mapping)

    Revalidate the pagecache \ ``inode``\  - pointer to host inode \ ``mapping``\  - pointer to mapping

    :param struct inode \*inode:
        *undescribed*

    :param struct address_space \*mapping:
        *undescribed*

.. _`nfs_revalidate_mapping_protected`:

nfs_revalidate_mapping_protected
================================

.. c:function:: int nfs_revalidate_mapping_protected(struct inode *inode, struct address_space *mapping)

    Revalidate the pagecache \ ``inode``\  - pointer to host inode \ ``mapping``\  - pointer to mapping

    :param struct inode \*inode:
        *undescribed*

    :param struct address_space \*mapping:
        *undescribed*

.. _`nfs_revalidate_mapping_protected.description`:

Description
-----------

Differs from \ :c:func:`nfs_revalidate_mapping`\  in that it grabs the inode->i_mutex
while invalidating the mapping.

.. _`nfs_check_inode_attributes`:

nfs_check_inode_attributes
==========================

.. c:function:: int nfs_check_inode_attributes(struct inode *inode, struct nfs_fattr *fattr)

    verify consistency of the inode attribute cache \ ``inode``\  - pointer to inode \ ``fattr``\  - updated attributes

    :param struct inode \*inode:
        *undescribed*

    :param struct nfs_fattr \*fattr:
        *undescribed*

.. _`nfs_check_inode_attributes.description`:

Description
-----------

Verifies the attribute cache. If we have just changed the attributes,
so that fattr carries weak cache consistency data, then it may
also update the ctime/mtime/change_attribute.

.. _`nfs_fattr_set_barrier`:

nfs_fattr_set_barrier
=====================

.. c:function:: void nfs_fattr_set_barrier(struct nfs_fattr *fattr)

    :param struct nfs_fattr \*fattr:
        attributes

.. _`nfs_fattr_set_barrier.description`:

Description
-----------

Used to set a barrier after an attribute was updated. This
barrier ensures that older attributes from RPC calls that may
have raced with our update cannot clobber these new values.
Note that you are still responsible for ensuring that other
operations which change the attribute on the server do not
collide.

.. _`nfs_inode_attrs_need_update`:

nfs_inode_attrs_need_update
===========================

.. c:function:: int nfs_inode_attrs_need_update(const struct inode *inode, const struct nfs_fattr *fattr)

    check if the inode attributes need updating \ ``inode``\  - pointer to inode \ ``fattr``\  - attributes

    :param const struct inode \*inode:
        *undescribed*

    :param const struct nfs_fattr \*fattr:
        *undescribed*

.. _`nfs_inode_attrs_need_update.description`:

Description
-----------

Attempt to divine whether or not an RPC call reply carrying stale
attributes got scheduled after another call carrying updated ones.

To do so, the function first assumes that a more recent ctime means
that the attributes in fattr are newer, however it also attempt to
catch the case where ctime either didn't change, or went backwards
(if someone reset the clock on the server) by looking at whether
or not this RPC call was started after the inode was last updated.
Note also the check for wraparound of 'attr_gencount'

The function returns 'true' if it thinks the attributes in 'fattr' are
more recent than the ones cached in the inode.

.. _`nfs_refresh_inode`:

nfs_refresh_inode
=================

.. c:function:: int nfs_refresh_inode(struct inode *inode, struct nfs_fattr *fattr)

    try to update the inode attribute cache \ ``inode``\  - pointer to inode \ ``fattr``\  - updated attributes

    :param struct inode \*inode:
        *undescribed*

    :param struct nfs_fattr \*fattr:
        *undescribed*

.. _`nfs_refresh_inode.description`:

Description
-----------

Check that an RPC call that returned attributes has not overlapped with
other recent updates of the inode metadata, then decide whether it is
safe to do a full update of the inode attributes, or whether just to
call nfs_check_inode_attributes.

.. _`nfs_post_op_update_inode`:

nfs_post_op_update_inode
========================

.. c:function:: int nfs_post_op_update_inode(struct inode *inode, struct nfs_fattr *fattr)

    try to update the inode attribute cache \ ``inode``\  - pointer to inode \ ``fattr``\  - updated attributes

    :param struct inode \*inode:
        *undescribed*

    :param struct nfs_fattr \*fattr:
        *undescribed*

.. _`nfs_post_op_update_inode.description`:

Description
-----------

After an operation that has changed the inode metadata, mark the
attribute cache as being invalid, then try to update it.

NB: if the server didn't return any post op attributes, this
function will force the retrieval of attributes before the next
NFS request.  Thus it should be used only for operations that
are expected to change one or more attributes, to avoid
unnecessary NFS requests and trips through \ :c:func:`nfs_update_inode`\ .

.. _`nfs_post_op_update_inode_force_wcc_locked`:

nfs_post_op_update_inode_force_wcc_locked
=========================================

.. c:function:: int nfs_post_op_update_inode_force_wcc_locked(struct inode *inode, struct nfs_fattr *fattr)

    update the inode attribute cache \ ``inode``\  - pointer to inode \ ``fattr``\  - updated attributes

    :param struct inode \*inode:
        *undescribed*

    :param struct nfs_fattr \*fattr:
        *undescribed*

.. _`nfs_post_op_update_inode_force_wcc_locked.description`:

Description
-----------

After an operation that has changed the inode metadata, mark the
attribute cache as being invalid, then try to update it. Fake up
weak cache consistency data, if none exist.

This function is mainly designed to be used by the ->\ :c:func:`write_done`\  functions.

.. _`nfs_post_op_update_inode_force_wcc`:

nfs_post_op_update_inode_force_wcc
==================================

.. c:function:: int nfs_post_op_update_inode_force_wcc(struct inode *inode, struct nfs_fattr *fattr)

    try to update the inode attribute cache \ ``inode``\  - pointer to inode \ ``fattr``\  - updated attributes

    :param struct inode \*inode:
        *undescribed*

    :param struct nfs_fattr \*fattr:
        *undescribed*

.. _`nfs_post_op_update_inode_force_wcc.description`:

Description
-----------

After an operation that has changed the inode metadata, mark the
attribute cache as being invalid, then try to update it. Fake up
weak cache consistency data, if none exist.

This function is mainly designed to be used by the ->\ :c:func:`write_done`\  functions.

.. This file was automatic generated / don't edit.

