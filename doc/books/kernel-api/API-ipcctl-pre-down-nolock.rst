
.. _API-ipcctl-pre-down-nolock:

======================
ipcctl_pre_down_nolock
======================

*man ipcctl_pre_down_nolock(9)*

*4.6.0-rc1*

retrieve an ipc and check permissions for some IPC_XXX cmd


Synopsis
========

.. c:function:: struct kern_ipc_perm ⋆ ipcctl_pre_down_nolock( struct ipc_namespace * ns, struct ipc_ids * ids, int id, int cmd, struct ipc64_perm * perm, int extra_perm )

Arguments
=========

``ns``
    ipc namespace

``ids``
    the table of ids where to look for the ipc

``id``
    the id of the ipc to retrieve

``cmd``
    the cmd to check

``perm``
    the permission to set

``extra_perm``
    one extra permission parameter used by msq


Description
===========

This function does some common audit and permissions check for some IPC_XXX cmd and is called from semctl_down, shmctl_down and msgctl_down. It must be called without any lock
held and - retrieves the ipc with the given id in the given table. - performs some audit and permission check, depending on the given cmd - returns a pointer to the ipc object or
otherwise, the corresponding error.

Call holding the both the rwsem and the rcu read lock.
