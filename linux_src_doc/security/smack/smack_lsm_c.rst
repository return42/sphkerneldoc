.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/smack/smack_lsm.c

.. _`smk_fetch`:

smk_fetch
=========

.. c:function:: struct smack_known *smk_fetch(const char *name, struct inode *ip, struct dentry *dp)

    Fetch the smack label from a file.

    :param const char \*name:
        type of the label (attribute)

    :param struct inode \*ip:
        a pointer to the inode

    :param struct dentry \*dp:
        a pointer to the dentry

.. _`smk_fetch.description`:

Description
-----------

Returns a pointer to the master list entry for the Smack label,
NULL if there was no label to fetch, or an error code.

.. _`new_inode_smack`:

new_inode_smack
===============

.. c:function:: struct inode_smack *new_inode_smack(struct smack_known *skp)

    allocate an inode security blob

    :param struct smack_known \*skp:
        a pointer to the Smack label entry to use in the blob

.. _`new_inode_smack.description`:

Description
-----------

Returns the new blob or NULL if there's no memory available

.. _`new_task_smack`:

new_task_smack
==============

.. c:function:: struct task_smack *new_task_smack(struct smack_known *task, struct smack_known *forked, gfp_t gfp)

    allocate a task security blob

    :param struct smack_known \*task:
        a pointer to the Smack label for the running task

    :param struct smack_known \*forked:
        a pointer to the Smack label for the forked task

    :param gfp_t gfp:
        type of the memory for the allocation

.. _`new_task_smack.description`:

Description
-----------

Returns the new blob or NULL if there's no memory available

.. _`smk_copy_rules`:

smk_copy_rules
==============

.. c:function:: int smk_copy_rules(struct list_head *nhead, struct list_head *ohead, gfp_t gfp)

    copy a rule set

    :param struct list_head \*nhead:
        new rules header pointer

    :param struct list_head \*ohead:
        old rules header pointer

    :param gfp_t gfp:
        type of the memory for the allocation

.. _`smk_copy_rules.description`:

Description
-----------

Returns 0 on success, -ENOMEM on error

.. _`smk_copy_relabel`:

smk_copy_relabel
================

.. c:function:: int smk_copy_relabel(struct list_head *nhead, struct list_head *ohead, gfp_t gfp)

    copy smk_relabel labels list

    :param struct list_head \*nhead:
        new rules header pointer

    :param struct list_head \*ohead:
        old rules header pointer

    :param gfp_t gfp:
        type of the memory for the allocation

.. _`smk_copy_relabel.description`:

Description
-----------

Returns 0 on success, -ENOMEM on error

.. _`smk_ptrace_mode`:

smk_ptrace_mode
===============

.. c:function:: unsigned int smk_ptrace_mode(unsigned int mode)

    helper function for converting PTRACE_MODE\_\* into MAY\_\* \ ``mode``\  - input mode in form of PTRACE_MODE\_\*

    :param unsigned int mode:
        *undescribed*

.. _`smk_ptrace_mode.description`:

Description
-----------

Returns a converted MAY\_\* mode usable by smack rules

.. _`smk_ptrace_rule_check`:

smk_ptrace_rule_check
=====================

.. c:function:: int smk_ptrace_rule_check(struct task_struct *tracer, struct smack_known *tracee_known, unsigned int mode, const char *func)

    helper for ptrace access

    :param struct task_struct \*tracer:
        tracer process

    :param struct smack_known \*tracee_known:
        label entry of the process that's about to be traced

    :param unsigned int mode:
        ptrace attachment mode (PTRACE_MODE\_\*)

    :param const char \*func:
        name of the function that called us, used for audit

.. _`smk_ptrace_rule_check.description`:

Description
-----------

Returns 0 on access granted, -error on error

.. _`smack_ptrace_access_check`:

smack_ptrace_access_check
=========================

.. c:function:: int smack_ptrace_access_check(struct task_struct *ctp, unsigned int mode)

    Smack approval on PTRACE_ATTACH

    :param struct task_struct \*ctp:
        child task pointer

    :param unsigned int mode:
        ptrace attachment mode (PTRACE_MODE\_\*)

.. _`smack_ptrace_access_check.description`:

Description
-----------

Returns 0 if access is OK, an error code otherwise

Do the capability checks.

.. _`smack_ptrace_traceme`:

smack_ptrace_traceme
====================

.. c:function:: int smack_ptrace_traceme(struct task_struct *ptp)

    Smack approval on PTRACE_TRACEME

    :param struct task_struct \*ptp:
        parent task pointer

.. _`smack_ptrace_traceme.description`:

Description
-----------

Returns 0 if access is OK, an error code otherwise

Do the capability checks, and require PTRACE_MODE_ATTACH.

.. _`smack_syslog`:

smack_syslog
============

.. c:function:: int smack_syslog(int typefrom_file)

    Smack approval on syslog

    :param int typefrom_file:
        *undescribed*

.. _`smack_syslog.description`:

Description
-----------

Returns 0 on success, error code otherwise.

.. _`smack_sb_alloc_security`:

smack_sb_alloc_security
=======================

.. c:function:: int smack_sb_alloc_security(struct super_block *sb)

    allocate a superblock blob

    :param struct super_block \*sb:
        the superblock getting the blob

.. _`smack_sb_alloc_security.description`:

Description
-----------

Returns 0 on success or -ENOMEM on error.

.. _`smack_sb_free_security`:

smack_sb_free_security
======================

.. c:function:: void smack_sb_free_security(struct super_block *sb)

    free a superblock blob

    :param struct super_block \*sb:
        the superblock getting the blob

.. _`smack_sb_copy_data`:

smack_sb_copy_data
==================

.. c:function:: int smack_sb_copy_data(char *orig, char *smackopts)

    copy mount options data for processing

    :param char \*orig:
        where to start

    :param char \*smackopts:
        mount options string

.. _`smack_sb_copy_data.description`:

Description
-----------

Returns 0 on success or -ENOMEM on error.

Copy the Smack specific mount options out of the mount
options list.

.. _`smack_parse_opts_str`:

smack_parse_opts_str
====================

.. c:function:: int smack_parse_opts_str(char *options, struct security_mnt_opts *opts)

    parse Smack specific mount options

    :param char \*options:
        mount options string

    :param struct security_mnt_opts \*opts:
        where to store converted mount opts

.. _`smack_parse_opts_str.description`:

Description
-----------

Returns 0 on success or -ENOMEM on error.

converts Smack specific mount options to generic security option format

.. _`smack_set_mnt_opts`:

smack_set_mnt_opts
==================

