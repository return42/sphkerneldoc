.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/securityfs_if.c

.. _`tomoyo_check_task_acl`:

tomoyo_check_task_acl
=====================

.. c:function:: bool tomoyo_check_task_acl(struct tomoyo_request_info *r, const struct tomoyo_acl_info *ptr)

    Check permission for task operation.

    :param struct tomoyo_request_info \*r:
        Pointer to "struct tomoyo_request_info".

    :param const struct tomoyo_acl_info \*ptr:
        Pointer to "struct tomoyo_acl_info".

.. _`tomoyo_check_task_acl.description`:

Description
-----------

Returns true if granted, false otherwise.

.. _`tomoyo_write_self`:

tomoyo_write_self
=================

.. c:function:: ssize_t tomoyo_write_self(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /sys/kernel/security/tomoyo/self_domain interface.

    :param struct file \*file:
        Pointer to "struct file".

    :param const char __user \*buf:
        Domainname to transit to.

    :param size_t count:
        Size of \ ``buf``\ .

    :param loff_t \*ppos:
        Unused.

.. _`tomoyo_write_self.description`:

Description
-----------

Returns \ ``count``\  on success, negative value otherwise.

If domain transition was permitted but the domain transition failed, this
function returns error rather than terminating current thread with SIGKILL.

.. _`tomoyo_read_self`:

tomoyo_read_self
================

.. c:function:: ssize_t tomoyo_read_self(struct file *file, char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`read`\  for /sys/kernel/security/tomoyo/self_domain interface.

    :param struct file \*file:
        Pointer to "struct file".

    :param char __user \*buf:
        Domainname which current thread belongs to.

    :param size_t count:
        Size of \ ``buf``\ .

    :param loff_t \*ppos:
        Bytes read by now.

.. _`tomoyo_read_self.description`:

Description
-----------

Returns read size on success, negative value otherwise.

.. _`tomoyo_open`:

tomoyo_open
===========

.. c:function:: int tomoyo_open(struct inode *inode, struct file *file)

    \ :c:func:`open`\  for /sys/kernel/security/tomoyo/ interface.

    :param struct inode \*inode:
        Pointer to "struct inode".

    :param struct file \*file:
        Pointer to "struct file".

.. _`tomoyo_open.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_release`:

tomoyo_release
==============

.. c:function:: int tomoyo_release(struct inode *inode, struct file *file)

    \ :c:func:`close`\  for /sys/kernel/security/tomoyo/ interface.

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*file:
        Pointer to "struct file".

.. _`tomoyo_poll`:

tomoyo_poll
===========

.. c:function:: __poll_t tomoyo_poll(struct file *file, poll_table *wait)

    \ :c:func:`poll`\  for /sys/kernel/security/tomoyo/ interface.

    :param struct file \*file:
        Pointer to "struct file".

    :param poll_table \*wait:
        Pointer to "poll_table". Maybe NULL.

.. _`tomoyo_poll.description`:

Description
-----------

Returns EPOLLIN \| EPOLLRDNORM \| EPOLLOUT \| EPOLLWRNORM if ready to read/write,
EPOLLOUT \| EPOLLWRNORM otherwise.

.. _`tomoyo_read`:

tomoyo_read
===========

.. c:function:: ssize_t tomoyo_read(struct file *file, char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`read`\  for /sys/kernel/security/tomoyo/ interface.

    :param struct file \*file:
        Pointer to "struct file".

    :param char __user \*buf:
        Pointer to buffer.

    :param size_t count:
        Size of \ ``buf``\ .

    :param loff_t \*ppos:
        Unused.

.. _`tomoyo_read.description`:

Description
-----------

Returns bytes read on success, negative value otherwise.

.. _`tomoyo_write`:

tomoyo_write
============

.. c:function:: ssize_t tomoyo_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /sys/kernel/security/tomoyo/ interface.

    :param struct file \*file:
        Pointer to "struct file".

    :param const char __user \*buf:
        Pointer to buffer.

    :param size_t count:
        Size of \ ``buf``\ .

    :param loff_t \*ppos:
        Unused.

.. _`tomoyo_write.description`:

Description
-----------

Returns \ ``count``\  on success, negative value otherwise.

.. _`tomoyo_create_entry`:

tomoyo_create_entry
===================

.. c:function:: void tomoyo_create_entry(const char *name, const umode_t mode, struct dentry *parent, const u8 key)

    Create interface files under /sys/kernel/security/tomoyo/ directory.

    :param const char \*name:
        The name of the interface file.

    :param const umode_t mode:
        The permission of the interface file.

    :param struct dentry \*parent:
        The parent directory.

    :param const u8 key:
        Type of interface.

.. _`tomoyo_create_entry.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_initerface_init`:

tomoyo_initerface_init
======================

.. c:function:: int tomoyo_initerface_init( void)

    Initialize /sys/kernel/security/tomoyo/ interface.

    :param  void:
        no arguments

.. _`tomoyo_initerface_init.description`:

Description
-----------

Returns 0.

.. This file was automatic generated / don't edit.

