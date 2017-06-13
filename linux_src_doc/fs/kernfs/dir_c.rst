.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/kernfs/dir.c

.. _`kernfs_path_from_node_locked`:

kernfs_path_from_node_locked
============================

.. c:function:: int kernfs_path_from_node_locked(struct kernfs_node *kn_to, struct kernfs_node *kn_from, char *buf, size_t buflen)

    find a pseudo-absolute path to \ ``kn_to``\ , where kn_from is treated as root of the path.

    :param struct kernfs_node \*kn_to:
        kernfs node to which path is needed

    :param struct kernfs_node \*kn_from:
        kernfs node which should be treated as root for the path

    :param char \*buf:
        buffer to copy the path into

    :param size_t buflen:
        size of \ ``buf``\ 

.. _`kernfs_path_from_node_locked.we-need-to-handle-couple-of-scenarios-here`:

We need to handle couple of scenarios here
------------------------------------------

[1] when \ ``kn_from``\  is an ancestor of \ ``kn_to``\  at some level

.. _`kernfs_path_from_node_locked.kn_from`:

kn_from
-------

/n1/n2/n3

/n1/n2/n3/n4

/n1/n2/n3/n4/n5   [depth=5]

.. _`kernfs_path_from_node_locked.kn_to`:

kn_to
-----

/n1/n2/n3/n4/n5

/n1/n2/n5

/n1/n2/n3         [depth=3]

.. _`kernfs_path_from_node_locked.result`:

result
------

/n4/n5

[2] when \ ``kn_from``\  is on a different hierarchy and we need to find common
ancestor between \ ``kn_from``\  and \ ``kn_to``\ .

/../../n5
OR

/../..

[3] when \ ``kn_to``\  is NULL result will be "(null)"

Returns the length of the full path.  If the full length is equal to or
greater than \ ``buflen``\ , \ ``buf``\  contains the truncated path with the trailing
'\0'.  On error, -errno is returned.

.. _`kernfs_name`:

kernfs_name
===========

.. c:function:: int kernfs_name(struct kernfs_node *kn, char *buf, size_t buflen)

    obtain the name of a given node

    :param struct kernfs_node \*kn:
        kernfs_node of interest

    :param char \*buf:
        buffer to copy \ ``kn``\ 's name into

    :param size_t buflen:
        size of \ ``buf``\ 

.. _`kernfs_name.description`:

Description
-----------

Copies the name of \ ``kn``\  into \ ``buf``\  of \ ``buflen``\  bytes.  The behavior is
similar to \ :c:func:`strlcpy`\ .  It returns the length of \ ``kn``\ 's name and if \ ``buf``\ 
isn't long enough, it's filled upto \ ``buflen``\ -1 and nul terminated.

Fills buffer with "(null)" if \ ``kn``\  is NULL.

This function can be called from any context.

.. _`kernfs_path_from_node`:

kernfs_path_from_node
=====================

.. c:function:: int kernfs_path_from_node(struct kernfs_node *to, struct kernfs_node *from, char *buf, size_t buflen)

    build path of node \ ``to``\  relative to \ ``from``\ .

    :param struct kernfs_node \*to:
        kernfs_node of interest

    :param struct kernfs_node \*from:
        parent kernfs_node relative to which we need to build the path

    :param char \*buf:
        buffer to copy \ ``to``\ 's path into

    :param size_t buflen:
        size of \ ``buf``\ 

.. _`kernfs_path_from_node.description`:

Description
-----------

Builds \ ``to``\ 's path relative to \ ``from``\  in \ ``buf``\ . \ ``from``\  and \ ``to``\  must
be on the same kernfs-root. If \ ``from``\  is not parent of \ ``to``\ , then a relative
path (which includes '..'s) as needed to reach from \ ``from``\  to \ ``to``\  is
returned.

Returns the length of the full path.  If the full length is equal to or
greater than \ ``buflen``\ , \ ``buf``\  contains the truncated path with the trailing
'\0'.  On error, -errno is returned.

.. _`pr_cont_kernfs_name`:

pr_cont_kernfs_name
===================

.. c:function:: void pr_cont_kernfs_name(struct kernfs_node *kn)

    pr_cont name of a kernfs_node

    :param struct kernfs_node \*kn:
        kernfs_node of interest