.. c:function:: int smack_set_mnt_opts(struct super_block *sb, struct security_mnt_opts *opts, unsigned long kern_flags, unsigned long *set_kern_flags)

    set Smack specific mount options

    :param struct super_block \*sb:
        the file system superblock

    :param struct security_mnt_opts \*opts:
        Smack mount options

    :param unsigned long kern_flags:
        mount option from kernel space or user space

    :param unsigned long \*set_kern_flags:
        where to store converted mount opts

.. _`smack_set_mnt_opts.description`:

Description
-----------

Returns 0 on success, an error code on failure

Allow filesystems with binary mount data to explicitly set Smack mount
labels.

.. _`smack_sb_kern_mount`:

smack_sb_kern_mount
===================

.. c:function:: int smack_sb_kern_mount(struct super_block *sb, int flags, void *data)

    Smack specific mount processing

    :param struct super_block \*sb:
        the file system superblock

    :param int flags:
        the mount flags

    :param void \*data:
        the smack mount options

.. _`smack_sb_kern_mount.description`:

Description
-----------

Returns 0 on success, an error code on failure

.. _`smack_sb_statfs`:

smack_sb_statfs
===============

.. c:function:: int smack_sb_statfs(struct dentry *dentry)

    Smack check on statfs

    :param struct dentry \*dentry:
        identifies the file system in question

.. _`smack_sb_statfs.description`:

Description
-----------

Returns 0 if current can read the floor of the filesystem,
and error code otherwise

.. _`smack_bprm_set_creds`:

smack_bprm_set_creds
====================

.. c:function:: int smack_bprm_set_creds(struct linux_binprm *bprm)

    set creds for exec

    :param struct linux_binprm \*bprm:
        the exec information

.. _`smack_bprm_set_creds.description`:

Description
-----------

Returns 0 if it gets a blob, -EPERM if exec forbidden and -ENOMEM otherwise

.. _`smack_inode_alloc_security`:

smack_inode_alloc_security
==========================

.. c:function:: int smack_inode_alloc_security(struct inode *inode)

    allocate an inode blob

    :param struct inode \*inode:
        the inode in need of a blob

.. _`smack_inode_alloc_security.description`:

Description
-----------

Returns 0 if it gets a blob, -ENOMEM otherwise

.. _`smack_inode_free_rcu`:

smack_inode_free_rcu
====================

.. c:function:: void smack_inode_free_rcu(struct rcu_head *head)

    Free inode_smack blob from cache

    :param struct rcu_head \*head:
        the rcu_head for getting inode_smack pointer

.. _`smack_inode_free_rcu.description`:

Description
-----------

Call back function called from \ :c:func:`call_rcu`\  to free
the i_security blob pointer in inode

.. _`smack_inode_free_security`:

smack_inode_free_security
=========================

.. c:function:: void smack_inode_free_security(struct inode *inode)

    free an inode blob using \ :c:func:`call_rcu`\ 

    :param struct inode \*inode:
        the inode with a blob

.. _`smack_inode_free_security.description`:

Description
-----------

Clears the blob pointer in inode using RCU

.. _`smack_inode_init_security`:

smack_inode_init_security
=========================

.. c:function:: int smack_inode_init_security(struct inode *inode, struct inode *dir, const struct qstr *qstr, const char **name, void **value, size_t *len)

    copy out the smack from an inode

    :param struct inode \*inode:
        the newly created inode

    :param struct inode \*dir:
        containing directory object

    :param const struct qstr \*qstr:
        unused

    :param const char \*\*name:
        where to put the attribute name

    :param void \*\*value:
        where to put the attribute value

    :param size_t \*len:
        where to put the length of the attribute

.. _`smack_inode_init_security.description`:

Description
-----------

Returns 0 if it all works out, -ENOMEM if there's no memory

.. _`smack_inode_link`:

smack_inode_link
================

.. c:function:: int smack_inode_link(struct dentry *old_dentry, struct inode *dir, struct dentry *new_dentry)

    Smack check on link

    :param struct dentry \*old_dentry:
        the existing object

    :param struct inode \*dir:
        unused

    :param struct dentry \*new_dentry:
        the new object

.. _`smack_inode_link.description`:

Description
-----------

Returns 0 if access is permitted, an error code otherwise

.. _`smack_inode_unlink`:

smack_inode_unlink
==================

.. c:function:: int smack_inode_unlink(struct inode *dir, struct dentry *dentry)

    Smack check on inode deletion

    :param struct inode \*dir:
        containing directory object

    :param struct dentry \*dentry:
        file to unlink

.. _`smack_inode_unlink.description`:

Description
-----------

Returns 0 if current can write the containing directory
and the object, error code otherwise

.. _`smack_inode_rmdir`:

smack_inode_rmdir
=================

.. c:function:: int smack_inode_rmdir(struct inode *dir, struct dentry *dentry)

    Smack check on directory deletion

    :param struct inode \*dir:
        containing directory object

    :param struct dentry \*dentry:
        directory to unlink

.. _`smack_inode_rmdir.description`:

Description
-----------

Returns 0 if current can write the containing directory
and the directory, error code otherwise

.. _`smack_inode_rename`:

smack_inode_rename
==================

.. c:function:: int smack_inode_rename(struct inode *old_inode, struct dentry *old_dentry, struct inode *new_inode, struct dentry *new_dentry)

    Smack check on rename

    :param struct inode \*old_inode:
        unused

    :param struct dentry \*old_dentry:
        the old object

    :param struct inode \*new_inode:
        unused

    :param struct dentry \*new_dentry:
        the new object

.. _`smack_inode_rename.description`:

Description
-----------

Read and write access is required on both the old and
new directories.

Returns 0 if access is permitted, an error code otherwise

.. _`smack_inode_permission`:

smack_inode_permission
======================

.. c:function:: int smack_inode_permission(struct inode *inode, int mask)

    Smack version of \ :c:func:`permission`\ 

    :param struct inode \*inode:
        the inode in question

    :param int mask:
        the access requested

.. _`smack_inode_permission.description`:

Description
-----------

This is the important Smack hook.

Returns 0 if access is permitted, -EACCES otherwise

.. _`smack_inode_setattr`:

smack_inode_setattr
===================

.. c:function:: int smack_inode_setattr(struct dentry *dentry, struct iattr *iattr)

    Smack check for setting attributes

    :param struct dentry \*dentry:
        the object

    :param struct iattr \*iattr:
        for the force flag

.. _`smack_inode_setattr.description`:

Description
-----------

Returns 0 if access is permitted, an error code otherwise

.. _`smack_inode_getattr`:

smack_inode_getattr
===================

.. c:function:: int smack_inode_getattr(const struct path *path)

    Smack check for getting attributes

    :param const struct path \*path:
        *undescribed*

.. _`smack_inode_getattr.description`:

Description
-----------

Returns 0 if access is permitted, an error code otherwise

.. _`smack_inode_setxattr`:

