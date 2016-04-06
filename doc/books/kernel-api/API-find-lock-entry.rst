
.. _API-find-lock-entry:

===============
find_lock_entry
===============

*man find_lock_entry(9)*

*4.6.0-rc1*

locate, pin and lock a page cache entry


Synopsis
========

.. c:function:: struct page ⋆ find_lock_entry( struct address_space * mapping, pgoff_t offset )

Arguments
=========

``mapping``
    the address_space to search

``offset``
    the page cache index


Description
===========

Looks up the page cache slot at ``mapping`` & ``offset``. If there is a page cache page, it is returned locked and with an increased refcount.

If the slot holds a shadow entry of a previously evicted page, or a swap entry from shmem/tmpfs, it is returned.

Otherwise, ``NULL`` is returned.

``find_lock_entry`` may sleep.
