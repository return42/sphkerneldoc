.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/kernfs/file.c

.. _`kernfs_fop_read`:

kernfs_fop_read
===============

.. c:function:: ssize_t kernfs_fop_read(struct file *file, char __user *user_buf, size_t count, loff_t *ppos)

    kernfs vfs read callback

    :param struct file \*file:
        file pointer

    :param char __user \*user_buf:
        data to write

    :param size_t count:
        number of bytes

    :param loff_t \*ppos:
        starting offset

.. _`kernfs_fop_write`:

kernfs_fop_write
================

.. c:function:: ssize_t kernfs_fop_write(struct file *file, const char __user *user_buf, size_t count, loff_t *ppos)

    kernfs vfs write callback

    :param struct file \*file:
        file pointer

    :param const char __user \*user_buf:
        data to write

    :param size_t count:
        number of bytes

    :param loff_t \*ppos:
        starting offset

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

    :param struct kernfs_node \*kn:
        target kernfs_node

    :param struct kernfs_open_file \*of:
        kernfs_open_file for this instance of open

.. _`kernfs_get_open_node.description`:

Description
-----------

If \ ``kn``\ ->attr.open exists, increment its reference count; otherwise,
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

    :param struct kernfs_node \*kn:
        target kernfs_nodet

    :param struct kernfs_open_file \*of:
        associated kernfs_open_file

.. _`kernfs_put_open_node.description`:

Description
-----------

Put \ ``kn``\ ->attr.open and unlink \ ``of``\  from the files list.  If
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

    :param struct kernfs_node \*kn:
        file to notify

.. _`kernfs_notify.description`:

Description
-----------

Notify \ ``kn``\  such that poll(2) on \ ``kn``\  wakes up.  Maybe be called from any
context.

.. _`__kernfs_create_file`:

\__kernfs_create_file
=====================

.. c:function:: struct kernfs_node *__kernfs_create_file(struct kernfs_node *parent, const char *name, umode_t mode, loff_t size, const struct kernfs_ops *ops, void *priv, const void *ns, struct lock_class_key *key)

    kernfs internal function to create a file

    :param struct kernfs_node \*parent:
        directory to create the file in

    :param const char \*name:
        name of the file

    :param umode_t mode:
        mode of the file

    :param loff_t size:
        size of the file

    :param const struct kernfs_ops \*ops:
        kernfs operations for the file

    :param void \*priv:
        private data for the file

    :param const void \*ns:
        optional namespace tag of the file

    :param struct lock_class_key \*key:
        lockdep key for the file's active_ref, \ ``NULL``\  to disable lockdep

.. _`__kernfs_create_file.description`:

Description
-----------

Returns the created node on success, \ :c:func:`ERR_PTR`\  value on error.

.. This file was automatic generated / don't edit.

