.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/cred.c

.. _`__put_cred`:

\__put_cred
===========

.. c:function:: void __put_cred(struct cred *cred)

    Destroy a set of credentials

    :param cred:
        The record to release
    :type cred: struct cred \*

.. _`__put_cred.description`:

Description
-----------

Destroy a set of credentials on which no references remain.

.. _`get_task_cred`:

get_task_cred
=============

.. c:function:: const struct cred *get_task_cred(struct task_struct *task)

    Get another task's objective credentials

    :param task:
        The task to query
    :type task: struct task_struct \*

.. _`get_task_cred.description`:

Description
-----------

Get the objective credentials of a task, pinning them so that they can't go
away.  Accessing a task's credentials directly is not permitted.

The caller must also make sure task doesn't get deleted, either by holding a
ref on task or by holding tasklist_lock to prevent it from being unlinked.

.. _`prepare_creds`:

prepare_creds
=============

.. c:function:: struct cred *prepare_creds( void)

    Prepare a new set of credentials for modification

    :param void:
        no arguments
    :type void: 

.. _`prepare_creds.description`:

Description
-----------

Prepare a new set of task credentials for modification.  A task's creds
shouldn't generally be modified directly, therefore this function is used to
prepare a new copy, which the caller then modifies and then commits by
calling \ :c:func:`commit_creds`\ .

Preparation involves making a copy of the objective creds for modification.

Returns a pointer to the new creds-to-be if successful, NULL otherwise.

Call \ :c:func:`commit_creds`\  or \ :c:func:`abort_creds`\  to clean up.

.. _`commit_creds`:

commit_creds
============

.. c:function:: int commit_creds(struct cred *new)

    Install new credentials upon the current task

    :param new:
        The credentials to be assigned
    :type new: struct cred \*

.. _`commit_creds.description`:

Description
-----------

Install a new set of credentials to the current task, using RCU to replace
the old set.  Both the objective and the subjective credentials pointers are
updated.  This function may not be called if the subjective credentials are
in an overridden state.

This function eats the caller's reference to the new credentials.

Always returns 0 thus allowing this function to be tail-called at the end
of, say, \ :c:func:`sys_setgid`\ .

.. _`abort_creds`:

abort_creds
===========

.. c:function:: void abort_creds(struct cred *new)

    Discard a set of credentials and unlock the current task

    :param new:
        The credentials that were going to be applied
    :type new: struct cred \*

.. _`abort_creds.description`:

Description
-----------

Discard a set of credentials that were under construction and unlock the
current task.

.. _`override_creds`:

override_creds
==============

.. c:function:: const struct cred *override_creds(const struct cred *new)

    Override the current process's subjective credentials

    :param new:
        The credentials to be assigned
    :type new: const struct cred \*

.. _`override_creds.description`:

Description
-----------

Install a set of temporary override subjective credentials on the current
process, returning the old set for later reversion.

.. _`revert_creds`:

revert_creds
============

.. c:function:: void revert_creds(const struct cred *old)

    Revert a temporary subjective credentials override

    :param old:
        The credentials to be restored
    :type old: const struct cred \*

.. _`revert_creds.description`:

Description
-----------

Revert a temporary set of override subjective credentials to an old set,
discarding the override set.

.. _`prepare_kernel_cred`:

prepare_kernel_cred
===================

.. c:function:: struct cred *prepare_kernel_cred(struct task_struct *daemon)

    Prepare a set of credentials for a kernel service

    :param daemon:
        A userspace daemon to be used as a reference
    :type daemon: struct task_struct \*

.. _`prepare_kernel_cred.description`:

Description
-----------

Prepare a set of credentials for a kernel service.  This can then be used to
override a task's own credentials so that work can be done on behalf of that
task that requires a different subjective context.

\ ``daemon``\  is used to provide a base for the security record, but can be NULL.
If \ ``daemon``\  is supplied, then the security data will be derived from that;
otherwise they'll be set to 0 and no groups, full capabilities and no keys.

The caller may change these controls afterwards if desired.

Returns the new credentials or NULL if out of memory.

Does not take, and does not return holding current->cred_replace_mutex.

.. _`set_security_override`:

set_security_override
=====================

.. c:function:: int set_security_override(struct cred *new, u32 secid)

    Set the security ID in a set of credentials

    :param new:
        The credentials to alter
    :type new: struct cred \*

    :param secid:
        The LSM security ID to set
    :type secid: u32

.. _`set_security_override.description`:

Description
-----------

Set the LSM security ID in a set of credentials so that the subjective
security is overridden when an alternative set of credentials is used.

.. _`set_security_override_from_ctx`:

set_security_override_from_ctx
==============================

.. c:function:: int set_security_override_from_ctx(struct cred *new, const char *secctx)

    Set the security ID in a set of credentials

    :param new:
        The credentials to alter
    :type new: struct cred \*

    :param secctx:
        The LSM security context to generate the security ID from.
    :type secctx: const char \*

.. _`set_security_override_from_ctx.description`:

Description
-----------

Set the LSM security ID in a set of credentials so that the subjective
security is overridden when an alternative set of credentials is used.  The
security ID is specified in string form as a security context to be
interpreted by the LSM.

.. _`set_create_files_as`:

set_create_files_as
===================

.. c:function:: int set_create_files_as(struct cred *new, struct inode *inode)

    Set the LSM file create context in a set of credentials

    :param new:
        The credentials to alter
    :type new: struct cred \*

    :param inode:
        The inode to take the context from
    :type inode: struct inode \*

.. _`set_create_files_as.description`:

Description
-----------

Change the LSM file creation context in a set of credentials to be the same
as the object context of the specified inode, so that the new inodes have
the same MAC context as that inode.

.. This file was automatic generated / don't edit.

