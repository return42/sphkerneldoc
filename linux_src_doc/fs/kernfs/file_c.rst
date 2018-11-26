.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/kernfs/file.c

.. _`kernfs_fop_read`:

kernfs_fop_read
===============

.. c:function:: ssize_t kernfs_fop_read(struct file *file, char __user *user_buf, size_t count, loff_t *ppos)

    kernfs vfs read callback

    :param file:
        file pointer
    :type file: struct file \*

    :param user_buf:
        data to write
    :type user_buf: char __user \*

    :param count:
        number of bytes
    :type count: size_t

    :param ppos:
        starting offset
    :type ppos: loff_t \*

.. _`kernfs_fop_write`:

kernfs_fop_write
================

.. c:function:: ssize_t kernfs_fop_write(struct file *file, const char __user *user_buf, size_t count, loff_t *ppos)

    kernfs vfs write callback

    :param file:
        file pointer
    :type file: struct file \*

    :param user_buf:
        data to write
    :type user_buf: const char __user \*

    :param count:
        number of bytes
    :type count: size_t

    :param ppos:
        starting offset
    :type ppos: loff_t \*

.. _`kernfs_fop_write.description`:

Description
-----------

Copy data in from userland and pass it to the matching kernfs write
operation.

There is no easy way for us to know if userspace is only doing a partial
write, so we don't support them. We expect the entire buffer to come on
the first write.  Hint: if you're writing a value, first read the file,
modify only the the value you're changing, then write entire buffer
back.

.. _`kernfs_get_open_node`:

kernfs_get_open_node
====================

.. c:function:: int kernfs_get_open_node(struct kernfs_node *kn, struct kernfs_open_file *of)

    get or create kernfs_open_node

    :param kn:
        target kernfs_node
    :type kn: struct kernfs_node \*

    :param of:
        kernfs_open_file for this instance of open
    :type of: struct kernfs_open_file \*

.. _`kernfs_get_open_node.description`:

Description
-----------

If \ ``kn->attr.open``\  exists, increment its reference count; otherwise,
create one.  \ ``of``\  is chained to the files list.

.. _`kernfs_get_open_node.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`kernfs_get_open_node.return`:

Return
------

0 on success, -errno on failure.

.. _`kernfs_put_open_node`:

kernfs_put_open_node
====================

.. c:function:: void kernfs_put_open_node(struct kernfs_node *kn, struct kernfs_open_file *of)

    put kernfs_open_node

    :param kn:
        target kernfs_nodet
    :type kn: struct kernfs_node \*

    :param of:
        associated kernfs_open_file
    :type of: struct kernfs_open_file \*

.. _`kernfs_put_open_node.description`:

Description
-----------

Put \ ``kn->attr.open``\  and unlink \ ``of``\  from the files list.  If
reference count reaches zero, disassociate and free it.

.. _`kernfs_put_open_node.locking`:

LOCKING
-------

None.

.. _`kernfs_notify`:

kernfs_notify
=============

.. c:function:: void kernfs_notify(struct kernfs_node *kn)

    notify a kernfs file

    :param kn:
        file to notify
    :type kn: struct kernfs_node \*

.. _`kernfs_notify.description`:

Description
-----------

Notify \ ``kn``\  such that poll(2) on \ ``kn``\  wakes up.  Maybe be called from any
context.

.. _`__kernfs_create_file`:

\__kernfs_create_file
=====================

.. c:function:: struct kernfs_node *__kernfs_create_file(struct kernfs_node *parent, const char *name, umode_t mode, kuid_t uid, kgid_t gid, loff_t size, const struct kernfs_ops *ops, void *priv, const void *ns, struct lock_class_key *key)

    kernfs internal function to create a file

    :param parent:
        directory to create the file in
    :type parent: struct kernfs_node \*

    :param name:
        name of the file
    :type name: const char \*

    :param mode:
        mode of the file
    :type mode: umode_t

    :param uid:
        uid of the file
    :type uid: kuid_t

    :param gid:
        gid of the file
    :type gid: kgid_t

    :param size:
        size of the file
    :type size: loff_t

    :param ops:
        kernfs operations for the file
    :type ops: const struct kernfs_ops \*

    :param priv:
        private data for the file
    :type priv: void \*

    :param ns:
        optional namespace tag of the file
    :type ns: const void \*

    :param key:
        lockdep key for the file's active_ref, \ ``NULL``\  to disable lockdep
    :type key: struct lock_class_key \*

.. _`__kernfs_create_file.description`:

Description
-----------

Returns the created node on success, \ :c:func:`ERR_PTR`\  value on error.

.. This file was automatic generated / don't edit.

