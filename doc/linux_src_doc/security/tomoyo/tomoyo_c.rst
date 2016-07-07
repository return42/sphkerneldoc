.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/tomoyo.c

.. _`tomoyo_cred_alloc_blank`:

tomoyo_cred_alloc_blank
=======================

.. c:function:: int tomoyo_cred_alloc_blank(struct cred *new, gfp_t gfp)

    Target for \ :c:func:`security_cred_alloc_blank`\ .

    :param struct cred \*new:
        Pointer to "struct cred".

    :param gfp_t gfp:
        Memory allocation flags.

.. _`tomoyo_cred_alloc_blank.description`:

Description
-----------

Returns 0.

.. _`tomoyo_cred_prepare`:

tomoyo_cred_prepare
===================

.. c:function:: int tomoyo_cred_prepare(struct cred *new, const struct cred *old, gfp_t gfp)

    Target for \ :c:func:`security_prepare_creds`\ .

    :param struct cred \*new:
        Pointer to "struct cred".

    :param const struct cred \*old:
        Pointer to "struct cred".

    :param gfp_t gfp:
        Memory allocation flags.

.. _`tomoyo_cred_prepare.description`:

Description
-----------

Returns 0.

.. _`tomoyo_cred_transfer`:

tomoyo_cred_transfer
====================

.. c:function:: void tomoyo_cred_transfer(struct cred *new, const struct cred *old)

    Target for \ :c:func:`security_transfer_creds`\ .

    :param struct cred \*new:
        Pointer to "struct cred".

    :param const struct cred \*old:
        Pointer to "struct cred".

.. _`tomoyo_cred_free`:

tomoyo_cred_free
================

.. c:function:: void tomoyo_cred_free(struct cred *cred)

    Target for \ :c:func:`security_cred_free`\ .

    :param struct cred \*cred:
        Pointer to "struct cred".

.. _`tomoyo_bprm_set_creds`:

tomoyo_bprm_set_creds
=====================

.. c:function:: int tomoyo_bprm_set_creds(struct linux_binprm *bprm)

    Target for \ :c:func:`security_bprm_set_creds`\ .

    :param struct linux_binprm \*bprm:
        Pointer to "struct linux_binprm".

.. _`tomoyo_bprm_set_creds.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_bprm_check_security`:

tomoyo_bprm_check_security
==========================

.. c:function:: int tomoyo_bprm_check_security(struct linux_binprm *bprm)

    Target for \ :c:func:`security_bprm_check`\ .

    :param struct linux_binprm \*bprm:
        Pointer to "struct linux_binprm".

.. _`tomoyo_bprm_check_security.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_inode_getattr`:

tomoyo_inode_getattr
====================

.. c:function:: int tomoyo_inode_getattr(const struct path *path)

    Target for \ :c:func:`security_inode_getattr`\ .

    :param const struct path \*path:
        *undescribed*

.. _`tomoyo_inode_getattr.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_truncate`:

tomoyo_path_truncate
====================

.. c:function:: int tomoyo_path_truncate(const struct path *path)

    Target for \ :c:func:`security_path_truncate`\ .

    :param const struct path \*path:
        Pointer to "struct path".

.. _`tomoyo_path_truncate.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_unlink`:

tomoyo_path_unlink
==================

.. c:function:: int tomoyo_path_unlink(const struct path *parent, struct dentry *dentry)

    Target for \ :c:func:`security_path_unlink`\ .

    :param const struct path \*parent:
        Pointer to "struct path".

    :param struct dentry \*dentry:
        Pointer to "struct dentry".

.. _`tomoyo_path_unlink.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_mkdir`:

tomoyo_path_mkdir
=================

.. c:function:: int tomoyo_path_mkdir(const struct path *parent, struct dentry *dentry, umode_t mode)

    Target for \ :c:func:`security_path_mkdir`\ .

    :param const struct path \*parent:
        Pointer to "struct path".

    :param struct dentry \*dentry:
        Pointer to "struct dentry".

    :param umode_t mode:
        DAC permission mode.

.. _`tomoyo_path_mkdir.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_rmdir`:

tomoyo_path_rmdir
=================

