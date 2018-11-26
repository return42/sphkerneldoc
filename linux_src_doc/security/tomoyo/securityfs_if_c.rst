.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/securityfs_if.c

.. _`tomoyo_check_task_acl`:

tomoyo_check_task_acl
=====================

.. c:function:: bool tomoyo_check_task_acl(struct tomoyo_request_info *r, const struct tomoyo_acl_info *ptr)

    Check permission for task operation.

    :param r:
        Pointer to "struct tomoyo_request_info".
    :type r: struct tomoyo_request_info \*

    :param ptr:
        Pointer to "struct tomoyo_acl_info".
    :type ptr: const struct tomoyo_acl_info \*

.. _`tomoyo_check_task_acl.description`:

Description
-----------

Returns true if granted, false otherwise.

.. _`tomoyo_write_self`:

tomoyo_write_self
=================

.. c:function:: ssize_t tomoyo_write_self(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /sys/kernel/security/tomoyo/self_domain interface.

    :param file:
        Pointer to "struct file".
    :type file: struct file \*

    :param buf:
        Domainname to transit to.
    :type buf: const char __user \*

    :param count:
        Size of \ ``buf``\ .
    :type count: size_t

    :param ppos:
        Unused.
    :type ppos: loff_t \*

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

    :param file:
        Pointer to "struct file".
    :type file: struct file \*

    :param buf:
        Domainname which current thread belongs to.
    :type buf: char __user \*

    :param count:
        Size of \ ``buf``\ .
    :type count: size_t

    :param ppos:
        Bytes read by now.
    :type ppos: loff_t \*

.. _`tomoyo_read_self.description`:

Description
-----------

Returns read size on success, negative value otherwise.

.. _`tomoyo_open`:

tomoyo_open
===========

.. c:function:: int tomoyo_open(struct inode *inode, struct file *file)

    \ :c:func:`open`\  for /sys/kernel/security/tomoyo/ interface.

    :param inode:
        Pointer to "struct inode".
    :type inode: struct inode \*

    :param file:
        Pointer to "struct file".
    :type file: struct file \*

.. _`tomoyo_open.description`:

Description
-----------

Returns 0 on success, negative value otherwise.

.. _`tomoyo_release`:

tomoyo_release
==============

.. c:function:: int tomoyo_release(struct inode *inode, struct file *file)

    \ :c:func:`close`\  for /sys/kernel/security/tomoyo/ interface.

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param file:
        Pointer to "struct file".
    :type file: struct file \*

.. _`tomoyo_poll`:

tomoyo_poll
===========

.. c:function:: __poll_t tomoyo_poll(struct file *file, poll_table *wait)

    \ :c:func:`poll`\  for /sys/kernel/security/tomoyo/ interface.

    :param file:
        Pointer to "struct file".
    :type file: struct file \*

    :param wait:
        Pointer to "poll_table". Maybe NULL.
    :type wait: poll_table \*

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

    :param file:
        Pointer to "struct file".
    :type file: struct file \*

    :param buf:
        Pointer to buffer.
    :type buf: char __user \*

    :param count:
        Size of \ ``buf``\ .
    :type count: size_t

    :param ppos:
        Unused.
    :type ppos: loff_t \*

.. _`tomoyo_read.description`:

Description
-----------

Returns bytes read on success, negative value otherwise.

.. _`tomoyo_write`:

tomoyo_write
============

.. c:function:: ssize_t tomoyo_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /sys/kernel/security/tomoyo/ interface.

    :param file:
        Pointer to "struct file".
    :type file: struct file \*

    :param buf:
        Pointer to buffer.
    :type buf: const char __user \*

    :param count:
        Size of \ ``buf``\ .
    :type count: size_t

    :param ppos:
        Unused.
    :type ppos: loff_t \*

.. _`tomoyo_write.description`:

Description
-----------

Returns \ ``count``\  on success, negative value otherwise.

.. _`tomoyo_create_entry`:

tomoyo_create_entry
===================

.. c:function:: void tomoyo_create_entry(const char *name, const umode_t mode, struct dentry *parent, const u8 key)

    Create interface files under /sys/kernel/security/tomoyo/ directory.

    :param name:
        The name of the interface file.
    :type name: const char \*

    :param mode:
        The permission of the interface file.
    :type mode: const umode_t

    :param parent:
        The parent directory.
    :type parent: struct dentry \*

    :param key:
        Type of interface.
    :type key: const u8

.. _`tomoyo_create_entry.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_initerface_init`:

tomoyo_initerface_init
======================

.. c:function:: int tomoyo_initerface_init( void)

    Initialize /sys/kernel/security/tomoyo/ interface.

    :param void:
        no arguments
    :type void: 

.. _`tomoyo_initerface_init.description`:

Description
-----------

Returns 0.

.. This file was automatic generated / don't edit.

