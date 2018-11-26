.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/evm/evm_secfs.c

.. _`evm_read_key`:

evm_read_key
============

.. c:function:: ssize_t evm_read_key(struct file *filp, char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`read`\  for <securityfs>/evm

    :param filp:
        file pointer, not actually used
    :type filp: struct file \*

    :param buf:
        where to put the result
    :type buf: char __user \*

    :param count:
        maximum to send along
    :type count: size_t

    :param ppos:
        where to start
    :type ppos: loff_t \*

.. _`evm_read_key.description`:

Description
-----------

Returns number of bytes read or error code, as appropriate

.. _`evm_write_key`:

evm_write_key
=============

.. c:function:: ssize_t evm_write_key(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for <securityfs>/evm

    :param file:
        file pointer, not actually used
    :type file: struct file \*

    :param buf:
        where to get the data from
    :type buf: const char __user \*

    :param count:
        bytes sent
    :type count: size_t

    :param ppos:
        where to start
    :type ppos: loff_t \*

.. _`evm_write_key.description`:

Description
-----------

Used to signal that key is on the kernel key ring.
- get the integrity hmac key from the kernel key ring
- create list of hmac protected extended attributes
Returns number of bytes written or error code, as appropriate

.. _`evm_read_xattrs`:

evm_read_xattrs
===============

.. c:function:: ssize_t evm_read_xattrs(struct file *filp, char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`read`\  for <securityfs>/evm_xattrs

    :param filp:
        file pointer, not actually used
    :type filp: struct file \*

    :param buf:
        where to put the result
    :type buf: char __user \*

    :param count:
        maximum to send along
    :type count: size_t

    :param ppos:
        where to start
    :type ppos: loff_t \*

.. _`evm_read_xattrs.description`:

Description
-----------

Returns number of bytes read or error code, as appropriate

.. _`evm_write_xattrs`:

evm_write_xattrs
================

.. c:function:: ssize_t evm_write_xattrs(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for <securityfs>/evm_xattrs

    :param file:
        file pointer, not actually used
    :type file: struct file \*

    :param buf:
        where to get the data from
    :type buf: const char __user \*

    :param count:
        bytes sent
    :type count: size_t

    :param ppos:
        where to start
    :type ppos: loff_t \*

.. _`evm_write_xattrs.description`:

Description
-----------

Returns number of bytes written or error code, as appropriate

.. This file was automatic generated / don't edit.

