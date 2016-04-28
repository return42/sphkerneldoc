.. -*- coding: utf-8; mode: rst -*-

.. _API-add-page-wait-queue:

===================
add_page_wait_queue
===================

*man add_page_wait_queue(9)*

*4.6.0-rc5*

Add an arbitrary waiter to a page's wait queue


Synopsis
========

.. c:function:: void add_page_wait_queue( struct page * page, wait_queue_t * waiter )

Arguments
=========

``page``
    Page defining the wait queue of interest

``waiter``
    Waiter to add to the queue


Description
===========

Add an arbitrary ``waiter`` to the wait queue for the nominated
``page``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
