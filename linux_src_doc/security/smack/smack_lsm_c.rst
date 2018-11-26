.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/smack/smack_lsm.c

.. _`smk_fetch`:

smk_fetch
=========

.. c:function:: struct smack_known *smk_fetch(const char *name, struct inode *ip, struct dentry *dp)

    Fetch the smack label from a file.

    :param name:
        type of the label (attribute)
    :type name: const char \*

    :param ip:
        a pointer to the inode
    :type ip: struct inode \*

    :param dp:
        a pointer to the dentry
    :type dp: struct dentry \*

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

    :param skp:
        a pointer to the Smack label entry to use in the blob
    :type skp: struct smack_known \*

.. _`new_inode_smack.description`:

Description
-----------

Returns the new blob or NULL if there's no memory available

.. _`new_task_smack`:

new_task_smack
==============

.. c:function:: struct task_smack *new_task_smack(struct smack_known *task, struct smack_known *forked, gfp_t gfp)

    allocate a task security blob

    :param task:
        a pointer to the Smack label for the running task
    :type task: struct smack_known \*

    :param forked:
        a pointer to the Smack label for the forked task
    :type forked: struct smack_known \*

    :param gfp:
        type of the memory for the allocation
    :type gfp: gfp_t

.. _`new_task_smack.description`:

Description
-----------

Returns the new blob or NULL if there's no memory available

.. _`smk_copy_rules`:

smk_copy_rules
==============

.. c:function:: int smk_copy_rules(struct list_head *nhead, struct list_head *ohead, gfp_t gfp)

    copy a rule set

    :param nhead:
        new rules header pointer
    :type nhead: struct list_head \*

    :param ohead:
        old rules header pointer
    :type ohead: struct list_head \*

    :param gfp:
        type of the memory for the allocation
    :type gfp: gfp_t

.. _`smk_copy_rules.description`:

Description
-----------

Returns 0 on success, -ENOMEM on error

.. _`smk_copy_relabel`:

smk_copy_relabel
================

.. c:function:: int smk_copy_relabel(struct list_head *nhead, struct list_head *ohead, gfp_t gfp)

    copy smk_relabel labels list

    :param nhead:
        new rules header pointer
    :type nhead: struct list_head \*

    :param ohead:
        old rules header pointer
    :type ohead: struct list_head \*

    :param gfp:
        type of the memory for the allocation
    :type gfp: gfp_t

.. _`smk_copy_relabel.description`:

Description
-----------

Returns 0 on success, -ENOMEM on error

.. _`smk_ptrace_mode`:

smk_ptrace_mode
===============

.. c:function:: unsigned int smk_ptrace_mode(unsigned int mode)

    helper function for converting PTRACE_MODE\_\* into MAY\_\* \ ``mode``\  - input mode in form of PTRACE_MODE\_\*

    :param mode:
        *undescribed*
    :type mode: unsigned int

.. _`smk_ptrace_mode.description`:

Description
-----------

Returns a converted MAY\_\* mode usable by smack rules

.. _`smk_ptrace_rule_check`:

smk_ptrace_rule_check
=====================

.. c:function:: int smk_ptrace_rule_check(struct task_struct *tracer, struct smack_known *tracee_known, unsigned int mode, const char *func)

    helper for ptrace access

    :param tracer:
        tracer process
    :type tracer: struct task_struct \*

    :param tracee_known:
        label entry of the process that's about to be traced
    :type tracee_known: struct smack_known \*

    :param mode:
        ptrace attachment mode (PTRACE_MODE\_\*)
    :type mode: unsigned int

    :param func:
        name of the function that called us, used for audit
    :type func: const char \*

.. _`smk_ptrace_rule_check.description`:

Description
-----------

Returns 0 on access granted, -error on error

.. _`smack_ptrace_access_check`:

smack_ptrace_access_check
=========================

.. c:function:: int smack_ptrace_access_check(struct task_struct *ctp, unsigned int mode)

    Smack approval on PTRACE_ATTACH

    :param ctp:
        child task pointer
    :type ctp: struct task_struct \*

    :param mode:
        ptrace attachment mode (PTRACE_MODE\_\*)
    :type mode: unsigned int

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

    :param ptp:
        parent task pointer
    :type ptp: struct task_struct \*

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

    :param typefrom_file:
        *undescribed*
    :type typefrom_file: int

.. _`smack_syslog.description`:

Description
-----------

Returns 0 on success, error code otherwise.

.. _`smack_sb_alloc_security`:

smack_sb_alloc_security
=======================

.. c:function:: int smack_sb_alloc_security(struct super_block *sb)

    allocate a superblock blob

    :param sb:
        the superblock getting the blob
    :type sb: struct super_block \*

.. _`smack_sb_alloc_security.description`:

Description
-----------

Returns 0 on success or -ENOMEM on error.

.. _`smack_sb_free_security`:

smack_sb_free_security
======================

.. c:function:: void smack_sb_free_security(struct super_block *sb)

    free a superblock blob

    :param sb:
        the superblock getting the blob
    :type sb: struct super_block \*

.. _`smack_sb_copy_data`:

smack_sb_copy_data
==================

