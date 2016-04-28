.. -*- coding: utf-8; mode: rst -*-

.. _API---lock-page:

===========
__lock_page
===========

*man __lock_page(9)*

*4.6.0-rc5*

get a lock on the page, assuming we need to sleep to get it


Synopsis
========

.. c:function:: void __lock_page( struct page * page )

Arguments
=========

``page``
    the page to lock


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
