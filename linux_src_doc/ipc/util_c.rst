.. -*- coding: utf-8; mode: rst -*-
.. src-file: ipc/util.c

.. _`ipc_init`:

ipc_init
========

.. c:function:: int ipc_init( void)

    initialise ipc subsystem

    :param void:
        no arguments
    :type void: 

.. _`ipc_init.description`:

Description
-----------

The various sysv ipc resources (semaphores, messages and shared
memory) are initialised.

A callback routine is registered into the memory hotplug notifier
chain: since msgmni scales to lowmem this callback routine will be
called upon successful memory add / remove to recompute msmgni.

.. _`ipc_init_ids`:

ipc_init_ids
============

.. c:function:: void ipc_init_ids(struct ipc_ids *ids)

    initialise ipc identifiers

    :param ids:
        ipc identifier set
    :type ids: struct ipc_ids \*

.. _`ipc_init_ids.description`:

Description
-----------

Set up the sequence range to use for the ipc identifier range (limited
below IPCMNI) then initialise the keys hashtable and ids idr.

.. _`ipc_init_proc_interface`:

ipc_init_proc_interface
=======================

.. c:function:: void ipc_init_proc_interface(const char *path, const char *header, int ids, int (*show)(struct seq_file *, void *))

    create a proc interface for sysipc types using a seq_file interface.

    :param path:
        Path in procfs
    :type path: const char \*

    :param header:
        Banner to be printed at the beginning of the file.
    :type header: const char \*

    :param ids:
        ipc id table to iterate.
    :type ids: int

    :param int (\*show)(struct seq_file \*, void \*):
        show routine.

.. _`ipc_findkey`:

ipc_findkey
===========

.. c:function:: struct kern_ipc_perm *ipc_findkey(struct ipc_ids *ids, key_t key)

    find a key in an ipc identifier set

    :param ids:
        ipc identifier set
    :type ids: struct ipc_ids \*

    :param key:
        key to find
    :type key: key_t

.. _`ipc_findkey.description`:

Description
-----------

Returns the locked pointer to the ipc structure if found or NULL
otherwise. If key is found ipc points to the owning ipc structure

Called with writer ipc_ids.rwsem held.

.. _`ipc_addid`:

ipc_addid
=========

.. c:function:: int ipc_addid(struct ipc_ids *ids, struct kern_ipc_perm *new, int limit)

    add an ipc identifier

    :param ids:
        ipc identifier set
    :type ids: struct ipc_ids \*

    :param new:
        new ipc permission set
    :type new: struct kern_ipc_perm \*

    :param limit:
        limit for the number of used ids
    :type limit: int

.. _`ipc_addid.description`:

Description
-----------

Add an entry 'new' to the ipc ids idr. The permissions object is
initialised and the first free entry is set up and the index assigned
is returned. The 'new' entry is returned in a locked state on success.

On failure the entry is not locked and a negative err-code is returned.
The caller must use \ :c:func:`ipc_rcu_putref`\  to free the identifier.

Called with writer ipc_ids.rwsem held.

.. _`ipcget_new`:

ipcget_new
==========

.. c:function:: int ipcget_new(struct ipc_namespace *ns, struct ipc_ids *ids, const struct ipc_ops *ops, struct ipc_params *params)

    create a new ipc object

    :param ns:
        ipc namespace
    :type ns: struct ipc_namespace \*

    :param ids:
        ipc identifier set
    :type ids: struct ipc_ids \*

    :param ops:
        the actual creation routine to call
    :type ops: const struct ipc_ops \*

    :param params:
        its parameters
    :type params: struct ipc_params \*

.. _`ipcget_new.description`:

Description
-----------

This routine is called by sys_msgget, \ :c:func:`sys_semget`\  and \ :c:func:`sys_shmget`\ 
when the key is IPC_PRIVATE.

.. _`ipc_check_perms`:

ipc_check_perms
===============

.. c:function:: int ipc_check_perms(struct ipc_namespace *ns, struct kern_ipc_perm *ipcp, const struct ipc_ops *ops, struct ipc_params *params)

    check security and permissions for an ipc object

    :param ns:
        ipc namespace
    :type ns: struct ipc_namespace \*

    :param ipcp:
        ipc permission set
    :type ipcp: struct kern_ipc_perm \*

    :param ops:
        the actual security routine to call
    :type ops: const struct ipc_ops \*

    :param params:
        its parameters
    :type params: struct ipc_params \*

.. _`ipc_check_perms.description`:

Description
-----------

