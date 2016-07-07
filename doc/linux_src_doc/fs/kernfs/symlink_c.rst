.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/kernfs/symlink.c

.. _`kernfs_create_link`:

kernfs_create_link
==================

.. c:function:: struct kernfs_node *kernfs_create_link(struct kernfs_node *parent, const char *name, struct kernfs_node *target)

    create a symlink

    :param struct kernfs_node \*parent:
        directory to create the symlink in

    :param const char \*name:
        name of the symlink

    :param struct kernfs_node \*target:
        target node for the symlink to point to

.. _`kernfs_create_link.description`:

Description
-----------

Returns the created node on success, \ :c:func:`ERR_PTR`\  value on error.

.. This file was automatic generated / don't edit.