.. c:function:: int smack_sb_copy_data(char *orig, char *smackopts)

    copy mount options data for processing

    :param orig:
        where to start
    :type orig: char \*

    :param smackopts:
        mount options string
    :type smackopts: char \*

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

    :param options:
        mount options string
    :type options: char \*

    :param opts:
        where to store converted mount opts
    :type opts: struct security_mnt_opts \*

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

    :param sb:
        the file system superblock
    :type sb: struct super_block \*

    :param opts:
        Smack mount options
    :type opts: struct security_mnt_opts \*

    :param kern_flags:
        mount option from kernel space or user space
    :type kern_flags: unsigned long

    :param set_kern_flags:
        where to store converted mount opts
    :type set_kern_flags: unsigned long \*

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

    :param sb:
        the file system superblock
    :type sb: struct super_block \*

    :param flags:
        the mount flags
    :type flags: int

    :param data:
        the smack mount options
    :type data: void \*

.. _`smack_sb_kern_mount.description`:

Description
-----------

Returns 0 on success, an error code on failure

.. _`smack_sb_statfs`:

smack_sb_statfs
===============

.. c:function:: int smack_sb_statfs(struct dentry *dentry)

    Smack check on statfs

    :param dentry:
        identifies the file system in question
    :type dentry: struct dentry \*

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

    :param bprm:
        the exec information
    :type bprm: struct linux_binprm \*

.. _`smack_bprm_set_creds.description`:

Description
-----------

Returns 0 if it gets a blob, -EPERM if exec forbidden and -ENOMEM otherwise

.. _`smack_inode_alloc_security`:

smack_inode_alloc_security
==========================

.. c:function:: int smack_inode_alloc_security(struct inode *inode)

    allocate an inode blob

    :param inode:
        the inode in need of a blob
    :type inode: struct inode \*

.. _`smack_inode_alloc_security.description`:

Description
-----------

Returns 0 if it gets a blob, -ENOMEM otherwise

.. _`smack_inode_free_rcu`:

smack_inode_free_rcu
====================

.. c:function:: void smack_inode_free_rcu(struct rcu_head *head)

    Free inode_smack blob from cache

    :param head:
        the rcu_head for getting inode_smack pointer
    :type head: struct rcu_head \*

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

    :param inode:
        the inode with a blob
    :type inode: struct inode \*

.. _`smack_inode_free_security.description`:

Description
-----------

Clears the blob pointer in inode using RCU

.. _`smack_inode_init_security`:

smack_inode_init_security
=========================

.. c:function:: int smack_inode_init_security(struct inode *inode, struct inode *dir, const struct qstr *qstr, const char **name, void **value, size_t *len)

    copy out the smack from an inode

    :param inode:
        the newly created inode
    :type inode: struct inode \*

    :param dir:
        containing directory object
    :type dir: struct inode \*

    :param qstr:
        unused
    :type qstr: const struct qstr \*

    :param name:
        where to put the attribute name
    :type name: const char \*\*

    :param value:
        where to put the attribute value
    :type value: void \*\*

    :param len:
        where to put the length of the attribute
    :type len: size_t \*

.. _`smack_inode_init_security.description`:

Description
-----------

Returns 0 if it all works out, -ENOMEM if there's no memory

.. _`smack_inode_link`:

smack_inode_link
================

.. c:function:: int smack_inode_link(struct dentry *old_dentry, struct inode *dir, struct dentry *new_dentry)

    Smack check on link

    :param old_dentry:
        the existing object
    :type old_dentry: struct dentry \*

    :param dir:
        unused
    :type dir: struct inode \*

    :param new_dentry:
        the new object
    :type new_dentry: struct dentry \*

.. _`smack_inode_link.description`:

Description
-----------

Returns 0 if access is permitted, an error code otherwise

.. _`smack_inode_unlink`:

smack_inode_unlink
==================

.. c:function:: int smack_inode_unlink(struct inode *dir, struct dentry *dentry)

    Smack check on inode deletion

    :param dir:
        containing directory object
    :type dir: struct inode \*

    :param dentry:
        file to unlink
    :type dentry: struct dentry \*

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

    :param dir:
        containing directory object
    :type dir: struct inode \*

    :param dentry:
        directory to unlink
    :type dentry: struct dentry \*

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

    :param old_inode:
        unused
    :type old_inode: struct inode \*

    :param old_dentry:
        the old object
    :type old_dentry: struct dentry \*

    :param new_inode:
        unused
    :type new_inode: struct inode \*

    :param new_dentry:
        the new object
    :type new_dentry: struct dentry \*

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

    :param inode:
        the inode in question
    :type inode: struct inode \*

    :param mask:
        the access requested
    :type mask: int

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

    :param dentry:
        the object
    :type dentry: struct dentry \*

    :param iattr:
        for the force flag
    :type iattr: struct iattr \*

.. _`smack_inode_setattr.description`:

Description
-----------

Returns 0 if access is permitted, an error code otherwise

.. _`smack_inode_getattr`:

smack_inode_getattr
===================

.. c:function:: int smack_inode_getattr(const struct path *path)

    Smack check for getting attributes

    :param path:
        *undescribed*
    :type path: const struct path \*

.. _`smack_inode_getattr.description`:

Description
-----------

Returns 0 if access is permitted, an error code otherwise

.. _`smack_inode_setxattr`:

smack_inode_setxattr
====================