smack_inode_setxattr
====================

.. c:function:: int smack_inode_setxattr(struct dentry *dentry, const char *name, const void *value, size_t size, int flags)

    Smack check for setting xattrs

    :param struct dentry \*dentry:
        the object

    :param const char \*name:
        name of the attribute

    :param const void \*value:
        value of the attribute

    :param size_t size:
        size of the value

    :param int flags:
        unused

.. _`smack_inode_setxattr.description`:

Description
-----------

This protects the Smack attribute explicitly.

Returns 0 if access is permitted, an error code otherwise

.. _`smack_inode_post_setxattr`:

smack_inode_post_setxattr
=========================

.. c:function:: void smack_inode_post_setxattr(struct dentry *dentry, const char *name, const void *value, size_t size, int flags)

    Apply the Smack update approved above

    :param struct dentry \*dentry:
        object

    :param const char \*name:
        attribute name

    :param const void \*value:
        attribute value

    :param size_t size:
        attribute size

    :param int flags:
        unused

.. _`smack_inode_post_setxattr.description`:

Description
-----------

Set the pointer in the inode blob to the entry found
in the master label list.

.. _`smack_inode_getxattr`:

smack_inode_getxattr
====================

.. c:function:: int smack_inode_getxattr(struct dentry *dentry, const char *name)

    Smack check on getxattr

    :param struct dentry \*dentry:
        the object

    :param const char \*name:
        unused

.. _`smack_inode_getxattr.description`:

Description
-----------

Returns 0 if access is permitted, an error code otherwise

.. _`smack_inode_removexattr`:

smack_inode_removexattr
=======================

.. c:function:: int smack_inode_removexattr(struct dentry *dentry, const char *name)

    Smack check on removexattr

    :param struct dentry \*dentry:
        the object

    :param const char \*name:
        name of the attribute

.. _`smack_inode_removexattr.description`:

Description
-----------

Removing the Smack attribute requires CAP_MAC_ADMIN

Returns 0 if access is permitted, an error code otherwise

.. _`smack_inode_getsecurity`:

smack_inode_getsecurity
=======================

.. c:function:: int smack_inode_getsecurity(struct inode *inode, const char *name, void **buffer, bool alloc)

    get smack xattrs

    :param struct inode \*inode:
        the object

    :param const char \*name:
        attribute name

    :param void \*\*buffer:
        where to put the result

    :param bool alloc:
        duplicate memory

.. _`smack_inode_getsecurity.description`:

Description
-----------

Returns the size of the attribute or an error code

.. _`smack_inode_listsecurity`:

smack_inode_listsecurity
========================

.. c:function:: int smack_inode_listsecurity(struct inode *inode, char *buffer, size_t buffer_size)

    list the Smack attributes

    :param struct inode \*inode:
        the object

    :param char \*buffer:
        where they go

    :param size_t buffer_size:
        size of buffer

.. _`smack_inode_getsecid`:

smack_inode_getsecid
====================

.. c:function:: void smack_inode_getsecid(struct inode *inode, u32 *secid)

    Extract inode's security id

    :param struct inode \*inode:
        inode to extract the info from

    :param u32 \*secid:
        where result will be saved

.. _`smack_file_alloc_security`:

smack_file_alloc_security
=========================

.. c:function:: int smack_file_alloc_security(struct file *file)

    assign a file security blob

    :param struct file \*file:
        the object

.. _`smack_file_alloc_security.description`:

Description
-----------

The security blob for a file is a pointer to the master
label list, so no allocation is done.

f_security is the owner security information. It
isn't used on file access checks, it's for send_sigio.

Returns 0

.. _`smack_file_free_security`:

smack_file_free_security
========================

.. c:function:: void smack_file_free_security(struct file *file)

    clear a file security blob

    :param struct file \*file:
        the object

.. _`smack_file_free_security.description`:

Description
-----------

The security blob for a file is a pointer to the master
label list, so no memory is freed.

.. _`smack_file_ioctl`:

smack_file_ioctl
================

.. c:function:: int smack_file_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    Smack check on ioctls

    :param struct file \*file:
        the object

    :param unsigned int cmd:
        what to do

    :param unsigned long arg:
        unused

.. _`smack_file_ioctl.description`:

Description
-----------

Relies heavily on the correct use of the ioctl command conventions.

Returns 0 if allowed, error code otherwise

.. _`smack_file_lock`:

smack_file_lock
===============

.. c:function:: int smack_file_lock(struct file *file, unsigned int cmd)

    Smack check on file locking

    :param struct file \*file:
        the object

    :param unsigned int cmd:
        unused

.. _`smack_file_lock.description`:

Description
-----------

Returns 0 if current has lock access, error code otherwise

.. _`smack_file_fcntl`:

smack_file_fcntl
================

.. c:function:: int smack_file_fcntl(struct file *file, unsigned int cmd, unsigned long arg)

    Smack check on fcntl

    :param struct file \*file:
        the object

    :param unsigned int cmd:
        what action to check

    :param unsigned long arg:
        unused

.. _`smack_file_fcntl.description`:

Description
-----------

Generally these operations are harmless.
File locking operations present an obvious mechanism
for passing information, so they require write access.

Returns 0 if current has access, error code otherwise

.. _`smack_mmap_file`:

smack_mmap_file
===============

.. c:function:: int smack_mmap_file(struct file *file, unsigned long reqprot, unsigned long prot, unsigned long flags)

    Check permissions for a mmap operation.  The \ ``file``\  may be NULL, e.g. if mapping anonymous memory. \ ``file``\  contains the file structure for file to map (may be NULL). \ ``reqprot``\  contains the protection requested by the application. \ ``prot``\  contains the protection that will be applied by the kernel. \ ``flags``\  contains the operational flags. Return 0 if permission is granted.

    :param struct file \*file:
        *undescribed*

    :param unsigned long reqprot:
        *undescribed*

    :param unsigned long prot:
        *undescribed*

    :param unsigned long flags:
        *undescribed*

.. _`smack_file_set_fowner`:

smack_file_set_fowner
=====================

.. c:function:: void smack_file_set_fowner(struct file *file)

    set the file security blob value

    :param struct file \*file:
        object in question

.. _`smack_file_send_sigiotask`:

smack_file_send_sigiotask
=========================

.. c:function:: int smack_file_send_sigiotask(struct task_struct *tsk, struct fown_struct *fown, int signum)

    Smack on sigio

    :param struct task_struct \*tsk:
        The target task

    :param struct fown_struct \*fown:
        the object the signal come from

    :param int signum:
        unused

.. _`smack_file_send_sigiotask.description`:

Description
-----------

Allow a privileged task to get signals even if it shouldn't

Returns 0 if a subject with the object's smack could
write to the task, an error code otherwise.

