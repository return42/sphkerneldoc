.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/lsm.c

.. _`common_perm`:

common_perm
===========

.. c:function:: int common_perm(int op, const struct path *path, u32 mask, struct path_cond *cond)

    basic common permission check wrapper fn for paths

    :param int op:
        operation being checked

    :param const struct path \*path:
        path to check permission of  (NOT NULL)

    :param u32 mask:
        requested permissions mask

    :param struct path_cond \*cond:
        conditional info for the permission request  (NOT NULL)

.. _`common_perm.return`:

Return
------

%0 else error code if error or permission denied

.. _`common_perm_dir_dentry`:

common_perm_dir_dentry
======================

.. c:function:: int common_perm_dir_dentry(int op, const struct path *dir, struct dentry *dentry, u32 mask, struct path_cond *cond)

    common permission wrapper when path is dir, dentry

    :param int op:
        operation being checked

    :param const struct path \*dir:
        directory of the dentry  (NOT NULL)

    :param struct dentry \*dentry:
        dentry to check  (NOT NULL)

    :param u32 mask:
        requested permissions mask

    :param struct path_cond \*cond:
        conditional info for the permission request  (NOT NULL)

.. _`common_perm_dir_dentry.return`:

Return
------

%0 else error code if error or permission denied

.. _`common_perm_path`:

common_perm_path
================

.. c:function:: int common_perm_path(int op, const struct path *path, u32 mask)

    common permission wrapper when mnt, dentry

    :param int op:
        operation being checked

    :param const struct path \*path:
        location to check (NOT NULL)

    :param u32 mask:
        requested permissions mask

.. _`common_perm_path.return`:

Return
------

%0 else error code if error or permission denied

.. _`common_perm_rm`:

common_perm_rm
==============

.. c:function:: int common_perm_rm(int op, const struct path *dir, struct dentry *dentry, u32 mask)

    common permission wrapper for operations doing rm

    :param int op:
        operation being checked

    :param const struct path \*dir:
        directory that the dentry is in  (NOT NULL)

    :param struct dentry \*dentry:
        dentry being rm'd  (NOT NULL)

    :param u32 mask:
        requested permission mask

.. _`common_perm_rm.return`:

Return
------

%0 else error code if error or permission denied

.. _`common_perm_create`:

common_perm_create
==================

.. c:function:: int common_perm_create(int op, const struct path *dir, struct dentry *dentry, u32 mask, umode_t mode)

    common permission wrapper for operations doing create

    :param int op:
        operation being checked

    :param const struct path \*dir:
        directory that dentry will be created in  (NOT NULL)

    :param struct dentry \*dentry:
        dentry to create   (NOT NULL)

    :param u32 mask:
        request permission mask

    :param umode_t mode:
        created file mode

.. _`common_perm_create.return`:

Return
------

%0 else error code if error or permission denied

.. _`set_init_cxt`:

set_init_cxt
============

.. c:function:: int set_init_cxt( void)

    set a task context and profile on the first task.

    :param  void:
        no arguments

.. _`set_init_cxt.todo`:

TODO
----

allow setting an alternate profile than unconfined

.. This file was automatic generated / don't edit.