.. c:function:: int smack_inode_setxattr(struct dentry *dentry, const char *name, const void *value, size_t size, int flags)

    Smack check for setting xattrs

    :param dentry:
        the object
    :type dentry: struct dentry \*

    :param name:
        name of the attribute
    :type name: const char \*

    :param value:
        value of the attribute
    :type value: const void \*

    :param size:
        size of the value
    :type size: size_t

    :param flags:
        unused
    :type flags: int

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

    :param dentry:
        object
    :type dentry: struct dentry \*

    :param name:
        attribute name
    :type name: const char \*

    :param value:
        attribute value
    :type value: const void \*

    :param size:
        attribute size
    :type size: size_t

    :param flags:
        unused
    :type flags: int

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

    :param dentry:
        the object
    :type dentry: struct dentry \*

    :param name:
        unused
    :type name: const char \*

.. _`smack_inode_getxattr.description`:

Description
-----------

Returns 0 if access is permitted, an error code otherwise

.. _`smack_inode_removexattr`:

smack_inode_removexattr
=======================

.. c:function:: int smack_inode_removexattr(struct dentry *dentry, const char *name)

    Smack check on removexattr

    :param dentry:
        the object
    :type dentry: struct dentry \*

    :param name:
        name of the attribute
    :type name: const char \*

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

    :param inode:
        the object
    :type inode: struct inode \*

    :param name:
        attribute name
    :type name: const char \*

    :param buffer:
        where to put the result
    :type buffer: void \*\*

    :param alloc:
        duplicate memory
    :type alloc: bool

.. _`smack_inode_getsecurity.description`:

Description
-----------

Returns the size of the attribute or an error code

.. _`smack_inode_listsecurity`:

smack_inode_listsecurity
========================

.. c:function:: int smack_inode_listsecurity(struct inode *inode, char *buffer, size_t buffer_size)

    list the Smack attributes

    :param inode:
        the object
    :type inode: struct inode \*

    :param buffer:
        where they go
    :type buffer: char \*

    :param buffer_size:
        size of buffer
    :type buffer_size: size_t

.. _`smack_inode_getsecid`:

smack_inode_getsecid
====================

.. c:function:: void smack_inode_getsecid(struct inode *inode, u32 *secid)

    Extract inode's security id

    :param inode:
        inode to extract the info from
    :type inode: struct inode \*

    :param secid:
        where result will be saved
    :type secid: u32 \*

.. _`smack_file_alloc_security`:

smack_file_alloc_security
=========================

.. c:function:: int smack_file_alloc_security(struct file *file)

    assign a file security blob

    :param file:
        the object
    :type file: struct file \*

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

    :param file:
        the object
    :type file: struct file \*

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

    :param file:
        the object
    :type file: struct file \*

    :param cmd:
        what to do
    :type cmd: unsigned int

    :param arg:
        unused
    :type arg: unsigned long

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

    :param file:
        the object
    :type file: struct file \*

    :param cmd:
        unused
    :type cmd: unsigned int

.. _`smack_file_lock.description`:

Description
-----------

Returns 0 if current has lock access, error code otherwise

.. _`smack_file_fcntl`:

smack_file_fcntl
================

.. c:function:: int smack_file_fcntl(struct file *file, unsigned int cmd, unsigned long arg)

    Smack check on fcntl

    :param file:
        the object
    :type file: struct file \*

    :param cmd:
        what action to check
    :type cmd: unsigned int

    :param arg:
        unused
    :type arg: unsigned long

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

    :param file:
        *undescribed*
    :type file: struct file \*

    :param reqprot:
        *undescribed*
    :type reqprot: unsigned long

    :param prot:
        *undescribed*
    :type prot: unsigned long

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`smack_file_set_fowner`:

smack_file_set_fowner
=====================

.. c:function:: void smack_file_set_fowner(struct file *file)

    set the file security blob value

    :param file:
        object in question
    :type file: struct file \*

.. _`smack_file_send_sigiotask`:

smack_file_send_sigiotask
=========================

.. c:function:: int smack_file_send_sigiotask(struct task_struct *tsk, struct fown_struct *fown, int signum)

    Smack on sigio

    :param tsk:
        The target task
    :type tsk: struct task_struct \*

    :param fown:
        the object the signal come from
    :type fown: struct fown_struct \*

    :param signum:
        unused
    :type signum: int

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

    :param file:
        the object
    :type file: struct file \*

.. _`smack_file_receive.description`:

Description
-----------

Returns 0 if current has access, error code otherwise

.. _`smack_file_open`:

smack_file_open
===============

.. c:function:: int smack_file_open(struct file *file)

    Smack dentry open processing

    :param file:
        the object
    :type file: struct file \*

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

    :param cred:
        *undescribed*
    :type cred: struct cred \*

    :param gfp:
        the atomicity of any memory allocations
    :type gfp: gfp_t

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

    :param cred:
        the credentials in question
    :type cred: struct cred \*

.. _`smack_cred_prepare`:

smack_cred_prepare
==================

.. c:function:: int smack_cred_prepare(struct cred *new, const struct cred *old, gfp_t gfp)

    prepare new set of credentials for modification

    :param new:
        the new credentials
    :type new: struct cred \*

    :param old:
        the original credentials
    :type old: const struct cred \*

    :param gfp:
        the atomicity of any memory allocations
    :type gfp: gfp_t

