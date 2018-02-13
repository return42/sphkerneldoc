.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/lsm.c

.. _`common_perm`:

common_perm
===========

.. c:function:: int common_perm(const char *op, const struct path *path, u32 mask, struct path_cond *cond)

    basic common permission check wrapper fn for paths

    :param const char \*op:
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

\ ``0``\  else error code if error or permission denied

.. _`common_perm_cond`:

common_perm_cond
================

.. c:function:: int common_perm_cond(const char *op, const struct path *path, u32 mask)

    common permission wrapper around inode cond

    :param const char \*op:
        operation being checked

    :param const struct path \*path:
        location to check (NOT NULL)

    :param u32 mask:
        requested permissions mask

.. _`common_perm_cond.return`:

Return
------

\ ``0``\  else error code if error or permission denied

.. _`common_perm_dir_dentry`:

common_perm_dir_dentry
======================

.. c:function:: int common_perm_dir_dentry(const char *op, const struct path *dir, struct dentry *dentry, u32 mask, struct path_cond *cond)

    common permission wrapper when path is dir, dentry

    :param const char \*op:
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

\ ``0``\  else error code if error or permission denied

.. _`common_perm_rm`:

common_perm_rm
==============

.. c:function:: int common_perm_rm(const char *op, const struct path *dir, struct dentry *dentry, u32 mask)

    common permission wrapper for operations doing rm

    :param const char \*op:
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

\ ``0``\  else error code if error or permission denied

.. _`common_perm_create`:

common_perm_create
==================

.. c:function:: int common_perm_create(const char *op, const struct path *dir, struct dentry *dentry, u32 mask, umode_t mode)

    common permission wrapper for operations doing create

    :param const char \*op:
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

\ ``0``\  else error code if error or permission denied

.. _`apparmor_bprm_committing_creds`:

apparmor_bprm_committing_creds
==============================

.. c:function:: void apparmor_bprm_committing_creds(struct linux_binprm *bprm)

    do task cleanup on committing new creds

    :param struct linux_binprm \*bprm:
        binprm for the exec  (NOT NULL)

.. _`apparmor_bprm_committed_creds`:

apparmor_bprm_committed_creds
=============================

.. c:function:: void apparmor_bprm_committed_creds(struct linux_binprm *bprm)

    do cleanup after new creds committed

    :param struct linux_binprm \*bprm:
        binprm for the exec  (NOT NULL)

.. _`set_init_ctx`:

set_init_ctx
============

.. c:function:: int set_init_ctx( void)

    set a task context and profile on the first task.

    :param  void:
        no arguments

.. _`set_init_ctx.todo`:

TODO
----

allow setting an alternate profile than unconfined

.. This file was automatic generated / don't edit.