.. _`smack_file_receive`:

smack_file_receive
==================

.. c:function:: int smack_file_receive(struct file *file)

    Smack file receive check

    :param struct file \*file:
        the object

.. _`smack_file_receive.description`:

Description
-----------

Returns 0 if current has access, error code otherwise

.. _`smack_file_open`:

smack_file_open
===============

.. c:function:: int smack_file_open(struct file *file, const struct cred *cred)

    Smack dentry open processing

    :param struct file \*file:
        the object

    :param const struct cred \*cred:
        task credential

.. _`smack_file_open.description`:

Description
-----------

Set the security blob in the file structure.
Allow the open only if the task has read access. There are
many read operations (e.g. fstat) that you can do with an
fd even if you have the file open write-only.

Returns 0

.. _`smack_cred_alloc_blank`:

smack_cred_alloc_blank
======================

.. c:function:: int smack_cred_alloc_blank(struct cred *cred, gfp_t gfp)

    "allocate" blank task-level security credentials

    :param struct cred \*cred:
        *undescribed*

    :param gfp_t gfp:
        the atomicity of any memory allocations

.. _`smack_cred_alloc_blank.description`:

Description
-----------

Prepare a blank set of credentials for modification.  This must allocate all
the memory the LSM module might require such that \ :c:func:`cred_transfer`\  can
complete without error.

.. _`smack_cred_free`:

smack_cred_free
===============

.. c:function:: void smack_cred_free(struct cred *cred)

    "free" task-level security credentials

    :param struct cred \*cred:
        the credentials in question

.. _`smack_cred_prepare`:

smack_cred_prepare
==================

.. c:function:: int smack_cred_prepare(struct cred *new, const struct cred *old, gfp_t gfp)

    prepare new set of credentials for modification

    :param struct cred \*new:
        the new credentials

    :param const struct cred \*old:
        the original credentials

    :param gfp_t gfp:
        the atomicity of any memory allocations

.. _`smack_cred_prepare.description`:

Description
-----------

Prepare a new set of credentials for modification.

.. _`smack_cred_transfer`:

smack_cred_transfer
===================

.. c:function:: void smack_cred_transfer(struct cred *new, const struct cred *old)

    Transfer the old credentials to the new credentials

    :param struct cred \*new:
        the new credentials

    :param const struct cred \*old:
        the original credentials

.. _`smack_cred_transfer.description`:

Description
-----------

Fill in a set of blank credentials from another set of credentials.

.. _`smack_cred_getsecid`:

smack_cred_getsecid
===================

.. c:function:: void smack_cred_getsecid(const struct cred *c, u32 *secid)

    get the secid corresponding to a creds structure

    :param const struct cred \*c:
        the object creds

    :param u32 \*secid:
        where to put the result

.. _`smack_cred_getsecid.description`:

Description
-----------

Sets the secid to contain a u32 version of the smack label.

.. _`smack_kernel_act_as`:

smack_kernel_act_as
===================

.. c:function:: int smack_kernel_act_as(struct cred *new, u32 secid)

    Set the subjective context in a set of credentials

    :param struct cred \*new:
        points to the set of credentials to be modified.

    :param u32 secid:
        specifies the security ID to be set

.. _`smack_kernel_act_as.description`:

Description
-----------

Set the security data for a kernel service.

.. _`smack_kernel_create_files_as`:

smack_kernel_create_files_as
============================

.. c:function:: int smack_kernel_create_files_as(struct cred *new, struct inode *inode)

    Set the file creation label in a set of creds

    :param struct cred \*new:
        points to the set of credentials to be modified

    :param struct inode \*inode:
        points to the inode to use as a reference

.. _`smack_kernel_create_files_as.description`:

Description
-----------

Set the file creation context in a set of credentials to the same
as the objective context of the specified inode

.. _`smk_curacc_on_task`:

smk_curacc_on_task
==================

.. c:function:: int smk_curacc_on_task(struct task_struct *p, int access, const char *caller)

    helper to log task related access

    :param struct task_struct \*p:
        the task object

    :param int access:
        the access requested

    :param const char \*caller:
        name of the calling function for audit

.. _`smk_curacc_on_task.description`:

Description
-----------

Return 0 if access is permitted

.. _`smack_task_setpgid`:

smack_task_setpgid
==================

.. c:function:: int smack_task_setpgid(struct task_struct *p, pid_t pgid)

    Smack check on setting pgid

    :param struct task_struct \*p:
        the task object

    :param pid_t pgid:
        unused

.. _`smack_task_setpgid.description`:

Description
-----------

Return 0 if write access is permitted

.. _`smack_task_getpgid`:

smack_task_getpgid
==================

.. c:function:: int smack_task_getpgid(struct task_struct *p)

    Smack access check for getpgid

    :param struct task_struct \*p:
        the object task

.. _`smack_task_getpgid.description`:

Description
-----------

Returns 0 if current can read the object task, error code otherwise

.. _`smack_task_getsid`:

smack_task_getsid
=================

.. c:function:: int smack_task_getsid(struct task_struct *p)

    Smack access check for getsid

    :param struct task_struct \*p:
        the object task

.. _`smack_task_getsid.description`:

Description
-----------

Returns 0 if current can read the object task, error code otherwise

.. _`smack_task_getsecid`:

smack_task_getsecid
===================

.. c:function:: void smack_task_getsecid(struct task_struct *p, u32 *secid)

    get the secid of the task

    :param struct task_struct \*p:
        the object task

    :param u32 \*secid:
        where to put the result

.. _`smack_task_getsecid.description`:

Description
-----------

Sets the secid to contain a u32 version of the smack label.

.. _`smack_task_setnice`:

smack_task_setnice
==================

.. c:function:: int smack_task_setnice(struct task_struct *p, int nice)

    Smack check on setting nice

    :param struct task_struct \*p:
        the task object

    :param int nice:
        unused

.. _`smack_task_setnice.description`:

Description
-----------

Return 0 if write access is permitted

.. _`smack_task_setioprio`:

smack_task_setioprio
====================

.. c:function:: int smack_task_setioprio(struct task_struct *p, int ioprio)

    Smack check on setting ioprio

    :param struct task_struct \*p:
        the task object

    :param int ioprio:
        unused

.. _`smack_task_setioprio.description`:

Description
-----------

Return 0 if write access is permitted

.. _`smack_task_getioprio`:

smack_task_getioprio
====================

.. c:function:: int smack_task_getioprio(struct task_struct *p)

    Smack check on reading ioprio

    :param struct task_struct \*p:
        the task object

.. _`smack_task_getioprio.description`:

Description
-----------

Return 0 if read access is permitted

.. _`smack_task_setscheduler`:

smack_task_setscheduler
=======================