.. _`smack_cred_prepare.description`:

Description
-----------

Prepare a new set of credentials for modification.

.. _`smack_cred_transfer`:

smack_cred_transfer
===================

.. c:function:: void smack_cred_transfer(struct cred *new, const struct cred *old)

    Transfer the old credentials to the new credentials

    :param new:
        the new credentials
    :type new: struct cred \*

    :param old:
        the original credentials
    :type old: const struct cred \*

.. _`smack_cred_transfer.description`:

Description
-----------

Fill in a set of blank credentials from another set of credentials.

.. _`smack_cred_getsecid`:

smack_cred_getsecid
===================

.. c:function:: void smack_cred_getsecid(const struct cred *c, u32 *secid)

    get the secid corresponding to a creds structure

    :param c:
        the object creds
    :type c: const struct cred \*

    :param secid:
        where to put the result
    :type secid: u32 \*

.. _`smack_cred_getsecid.description`:

Description
-----------

Sets the secid to contain a u32 version of the smack label.

.. _`smack_kernel_act_as`:

smack_kernel_act_as
===================

.. c:function:: int smack_kernel_act_as(struct cred *new, u32 secid)

    Set the subjective context in a set of credentials

    :param new:
        points to the set of credentials to be modified.
    :type new: struct cred \*

    :param secid:
        specifies the security ID to be set
    :type secid: u32

.. _`smack_kernel_act_as.description`:

Description
-----------

Set the security data for a kernel service.

.. _`smack_kernel_create_files_as`:

smack_kernel_create_files_as
============================

.. c:function:: int smack_kernel_create_files_as(struct cred *new, struct inode *inode)

    Set the file creation label in a set of creds

    :param new:
        points to the set of credentials to be modified
    :type new: struct cred \*

    :param inode:
        points to the inode to use as a reference
    :type inode: struct inode \*

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

    :param p:
        the task object
    :type p: struct task_struct \*

    :param access:
        the access requested
    :type access: int

    :param caller:
        name of the calling function for audit
    :type caller: const char \*

.. _`smk_curacc_on_task.description`:

Description
-----------

Return 0 if access is permitted

.. _`smack_task_setpgid`:

smack_task_setpgid
==================

.. c:function:: int smack_task_setpgid(struct task_struct *p, pid_t pgid)

    Smack check on setting pgid

    :param p:
        the task object
    :type p: struct task_struct \*

    :param pgid:
        unused
    :type pgid: pid_t

.. _`smack_task_setpgid.description`:

Description
-----------

Return 0 if write access is permitted

.. _`smack_task_getpgid`:

smack_task_getpgid
==================

.. c:function:: int smack_task_getpgid(struct task_struct *p)

    Smack access check for getpgid

    :param p:
        the object task
    :type p: struct task_struct \*

.. _`smack_task_getpgid.description`:

Description
-----------

Returns 0 if current can read the object task, error code otherwise

.. _`smack_task_getsid`:

smack_task_getsid
=================

.. c:function:: int smack_task_getsid(struct task_struct *p)

    Smack access check for getsid

    :param p:
        the object task
    :type p: struct task_struct \*

.. _`smack_task_getsid.description`:

Description
-----------

Returns 0 if current can read the object task, error code otherwise

.. _`smack_task_getsecid`:

smack_task_getsecid
===================

.. c:function:: void smack_task_getsecid(struct task_struct *p, u32 *secid)

    get the secid of the task

    :param p:
        the object task
    :type p: struct task_struct \*

    :param secid:
        where to put the result
    :type secid: u32 \*

.. _`smack_task_getsecid.description`:

Description
-----------

Sets the secid to contain a u32 version of the smack label.

.. _`smack_task_setnice`:

smack_task_setnice
==================

.. c:function:: int smack_task_setnice(struct task_struct *p, int nice)

    Smack check on setting nice

    :param p:
        the task object
    :type p: struct task_struct \*

    :param nice:
        unused
    :type nice: int

.. _`smack_task_setnice.description`:

Description
-----------

Return 0 if write access is permitted

.. _`smack_task_setioprio`:

smack_task_setioprio
====================

.. c:function:: int smack_task_setioprio(struct task_struct *p, int ioprio)

    Smack check on setting ioprio

    :param p:
        the task object
    :type p: struct task_struct \*

    :param ioprio:
        unused
    :type ioprio: int

.. _`smack_task_setioprio.description`:

Description
-----------

Return 0 if write access is permitted

.. _`smack_task_getioprio`:

smack_task_getioprio
====================

.. c:function:: int smack_task_getioprio(struct task_struct *p)

    Smack check on reading ioprio

    :param p:
        the task object
    :type p: struct task_struct \*

.. _`smack_task_getioprio.description`:

Description
-----------

Return 0 if read access is permitted

.. _`smack_task_setscheduler`:

smack_task_setscheduler
=======================

.. c:function:: int smack_task_setscheduler(struct task_struct *p)

    Smack check on setting scheduler

    :param p:
        the task object
    :type p: struct task_struct \*

.. _`smack_task_setscheduler.description`:

Description
-----------

Return 0 if read access is permitted

.. _`smack_task_getscheduler`:

smack_task_getscheduler
=======================