.. _`pr_cont_kernfs_name.description`:

Description
-----------

This function can be called from any context.

.. _`pr_cont_kernfs_path`:

pr_cont_kernfs_path
===================

.. c:function:: void pr_cont_kernfs_path(struct kernfs_node *kn)

    pr_cont path of a kernfs_node

    :param struct kernfs_node \*kn:
        kernfs_node of interest

.. _`pr_cont_kernfs_path.description`:

Description
-----------

This function can be called from any context.

.. _`kernfs_get_parent`:

kernfs_get_parent
=================

.. c:function:: struct kernfs_node *kernfs_get_parent(struct kernfs_node *kn)

    determine the parent node and pin it

    :param struct kernfs_node \*kn:
        kernfs_node of interest

.. _`kernfs_get_parent.description`:

Description
-----------

Determines \ ``kn``\ 's parent, pins and returns it.  This function can be
called from any context.

.. _`kernfs_name_hash`:

kernfs_name_hash
================

.. c:function:: unsigned int kernfs_name_hash(const char *name, const void *ns)

    :param const char \*name:
        Null terminated string to hash

    :param const void \*ns:
        Namespace tag to hash

.. _`kernfs_name_hash.description`:

Description
-----------

Returns 31 bit hash of ns + name (so it fits in an off_t )

.. _`kernfs_link_sibling`:

kernfs_link_sibling
===================

.. c:function:: int kernfs_link_sibling(struct kernfs_node *kn)

    link kernfs_node into sibling rbtree

    :param struct kernfs_node \*kn:
        kernfs_node of interest

.. _`kernfs_link_sibling.description`:

Description
-----------

Link \ ``kn``\  into its sibling rbtree which starts from
\ ``kn``\ ->parent->dir.children.

.. _`kernfs_link_sibling.locking`:

Locking
-------

mutex_lock(kernfs_mutex)

.. _`kernfs_link_sibling.return`:

Return
------

0 on susccess -EEXIST on failure.

.. _`kernfs_unlink_sibling`:

kernfs_unlink_sibling
=====================

.. c:function:: bool kernfs_unlink_sibling(struct kernfs_node *kn)

    unlink kernfs_node from sibling rbtree

    :param struct kernfs_node \*kn:
        kernfs_node of interest

.. _`kernfs_unlink_sibling.description`:

Description
-----------

Try to unlink \ ``kn``\  from its sibling rbtree which starts from
kn->parent->dir.children.  Returns \ ``true``\  if \ ``kn``\  was actually
removed, \ ``false``\  if \ ``kn``\  wasn't on the rbtree.

.. _`kernfs_unlink_sibling.locking`:

Locking
-------

mutex_lock(kernfs_mutex)

.. _`kernfs_get_active`:

kernfs_get_active
=================

.. c:function:: struct kernfs_node *kernfs_get_active(struct kernfs_node *kn)

    get an active reference to kernfs_node

    :param struct kernfs_node \*kn:
        kernfs_node to get an active reference to

.. _`kernfs_get_active.description`:

Description
-----------

Get an active reference of \ ``kn``\ .  This function is noop if \ ``kn``\ 
is NULL.

.. _`kernfs_get_active.return`:

Return
------

Pointer to \ ``kn``\  on success, NULL on failure.

.. _`kernfs_put_active`:

kernfs_put_active
=================

.. c:function:: void kernfs_put_active(struct kernfs_node *kn)

    put an active reference to kernfs_node

    :param struct kernfs_node \*kn:
        kernfs_node to put an active reference to

.. _`kernfs_put_active.description`:

Description
-----------

Put an active reference to \ ``kn``\ .  This function is noop if \ ``kn``\ 
is NULL.

.. _`kernfs_drain`:

kernfs_drain
============

.. c:function:: void kernfs_drain(struct kernfs_node *kn)

    drain kernfs_node

    :param struct kernfs_node \*kn:
        kernfs_node to drain

.. _`kernfs_drain.description`:

Description
-----------

Drain existing usages and nuke all existing mmaps of \ ``kn``\ .  Mutiple
removers may invoke this function concurrently on \ ``kn``\  and all will
return after draining is complete.

