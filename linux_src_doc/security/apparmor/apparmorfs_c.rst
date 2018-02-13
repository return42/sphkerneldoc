.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/apparmorfs.c

.. _`mangle_name`:

mangle_name
===========

.. c:function:: int mangle_name(const char *name, char *target)

    mangle a profile name to std profile layout form

    :param const char \*name:
        profile name to mangle  (NOT NULL)

    :param char \*target:
        buffer to store mangled name, same length as \ ``name``\  (MAYBE NULL)

.. _`mangle_name.return`:

Return
------

length of mangled name

.. _`__aafs_setup_d_inode`:

\__aafs_setup_d_inode
=====================

.. c:function:: int __aafs_setup_d_inode(struct inode *dir, struct dentry *dentry, umode_t mode, void *data, char *link, const struct file_operations *fops, const struct inode_operations *iops)

    basic inode setup for apparmorfs

    :param struct inode \*dir:
        parent directory for the dentry

    :param struct dentry \*dentry:
        dentry we are seting the inode up for

    :param umode_t mode:
        permissions the file should have

    :param void \*data:
        data to store on inode.i_private, available in \ :c:func:`open`\ 

    :param char \*link:
        if symlink, symlink target string

    :param const struct file_operations \*fops:
        struct file_operations that should be used

    :param const struct inode_operations \*iops:
        struct of inode_operations that should be used

.. _`aafs_create`:

aafs_create
===========

.. c:function:: struct dentry *aafs_create(const char *name, umode_t mode, struct dentry *parent, void *data, void *link, const struct file_operations *fops, const struct inode_operations *iops)

    create a dentry in the apparmorfs filesystem

    :param const char \*name:
        name of dentry to create

    :param umode_t mode:
        permissions the file should have

    :param struct dentry \*parent:
        parent directory for this dentry

    :param void \*data:
        data to store on inode.i_private, available in \ :c:func:`open`\ 

    :param void \*link:
        if symlink, symlink target string

    :param const struct file_operations \*fops:
        struct file_operations that should be used for

    :param const struct inode_operations \*iops:
        struct of inode_operations that should be used

.. _`aafs_create.description`:

Description
-----------

This is the basic "create a xxx" function for apparmorfs.

Returns a pointer to a dentry if it succeeds, that must be free with
\ :c:func:`aafs_remove`\ . Will return ERR_PTR on failure.

.. _`aafs_create_file`:

aafs_create_file
================

.. c:function:: struct dentry *aafs_create_file(const char *name, umode_t mode, struct dentry *parent, void *data, const struct file_operations *fops)

    create a file in the apparmorfs filesystem

    :param const char \*name:
        name of dentry to create

    :param umode_t mode:
        permissions the file should have

    :param struct dentry \*parent:
        parent directory for this dentry

    :param void \*data:
        data to store on inode.i_private, available in \ :c:func:`open`\ 

    :param const struct file_operations \*fops:
        struct file_operations that should be used for

.. _`aafs_create_file.description`:

Description
-----------

see aafs_create

.. _`aafs_create_dir`:

aafs_create_dir
===============

.. c:function:: struct dentry *aafs_create_dir(const char *name, struct dentry *parent)

    create a directory in the apparmorfs filesystem

    :param const char \*name:
        name of dentry to create

    :param struct dentry \*parent:
        parent directory for this dentry

.. _`aafs_create_dir.description`:

Description
-----------

see aafs_create

.. _`aafs_create_symlink`:

aafs_create_symlink
===================

.. c:function:: struct dentry *aafs_create_symlink(const char *name, struct dentry *parent, const char *target, const struct inode_operations *iops)

    create a symlink in the apparmorfs filesystem

    :param const char \*name:
        name of dentry to create

    :param struct dentry \*parent:
        parent directory for this dentry

    :param const char \*target:
        if symlink, symlink target string

    :param const struct inode_operations \*iops:
        struct of inode_operations that should be used

.. _`aafs_create_symlink.description`:

Description
-----------

If \ ``target``\  parameter is \ ``NULL``\ , then the \ ``iops``\  parameter needs to be
setup to handle .readlink and .get_link inode_operations.

.. _`aafs_remove`:

aafs_remove
===========

.. c:function:: void aafs_remove(struct dentry *dentry)

    removes a file or directory from the apparmorfs filesystem

    :param struct dentry \*dentry:
        dentry of the file/directory/symlink to removed.

.. _`aa_simple_write_to_buffer`:

aa_simple_write_to_buffer
=========================

.. c:function:: struct aa_loaddata *aa_simple_write_to_buffer(const char __user *userbuf, size_t alloc_size, size_t copy_size, loff_t *pos)

    common routine for getting policy from user

    :param const char __user \*userbuf:
        user buffer to copy data from  (NOT NULL)

    :param size_t alloc_size:
        size of user buffer (REQUIRES: \ ``alloc_size``\  >= \ ``copy_size``\ )

    :param size_t copy_size:
        size of data to copy from user buffer

    :param loff_t \*pos:
        position write is at in the file (NOT NULL)