.. c:function:: int smack_task_getscheduler(struct task_struct *p)

    Smack check on reading scheduler

    :param p:
        the task object
    :type p: struct task_struct \*

.. _`smack_task_getscheduler.description`:

Description
-----------

Return 0 if read access is permitted

.. _`smack_task_movememory`:

smack_task_movememory
=====================

.. c:function:: int smack_task_movememory(struct task_struct *p)

    Smack check on moving memory

    :param p:
        the task object
    :type p: struct task_struct \*

.. _`smack_task_movememory.description`:

Description
-----------

Return 0 if write access is permitted

.. _`smack_task_kill`:

smack_task_kill
===============

.. c:function:: int smack_task_kill(struct task_struct *p, struct kernel_siginfo *info, int sig, const struct cred *cred)

    Smack check on signal delivery

    :param p:
        the task object
    :type p: struct task_struct \*

    :param info:
        unused
    :type info: struct kernel_siginfo \*

    :param sig:
        unused
    :type sig: int

    :param cred:
        identifies the cred to use in lieu of current's
    :type cred: const struct cred \*

.. _`smack_task_kill.description`:

Description
-----------

Return 0 if write access is permitted

.. _`smack_task_to_inode`:

smack_task_to_inode
===================

.. c:function:: void smack_task_to_inode(struct task_struct *p, struct inode *inode)

    copy task smack into the inode blob

    :param p:
        task to copy from
    :type p: struct task_struct \*

    :param inode:
        inode to copy to
    :type inode: struct inode \*

.. _`smack_task_to_inode.description`:

Description
-----------

Sets the smack pointer in the inode security blob

.. _`smack_sk_alloc_security`:

smack_sk_alloc_security
=======================

.. c:function:: int smack_sk_alloc_security(struct sock *sk, int family, gfp_t gfp_flags)

    Allocate a socket blob

    :param sk:
        the socket
    :type sk: struct sock \*

    :param family:
        unused
    :type family: int

    :param gfp_flags:
        memory allocation flags
    :type gfp_flags: gfp_t

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

    :param sk:
        the socket
    :type sk: struct sock \*

.. _`smack_sk_free_security.description`:

Description
-----------

Clears the blob pointer

.. _`smack_ipv4host_label`:

smack_ipv4host_label
====================

.. c:function:: struct smack_known *smack_ipv4host_label(struct sockaddr_in *sip)

    check host based restrictions

    :param sip:
        the object end
    :type sip: struct sockaddr_in \*

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

    :param sip:
        the object end
    :type sip: struct sockaddr_in6 \*

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

    :param sk:
        the socket
    :type sk: struct sock \*

    :param labeled:
        socket label scheme
    :type labeled: int

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

    :param sk:
        the socket
    :type sk: struct sock \*

    :param sap:
        the destination address
    :type sap: struct sockaddr_in \*

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

    :param subject:
        subject Smack label
    :type subject: struct smack_known \*

    :param object:
        object Smack label
    :type object: struct smack_known \*

    :param address:
        address
    :type address: struct sockaddr_in6 \*

    :param act:
        the action being taken
    :type act: int

.. _`smk_ipv6_check.description`:

Description
-----------

Check an IPv6 access

.. _`smk_ipv6_port_label`:

smk_ipv6_port_label
===================

.. c:function:: void smk_ipv6_port_label(struct socket *sock, struct sockaddr *address)

    Smack port access table management

    :param sock:
        socket
    :type sock: struct socket \*

    :param address:
        address
    :type address: struct sockaddr \*

.. _`smk_ipv6_port_label.description`:

Description
-----------

Create or update the port list entry

.. _`smk_ipv6_port_check`:

smk_ipv6_port_check
===================

.. c:function:: int smk_ipv6_port_check(struct sock *sk, struct sockaddr_in6 *address, int act)

    check Smack port access

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param address:
        address
    :type address: struct sockaddr_in6 \*

    :param act:
        *undescribed*
    :type act: int

.. _`smk_ipv6_port_check.description`:

Description
-----------

Create or update the port list entry

.. _`smack_inode_setsecurity`:

smack_inode_setsecurity
=======================

.. c:function:: int smack_inode_setsecurity(struct inode *inode, const char *name, const void *value, size_t size, int flags)

    set smack xattrs

    :param inode:
        the object
    :type inode: struct inode \*

    :param name:
        attribute name
    :type name: const char \*

    :param value:
        attribute value
    :type value: const void \*

    :param size:
        size of the attribute
    :type size: size_t

    :param flags:
        unused
    :type flags: int

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

    :param sock:
        the socket
    :type sock: struct socket \*

    :param family:
        protocol family
    :type family: int

    :param type:
        unused
    :type type: int

    :param protocol:
        unused
    :type protocol: int

    :param kern:
        unused
    :type kern: int

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

    :param socka:
        one socket
    :type socka: struct socket \*

    :param sockb:
        another socket
    :type sockb: struct socket \*

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

    :param sock:
        the socket
    :type sock: struct socket \*

    :param address:
        the port address
    :type address: struct sockaddr \*

    :param addrlen:
        size of the address
    :type addrlen: int

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

    :param sock:
        the socket
    :type sock: struct socket \*

    :param sap:
        the other end
    :type sap: struct sockaddr \*

    :param addrlen:
        size of sap
    :type addrlen: int

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

    :param flags:
        the S\_ value
    :type flags: int