.. c:function:: int tomoyo_path_rmdir(const struct path *parent, struct dentry *dentry)

    Target for \ :c:func:`security_path_rmdir`\ .

    :param const struct path \*parent:
        Pointer to "struct path".

    :param struct dentry \*dentry:
        Pointer to "struct dentry".

.. _`tomoyo_path_rmdir.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_symlink`:

tomoyo_path_symlink
===================

.. c:function:: int tomoyo_path_symlink(const struct path *parent, struct dentry *dentry, const char *old_name)

    Target for \ :c:func:`security_path_symlink`\ .

    :param const struct path \*parent:
        Pointer to "struct path".

    :param struct dentry \*dentry:
        Pointer to "struct dentry".

    :param const char \*old_name:
        Symlink's content.

.. _`tomoyo_path_symlink.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_mknod`:

tomoyo_path_mknod
=================

.. c:function:: int tomoyo_path_mknod(const struct path *parent, struct dentry *dentry, umode_t mode, unsigned int dev)

    Target for \ :c:func:`security_path_mknod`\ .

    :param const struct path \*parent:
        Pointer to "struct path".

    :param struct dentry \*dentry:
        Pointer to "struct dentry".

    :param umode_t mode:
        DAC permission mode.

    :param unsigned int dev:
        Device attributes.

.. _`tomoyo_path_mknod.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_link`:

tomoyo_path_link
================

.. c:function:: int tomoyo_path_link(struct dentry *old_dentry, const struct path *new_dir, struct dentry *new_dentry)

    Target for \ :c:func:`security_path_link`\ .

    :param struct dentry \*old_dentry:
        Pointer to "struct dentry".

    :param const struct path \*new_dir:
        Pointer to "struct path".

    :param struct dentry \*new_dentry:
        Pointer to "struct dentry".

.. _`tomoyo_path_link.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_rename`:

tomoyo_path_rename
==================

.. c:function:: int tomoyo_path_rename(const struct path *old_parent, struct dentry *old_dentry, const struct path *new_parent, struct dentry *new_dentry)

    Target for \ :c:func:`security_path_rename`\ .

    :param const struct path \*old_parent:
        Pointer to "struct path".

    :param struct dentry \*old_dentry:
        Pointer to "struct dentry".

    :param const struct path \*new_parent:
        Pointer to "struct path".

    :param struct dentry \*new_dentry:
        Pointer to "struct dentry".

.. _`tomoyo_path_rename.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_file_fcntl`:

tomoyo_file_fcntl
=================

.. c:function:: int tomoyo_file_fcntl(struct file *file, unsigned int cmd, unsigned long arg)

    Target for \ :c:func:`security_file_fcntl`\ .

    :param struct file \*file:
        Pointer to "struct file".

    :param unsigned int cmd:
        Command for \ :c:func:`fcntl`\ .

    :param unsigned long arg:
        Argument for \ ``cmd``\ .

.. _`tomoyo_file_fcntl.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_file_open`:

tomoyo_file_open
================

.. c:function:: int tomoyo_file_open(struct file *f, const struct cred *cred)

    Target for \ :c:func:`security_file_open`\ .

    :param struct file \*f:
        Pointer to "struct file".

    :param const struct cred \*cred:
        Pointer to "struct cred".

.. _`tomoyo_file_open.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_file_ioctl`:

tomoyo_file_ioctl
=================

.. c:function:: int tomoyo_file_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    Target for \ :c:func:`security_file_ioctl`\ .

    :param struct file \*file:
        Pointer to "struct file".

    :param unsigned int cmd:
        Command for \ :c:func:`ioctl`\ .

    :param unsigned long arg:
        Argument for \ ``cmd``\ .

.. _`tomoyo_file_ioctl.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_chmod`:

tomoyo_path_chmod
=================

.. c:function:: int tomoyo_path_chmod(const struct path *path, umode_t mode)

    Target for \ :c:func:`security_path_chmod`\ .

    :param const struct path \*path:
        Pointer to "struct path".

    :param umode_t mode:
        DAC permission mode.

.. _`tomoyo_path_chmod.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_chown`:

tomoyo_path_chown
=================