.. c:function:: int smack_task_setscheduler(struct task_struct *p)

    Smack check on setting scheduler

    :param struct task_struct \*p:
        the task object

.. _`smack_task_setscheduler.description`:

Description
-----------

Return 0 if read access is permitted

.. _`smack_task_getscheduler`:

smack_task_getscheduler
=======================

.. c:function:: int smack_task_getscheduler(struct task_struct *p)

    Smack check on reading scheduler

    :param struct task_struct \*p:
        the task object

.. _`smack_task_getscheduler.description`:

Description
-----------

Return 0 if read access is permitted

.. _`smack_task_movememory`:

smack_task_movememory
=====================

.. c:function:: int smack_task_movememory(struct task_struct *p)

    Smack check on moving memory

    :param struct task_struct \*p:
        the task object

.. _`smack_task_movememory.description`:

Description
-----------

Return 0 if write access is permitted

.. _`smack_task_kill`:

smack_task_kill
===============

.. c:function:: int smack_task_kill(struct task_struct *p, struct siginfo *info, int sig, const struct cred *cred)

    Smack check on signal delivery

    :param struct task_struct \*p:
        the task object

    :param struct siginfo \*info:
        unused

    :param int sig:
        unused

    :param const struct cred \*cred:
        identifies the cred to use in lieu of current's

.. _`smack_task_kill.description`:

Description
-----------

Return 0 if write access is permitted

.. _`smack_task_to_inode`:

smack_task_to_inode
===================

.. c:function:: void smack_task_to_inode(struct task_struct *p, struct inode *inode)

    copy task smack into the inode blob

    :param struct task_struct \*p:
        task to copy from

    :param struct inode \*inode:
        inode to copy to

.. _`smack_task_to_inode.description`:

Description
-----------

Sets the smack pointer in the inode security blob

.. _`smack_sk_alloc_security`:

smack_sk_alloc_security
=======================

.. c:function:: int smack_sk_alloc_security(struct sock *sk, int family, gfp_t gfp_flags)

    Allocate a socket blob

    :param struct sock \*sk:
        the socket

    :param int family:
        unused

    :param gfp_t gfp_flags:
        memory allocation flags

.. _`smack_sk_alloc_security.description`:

Description
-----------

Assign Smack pointers to current

Returns 0 on success, -ENOMEM is there's no memory

.. _`smack_sk_free_security`:

smack_sk_free_security
======================

.. c:function:: void smack_sk_free_security(struct sock *sk)

    Free a socket blob

    :param struct sock \*sk:
        the socket

.. _`smack_sk_free_security.description`:

Description
-----------

Clears the blob pointer

.. _`smack_ipv4host_label`:

smack_ipv4host_label
====================

.. c:function:: struct smack_known *smack_ipv4host_label(struct sockaddr_in *sip)

    check host based restrictions

    :param struct sockaddr_in \*sip:
        the object end

.. _`smack_ipv4host_label.description`:

Description
-----------

looks for host based access restrictions

This version will only be appropriate for really small sets of single label
hosts.  The caller is responsible for ensuring that the RCU read lock is
taken before calling this function.

Returns the label of the far end or NULL if it's not special.

.. _`smack_ipv6host_label`:

smack_ipv6host_label
====================

.. c:function:: struct smack_known *smack_ipv6host_label(struct sockaddr_in6 *sip)

    check host based restrictions

    :param struct sockaddr_in6 \*sip:
        the object end

.. _`smack_ipv6host_label.description`:

Description
-----------

looks for host based access restrictions

This version will only be appropriate for really small sets of single label
hosts.  The caller is responsible for ensuring that the RCU read lock is
taken before calling this function.

Returns the label of the far end or NULL if it's not special.

.. _`smack_netlabel`:

smack_netlabel
==============

.. c:function:: int smack_netlabel(struct sock *sk, int labeled)

    Set the secattr on a socket

    :param struct sock \*sk:
        the socket

    :param int labeled:
        socket label scheme

.. _`smack_netlabel.description`:

Description
-----------

Convert the outbound smack value (smk_out) to a
secattr and attach it to the socket.

Returns 0 on success or an error code

.. _`smack_netlabel_send`:

smack_netlabel_send
===================

.. c:function:: int smack_netlabel_send(struct sock *sk, struct sockaddr_in *sap)

    Set the secattr on a socket and perform access checks

    :param struct sock \*sk:
        the socket

    :param struct sockaddr_in \*sap:
        the destination address

.. _`smack_netlabel_send.description`:

Description
-----------

Set the correct secattr for the given socket based on the destination
address and perform any outbound access checks needed.

Returns 0 on success or an error code.

.. _`smk_ipv6_check`:

smk_ipv6_check
==============

.. c:function:: int smk_ipv6_check(struct smack_known *subject, struct smack_known *object, struct sockaddr_in6 *address, int act)

    check Smack access

    :param struct smack_known \*subject:
        subject Smack label

    :param struct smack_known \*object:
        object Smack label

    :param struct sockaddr_in6 \*address:
        address

    :param int act:
        the action being taken

.. _`smk_ipv6_check.description`:

Description
-----------

Check an IPv6 access

.. _`smk_ipv6_port_label`:

smk_ipv6_port_label
===================

.. c:function:: void smk_ipv6_port_label(struct socket *sock, struct sockaddr *address)

    Smack port access table management

    :param struct socket \*sock:
        socket

    :param struct sockaddr \*address:
        address

.. _`smk_ipv6_port_label.description`:

Description
-----------

Create or update the port list entry

.. _`smk_ipv6_port_check`:

smk_ipv6_port_check
===================

.. c:function:: int smk_ipv6_port_check(struct sock *sk, struct sockaddr_in6 *address, int act)

    check Smack port access

    :param struct sock \*sk:
        *undescribed*

    :param struct sockaddr_in6 \*address:
        address

    :param int act:
        *undescribed*

.. _`smk_ipv6_port_check.description`:

Description
-----------

Create or update the port list entry

.. _`smack_inode_setsecurity`:

smack_inode_setsecurity
=======================

.. c:function:: int smack_inode_setsecurity(struct inode *inode, const char *name, const void *value, size_t size, int flags)

    set smack xattrs

    :param struct inode \*inode:
        the object

    :param const char \*name:
        attribute name

    :param const void \*value:
        attribute value

    :param size_t size:
        size of the attribute

    :param int flags:
        unused

.. _`smack_inode_setsecurity.description`:

Description
-----------

Sets the named attribute in the appropriate blob

Returns 0 on success, or an error code

.. _`smack_socket_post_create`:

smack_socket_post_create
========================