.. _`kernfs_get`:

kernfs_get
==========

.. c:function:: void kernfs_get(struct kernfs_node *kn)

    get a reference count on a kernfs_node

    :param struct kernfs_node \*kn:
        the target kernfs_node

.. _`kernfs_put`:

kernfs_put
==========

.. c:function:: void kernfs_put(struct kernfs_node *kn)

    put a reference count on a kernfs_node

    :param struct kernfs_node \*kn:
        the target kernfs_node

.. _`kernfs_put.description`:

Description
-----------

Put a reference count of \ ``kn``\  and destroy it if it reached zero.

.. _`kernfs_node_from_dentry`:

kernfs_node_from_dentry
=======================

.. c:function:: struct kernfs_node *kernfs_node_from_dentry(struct dentry *dentry)

    determine kernfs_node associated with a dentry

    :param struct dentry \*dentry:
        the dentry in question

.. _`kernfs_node_from_dentry.description`:

Description
-----------

Return the kernfs_node associated with \ ``dentry``\ .  If \ ``dentry``\  is not a
kernfs one, \ ``NULL``\  is returned.

While the returned kernfs_node will stay accessible as long as \ ``dentry``\ 
is accessible, the returned node can be in any state and the caller is
fully responsible for determining what's accessible.

.. _`kernfs_add_one`:

kernfs_add_one
==============

.. c:function:: int kernfs_add_one(struct kernfs_node *kn)

    add kernfs_node to parent without warning

    :param struct kernfs_node \*kn:
        kernfs_node to be added

.. _`kernfs_add_one.description`:

Description
-----------

The caller must already have initialized \ ``kn``\ ->parent.  This
function increments nlink of the parent's inode if \ ``kn``\  is a
directory and link into the children list of the parent.

.. _`kernfs_add_one.return`:

Return
------

0 on success, -EEXIST if entry with the given name already
exists.

.. _`kernfs_find_ns`:

kernfs_find_ns
==============

.. c:function:: struct kernfs_node *kernfs_find_ns(struct kernfs_node *parent, const unsigned char *name, const void *ns)

    find kernfs_node with the given name

    :param struct kernfs_node \*parent:
        kernfs_node to search under

    :param const unsigned char \*name:
        name to look for

    :param const void \*ns:
        the namespace tag to use

.. _`kernfs_find_ns.description`:

Description
-----------

Look for kernfs_node with name \ ``name``\  under \ ``parent``\ .  Returns pointer to
the found kernfs_node on success, \ ``NULL``\  on failure.

.. _`kernfs_find_and_get_ns`:

kernfs_find_and_get_ns
======================

.. c:function:: struct kernfs_node *kernfs_find_and_get_ns(struct kernfs_node *parent, const char *name, const void *ns)

    find and get kernfs_node with the given name

    :param struct kernfs_node \*parent:
        kernfs_node to search under

    :param const char \*name:
        name to look for

    :param const void \*ns:
        the namespace tag to use

.. _`kernfs_find_and_get_ns.description`:

Description
-----------

Look for kernfs_node with name \ ``name``\  under \ ``parent``\  and get a reference
if found.  This function may sleep and returns pointer to the found
kernfs_node on success, \ ``NULL``\  on failure.

.. _`kernfs_walk_and_get_ns`:

kernfs_walk_and_get_ns
======================

.. c:function:: struct kernfs_node *kernfs_walk_and_get_ns(struct kernfs_node *parent, const char *path, const void *ns)

    find and get kernfs_node with the given path

    :param struct kernfs_node \*parent:
        kernfs_node to search under

    :param const char \*path:
        path to look for

    :param const void \*ns:
        the namespace tag to use

.. _`kernfs_walk_and_get_ns.description`:

Description
-----------

Look for kernfs_node with path \ ``path``\  under \ ``parent``\  and get a reference
if found.  This function may sleep and returns pointer to the found
kernfs_node on success, \ ``NULL``\  on failure.

.. _`kernfs_create_root`:

kernfs_create_root
==================

