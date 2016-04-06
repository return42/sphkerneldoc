
.. _API---lock-page:

===========
__lock_page
===========

*man __lock_page(9)*

*4.6.0-rc1*

get a lock on the page, assuming we need to sleep to get it


Synopsis
========

.. c:function:: void __lock_page( struct page * page )

Arguments
=========

``page``
    the page to lock
