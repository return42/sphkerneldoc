.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/tomoyo.c

.. _`tomoyo_cred_alloc_blank`:

tomoyo_cred_alloc_blank
=======================

.. c:function:: int tomoyo_cred_alloc_blank(struct cred *new, gfp_t gfp)

    Target for \ :c:func:`security_cred_alloc_blank`\ .

    :param new:
        Pointer to "struct cred".
    :type new: struct cred \*

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`tomoyo_cred_alloc_blank.description`:

Description
-----------

Returns 0.

.. _`tomoyo_cred_prepare`:

tomoyo_cred_prepare
===================

.. c:function:: int tomoyo_cred_prepare(struct cred *new, const struct cred *old, gfp_t gfp)

    Target for \ :c:func:`security_prepare_creds`\ .

    :param new:
        Pointer to "struct cred".
    :type new: struct cred \*

    :param old:
        Pointer to "struct cred".
    :type old: const struct cred \*

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`tomoyo_cred_prepare.description`:

Description
-----------

Returns 0.

.. _`tomoyo_cred_transfer`:

tomoyo_cred_transfer
====================

.. c:function:: void tomoyo_cred_transfer(struct cred *new, const struct cred *old)

    Target for \ :c:func:`security_transfer_creds`\ .

    :param new:
        Pointer to "struct cred".
    :type new: struct cred \*

    :param old:
        Pointer to "struct cred".
    :type old: const struct cred \*

.. _`tomoyo_cred_free`:

tomoyo_cred_free
================

.. c:function:: void tomoyo_cred_free(struct cred *cred)

    Target for \ :c:func:`security_cred_free`\ .

    :param cred:
        Pointer to "struct cred".
    :type cred: struct cred \*

.. _`tomoyo_bprm_set_creds`:

tomoyo_bprm_set_creds
=====================

.. c:function:: int tomoyo_bprm_set_creds(struct linux_binprm *bprm)

    Target for \ :c:func:`security_bprm_set_creds`\ .

    :param bprm:
        Pointer to "struct linux_binprm".
    :type bprm: struct linux_binprm \*

.. _`tomoyo_bprm_set_creds.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_bprm_check_security`:

tomoyo_bprm_check_security
==========================

.. c:function:: int tomoyo_bprm_check_security(struct linux_binprm *bprm)

    Target for \ :c:func:`security_bprm_check`\ .

    :param bprm:
        Pointer to "struct linux_binprm".
    :type bprm: struct linux_binprm \*

.. _`tomoyo_bprm_check_security.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_inode_getattr`:

tomoyo_inode_getattr
====================

.. c:function:: int tomoyo_inode_getattr(const struct path *path)

    Target for \ :c:func:`security_inode_getattr`\ .

    :param path:
        *undescribed*
    :type path: const struct path \*

.. _`tomoyo_inode_getattr.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_truncate`:

tomoyo_path_truncate
====================

.. c:function:: int tomoyo_path_truncate(const struct path *path)

    Target for \ :c:func:`security_path_truncate`\ .

    :param path:
        Pointer to "struct path".
    :type path: const struct path \*

.. _`tomoyo_path_truncate.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_unlink`:

tomoyo_path_unlink
==================

.. c:function:: int tomoyo_path_unlink(const struct path *parent, struct dentry *dentry)

    Target for \ :c:func:`security_path_unlink`\ .

    :param parent:
        Pointer to "struct path".
    :type parent: const struct path \*

    :param dentry:
        Pointer to "struct dentry".
    :type dentry: struct dentry \*

.. _`tomoyo_path_unlink.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_mkdir`:

tomoyo_path_mkdir
=================

.. c:function:: int tomoyo_path_mkdir(const struct path *parent, struct dentry *dentry, umode_t mode)

    Target for \ :c:func:`security_path_mkdir`\ .

    :param parent:
        Pointer to "struct path".
    :type parent: const struct path \*

    :param dentry:
        Pointer to "struct dentry".
    :type dentry: struct dentry \*

    :param mode:
        DAC permission mode.
    :type mode: umode_t

.. _`tomoyo_path_mkdir.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_rmdir`:

tomoyo_path_rmdir
=================

.. c:function:: int tomoyo_path_rmdir(const struct path *parent, struct dentry *dentry)

    Target for \ :c:func:`security_path_rmdir`\ .

    :param parent:
        Pointer to "struct path".
    :type parent: const struct path \*

    :param dentry:
        Pointer to "struct dentry".
    :type dentry: struct dentry \*