.. _`smack_flags_to_may.description`:

Description
-----------

Returns the equivalent MAY\_ value

.. _`smack_msg_msg_alloc_security`:

smack_msg_msg_alloc_security
============================

.. c:function:: int smack_msg_msg_alloc_security(struct msg_msg *msg)

    Set the security blob for msg_msg

    :param msg:
        the object
    :type msg: struct msg_msg \*

.. _`smack_msg_msg_alloc_security.description`:

Description
-----------

Returns 0

.. _`smack_msg_msg_free_security`:

smack_msg_msg_free_security
===========================

.. c:function:: void smack_msg_msg_free_security(struct msg_msg *msg)

    Clear the security blob for msg_msg

    :param msg:
        the object
    :type msg: struct msg_msg \*

.. _`smack_msg_msg_free_security.description`:

Description
-----------

Clears the blob pointer

.. _`smack_of_ipc`:

smack_of_ipc
============

.. c:function:: struct smack_known *smack_of_ipc(struct kern_ipc_perm *isp)

    the smack pointer for the ipc

    :param isp:
        the object
    :type isp: struct kern_ipc_perm \*

.. _`smack_of_ipc.description`:

Description
-----------

Returns a pointer to the smack value

.. _`smack_ipc_alloc_security`:

smack_ipc_alloc_security
========================

.. c:function:: int smack_ipc_alloc_security(struct kern_ipc_perm *isp)

    Set the security blob for ipc

    :param isp:
        the object
    :type isp: struct kern_ipc_perm \*

.. _`smack_ipc_alloc_security.description`:

Description
-----------

Returns 0

.. _`smack_ipc_free_security`:

smack_ipc_free_security
=======================

.. c:function:: void smack_ipc_free_security(struct kern_ipc_perm *isp)

    Clear the security blob for ipc

    :param isp:
        the object
    :type isp: struct kern_ipc_perm \*

.. _`smack_ipc_free_security.description`:

Description
-----------

Clears the blob pointer

.. _`smk_curacc_shm`:

smk_curacc_shm
==============

.. c:function:: int smk_curacc_shm(struct kern_ipc_perm *isp, int access)

    check if current has access on shm

    :param isp:
        the object
    :type isp: struct kern_ipc_perm \*

    :param access:
        access requested
    :type access: int

.. _`smk_curacc_shm.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_shm_associate`:

smack_shm_associate
===================

.. c:function:: int smack_shm_associate(struct kern_ipc_perm *isp, int shmflg)

    Smack access check for shm

    :param isp:
        the object
    :type isp: struct kern_ipc_perm \*

    :param shmflg:
        access requested
    :type shmflg: int

.. _`smack_shm_associate.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_shm_shmctl`:

smack_shm_shmctl
================

.. c:function:: int smack_shm_shmctl(struct kern_ipc_perm *isp, int cmd)

    Smack access check for shm

    :param isp:
        the object
    :type isp: struct kern_ipc_perm \*

    :param cmd:
        what it wants to do
    :type cmd: int

.. _`smack_shm_shmctl.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_shm_shmat`:

smack_shm_shmat
===============

.. c:function:: int smack_shm_shmat(struct kern_ipc_perm *ipc, char __user *shmaddr, int shmflg)

    Smack access for shmat

    :param ipc:
        *undescribed*
    :type ipc: struct kern_ipc_perm \*

    :param shmaddr:
        unused
    :type shmaddr: char __user \*

    :param shmflg:
        access requested
    :type shmflg: int

.. _`smack_shm_shmat.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smk_curacc_sem`:

smk_curacc_sem
==============

.. c:function:: int smk_curacc_sem(struct kern_ipc_perm *isp, int access)

    check if current has access on sem

    :param isp:
        the object
    :type isp: struct kern_ipc_perm \*

    :param access:
        access requested
    :type access: int

.. _`smk_curacc_sem.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_sem_associate`:

smack_sem_associate
===================

.. c:function:: int smack_sem_associate(struct kern_ipc_perm *isp, int semflg)

    Smack access check for sem

    :param isp:
        the object
    :type isp: struct kern_ipc_perm \*

    :param semflg:
        access requested
    :type semflg: int

.. _`smack_sem_associate.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_sem_semctl`:

smack_sem_semctl
================

.. c:function:: int smack_sem_semctl(struct kern_ipc_perm *isp, int cmd)

    Smack access check for sem

    :param isp:
        the object
    :type isp: struct kern_ipc_perm \*

    :param cmd:
        what it wants to do
    :type cmd: int

.. _`smack_sem_semctl.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_sem_semop`:

smack_sem_semop
===============

.. c:function:: int smack_sem_semop(struct kern_ipc_perm *isp, struct sembuf *sops, unsigned nsops, int alter)

    Smack checks of semaphore operations

    :param isp:
        the object
    :type isp: struct kern_ipc_perm \*

    :param sops:
        unused
    :type sops: struct sembuf \*

    :param nsops:
        unused
    :type nsops: unsigned

    :param alter:
        unused
    :type alter: int

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

    :param isp:
        the msq
    :type isp: struct kern_ipc_perm \*

    :param access:
        access requested
    :type access: int