This routine is called by \ :c:func:`sys_msgget`\ , \ :c:func:`sys_semget`\  and \ :c:func:`sys_shmget`\ 
when the key is not IPC_PRIVATE and that key already exists in the
ds IDR.

On success, the ipc id is returned.

It is called with ipc_ids.rwsem and ipcp->lock held.

.. _`ipcget_public`:

ipcget_public
=============

.. c:function:: int ipcget_public(struct ipc_namespace *ns, struct ipc_ids *ids, const struct ipc_ops *ops, struct ipc_params *params)

    get an ipc object or create a new one

    :param ns:
        ipc namespace
    :type ns: struct ipc_namespace \*

    :param ids:
        ipc identifier set
    :type ids: struct ipc_ids \*

    :param ops:
        the actual creation routine to call
    :type ops: const struct ipc_ops \*

    :param params:
        its parameters
    :type params: struct ipc_params \*

.. _`ipcget_public.description`:

Description
-----------

This routine is called by sys_msgget, \ :c:func:`sys_semget`\  and \ :c:func:`sys_shmget`\ 
when the key is not IPC_PRIVATE.
It adds a new entry if the key is not found and does some permission
/ security checkings if the key is found.

On success, the ipc id is returned.

.. _`ipc_kht_remove`:

ipc_kht_remove
==============

.. c:function:: void ipc_kht_remove(struct ipc_ids *ids, struct kern_ipc_perm *ipcp)

    remove an ipc from the key hashtable

    :param ids:
        ipc identifier set
    :type ids: struct ipc_ids \*

    :param ipcp:
        ipc perm structure containing the key to remove
    :type ipcp: struct kern_ipc_perm \*

.. _`ipc_kht_remove.description`:

Description
-----------

ipc_ids.rwsem (as a writer) and the spinlock for this ID are held
before this function is called, and remain locked on the exit.

.. _`ipc_rmid`:

ipc_rmid
========

.. c:function:: void ipc_rmid(struct ipc_ids *ids, struct kern_ipc_perm *ipcp)

    remove an ipc identifier

    :param ids:
        ipc identifier set
    :type ids: struct ipc_ids \*

    :param ipcp:
        ipc perm structure containing the identifier to remove
    :type ipcp: struct kern_ipc_perm \*

.. _`ipc_rmid.description`:

Description
-----------

ipc_ids.rwsem (as a writer) and the spinlock for this ID are held
before this function is called, and remain locked on the exit.

.. _`ipc_set_key_private`:

ipc_set_key_private
===================

.. c:function:: void ipc_set_key_private(struct ipc_ids *ids, struct kern_ipc_perm *ipcp)

    switch the key of an existing ipc to IPC_PRIVATE

    :param ids:
        ipc identifier set
    :type ids: struct ipc_ids \*

    :param ipcp:
        ipc perm structure containing the key to modify
    :type ipcp: struct kern_ipc_perm \*

.. _`ipc_set_key_private.description`:

Description
-----------

ipc_ids.rwsem (as a writer) and the spinlock for this ID are held
before this function is called, and remain locked on the exit.

.. _`ipcperms`:

ipcperms
========

.. c:function:: int ipcperms(struct ipc_namespace *ns, struct kern_ipc_perm *ipcp, short flag)

    check ipc permissions

    :param ns:
        ipc namespace
    :type ns: struct ipc_namespace \*

    :param ipcp:
        ipc permission set
    :type ipcp: struct kern_ipc_perm \*

    :param flag:
        desired permission set
    :type flag: short

.. _`ipcperms.description`:

Description
-----------

Check user, group, other permissions for access
to ipc resources. return 0 if allowed

\ ``flag``\  will most probably be 0 or ``S_...UGO`` from <linux/stat.h>

.. _`kernel_to_ipc64_perm`:

kernel_to_ipc64_perm
====================

.. c:function:: void kernel_to_ipc64_perm(struct kern_ipc_perm *in, struct ipc64_perm *out)

    convert kernel ipc permissions to user

    :param in:
        kernel permissions
    :type in: struct kern_ipc_perm \*

    :param out:
        new style ipc permissions
    :type out: struct ipc64_perm \*

.. _`kernel_to_ipc64_perm.description`:

Description
-----------

Turn the kernel object \ ``in``\  into a set of permissions descriptions
for returning to userspace (@out).

.. _`ipc64_perm_to_ipc_perm`:

ipc64_perm_to_ipc_perm
======================

