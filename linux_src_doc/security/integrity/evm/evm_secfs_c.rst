.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/evm/evm_secfs.c

.. _`evm_read_key`:

evm_read_key
============

.. c:function:: ssize_t evm_read_key(struct file *filp, char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`read`\  for <securityfs>/evm

    :param struct file \*filp:
        file pointer, not actually used

    :param char __user \*buf:
        where to put the result

    :param size_t count:
        maximum to send along

    :param loff_t \*ppos:
        where to start

.. _`evm_read_key.description`:

Description
-----------

Returns number of bytes read or error code, as appropriate

.. _`evm_write_key`:

evm_write_key
=============

.. c:function:: ssize_t evm_write_key(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for <securityfs>/evm

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start

.. _`evm_write_key.description`:

Description
-----------

Used to signal that key is on the kernel key ring.
- get the integrity hmac key from the kernel key ring
- create list of hmac protected extended attributes
Returns number of bytes written or error code, as appropriate

.. This file was automatic generated / don't edit.