.. _`smk_curacc_msq.description`:

Description
-----------

return 0 if current has access, error otherwise

.. _`smack_msg_queue_associate`:

smack_msg_queue_associate
=========================

.. c:function:: int smack_msg_queue_associate(struct kern_ipc_perm *isp, int msqflg)

    Smack access check for msg_queue

    :param isp:
        the object
    :type isp: struct kern_ipc_perm \*

    :param msqflg:
        access requested
    :type msqflg: int

.. _`smack_msg_queue_associate.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_msg_queue_msgctl`:

smack_msg_queue_msgctl
======================

.. c:function:: int smack_msg_queue_msgctl(struct kern_ipc_perm *isp, int cmd)

    Smack access check for msg_queue

    :param isp:
        the object
    :type isp: struct kern_ipc_perm \*

    :param cmd:
        what it wants to do
    :type cmd: int

.. _`smack_msg_queue_msgctl.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_msg_queue_msgsnd`:

smack_msg_queue_msgsnd
======================

.. c:function:: int smack_msg_queue_msgsnd(struct kern_ipc_perm *isp, struct msg_msg *msg, int msqflg)

    Smack access check for msg_queue

    :param isp:
        the object
    :type isp: struct kern_ipc_perm \*

    :param msg:
        unused
    :type msg: struct msg_msg \*

    :param msqflg:
        access requested
    :type msqflg: int

.. _`smack_msg_queue_msgsnd.description`:

Description
-----------

Returns 0 if current has the requested access, error code otherwise

.. _`smack_msg_queue_msgrcv`:

smack_msg_queue_msgrcv
======================

.. c:function:: int smack_msg_queue_msgrcv(struct kern_ipc_perm *isp, struct msg_msg *msg, struct task_struct *target, long type, int mode)

    Smack access check for msg_queue

    :param isp:
        the object
    :type isp: struct kern_ipc_perm \*

    :param msg:
        unused
    :type msg: struct msg_msg \*

    :param target:
        unused
    :type target: struct task_struct \*

    :param type:
        unused
    :type type: long

    :param mode:
        unused
    :type mode: int

.. _`smack_msg_queue_msgrcv.description`:

Description
-----------

Returns 0 if current has read and write access, error code otherwise

.. _`smack_ipc_permission`:

smack_ipc_permission
====================

.. c:function:: int smack_ipc_permission(struct kern_ipc_perm *ipp, short flag)

    Smack access for \ :c:func:`ipc_permission`\ 

    :param ipp:
        the object permissions
    :type ipp: struct kern_ipc_perm \*

    :param flag:
        access requested
    :type flag: short

.. _`smack_ipc_permission.description`:

Description
-----------

Returns 0 if current has read and write access, error code otherwise

.. _`smack_ipc_getsecid`:

smack_ipc_getsecid
==================

.. c:function:: void smack_ipc_getsecid(struct kern_ipc_perm *ipp, u32 *secid)

    Extract smack security id

    :param ipp:
        the object permissions
    :type ipp: struct kern_ipc_perm \*

    :param secid:
        where result will be saved
    :type secid: u32 \*

.. _`smack_d_instantiate`:

smack_d_instantiate
===================

.. c:function:: void smack_d_instantiate(struct dentry *opt_dentry, struct inode *inode)

    Make sure the blob is correct on an inode

    :param opt_dentry:
        dentry where inode will be attached
    :type opt_dentry: struct dentry \*

    :param inode:
        the object
    :type inode: struct inode \*

.. _`smack_d_instantiate.description`:

Description
-----------

Set the inode's security blob if it hasn't been done already.

.. _`smack_getprocattr`:

smack_getprocattr
=================

.. c:function:: int smack_getprocattr(struct task_struct *p, char *name, char **value)

    Smack process attribute access

    :param p:
        the object task
    :type p: struct task_struct \*

    :param name:
        the name of the attribute in /proc/.../attr
    :type name: char \*

    :param value:
        where to put the result
    :type value: char \*\*

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

    :param name:
        the name of the attribute in /proc/.../attr
    :type name: const char \*

    :param value:
        the value to set
    :type value: void \*

    :param size:
        the size of the value
    :type size: size_t

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

    :param sock:
        one sock
    :type sock: struct sock \*

    :param other:
        the other sock
    :type other: struct sock \*

    :param newsk:
        unused
    :type newsk: struct sock \*

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

    :param sock:
        one socket
    :type sock: struct socket \*

    :param other:
        the other socket
    :type other: struct socket \*

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

    :param sock:
        the socket
    :type sock: struct socket \*

    :param msg:
        the message
    :type msg: struct msghdr \*

    :param size:
        the size of the message
    :type size: int

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

    :param sap:
        netlabel secattr
    :type sap: struct netlbl_lsm_secattr \*

    :param ssp:
        socket security information
    :type ssp: struct socket_smack \*

.. _`smack_from_secattr.description`:

Description
-----------

Returns a pointer to a Smack label entry found on the label list.

.. _`smack_socket_sock_rcv_skb`:

smack_socket_sock_rcv_skb
=========================

.. c:function:: int smack_socket_sock_rcv_skb(struct sock *sk, struct sk_buff *skb)

    Smack packet delivery access check

    :param sk:
        socket
    :type sk: struct sock \*

    :param skb:
        packet
    :type skb: struct sk_buff \*

