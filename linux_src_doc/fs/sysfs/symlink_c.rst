.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/sysfs/symlink.c

.. _`sysfs_create_link_sd`:

sysfs_create_link_sd
====================

.. c:function:: int sysfs_create_link_sd(struct kernfs_node *kn, struct kobject *target, const char *name)

    create symlink to a given object.

    :param kn:
        directory we're creating the link in.
    :type kn: struct kernfs_node \*

    :param target:
        object we're pointing to.
    :type target: struct kobject \*

    :param name:
        name of the symlink.
    :type name: const char \*

.. _`sysfs_create_link`:

sysfs_create_link
=================

.. c:function:: int sysfs_create_link(struct kobject *kobj, struct kobject *target, const char *name)

    create symlink between two objects.

    :param kobj:
        object whose directory we're creating the link in.
    :type kobj: struct kobject \*

    :param target:
        object we're pointing to.
    :type target: struct kobject \*

    :param name:
        name of the symlink.
    :type name: const char \*

.. _`sysfs_create_link_nowarn`:

sysfs_create_link_nowarn
========================

.. c:function:: int sysfs_create_link_nowarn(struct kobject *kobj, struct kobject *target, const char *name)

    create symlink between two objects.

    :param kobj:
        object whose directory we're creating the link in.
    :type kobj: struct kobject \*

    :param target:
        object we're pointing to.
    :type target: struct kobject \*

    :param name:
        name of the symlink.
    :type name: const char \*

.. _`sysfs_create_link_nowarn.description`:

Description
-----------

     This function does the same as \ :c:func:`sysfs_create_link`\ , but it
     doesn't warn if the link already exists.

.. _`sysfs_delete_link`:

sysfs_delete_link
=================

.. c:function:: void sysfs_delete_link(struct kobject *kobj, struct kobject *targ, const char *name)

    remove symlink in object's directory.

    :param kobj:
        object we're acting for.
    :type kobj: struct kobject \*

    :param targ:
        object we're pointing to.
    :type targ: struct kobject \*

    :param name:
        name of the symlink to remove.
    :type name: const char \*

.. _`sysfs_delete_link.description`:

Description
-----------

     Unlike sysfs_remove_link sysfs_delete_link has enough information
     to successfully delete symlinks in tagged directories.

.. _`sysfs_remove_link`:

sysfs_remove_link
=================

.. c:function:: void sysfs_remove_link(struct kobject *kobj, const char *name)

    remove symlink in object's directory.

    :param kobj:
        object we're acting for.
    :type kobj: struct kobject \*

    :param name:
        name of the symlink to remove.
    :type name: const char \*

.. _`sysfs_rename_link_ns`:

sysfs_rename_link_ns
====================

.. c:function:: int sysfs_rename_link_ns(struct kobject *kobj, struct kobject *targ, const char *old, const char *new, const void *new_ns)

    rename symlink in object's directory.

    :param kobj:
        object we're acting for.
    :type kobj: struct kobject \*

    :param targ:
        object we're pointing to.
    :type targ: struct kobject \*

    :param old:
        previous name of the symlink.
    :type old: const char \*

    :param new:
        new name of the symlink.
    :type new: const char \*

    :param new_ns:
        new namespace of the symlink.
    :type new_ns: const void \*

.. _`sysfs_rename_link_ns.description`:

Description
-----------

     A helper function for the common rename symlink idiom.

.. This file was automatic generated / don't edit.