.. c:function:: int tomoyo_path_chown(const struct path *path, kuid_t uid, kgid_t gid)

    Target for \ :c:func:`security_path_chown`\ .

    :param const struct path \*path:
        Pointer to "struct path".

    :param kuid_t uid:
        Owner ID.

    :param kgid_t gid:
        Group ID.

.. _`tomoyo_path_chown.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_chroot`:

tomoyo_path_chroot
==================

.. c:function:: int tomoyo_path_chroot(const struct path *path)

    Target for \ :c:func:`security_path_chroot`\ .

    :param const struct path \*path:
        Pointer to "struct path".

.. _`tomoyo_path_chroot.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_sb_mount`:

tomoyo_sb_mount
===============

.. c:function:: int tomoyo_sb_mount(const char *dev_name, const struct path *path, const char *type, unsigned long flags, void *data)

    Target for \ :c:func:`security_sb_mount`\ .

    :param const char \*dev_name:
        Name of device file. Maybe NULL.

    :param const struct path \*path:
        Pointer to "struct path".

    :param const char \*type:
        Name of filesystem type. Maybe NULL.

    :param unsigned long flags:
        Mount options.

    :param void \*data:
        Optional data. Maybe NULL.

.. _`tomoyo_sb_mount.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_sb_umount`:

tomoyo_sb_umount
================

.. c:function:: int tomoyo_sb_umount(struct vfsmount *mnt, int flags)

    Target for \ :c:func:`security_sb_umount`\ .

    :param struct vfsmount \*mnt:
        Pointer to "struct vfsmount".

    :param int flags:
        Unmount options.

.. _`tomoyo_sb_umount.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_sb_pivotroot`:

tomoyo_sb_pivotroot
===================

.. c:function:: int tomoyo_sb_pivotroot(const struct path *old_path, const struct path *new_path)

    Target for \ :c:func:`security_sb_pivotroot`\ .

    :param const struct path \*old_path:
        Pointer to "struct path".

    :param const struct path \*new_path:
        Pointer to "struct path".

.. _`tomoyo_sb_pivotroot.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_socket_listen`:

tomoyo_socket_listen
====================

.. c:function:: int tomoyo_socket_listen(struct socket *sock, int backlog)

    Check permission for \ :c:func:`listen`\ .

    :param struct socket \*sock:
        Pointer to "struct socket".

    :param int backlog:
        Backlog parameter.

.. _`tomoyo_socket_listen.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_socket_connect`:

tomoyo_socket_connect
=====================

.. c:function:: int tomoyo_socket_connect(struct socket *sock, struct sockaddr *addr, int addr_len)

    Check permission for \ :c:func:`connect`\ .

    :param struct socket \*sock:
        Pointer to "struct socket".

    :param struct sockaddr \*addr:
        Pointer to "struct sockaddr".

    :param int addr_len:
        Size of \ ``addr``\ .

.. _`tomoyo_socket_connect.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_socket_bind`:

tomoyo_socket_bind
==================

.. c:function:: int tomoyo_socket_bind(struct socket *sock, struct sockaddr *addr, int addr_len)

    Check permission for \ :c:func:`bind`\ .

    :param struct socket \*sock:
        Pointer to "struct socket".

    :param struct sockaddr \*addr:
        Pointer to "struct sockaddr".

    :param int addr_len:
        Size of \ ``addr``\ .

.. _`tomoyo_socket_bind.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_socket_sendmsg`:

tomoyo_socket_sendmsg
=====================

.. c:function:: int tomoyo_socket_sendmsg(struct socket *sock, struct msghdr *msg, int size)

    Check permission for \ :c:func:`sendmsg`\ .

    :param struct socket \*sock:
        Pointer to "struct socket".

    :param struct msghdr \*msg:
        Pointer to "struct msghdr".

    :param int size:
        Size of message.

.. _`tomoyo_socket_sendmsg.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_init`:

tomoyo_init
===========

.. c:function:: int tomoyo_init( void)

    Register TOMOYO Linux as a LSM module.

    :param  void:
        no arguments

.. _`tomoyo_init.description`:

Description
-----------

Returns 0.

.. This file was automatic generated / don't edit.