.. c:function:: struct kernfs_root *kernfs_create_root(struct kernfs_syscall_ops *scops, unsigned int flags, void *priv)

    create a new kernfs hierarchy

    :param struct kernfs_syscall_ops \*scops:
        optional syscall operations for the hierarchy

    :param unsigned int flags:
        KERNFS_ROOT\_\* flags

    :param void \*priv:
        opaque data associated with the new directory

.. _`kernfs_create_root.description`:

Description
-----------

Returns the root of the new hierarchy on success, \ :c:func:`ERR_PTR`\  value on
failure.

.. _`kernfs_destroy_root`:

kernfs_destroy_root
===================

.. c:function:: void kernfs_destroy_root(struct kernfs_root *root)

    destroy a kernfs hierarchy

    :param struct kernfs_root \*root:
        root of the hierarchy to destroy

.. _`kernfs_destroy_root.description`:

Description
-----------

Destroy the hierarchy anchored at \ ``root``\  by removing all existing
directories and destroying \ ``root``\ .

.. _`kernfs_create_dir_ns`:

kernfs_create_dir_ns
====================

.. c:function:: struct kernfs_node *kernfs_create_dir_ns(struct kernfs_node *parent, const char *name, umode_t mode, void *priv, const void *ns)

    create a directory

    :param struct kernfs_node \*parent:
        parent in which to create a new directory

    :param const char \*name:
        name of the new directory

    :param umode_t mode:
        mode of the new directory

    :param void \*priv:
        opaque data associated with the new directory

    :param const void \*ns:
        optional namespace tag of the directory

.. _`kernfs_create_dir_ns.description`:

Description
-----------

Returns the created node on success, \ :c:func:`ERR_PTR`\  value on failure.

.. _`kernfs_create_empty_dir`:

kernfs_create_empty_dir
=======================

.. c:function:: struct kernfs_node *kernfs_create_empty_dir(struct kernfs_node *parent, const char *name)

    create an always empty directory

    :param struct kernfs_node \*parent:
        parent in which to create a new directory

    :param const char \*name:
        name of the new directory

.. _`kernfs_create_empty_dir.description`:

Description
-----------

Returns the created node on success, \ :c:func:`ERR_PTR`\  value on failure.

.. _`kernfs_next_descendant_post`:

kernfs_next_descendant_post
===========================

.. c:function:: struct kernfs_node *kernfs_next_descendant_post(struct kernfs_node *pos, struct kernfs_node *root)

    find the next descendant for post-order walk

    :param struct kernfs_node \*pos:
        the current position (%NULL to initiate traversal)

    :param struct kernfs_node \*root:
        kernfs_node whose descendants to walk

.. _`kernfs_next_descendant_post.description`:

Description
-----------

Find the next descendant to visit for post-order traversal of \ ``root``\ 's
descendants.  \ ``root``\  is included in the iteration and the last node to be
visited.

.. _`kernfs_activate`:

kernfs_activate
===============

.. c:function:: void kernfs_activate(struct kernfs_node *kn)

    activate a node which started deactivated

    :param struct kernfs_node \*kn:
        kernfs_node whose subtree is to be activated

.. _`kernfs_activate.description`:

Description
-----------

If the root has KERNFS_ROOT_CREATE_DEACTIVATED set, a newly created node
needs to be explicitly activated.  A node which hasn't been activated
isn't visible to userland and deactivation is skipped during its
removal.  This is useful to construct atomic init sequences where
creation of multiple nodes should either succeed or fail atomically.

The caller is responsible for ensuring that this function is not called
after kernfs_remove\*() is invoked on \ ``kn``\ .

.. _`kernfs_remove`:

kernfs_remove
=============

.. c:function:: void kernfs_remove(struct kernfs_node *kn)

    remove a kernfs_node recursively

    :param struct kernfs_node \*kn:
        the kernfs_node to remove

.. _`kernfs_remove.description`:

Description
-----------

Remove \ ``kn``\  along with all its subdirectories and files.

.. _`kernfs_break_active_protection`:

kernfs_break_active_protection
==============================

.. c:function:: void kernfs_break_active_protection(struct kernfs_node *kn)

    break out of active protection

    :param struct kernfs_node \*kn:
        the self kernfs_node

.. _`kernfs_break_active_protection.description`:

Description
-----------