.. c:function:: int smack_socket_post_create(struct socket *sock, int family, int type, int protocol, int kern)

    finish socket setup

    :param struct socket \*sock:
        the socket

    :param int family:
        protocol family

    :param int type:
        unused

    :param int protocol:
        unused

    :param int kern:
        unused

.. _`smack_socket_post_create.description`:

Description
-----------

Sets the netlabel information on the socket

Returns 0 on success, and error code otherwise

.. _`smack_socket_socketpair`:

smack_socket_socketpair
=======================

.. c:function:: int smack_socket_socketpair(struct socket *socka, struct socket *sockb)

    create socket pair

    :param struct socket \*socka:
        one socket

    :param struct socket \*sockb:
        another socket

.. _`smack_socket_socketpair.description`:

Description
-----------

Cross reference the peer labels for SO_PEERSEC

Returns 0 on success, and error code otherwise

.. _`smack_socket_bind`:

smack_socket_bind
=================

.. c:function:: int smack_socket_bind(struct socket *sock, struct sockaddr *address, int addrlen)

    record port binding information.

    :param struct socket \*sock:
        the socket

    :param struct sockaddr \*address:
        the port address

    :param int addrlen:
        size of the address

.. _`smack_socket_bind.description`:

Description
-----------

Records the label bound to a port.

Returns 0

.. _`smack_socket_connect`:

smack_socket_connect
====================

.. c:function:: int smack_socket_connect(struct socket *sock, struct sockaddr *sap, int addrlen)

    connect access check

    :param struct socket \*sock:
        the socket

    :param struct sockaddr \*sap:
        the other end

    :param int addrlen:
        size of sap

.. _`smack_socket_connect.description`:

Description
-----------

Verifies that a connection may be possible

Returns 0 on success, and error code otherwise

.. _`smack_flags_to_may`:

smack_flags_to_may
==================

.. c:function:: int smack_flags_to_may(int flags)

    convert S\_ to MAY\_ values

    :param int flags:
        the S\_ value

.. _`smack_flags_to_may.description`:

Description
-----------

Returns the equivalent MAY\_ value

.. _`smack_msg_msg_alloc_security`:

smack_msg_msg_alloc_security
============================

.. c:function:: int smack_msg_msg_alloc_security(struct msg_msg *msg)

    Set the security blob for msg_msg

    :param struct msg_msg \*msg:
        the object

.. _`smack_msg_msg_alloc_security.description`:

Description
-----------

Returns 0

.. _`smack_msg_msg_free_security`:

smack_msg_msg_free_security
===========================

.. c:function:: void smack_msg_msg_free_security(struct msg_msg *msg)

    Clear the security blob for msg_msg

    :param struct msg_msg \*msg:
        the object

.. _`smack_msg_msg_free_security.description`:

Description
-----------

Clears the blob pointer

.. _`smack_of_ipc`:

smack_of_ipc
============

.. c:function:: struct smack_known *smack_of_ipc(struct kern_ipc_perm *isp)

    the smack pointer for the ipc

    :param struct kern_ipc_perm \*isp:
        the object

.. _`smack_of_ipc.description`:

Description
-----------

Returns a pointer to the smack value

.. _`smack_ipc_alloc_security`:

smack_ipc_alloc_security
========================

.. c:function:: int smack_ipc_alloc_security(struct kern_ipc_perm *isp)

    Set the security blob for ipc

    :param struct kern_ipc_perm \*isp:
        the object

.. _`smack_ipc_alloc_security.description`:

Description
-----------

Returns 0

.. _`smack_ipc_free_security`:

smack_ipc_free_security
=======================

.. c:function:: void smack_ipc_free_security(struct kern_ipc_perm *isp)

    Clear the security blob for ipc

    :param struct kern_ipc_perm \*isp:
        the object

.. _`smack_ipc_free_security.description`:

Description
-----------

Clears the blob pointer

.. _`smk_curacc_shm`:

smk_curacc_shm
==============

.. c:function:: int smk_curacc_shm(struct kern_ipc_perm *isp, int access)

    check if current has access on shm

    :param struct kern_ipc_perm \*isp:
        the object

    :param int access:
        access requested

.. _`smk_curacc_shm.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_shm_associate`:

smack_shm_associate
===================

.. c:function:: int smack_shm_associate(struct kern_ipc_perm *isp, int shmflg)

    Smack access check for shm

    :param struct kern_ipc_perm \*isp:
        the object

    :param int shmflg:
        access requested

.. _`smack_shm_associate.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_shm_shmctl`:

smack_shm_shmctl
================

.. c:function:: int smack_shm_shmctl(struct kern_ipc_perm *isp, int cmd)

    Smack access check for shm

    :param struct kern_ipc_perm \*isp:
        the object

    :param int cmd:
        what it wants to do

.. _`smack_shm_shmctl.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_shm_shmat`:

smack_shm_shmat
===============

.. c:function:: int smack_shm_shmat(struct kern_ipc_perm *ipc, char __user *shmaddr, int shmflg)

    Smack access for shmat

    :param struct kern_ipc_perm \*ipc:
        *undescribed*

    :param char __user \*shmaddr:
        unused

    :param int shmflg:
        access requested

.. _`smack_shm_shmat.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smk_curacc_sem`:

smk_curacc_sem
==============

.. c:function:: int smk_curacc_sem(struct kern_ipc_perm *isp, int access)

    check if current has access on sem

    :param struct kern_ipc_perm \*isp:
        the object

    :param int access:
        access requested

.. _`smk_curacc_sem.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_sem_associate`:

smack_sem_associate
===================

.. c:function:: int smack_sem_associate(struct kern_ipc_perm *isp, int semflg)

    Smack access check for sem

    :param struct kern_ipc_perm \*isp:
        the object

    :param int semflg:
        access requested

.. _`smack_sem_associate.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_sem_semctl`:

smack_sem_semctl
================

.. c:function:: int smack_sem_semctl(struct kern_ipc_perm *isp, int cmd)

    Smack access check for sem

    :param struct kern_ipc_perm \*isp:
        the object

    :param int cmd:
        what it wants to do

.. _`smack_sem_semctl.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_sem_semop`:

smack_sem_semop
===============

.. c:function:: int smack_sem_semop(struct kern_ipc_perm *isp, struct sembuf *sops, unsigned nsops, int alter)

    Smack checks of semaphore operations

    :param struct kern_ipc_perm \*isp:
        the object

    :param struct sembuf \*sops:
        unused

    :param unsigned nsops:
        unused

    :param int alter:
        unused

.. _`smack_sem_semop.description`:

Description
-----------

Treated as read and write in all cases.

Returns 0 if access is allowed, error code otherwise

.. _`smk_curacc_msq`:

smk_curacc_msq
==============

.. c:function:: int smk_curacc_msq(struct kern_ipc_perm *isp, int access)

    helper to check if current has access on msq

    :param struct kern_ipc_perm \*isp:
        the msq

    :param int access:
        access requested

