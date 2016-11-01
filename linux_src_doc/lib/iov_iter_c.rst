.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/iov_iter.c

.. _`import_iovec`:

import_iovec
============

.. c:function:: int import_iovec(int type, const struct iovec __user *uvector, unsigned nr_segs, unsigned fast_segs, struct iovec **iov, struct iov_iter *i)

    Copy an array of \ :c:type:`struct iovec <iovec>`\  from userspace into the kernel, check that it is valid, and initialize a new \ :c:type:`struct iov_iter <iov_iter>`\  iterator to access it.

    :param int type:
        One of \ ``READ``\  or \ ``WRITE``\ .

    :param const struct iovec __user \*uvector:
        Pointer to the userspace array.

    :param unsigned nr_segs:
        Number of elements in userspace array.

    :param unsigned fast_segs:
        Number of elements in \ ``iov``\ .

    :param struct iovec \*\*iov:
        (input and output parameter) Pointer to pointer to (usually small
        on-stack) kernel array.

    :param struct iov_iter \*i:
        Pointer to iterator that will be initialized on success.

.. _`import_iovec.description`:

Description
-----------

If the array pointed to by \*@iov is large enough to hold all \ ``nr_segs``\ ,
then this function places \ ``NULL``\  in \*@iov on return. Otherwise, a new
array will be allocated and the result placed in \*@iov. This means that
the caller may call \ :c:func:`kfree`\  on \*@iov regardless of whether the small
on-stack array was used or not (and regardless of whether this function
returns an error or not).

.. _`import_iovec.return`:

Return
------

0 on success or negative error code on error.

.. This file was automatic generated / don't edit.

