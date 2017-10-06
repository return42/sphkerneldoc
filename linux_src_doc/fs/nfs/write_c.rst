.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/write.c

.. _`nfs_request_add_commit_list_locked`:

nfs_request_add_commit_list_locked
==================================

.. c:function:: void nfs_request_add_commit_list_locked(struct nfs_page *req, struct list_head *dst, struct nfs_commit_info *cinfo)

    add request to a commit list

    :param struct nfs_page \*req:
        pointer to a struct nfs_page

    :param struct list_head \*dst:
        commit list head

    :param struct nfs_commit_info \*cinfo:
        holds list lock and accounting info

.. _`nfs_request_add_commit_list_locked.description`:

Description
-----------

This sets the PG_CLEAN bit, updates the cinfo count of
number of outstanding requests requiring a commit as well as
the MM page stats.

The caller must hold NFS_I(cinfo->inode)->commit_mutex, and the
nfs_page lock.

.. _`nfs_request_add_commit_list`:

nfs_request_add_commit_list
===========================

.. c:function:: void nfs_request_add_commit_list(struct nfs_page *req, struct nfs_commit_info *cinfo)

    add request to a commit list

    :param struct nfs_page \*req:
        pointer to a struct nfs_page

    :param struct nfs_commit_info \*cinfo:
        holds list lock and accounting info

.. _`nfs_request_add_commit_list.description`:

Description
-----------

This sets the PG_CLEAN bit, updates the cinfo count of
number of outstanding requests requiring a commit as well as
the MM page stats.

The caller must \_not\_ hold the cinfo->lock, but must be
holding the nfs_page lock.

.. _`nfs_request_remove_commit_list`:

nfs_request_remove_commit_list
==============================

.. c:function:: void nfs_request_remove_commit_list(struct nfs_page *req, struct nfs_commit_info *cinfo)

    Remove request from a commit list

    :param struct nfs_page \*req:
        pointer to a nfs_page

    :param struct nfs_commit_info \*cinfo:
        holds list lock and accounting info

.. _`nfs_request_remove_commit_list.description`:

Description
-----------

This clears the PG_CLEAN bit, and updates the cinfo's count of
number of outstanding requests requiring a commit
It does not update the MM page stats.

The caller \_must\_ hold the cinfo->lock and the nfs_page lock.

.. This file was automatic generated / don't edit.