.. _`smk_curacc_msq.description`:

Description
-----------

return 0 if current has access, error otherwise

.. _`smack_msg_queue_associate`:

smack_msg_queue_associate
=========================

.. c:function:: int smack_msg_queue_associate(struct kern_ipc_perm *isp, int msqflg)

    Smack access check for msg_queue

    :param struct kern_ipc_perm \*isp:
        the object

    :param int msqflg:
        access requested

.. _`smack_msg_queue_associate.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_msg_queue_msgctl`:

smack_msg_queue_msgctl
======================

.. c:function:: int smack_msg_queue_msgctl(struct kern_ipc_perm *isp, int cmd)

    Smack access check for msg_queue

    :param struct kern_ipc_perm \*isp:
        the object

    :param int cmd:
        what it wants to do

.. _`smack_msg_queue_msgctl.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_msg_queue_msgsnd`:

smack_msg_queue_msgsnd
======================

.. c:function:: int smack_msg_queue_msgsnd(struct kern_ipc_perm *isp, struct msg_msg *msg, int msqflg)

    Smack access check for msg_queue

    :param struct kern_ipc_perm \*isp:
        the object

    :param struct msg_msg \*msg:
        unused

    :param int msqflg:
        access requested

.. _`smack_msg_queue_msgsnd.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_msg_queue_msgrcv`:

smack_msg_queue_msgrcv
======================

.. c:function:: int smack_msg_queue_msgrcv(struct kern_ipc_perm *isp, struct msg_msg *msg, struct task_struct *target, long type, int mode)

    Smack access check for msg_queue

    :param struct kern_ipc_perm \*isp:
        the object

    :param struct msg_msg \*msg:
        unused

    :param struct task_struct \*target:
        unused

    :param long type:
        unused

    :param int mode:
        unused

.. _`smack_msg_queue_msgrcv.description`:

Description
-----------

Returns 0 if current has read and write access, error code otherwise

.. _`smack_ipc_permission`:

smack_ipc_permission
====================

.. c:function:: int smack_ipc_permission(struct kern_ipc_perm *ipp, short flag)

    Smack access for \ :c:func:`ipc_permission`\ 

    :param struct kern_ipc_perm \*ipp:
        the object permissions

    :param short flag:
        access requested

.. _`smack_ipc_permission.description`:

Description
-----------

Returns 0 if current has read and write access, error code otherwise

.. _`smack_ipc_getsecid`:

smack_ipc_getsecid
==================

.. c:function:: void smack_ipc_getsecid(struct kern_ipc_perm *ipp, u32 *secid)

    Extract smack security id

    :param struct kern_ipc_perm \*ipp:
        the object permissions

    :param u32 \*secid:
        where result will be saved

.. _`smack_d_instantiate`:

smack_d_instantiate
===================

.. c:function:: void smack_d_instantiate(struct dentry *opt_dentry, struct inode *inode)

    Make sure the blob is correct on an inode

    :param struct dentry \*opt_dentry:
        dentry where inode will be attached

    :param struct inode \*inode:
        the object

.. _`smack_d_instantiate.description`:

Description
-----------

Set the inode's security blob if it hasn't been done already.

.. _`smack_getprocattr`:

smack_getprocattr
=================

.. c:function:: int smack_getprocattr(struct task_struct *p, char *name, char **value)

    Smack process attribute access

    :param struct task_struct \*p:
        the object task

    :param char \*name:
        the name of the attribute in /proc/.../attr

    :param char \*\*value:
        where to put the result

.. _`smack_getprocattr.description`:

Description
-----------

Places a copy of the task Smack into value

Returns the length of the smack label or an error code

.. _`smack_setprocattr`:

smack_setprocattr
=================

.. c:function:: int smack_setprocattr(const char *name, void *value, size_t size)

    Smack process attribute setting

    :param const char \*name:
        the name of the attribute in /proc/.../attr

    :param void \*value:
        the value to set

    :param size_t size:
        the size of the value

.. _`smack_setprocattr.description`:

Description
-----------

Sets the Smack value of the task. Only setting self
is permitted and only with privilege

Returns the length of the smack label or an error code

.. _`smack_unix_stream_connect`:

smack_unix_stream_connect
=========================

.. c:function:: int smack_unix_stream_connect(struct sock *sock, struct sock *other, struct sock *newsk)

    Smack access on UDS

    :param struct sock \*sock:
        one sock

    :param struct sock \*other:
        the other sock

    :param struct sock \*newsk:
        unused

.. _`smack_unix_stream_connect.description`:

Description
-----------

Return 0 if a subject with the smack of sock could access
an object with the smack of other, otherwise an error code

.. _`smack_unix_may_send`:

smack_unix_may_send
===================

.. c:function:: int smack_unix_may_send(struct socket *sock, struct socket *other)

    Smack access on UDS

    :param struct socket \*sock:
        one socket

    :param struct socket \*other:
        the other socket

.. _`smack_unix_may_send.description`:

Description
-----------

Return 0 if a subject with the smack of sock could access
an object with the smack of other, otherwise an error code

.. _`smack_socket_sendmsg`:

smack_socket_sendmsg
====================

.. c:function:: int smack_socket_sendmsg(struct socket *sock, struct msghdr *msg, int size)

    Smack check based on destination host

    :param struct socket \*sock:
        the socket

    :param struct msghdr \*msg:
        the message

    :param int size:
        the size of the message

.. _`smack_socket_sendmsg.description`:

Description
-----------

Return 0 if the current subject can write to the destination host.
For IPv4 this is only a question if the destination is a single label host.
For IPv6 this is a check against the label of the port.

.. _`smack_from_secattr`:

smack_from_secattr
==================

.. c:function:: struct smack_known *smack_from_secattr(struct netlbl_lsm_secattr *sap, struct socket_smack *ssp)

    Convert a netlabel attr.mls.lvl/attr.mls.cat pair to smack

    :param struct netlbl_lsm_secattr \*sap:
        netlabel secattr

    :param struct socket_smack \*ssp:
        socket security information

.. _`smack_from_secattr.description`:

Description
-----------

Returns a pointer to a Smack label entry found on the label list.

.. _`smack_socket_sock_rcv_skb`:

smack_socket_sock_rcv_skb
=========================

.. c:function:: int smack_socket_sock_rcv_skb(struct sock *sk, struct sk_buff *skb)

    Smack packet delivery access check

    :param struct sock \*sk:
        socket

    :param struct sk_buff \*skb:
        packet

.. _`smack_socket_sock_rcv_skb.description`:

Description
-----------

Returns 0 if the packet should be delivered, an error code otherwise

.. _`smack_socket_getpeersec_stream`:

