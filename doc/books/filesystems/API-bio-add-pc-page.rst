.. -*- coding: utf-8; mode: rst -*-

.. _API-bio-add-pc-page:

===============
bio_add_pc_page
===============

*man bio_add_pc_page(9)*

*4.6.0-rc5*

attempt to add page to bio


Synopsis
========

.. c:function:: int bio_add_pc_page( struct request_queue * q, struct bio * bio, struct page * page, unsigned int len, unsigned int offset )

Arguments
=========

``q``
    the target queue

``bio``
    destination bio

``page``
    page to add

``len``
    vec entry length

``offset``
    vec entry offset


Description
===========

Attempt to add a page to the bio_vec maplist. This can fail for a
number of reasons, such as the bio being full or target block device
limitations. The target block device must allow bio's up to PAGE_SIZE,
so it is always possible to add a single page to an empty bio.

This should only be used by REQ_PC bios.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
