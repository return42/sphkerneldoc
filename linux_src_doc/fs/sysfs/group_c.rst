.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/sysfs/group.c

.. _`sysfs_create_group`:

sysfs_create_group
==================

.. c:function:: int sysfs_create_group(struct kobject *kobj, const struct attribute_group *grp)

    given a directory kobject, create an attribute group

    :param kobj:
        The kobject to create the group on
    :type kobj: struct kobject \*

    :param grp:
        The attribute group to create
    :type grp: const struct attribute_group \*

.. _`sysfs_create_group.description`:

Description
-----------

This function creates a group for the first time.  It will explicitly
warn and error if any of the attribute files being created already exist.

Returns 0 on success or error code on failure.

.. _`sysfs_create_groups`:

sysfs_create_groups
===================

.. c:function:: int sysfs_create_groups(struct kobject *kobj, const struct attribute_group **groups)

    given a directory kobject, create a bunch of attribute groups

    :param kobj:
        The kobject to create the group on
    :type kobj: struct kobject \*

    :param groups:
        The attribute groups to create, NULL terminated
    :type groups: const struct attribute_group \*\*

.. _`sysfs_create_groups.description`:

Description
-----------

This function creates a bunch of attribute groups.  If an error occurs when
creating a group, all previously created groups will be removed, unwinding
everything back to the original state when this function was called.
It will explicitly warn and error if any of the attribute files being
created already exist.

Returns 0 on success or error code from sysfs_create_group on failure.

.. _`sysfs_update_group`:

sysfs_update_group
==================

.. c:function:: int sysfs_update_group(struct kobject *kobj, const struct attribute_group *grp)

    given a directory kobject, update an attribute group

    :param kobj:
        The kobject to update the group on
    :type kobj: struct kobject \*

    :param grp:
        The attribute group to update
    :type grp: const struct attribute_group \*

.. _`sysfs_update_group.description`:

Description
-----------

This function updates an attribute group.  Unlike
\ :c:func:`sysfs_create_group`\ , it will explicitly not warn or error if any
of the attribute files being created already exist.  Furthermore,
if the visibility of the files has changed through the \ :c:func:`is_visible`\ 
callback, it will update the permissions and add or remove the
relevant files. Changing a group's name (subdirectory name under
kobj's directory in sysfs) is not allowed.

The primary use for this function is to call it after making a change
that affects group visibility.

Returns 0 on success or error code on failure.

.. _`sysfs_remove_group`:

sysfs_remove_group
==================

.. c:function:: void sysfs_remove_group(struct kobject *kobj, const struct attribute_group *grp)

    remove a group from a kobject

    :param kobj:
        kobject to remove the group from
    :type kobj: struct kobject \*

    :param grp:
        group to remove
    :type grp: const struct attribute_group \*

.. _`sysfs_remove_group.description`:

Description
-----------

This function removes a group of attributes from a kobject.  The attributes
previously have to have been created for this group, otherwise it will fail.

.. _`sysfs_remove_groups`:

sysfs_remove_groups
===================

.. c:function:: void sysfs_remove_groups(struct kobject *kobj, const struct attribute_group **groups)

    remove a list of groups

    :param kobj:
        The kobject for the groups to be removed from
    :type kobj: struct kobject \*

    :param groups:
        NULL terminated list of groups to be removed
    :type groups: const struct attribute_group \*\*

.. _`sysfs_remove_groups.description`:

Description
-----------

If groups is not NULL, remove the specified groups from the kobject.

.. _`sysfs_merge_group`:

sysfs_merge_group
=================

.. c:function:: int sysfs_merge_group(struct kobject *kobj, const struct attribute_group *grp)

    merge files into a pre-existing attribute group.

    :param kobj:
        The kobject containing the group.
    :type kobj: struct kobject \*

    :param grp:
        The files to create and the attribute group they belong to.
    :type grp: const struct attribute_group \*

.. _`sysfs_merge_group.description`:

Description
-----------

This function returns an error if the group doesn't exist or any of the
files already exist in that group, in which case none of the new files
are created.

.. _`sysfs_unmerge_group`:

sysfs_unmerge_group
===================

.. c:function:: void sysfs_unmerge_group(struct kobject *kobj, const struct attribute_group *grp)

    remove files from a pre-existing attribute group.

    :param kobj:
        The kobject containing the group.
    :type kobj: struct kobject \*

    :param grp:
        The files to remove and the attribute group they belong to.
    :type grp: const struct attribute_group \*

.. _`sysfs_add_link_to_group`:

sysfs_add_link_to_group
=======================

.. c:function:: int sysfs_add_link_to_group(struct kobject *kobj, const char *group_name, struct kobject *target, const char *link_name)

    add a symlink to an attribute group.

    :param kobj:
        The kobject containing the group.
    :type kobj: struct kobject \*

    :param group_name:
        The name of the group.
    :type group_name: const char \*

    :param target:
        The target kobject of the symlink to create.
    :type target: struct kobject \*

    :param link_name:
        The name of the symlink to create.
    :type link_name: const char \*

.. _`sysfs_remove_link_from_group`:

sysfs_remove_link_from_group
============================

.. c:function:: void sysfs_remove_link_from_group(struct kobject *kobj, const char *group_name, const char *link_name)

    remove a symlink from an attribute group.

    :param kobj:
        The kobject containing the group.
    :type kobj: struct kobject \*

    :param group_name:
        The name of the group.
    :type group_name: const char \*

    :param link_name:
        The name of the symlink to remove.
    :type link_name: const char \*

.. _`__compat_only_sysfs_link_entry_to_kobj`:

\__compat_only_sysfs_link_entry_to_kobj
=======================================

.. c:function:: int __compat_only_sysfs_link_entry_to_kobj(struct kobject *kobj, struct kobject *target_kobj, const char *target_name)

    add a symlink to a kobject pointing to a group or an attribute

    :param kobj:
        The kobject containing the group.
    :type kobj: struct kobject \*

    :param target_kobj:
        The target kobject.
    :type target_kobj: struct kobject \*

    :param target_name:
        The name of the target group or attribute.
    :type target_name: const char \*

.. This file was automatic generated / don't edit.

