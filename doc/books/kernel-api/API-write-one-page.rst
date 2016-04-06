
.. _API-write-one-page:

==============
write_one_page
==============

*man write_one_page(9)*

*4.6.0-rc1*

write out a single page and optionally wait on I/O


Synopsis
========

.. c:function:: int write_one_page( struct page * page, int wait )

Arguments
=========

``page``
    the page to write

``wait``
    if true, wait on writeout


Description
===========

The page must be locked by the caller and will be unlocked upon return.

``write_one_page`` returns a negative error code if I/O failed.