smack_socket_getpeersec_stream
==============================

.. c:function:: int smack_socket_getpeersec_stream(struct socket *sock, char __user *optval, int __user *optlen, unsigned len)

    pull in packet label

    :param struct socket \*sock:
        the socket

    :param char __user \*optval:
        user's destination

    :param int __user \*optlen:
        size thereof

    :param unsigned len:
        max thereof

.. _`smack_socket_getpeersec_stream.description`:

Description
-----------

returns zero on success, an error code otherwise

.. _`smack_socket_getpeersec_dgram`:

smack_socket_getpeersec_dgram
=============================

.. c:function:: int smack_socket_getpeersec_dgram(struct socket *sock, struct sk_buff *skb, u32 *secid)

    pull in packet label

    :param struct socket \*sock:
        the peer socket

    :param struct sk_buff \*skb:
        packet data

    :param u32 \*secid:
        pointer to where to put the secid of the packet

.. _`smack_socket_getpeersec_dgram.description`:

Description
-----------

Sets the netlabel socket state on sk from parent

.. _`smack_sock_graft`:

smack_sock_graft
================

.. c:function:: void smack_sock_graft(struct sock *sk, struct socket *parent)

    Initialize a newly created socket with an existing sock

    :param struct sock \*sk:
        child sock

    :param struct socket \*parent:
        parent socket

.. _`smack_sock_graft.description`:

Description
-----------

Set the smk_{in,out} state of an existing sock based on the process that
is creating the new socket.

.. _`smack_inet_conn_request`:

smack_inet_conn_request
=======================

.. c:function:: int smack_inet_conn_request(struct sock *sk, struct sk_buff *skb, struct request_sock *req)

    Smack access check on connect

    :param struct sock \*sk:
        socket involved

    :param struct sk_buff \*skb:
        packet

    :param struct request_sock \*req:
        unused

.. _`smack_inet_conn_request.description`:

Description
-----------

Returns 0 if a task with the packet label could write to
the socket, otherwise an error code

.. _`smack_inet_csk_clone`:

smack_inet_csk_clone
====================

.. c:function:: void smack_inet_csk_clone(struct sock *sk, const struct request_sock *req)

    Copy the connection information to the new socket

    :param struct sock \*sk:
        the new socket

    :param const struct request_sock \*req:
        the connection's request_sock

.. _`smack_inet_csk_clone.description`:

Description
-----------

Transfer the connection's peer label to the newly created socket.

.. _`smack_key_alloc`:

smack_key_alloc
===============

.. c:function:: int smack_key_alloc(struct key *key, const struct cred *cred, unsigned long flags)

    Set the key security blob

    :param struct key \*key:
        object

    :param const struct cred \*cred:
        the credentials to use

    :param unsigned long flags:
        unused

.. _`smack_key_alloc.description`:

Description
-----------

No allocation required

Returns 0

.. _`smack_key_free`:

smack_key_free
==============

.. c:function:: void smack_key_free(struct key *key)

    Clear the key security blob

    :param struct key \*key:
        the object

.. _`smack_key_free.description`:

Description
-----------

Clear the blob pointer

.. _`smack_key_permission`:

smack_key_permission
====================

.. c:function:: int smack_key_permission(key_ref_t key_ref, const struct cred *cred, unsigned perm)

    Smack access on a key

    :param key_ref_t key_ref:
        gets to the object

    :param const struct cred \*cred:
        the credentials to use

    :param unsigned perm:
        requested key permissions

.. _`smack_key_permission.description`:

Description
-----------

Return 0 if the task has read and write to the object,
an error code otherwise

.. _`smack_audit_rule_init`:

smack_audit_rule_init
=====================

.. c:function:: int smack_audit_rule_init(u32 field, u32 op, char *rulestr, void **vrule)

    Initialize a smack audit rule

    :param u32 field:
        audit rule fields given from user-space (audit.h)

    :param u32 op:
        required testing operator (=, !=, >, <, ...)

    :param char \*rulestr:
        smack label to be audited

    :param void \*\*vrule:
        pointer to save our own audit rule representation

.. _`smack_audit_rule_init.description`:

Description
-----------

Prepare to audit cases where (@field \ ``op``\  \ ``rulestr``\ ) is true.
The label to be audited is created if necessay.

.. _`smack_audit_rule_known`:

smack_audit_rule_known
======================

.. c:function:: int smack_audit_rule_known(struct audit_krule *krule)

    Distinguish Smack audit rules

    :param struct audit_krule \*krule:
        rule of interest, in Audit kernel representation format

.. _`smack_audit_rule_known.description`:

Description
-----------

This is used to filter Smack rules from remaining Audit ones.
If it's proved that this rule belongs to us, the
audit_rule_match hook will be called to do the final judgement.

.. _`smack_audit_rule_match`:

smack_audit_rule_match
======================

.. c:function:: int smack_audit_rule_match(u32 secid, u32 field, u32 op, void *vrule, struct audit_context *actx)

    Audit given object ?

    :param u32 secid:
        security id for identifying the object to test

    :param u32 field:
        audit rule flags given from user-space

    :param u32 op:
        required testing operator

    :param void \*vrule:
        smack internal rule presentation

    :param struct audit_context \*actx:
        audit context associated with the check

.. _`smack_audit_rule_match.description`:

Description
-----------

The core Audit hook. It's used to take the decision of
whether to audit or not to audit a given object.

.. _`smack_ismaclabel`:

smack_ismaclabel
================

.. c:function:: int smack_ismaclabel(const char *name)

    check if xattr \ ``name``\  references a smack MAC label

    :param const char \*name:
        Full xattr name to check.

.. _`smack_secid_to_secctx`:

smack_secid_to_secctx
=====================

.. c:function:: int smack_secid_to_secctx(u32 secid, char **secdata, u32 *seclen)

    return the smack label for a secid

    :param u32 secid:
        incoming integer

    :param char \*\*secdata:
        destination

    :param u32 \*seclen:
        how long it is

.. _`smack_secid_to_secctx.description`:

Description
-----------

Exists for networking code.

.. _`smack_secctx_to_secid`:

smack_secctx_to_secid
=====================

.. c:function:: int smack_secctx_to_secid(const char *secdata, u32 seclen, u32 *secid)

    return the secid for a smack label

    :param const char \*secdata:
        smack label

    :param u32 seclen:
        how long result is

    :param u32 \*secid:
        outgoing integer

.. _`smack_secctx_to_secid.description`:

Description
-----------

Exists for audit and networking code.

.. _`smack_init`:

smack_init
==========

.. c:function:: int smack_init( void)

    initialize the smack system

    :param  void:
        no arguments

.. _`smack_init.description`:

Description
-----------

Returns 0

.. This file was automatic generated / don't edit.