.. _`aa_simple_write_to_buffer.return`:

Return
------

kernel buffer containing copy of user buffer data or an
ERR_PTR on failure.

.. _`query_data`:

query_data
==========

.. c:function:: ssize_t query_data(char *buf, size_t buf_len, char *query, size_t query_len)

    queries a policy and writes its data to buf

    :param char \*buf:
        the resulting data is stored here (NOT NULL)

    :param size_t buf_len:
        size of buf

    :param char \*query:
        query string used to retrieve data

    :param size_t query_len:
        size of query including second NUL byte

.. _`query_data.description`:

Description
-----------

The buffers pointed to by buf and query may overlap. The query buffer is
parsed before buf is written to.

The query should look like "<LABEL>\0<KEY>\0", where <LABEL> is the name of
the security confinement context and <KEY> is the name of the data to
retrieve. <LABEL> and <KEY> must not be NUL-terminated.

Don't expect the contents of buf to be preserved on failure.

.. _`query_data.return`:

Return
------

number of characters written to buf or -errno on failure

.. _`query_label`:

query_label
===========

.. c:function:: ssize_t query_label(char *buf, size_t buf_len, char *query, size_t query_len, bool view_only)

    queries a label and writes permissions to buf

    :param char \*buf:
        the resulting permissions string is stored here (NOT NULL)

    :param size_t buf_len:
        size of buf

    :param char \*query:
        binary query string to match against the dfa

    :param size_t query_len:
        size of query

    :param bool view_only:
        only compute for querier's view

.. _`query_label.description`:

Description
-----------

The buffers pointed to by buf and query may overlap. The query buffer is
parsed before buf is written to.

The query should look like "LABEL_NAME\0DFA_STRING" where LABEL_NAME is
the name of the label, in the current namespace, that is to be queried and
DFA_STRING is a binary string to match against the label(s)'s DFA.

LABEL_NAME must be NUL terminated. DFA_STRING may contain NUL characters
but must \*not\* be NUL terminated.

.. _`query_label.return`:

Return
------

number of characters written to buf or -errno on failure

.. _`aa_write_access`:

aa_write_access
===============

.. c:function:: ssize_t aa_write_access(struct file *file, const char __user *ubuf, size_t count, loff_t *ppos)

    generic permissions and data query

    :param struct file \*file:
        pointer to open apparmorfs/access file

    :param const char __user \*ubuf:
        user buffer containing the complete query string (NOT NULL)

    :param size_t count:
        size of ubuf

    :param loff_t \*ppos:
        position in the file (MUST BE ZERO)

.. _`aa_write_access.description`:

Description
-----------

Allows for one permissions or data query per \ :c:func:`open`\ , \ :c:func:`write`\ , and \ :c:func:`read`\ 
sequence. The only queries currently supported are label-based queries for
permissions or data.

For permissions queries, ubuf must begin with "label\0", followed by the
profile query specific format described in the \ :c:func:`query_label`\  function
documentation.

For data queries, ubuf must have the form "data\0<LABEL>\0<KEY>\0", where
<LABEL> is the name of the security confinement context and <KEY> is the
name of the data to retrieve.

.. _`aa_write_access.return`:

Return
------

number of bytes written or -errno on failure

.. _`__next_ns`:

\__next_ns
==========

.. c:function:: struct aa_ns *__next_ns(struct aa_ns *root, struct aa_ns *ns)

    find the next namespace to list

    :param struct aa_ns \*root:
        root namespace to stop search at (NOT NULL)

    :param struct aa_ns \*ns:
        current ns position (NOT NULL)

.. _`__next_ns.description`:

Description
-----------

Find the next namespace from \ ``ns``\  under \ ``root``\  and handle all locking needed
while switching current namespace.

.. _`__next_ns.return`:

Return
------

next namespace or NULL if at last namespace under \ ``root``\ 

.. _`__next_ns.requires`:

Requires
--------

ns->parent->lock to be held

.. _`__next_ns.note`:

NOTE
----

will not unlock root->lock

.. _`__first_profile`:

\__first_profile
================

.. c:function:: struct aa_profile *__first_profile(struct aa_ns *root, struct aa_ns *ns)

    find the first profile in a namespace

    :param struct aa_ns \*root:
        namespace that is root of profiles being displayed (NOT NULL)

    :param struct aa_ns \*ns:
        namespace to start in   (NOT NULL)

.. _`__first_profile.return`:

Return
------

unrefcounted profile or NULL if no profile

.. _`__first_profile.requires`:

Requires
--------

profile->ns.lock to be held