.. _`tomoyo_path_rmdir.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_symlink`:

tomoyo_path_symlink
===================

.. c:function:: int tomoyo_path_symlink(const struct path *parent, struct dentry *dentry, const char *old_name)

    Target for \ :c:func:`security_path_symlink`\ .

    :param parent:
        Pointer to "struct path".
    :type parent: const struct path \*

    :param dentry:
        Pointer to "struct dentry".
    :type dentry: struct dentry \*

    :param old_name:
        Symlink's content.
    :type old_name: const char \*

.. _`tomoyo_path_symlink.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_mknod`:

tomoyo_path_mknod
=================

.. c:function:: int tomoyo_path_mknod(const struct path *parent, struct dentry *dentry, umode_t mode, unsigned int dev)

    Target for \ :c:func:`security_path_mknod`\ .

    :param parent:
        Pointer to "struct path".
    :type parent: const struct path \*

    :param dentry:
        Pointer to "struct dentry".
    :type dentry: struct dentry \*

    :param mode:
        DAC permission mode.
    :type mode: umode_t

    :param dev:
        Device attributes.
    :type dev: unsigned int

.. _`tomoyo_path_mknod.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_link`:

tomoyo_path_link
================

.. c:function:: int tomoyo_path_link(struct dentry *old_dentry, const struct path *new_dir, struct dentry *new_dentry)

    Target for \ :c:func:`security_path_link`\ .

    :param old_dentry:
        Pointer to "struct dentry".
    :type old_dentry: struct dentry \*

    :param new_dir:
        Pointer to "struct path".
    :type new_dir: const struct path \*

    :param new_dentry:
        Pointer to "struct dentry".
    :type new_dentry: struct dentry \*

.. _`tomoyo_path_link.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_rename`:

tomoyo_path_rename
==================

.. c:function:: int tomoyo_path_rename(const struct path *old_parent, struct dentry *old_dentry, const struct path *new_parent, struct dentry *new_dentry)

    Target for \ :c:func:`security_path_rename`\ .

    :param old_parent:
        Pointer to "struct path".
    :type old_parent: const struct path \*

    :param old_dentry:
        Pointer to "struct dentry".
    :type old_dentry: struct dentry \*

    :param new_parent:
        Pointer to "struct path".
    :type new_parent: const struct path \*

    :param new_dentry:
        Pointer to "struct dentry".
    :type new_dentry: struct dentry \*

.. _`tomoyo_path_rename.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_file_fcntl`:

tomoyo_file_fcntl
=================

.. c:function:: int tomoyo_file_fcntl(struct file *file, unsigned int cmd, unsigned long arg)

    Target for \ :c:func:`security_file_fcntl`\ .

    :param file:
        Pointer to "struct file".
    :type file: struct file \*

    :param cmd:
        Command for \ :c:func:`fcntl`\ .
    :type cmd: unsigned int

    :param arg:
        Argument for \ ``cmd``\ .
    :type arg: unsigned long

.. _`tomoyo_file_fcntl.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_file_open`:

tomoyo_file_open
================

.. c:function:: int tomoyo_file_open(struct file *f)

    Target for \ :c:func:`security_file_open`\ .

    :param f:
        Pointer to "struct file".
    :type f: struct file \*

.. _`tomoyo_file_open.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_file_ioctl`:

tomoyo_file_ioctl
=================

.. c:function:: int tomoyo_file_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    Target for \ :c:func:`security_file_ioctl`\ .

    :param file:
        Pointer to "struct file".
    :type file: struct file \*

    :param cmd:
        Command for \ :c:func:`ioctl`\ .
    :type cmd: unsigned int

    :param arg:
        Argument for \ ``cmd``\ .
    :type arg: unsigned long

.. _`tomoyo_file_ioctl.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_chmod`:

tomoyo_path_chmod
=================

.. c:function:: int tomoyo_path_chmod(const struct path *path, umode_t mode)

    Target for \ :c:func:`security_path_chmod`\ .

    :param path:
        Pointer to "struct path".
    :type path: const struct path \*

    :param mode:
        DAC permission mode.
    :type mode: umode_t

.. _`tomoyo_path_chmod.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_chown`:

tomoyo_path_chown
=================