.. c:function:: void ipc64_perm_to_ipc_perm(struct ipc64_perm *in, struct ipc_perm *out)

    convert new ipc permissions to old

    :param in:
        new style ipc permissions
    :type in: struct ipc64_perm \*

    :param out:
        old style ipc permissions
    :type out: struct ipc_perm \*

.. _`ipc64_perm_to_ipc_perm.description`:

Description
-----------

Turn the new style permissions object \ ``in``\  into a compatibility
object and store it into the \ ``out``\  pointer.

.. _`ipc_obtain_object_idr`:

ipc_obtain_object_idr
=====================

.. c:function:: struct kern_ipc_perm *ipc_obtain_object_idr(struct ipc_ids *ids, int id)

    :param ids:
        ipc identifier set
    :type ids: struct ipc_ids \*

    :param id:
        ipc id to look for
    :type id: int

.. _`ipc_obtain_object_idr.description`:

Description
-----------

Look for an id in the ipc ids idr and return associated ipc object.

Call inside the RCU critical section.
The ipc object is *not* locked on exit.

.. _`ipc_obtain_object_check`:

ipc_obtain_object_check
=======================

.. c:function:: struct kern_ipc_perm *ipc_obtain_object_check(struct ipc_ids *ids, int id)

    :param ids:
        ipc identifier set
    :type ids: struct ipc_ids \*

    :param id:
        ipc id to look for
    :type id: int

.. _`ipc_obtain_object_check.description`:

Description
-----------

Similar to \ :c:func:`ipc_obtain_object_idr`\  but also checks the ipc object
sequence number.

Call inside the RCU critical section.
The ipc object is *not* locked on exit.

.. _`ipcget`:

ipcget
======

.. c:function:: int ipcget(struct ipc_namespace *ns, struct ipc_ids *ids, const struct ipc_ops *ops, struct ipc_params *params)

    Common sys_*get() code

    :param ns:
        namespace
    :type ns: struct ipc_namespace \*

    :param ids:
        ipc identifier set
    :type ids: struct ipc_ids \*

    :param ops:
        operations to be called on ipc object creation, permission checks
        and further checks
    :type ops: const struct ipc_ops \*

    :param params:
        the parameters needed by the previous operations.
    :type params: struct ipc_params \*

.. _`ipcget.description`:

Description
-----------

Common routine called by \ :c:func:`sys_msgget`\ , \ :c:func:`sys_semget`\  and \ :c:func:`sys_shmget`\ .

.. _`ipc_update_perm`:

ipc_update_perm
===============

.. c:function:: int ipc_update_perm(struct ipc64_perm *in, struct kern_ipc_perm *out)

    update the permissions of an ipc object

    :param in:
        the permission given as input.
    :type in: struct ipc64_perm \*

    :param out:
        the permission of the ipc to set.
    :type out: struct kern_ipc_perm \*

.. _`ipcctl_obtain_check`:

ipcctl_obtain_check
===================

.. c:function:: struct kern_ipc_perm *ipcctl_obtain_check(struct ipc_namespace *ns, struct ipc_ids *ids, int id, int cmd, struct ipc64_perm *perm, int extra_perm)

    retrieve an ipc object and check permissions

    :param ns:
        ipc namespace
    :type ns: struct ipc_namespace \*

    :param ids:
        the table of ids where to look for the ipc
    :type ids: struct ipc_ids \*

    :param id:
        the id of the ipc to retrieve
    :type id: int

    :param cmd:
        the cmd to check
    :type cmd: int

    :param perm:
        the permission to set
    :type perm: struct ipc64_perm \*

    :param extra_perm:
        one extra permission parameter used by msq
    :type extra_perm: int

.. _`ipcctl_obtain_check.description`:

Description
-----------

This function does some common audit and permissions check for some IPC_XXX
cmd and is called from semctl_down, shmctl_down and msgctl_down.

It:
  - retrieves the ipc object with the given id in the given table.
  - performs some audit and permission check, depending on the given cmd
  - returns a pointer to the ipc object or otherwise, the corresponding
    error.

Call holding the both the rwsem and the rcu read lock.

.. _`ipc_parse_version`:

ipc_parse_version
=================

.. c:function:: int ipc_parse_version(int *cmd)

    ipc call version

    :param cmd:
        pointer to command
    :type cmd: int \*

.. _`ipc_parse_version.description`:

Description
-----------

Return IPC_64 for new style IPC and IPC_OLD for old style IPC.
The \ ``cmd``\  value is turned from an encoding command and version into
just the command code.

.. This file was automatic generated / don't edit.