.. _`__next_profile`:

\__next_profile
===============

.. c:function:: struct aa_profile *__next_profile(struct aa_profile *p)

    step to the next profile in a profile tree

    :param struct aa_profile \*p:
        *undescribed*

.. _`__next_profile.description`:

Description
-----------

Perform a depth first traversal on the profile tree in a namespace

.. _`__next_profile.return`:

Return
------

next profile or NULL if done

.. _`__next_profile.requires`:

Requires
--------

profile->ns.lock to be held

.. _`next_profile`:

next_profile
============

.. c:function:: struct aa_profile *next_profile(struct aa_ns *root, struct aa_profile *profile)

    step to the next profile in where ever it may be

    :param struct aa_ns \*root:
        root namespace  (NOT NULL)

    :param struct aa_profile \*profile:
        current profile  (NOT NULL)

.. _`next_profile.return`:

Return
------

next profile or NULL if there isn't one

.. _`p_start`:

p_start
=======

.. c:function:: void *p_start(struct seq_file *f, loff_t *pos)

    start a depth first traversal of profile tree

    :param struct seq_file \*f:
        seq_file to fill

    :param loff_t \*pos:
        current position

.. _`p_start.return`:

Return
------

first profile under current namespace or NULL if none found

acquires first ns->lock

.. _`p_next`:

p_next
======

.. c:function:: void *p_next(struct seq_file *f, void *p, loff_t *pos)

    read the next profile entry

    :param struct seq_file \*f:
        seq_file to fill

    :param void \*p:
        profile previously returned

    :param loff_t \*pos:
        current position

.. _`p_next.return`:

Return
------

next profile after \ ``p``\  or NULL if none

may acquire/release locks in namespace tree as necessary

.. _`p_stop`:

p_stop
======

.. c:function:: void p_stop(struct seq_file *f, void *p)

    stop depth first traversal

    :param struct seq_file \*f:
        seq_file we are filling

    :param void \*p:
        the last profile writen

.. _`p_stop.description`:

Description
-----------

Release all locking done by p_start/p_next on namespace tree

.. _`seq_show_profile`:

seq_show_profile
================

.. c:function:: int seq_show_profile(struct seq_file *f, void *p)

    show a profile entry

    :param struct seq_file \*f:
        seq_file to file

    :param void \*p:
        current position (profile)    (NOT NULL)

.. _`seq_show_profile.return`:

Return
------

error on failure

.. _`entry_create_file`:

entry_create_file
=================

.. c:function:: int entry_create_file(struct aa_sfs_entry *fs_file, struct dentry *parent)

    create a file entry in the apparmor securityfs

    :param struct aa_sfs_entry \*fs_file:
        aa_sfs_entry to build an entry for (NOT NULL)

    :param struct dentry \*parent:
        the parent dentry in the securityfs

.. _`entry_create_file.description`:

Description
-----------

Use entry_remove_file to remove entries created with this fn.

.. _`entry_create_dir`:

entry_create_dir
================

.. c:function:: int entry_create_dir(struct aa_sfs_entry *fs_dir, struct dentry *parent)

    recursively create a directory entry in the securityfs

    :param struct aa_sfs_entry \*fs_dir:
        aa_sfs_entry (and all child entries) to build (NOT NULL)

    :param struct dentry \*parent:
        the parent dentry in the securityfs

.. _`entry_create_dir.description`:

Description
-----------

Use entry_remove_dir to remove entries created with this fn.

.. _`entry_remove_file`:

entry_remove_file
=================

.. c:function:: void entry_remove_file(struct aa_sfs_entry *fs_file)

    drop a single file entry in the apparmor securityfs

    :param struct aa_sfs_entry \*fs_file:
        aa_sfs_entry to detach from the securityfs (NOT NULL)

.. _`entry_remove_dir`:

entry_remove_dir
================

.. c:function:: void entry_remove_dir(struct aa_sfs_entry *fs_dir)

    recursively drop a directory entry from the securityfs

    :param struct aa_sfs_entry \*fs_dir:
        aa_sfs_entry (and all child entries) to detach (NOT NULL)

.. _`aa_destroy_aafs`:

aa_destroy_aafs
===============

.. c:function:: void aa_destroy_aafs( void)

    cleanup and free aafs

    :param  void:
        no arguments

.. _`aa_destroy_aafs.description`:

Description
-----------

releases dentries allocated by aa_create_aafs

.. _`aa_create_aafs`:

aa_create_aafs
==============

.. c:function:: int aa_create_aafs( void)

    create the apparmor security filesystem

    :param  void:
        no arguments

.. _`aa_create_aafs.description`:

Description
-----------

dentries created here are released by aa_destroy_aafs

.. _`aa_create_aafs.return`:

Return
------

error on failure

.. This file was automatic generated / don't edit.