.. c:function:: int tomoyo_path_chown(const struct path *path, kuid_t uid, kgid_t gid)

    Target for \ :c:func:`security_path_chown`\ .

    :param path:
        Pointer to "struct path".
    :type path: const struct path \*

    :param uid:
        Owner ID.
    :type uid: kuid_t

    :param gid:
        Group ID.
    :type gid: kgid_t

.. _`tomoyo_path_chown.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_path_chroot`:

tomoyo_path_chroot
==================

.. c:function:: int tomoyo_path_chroot(const struct path *path)

    Target for \ :c:func:`security_path_chroot`\ .

    :param path:
        Pointer to "struct path".
    :type path: const struct path \*

.. _`tomoyo_path_chroot.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_sb_mount`:

tomoyo_sb_mount
===============

.. c:function:: int tomoyo_sb_mount(const char *dev_name, const struct path *path, const char *type, unsigned long flags, void *data)

    Target for \ :c:func:`security_sb_mount`\ .

    :param dev_name:
        Name of device file. Maybe NULL.
    :type dev_name: const char \*

    :param path:
        Pointer to "struct path".
    :type path: const struct path \*

    :param type:
        Name of filesystem type. Maybe NULL.
    :type type: const char \*

    :param flags:
        Mount options.
    :type flags: unsigned long

    :param data:
        Optional data. Maybe NULL.
    :type data: void \*

.. _`tomoyo_sb_mount.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_sb_umount`:

tomoyo_sb_umount
================

.. c:function:: int tomoyo_sb_umount(struct vfsmount *mnt, int flags)

    Target for \ :c:func:`security_sb_umount`\ .

    :param mnt:
        Pointer to "struct vfsmount".
    :type mnt: struct vfsmount \*

    :param flags:
        Unmount options.
    :type flags: int

.. _`tomoyo_sb_umount.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_sb_pivotroot`:

tomoyo_sb_pivotroot
===================

.. c:function:: int tomoyo_sb_pivotroot(const struct path *old_path, const struct path *new_path)

    Target for \ :c:func:`security_sb_pivotroot`\ .

    :param old_path:
        Pointer to "struct path".
    :type old_path: const struct path \*

    :param new_path:
        Pointer to "struct path".
    :type new_path: const struct path \*

.. _`tomoyo_sb_pivotroot.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_socket_listen`:

tomoyo_socket_listen
====================

.. c:function:: int tomoyo_socket_listen(struct socket *sock, int backlog)

    Check permission for \ :c:func:`listen`\ .

    :param sock:
        Pointer to "struct socket".
    :type sock: struct socket \*

    :param backlog:
        Backlog parameter.
    :type backlog: int

.. _`tomoyo_socket_listen.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_socket_connect`:

tomoyo_socket_connect
=====================

.. c:function:: int tomoyo_socket_connect(struct socket *sock, struct sockaddr *addr, int addr_len)

    Check permission for \ :c:func:`connect`\ .

    :param sock:
        Pointer to "struct socket".
    :type sock: struct socket \*

    :param addr:
        Pointer to "struct sockaddr".
    :type addr: struct sockaddr \*

    :param addr_len:
        Size of \ ``addr``\ .
    :type addr_len: int

.. _`tomoyo_socket_connect.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_socket_bind`:

tomoyo_socket_bind
==================

.. c:function:: int tomoyo_socket_bind(struct socket *sock, struct sockaddr *addr, int addr_len)

    Check permission for \ :c:func:`bind`\ .

    :param sock:
        Pointer to "struct socket".
    :type sock: struct socket \*

    :param addr:
        Pointer to "struct sockaddr".
    :type addr: struct sockaddr \*

    :param addr_len:
        Size of \ ``addr``\ .
    :type addr_len: int

.. _`tomoyo_socket_bind.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_socket_sendmsg`:

tomoyo_socket_sendmsg
=====================

.. c:function:: int tomoyo_socket_sendmsg(struct socket *sock, struct msghdr *msg, int size)

    Check permission for \ :c:func:`sendmsg`\ .

    :param sock:
        Pointer to "struct socket".
    :type sock: struct socket \*

    :param msg:
        Pointer to "struct msghdr".
    :type msg: struct msghdr \*

    :param size:
        Size of message.
    :type size: int

.. _`tomoyo_socket_sendmsg.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_init`:

tomoyo_init
===========

.. c:function:: int tomoyo_init( void)

    Register TOMOYO Linux as a LSM module.

    :param void:
        no arguments
    :type void: 

.. _`tomoyo_init.description`:

Description
-----------

Returns 0.

.. This file was automatic generated / don't edit.

