.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/kernfs/symlink.c

.. _`kernfs_create_link`:

kernfs_create_link
==================

.. c:function:: struct kernfs_node *kernfs_create_link(struct kernfs_node *parent, const char *name, struct kernfs_node *target)

    create a symlink

    :param parent:
        directory to create the symlink in
    :type parent: struct kernfs_node \*

    :param name:
        name of the symlink
    :type name: const char \*

    :param target:
        target node for the symlink to point to
    :type target: struct kernfs_node \*

.. _`kernfs_create_link.description`:

Description
-----------

Returns the created node on success, \ :c:func:`ERR_PTR`\  value on error.
Ownership of the link matches ownership of the target.

.. This file was automatic generated / don't edit.