The caller must be running off of a kernfs operation which is invoked
with an active reference - e.g. one of kernfs_ops.  Each invocation of
this function must also be matched with an invocation of
\ :c:func:`kernfs_unbreak_active_protection`\ .

This function releases the active reference of \ ``kn``\  the caller is
holding.  Once this function is called, \ ``kn``\  may be removed at any point
and the caller is solely responsible for ensuring that the objects it
dereferences are accessible.

.. _`kernfs_unbreak_active_protection`:

kernfs_unbreak_active_protection
================================

.. c:function:: void kernfs_unbreak_active_protection(struct kernfs_node *kn)

    undo \ :c:func:`kernfs_break_active_protection`\ 

    :param struct kernfs_node \*kn:
        the self kernfs_node

.. _`kernfs_unbreak_active_protection.description`:

Description
-----------

If \ :c:func:`kernfs_break_active_protection`\  was called, this function must be
invoked before finishing the kernfs operation.  Note that while this
function restores the active reference, it doesn't and can't actually
restore the active protection - \ ``kn``\  may already or be in the process of
being removed.  Once \ :c:func:`kernfs_break_active_protection`\  is invoked, that
protection is irreversibly gone for the kernfs operation instance.

While this function may be called at any point after
\ :c:func:`kernfs_break_active_protection`\  is invoked, its most useful location
would be right before the enclosing kernfs operation returns.

.. _`kernfs_remove_self`:

kernfs_remove_self
==================

.. c:function:: bool kernfs_remove_self(struct kernfs_node *kn)

    remove a kernfs_node from its own method

    :param struct kernfs_node \*kn:
        the self kernfs_node to remove

.. _`kernfs_remove_self.description`:

Description
-----------

The caller must be running off of a kernfs operation which is invoked
with an active reference - e.g. one of kernfs_ops.  This can be used to
implement a file operation which deletes itself.

For example, the "delete" file for a sysfs device directory can be
implemented by invoking \ :c:func:`kernfs_remove_self`\  on the "delete" file
itself.  This function breaks the circular dependency of trying to
deactivate self while holding an active ref itself.  It isn't necessary
to modify the usual removal path to use \ :c:func:`kernfs_remove_self`\ .  The
"delete" implementation can simply invoke \ :c:func:`kernfs_remove_self`\  on self
before proceeding with the usual removal path.  kernfs will ignore later
\ :c:func:`kernfs_remove`\  on self.

\ :c:func:`kernfs_remove_self`\  can be called multiple times concurrently on the
same kernfs_node.  Only the first one actually performs removal and
returns \ ``true``\ .  All others will wait until the kernfs operation which
won self-removal finishes and return \ ``false``\ .  Note that the losers wait
for the completion of not only the winning \ :c:func:`kernfs_remove_self`\  but also
the whole kernfs_ops which won the arbitration.  This can be used to
guarantee, for example, all concurrent writes to a "delete" file to
finish only after the whole operation is complete.

.. _`kernfs_remove_by_name_ns`:

kernfs_remove_by_name_ns
========================

.. c:function:: int kernfs_remove_by_name_ns(struct kernfs_node *parent, const char *name, const void *ns)

    find a kernfs_node by name and remove it

    :param struct kernfs_node \*parent:
        parent of the target

    :param const char \*name:
        name of the kernfs_node to remove

    :param const void \*ns:
        namespace tag of the kernfs_node to remove

.. _`kernfs_remove_by_name_ns.description`:

Description
-----------

Look for the kernfs_node with \ ``name``\  and \ ``ns``\  under \ ``parent``\  and remove it.
Returns 0 on success, -ENOENT if such entry doesn't exist.

.. _`kernfs_rename_ns`:

kernfs_rename_ns
================

.. c:function:: int kernfs_rename_ns(struct kernfs_node *kn, struct kernfs_node *new_parent, const char *new_name, const void *new_ns)

    move and rename a kernfs_node

    :param struct kernfs_node \*kn:
        target node

    :param struct kernfs_node \*new_parent:
        new parent to put \ ``sd``\  under

    :param const char \*new_name:
        new name

    :param const void \*new_ns:
        new namespace tag

.. This file was automatic generated / don't edit.

