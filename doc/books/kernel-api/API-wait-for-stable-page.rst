.. -*- coding: utf-8; mode: rst -*-

.. _API-wait-for-stable-page:

====================
wait_for_stable_page
====================

*man wait_for_stable_page(9)*

*4.6.0-rc5*

wait for writeback to finish, if necessary.


Synopsis
========

.. c:function:: void wait_for_stable_page( struct page * page )

Arguments
=========

``page``
    The page to wait on.


Description
===========

This function determines if the given page is related to a backing
device that requires page contents to be held stable during writeback.
If so, then it will wait for any pending writeback to complete.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
