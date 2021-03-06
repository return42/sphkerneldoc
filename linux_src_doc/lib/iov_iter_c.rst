.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/iov_iter.c

.. _`_copy_to_iter_mcsafe`:

\_copy_to_iter_mcsafe
=====================

.. c:function:: size_t _copy_to_iter_mcsafe(const void *addr, size_t bytes, struct iov_iter *i)

    copy to user with source-read error exception handling

    :param addr:
        source kernel address
    :type addr: const void \*

    :param bytes:
        total transfer length
    :type bytes: size_t

    :param i:
        *undescribed*
    :type i: struct iov_iter \*

.. _`_copy_to_iter_mcsafe.description`:

Description
-----------

The pmem driver arranges for filesystem-dax to use this facility via
\ :c:func:`dax_copy_to_iter`\  for protecting read/write to persistent memory.
Unless / until an architecture can guarantee identical performance
between \_copy_to_iter_mcsafe() and \_copy_to_iter() it would be a
performance regression to switch more users to the mcsafe version.

Otherwise, the main differences between this and typical \_copy_to_iter().

\* Typical tail/residue handling after a fault retries the copy
byte-by-byte until the fault happens again. Re-triggering machine
checks is potentially fatal so the implementation uses source
alignment and poison alignment assumptions to avoid re-triggering
hardware exceptions.

\* ITER_KVEC, ITER_PIPE, and ITER_BVEC can return short copies.
Compare to \ :c:func:`copy_to_iter`\  where only ITER_IOVEC attempts might return
a short copy.

See MCSAFE_TEST for self-test.

.. _`_copy_from_iter_flushcache`:

\_copy_from_iter_flushcache
===========================

.. c:function:: size_t _copy_from_iter_flushcache(void *addr, size_t bytes, struct iov_iter *i)

    write destination through cpu cache

    :param addr:
        destination kernel address
    :type addr: void \*

    :param bytes:
        total transfer length
    :type bytes: size_t

    :param i:
        *undescribed*
    :type i: struct iov_iter \*

.. _`_copy_from_iter_flushcache.description`:

Description
-----------

The pmem driver arranges for filesystem-dax to use this facility via
\ :c:func:`dax_copy_from_iter`\  for ensuring that writes to persistent memory
are flushed through the CPU cache. It is differentiated from
\_copy_from_iter_nocache() in that guarantees all data is flushed for
all iterator types. The \_copy_from_iter_nocache() only attempts to
bypass the cache for the ITER_IOVEC case, and on some archs may use
instructions that strand dirty-data in the cache.

.. _`iov_iter_discard`:

iov_iter_discard
================

.. c:function:: void iov_iter_discard(struct iov_iter *i, unsigned int direction, size_t count)

    Initialise an I/O iterator that discards data

    :param i:
        The iterator to initialise.
    :type i: struct iov_iter \*

    :param direction:
        The direction of the transfer.
    :type direction: unsigned int

    :param count:
        The size of the I/O buffer in bytes.
    :type count: size_t

.. _`iov_iter_discard.description`:

Description
-----------

Set up an I/O iterator that just discards everything that's written to it.
It's only available as a READ iterator.

.. _`import_iovec`:

import_iovec
============

.. c:function:: int import_iovec(int type, const struct iovec __user *uvector, unsigned nr_segs, unsigned fast_segs, struct iovec **iov, struct iov_iter *i)

    Copy an array of \ :c:type:`struct iovec <iovec>`\  from userspace into the kernel, check that it is valid, and initialize a new \ :c:type:`struct iov_iter <iov_iter>`\  iterator to access it.

    :param type:
        One of \ ``READ``\  or \ ``WRITE``\ .
    :type type: int

    :param uvector:
        Pointer to the userspace array.
    :type uvector: const struct iovec __user \*

    :param nr_segs:
        Number of elements in userspace array.
    :type nr_segs: unsigned

    :param fast_segs:
        Number of elements in \ ``iov``\ .
    :type fast_segs: unsigned

    :param iov:
        (input and output parameter) Pointer to pointer to (usually small
        on-stack) kernel array.
    :type iov: struct iovec \*\*

    :param i:
        Pointer to iterator that will be initialized on success.
    :type i: struct iov_iter \*

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