.. _`smack_socket_sock_rcv_skb.description`:

Description
-----------

Returns 0 if the packet should be delivered, an error code otherwise

.. _`smack_socket_getpeersec_stream`:

smack_socket_getpeersec_stream
==============================

.. c:function:: int smack_socket_getpeersec_stream(struct socket *sock, char __user *optval, int __user *optlen, unsigned len)

    pull in packet label

    :param sock:
        the socket
    :type sock: struct socket \*

    :param optval:
        user's destination
    :type optval: char __user \*

    :param optlen:
        size thereof
    :type optlen: int __user \*

    :param len:
        max thereof
    :type len: unsigned

.. _`smack_socket_getpeersec_stream.description`:

Description
-----------

returns zero on success, an error code otherwise

.. _`smack_socket_getpeersec_dgram`:

smack_socket_getpeersec_dgram
=============================

.. c:function:: int smack_socket_getpeersec_dgram(struct socket *sock, struct sk_buff *skb, u32 *secid)

    pull in packet label

    :param sock:
        the peer socket
    :type sock: struct socket \*

    :param skb:
        packet data
    :type skb: struct sk_buff \*

    :param secid:
        pointer to where to put the secid of the packet
    :type secid: u32 \*

.. _`smack_socket_getpeersec_dgram.description`:

Description
-----------

Sets the netlabel socket state on sk from parent

.. _`smack_sock_graft`:

smack_sock_graft
================

.. c:function:: void smack_sock_graft(struct sock *sk, struct socket *parent)

    Initialize a newly created socket with an existing sock

    :param sk:
        child sock
    :type sk: struct sock \*

    :param parent:
        parent socket
    :type parent: struct socket \*

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

    :param sk:
        socket involved
    :type sk: struct sock \*

    :param skb:
        packet
    :type skb: struct sk_buff \*

    :param req:
        unused
    :type req: struct request_sock \*

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

    :param sk:
        the new socket
    :type sk: struct sock \*

    :param req:
        the connection's request_sock
    :type req: const struct request_sock \*

.. _`smack_inet_csk_clone.description`:

Description
-----------

Transfer the connection's peer label to the newly created socket.

.. _`smack_key_alloc`:

smack_key_alloc
===============

.. c:function:: int smack_key_alloc(struct key *key, const struct cred *cred, unsigned long flags)

    Set the key security blob

    :param key:
        object
    :type key: struct key \*

    :param cred:
        the credentials to use
    :type cred: const struct cred \*

    :param flags:
        unused
    :type flags: unsigned long

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

    :param key:
        the object
    :type key: struct key \*

.. _`smack_key_free.description`:

Description
-----------

Clear the blob pointer

.. _`smack_key_permission`:

smack_key_permission
====================

.. c:function:: int smack_key_permission(key_ref_t key_ref, const struct cred *cred, unsigned perm)

    Smack access on a key

    :param key_ref:
        gets to the object
    :type key_ref: key_ref_t

    :param cred:
        the credentials to use
    :type cred: const struct cred \*

    :param perm:
        requested key permissions
    :type perm: unsigned

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

    :param field:
        audit rule fields given from user-space (audit.h)
    :type field: u32

    :param op:
        required testing operator (=, !=, >, <, ...)
    :type op: u32

    :param rulestr:
        smack label to be audited
    :type rulestr: char \*

    :param vrule:
        pointer to save our own audit rule representation
    :type vrule: void \*\*

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

    :param krule:
        rule of interest, in Audit kernel representation format
    :type krule: struct audit_krule \*

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

    :param secid:
        security id for identifying the object to test
    :type secid: u32

    :param field:
        audit rule flags given from user-space
    :type field: u32

    :param op:
        required testing operator
    :type op: u32

    :param vrule:
        smack internal rule presentation
    :type vrule: void \*

    :param actx:
        audit context associated with the check
    :type actx: struct audit_context \*

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

    :param name:
        Full xattr name to check.
    :type name: const char \*

.. _`smack_secid_to_secctx`:

smack_secid_to_secctx
=====================

.. c:function:: int smack_secid_to_secctx(u32 secid, char **secdata, u32 *seclen)

    return the smack label for a secid

    :param secid:
        incoming integer
    :type secid: u32

    :param secdata:
        destination
    :type secdata: char \*\*

    :param seclen:
        how long it is
    :type seclen: u32 \*

.. _`smack_secid_to_secctx.description`:

Description
-----------

Exists for networking code.

.. _`smack_secctx_to_secid`:

smack_secctx_to_secid
=====================

.. c:function:: int smack_secctx_to_secid(const char *secdata, u32 seclen, u32 *secid)

    return the secid for a smack label

    :param secdata:
        smack label
    :type secdata: const char \*

    :param seclen:
        how long result is
    :type seclen: u32

    :param secid:
        outgoing integer
    :type secid: u32 \*

.. _`smack_secctx_to_secid.description`:

Description
-----------

Exists for audit and networking code.

.. _`smack_init`:

smack_init
==========

.. c:function:: int smack_init( void)

    initialize the smack system

    :param void:
        no arguments
    :type void: 

.. _`smack_init.description`:

Description
-----------

Returns 0

.. This file was automatic generated / don't edit.

