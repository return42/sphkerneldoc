
.. _API-get-futex-key:

=============
get_futex_key
=============

*man get_futex_key(9)*

*4.6.0-rc1*

Get parameters which are the keys for a futex


Synopsis
========

.. c:function:: int get_futex_key( u32 __user * uaddr, int fshared, union futex_key * key, int rw )

Arguments
=========

``uaddr``
    virtual address of the futex

``fshared``
    0 for a PROCESS_PRIVATE futex, 1 for PROCESS_SHARED

``key``
    address where result is stored.

``rw``
    mapping needs to be read/write (values: VERIFY_READ, VERIFY_WRITE)


Return
======

a negative error code or 0

The key words are stored in ⋆key on success.

For shared mappings, it's (page->index, file_inode(vma->vm_file), offset_within_page). For private mappings, it's (uaddr, current->mm). We can usually work out the index
without swapping in the page.

``lock_page`` might sleep, the caller should not hold a spinlock.
