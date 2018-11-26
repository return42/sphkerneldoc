.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/configfs/dir.c

.. _`configfs_create_dir`:

configfs_create_dir
===================

.. c:function:: int configfs_create_dir(struct config_item *item, struct dentry *dentry)

    create a directory for an config_item.

    :param item:
        config_itemwe're creating directory for.
    :type item: struct config_item \*

    :param dentry:
        config_item's dentry.
    :type dentry: struct dentry \*

.. _`configfs_create_dir.note`:

Note
----

user-created entries won't be allowed under this new directory
until it is validated by \ :c:func:`configfs_dir_set_ready`\ 

.. _`configfs_remove_dir`:

configfs_remove_dir
===================

.. c:function:: void configfs_remove_dir(struct config_item *item)

    remove an config_item's directory.

    :param item:
        config_item we're removing.
    :type item: struct config_item \*

.. _`configfs_remove_dir.description`:

Description
-----------

The only thing special about this is that we remove any files in
the directory before we remove the directory, and we've inlined
what used to be \ :c:func:`configfs_rmdir`\  below, instead of calling separately.

Caller holds the mutex of the item's inode

.. _`configfs_register_group`:

configfs_register_group
=======================

.. c:function:: int configfs_register_group(struct config_group *parent_group, struct config_group *group)

    creates a parent-child relation between two groups

    :param parent_group:
        parent group
    :type parent_group: struct config_group \*

    :param group:
        child group
    :type group: struct config_group \*

.. _`configfs_register_group.description`:

Description
-----------

link groups, creates dentry for the child and attaches it to the
parent dentry.

.. _`configfs_register_group.return`:

Return
------

0 on success, negative errno code on error

.. _`configfs_unregister_group`:

configfs_unregister_group
=========================

.. c:function:: void configfs_unregister_group(struct config_group *group)

    unregisters a child group from its parent

    :param group:
        parent group to be unregistered
    :type group: struct config_group \*

.. _`configfs_unregister_group.description`:

Description
-----------

Undoes \ :c:func:`configfs_register_group`\ 

.. _`configfs_register_default_group`:

configfs_register_default_group
===============================

.. c:function:: struct config_group *configfs_register_default_group(struct config_group *parent_group, const char *name, const struct config_item_type *item_type)

    allocates and registers a child group

    :param parent_group:
        parent group
    :type parent_group: struct config_group \*

    :param name:
        child group name
    :type name: const char \*

    :param item_type:
        child item type description
    :type item_type: const struct config_item_type \*

.. _`configfs_register_default_group.description`:

Description
-----------

boilerplate to allocate and register a child group with its parent. We need
kzalloc'ed memory because child's default_group is initially empty.

.. _`configfs_register_default_group.return`:

Return
------

allocated config group or \ :c:func:`ERR_PTR`\  on error

.. _`configfs_unregister_default_group`:

configfs_unregister_default_group
=================================

.. c:function:: void configfs_unregister_default_group(struct config_group *group)

    unregisters and frees a child group

    :param group:
        the group to act on
    :type group: struct config_group \*

.. This file was automatic generated / don't edit.

