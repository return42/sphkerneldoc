.. -*- coding: utf-8; mode: rst -*-

.. _API-bio-add-page:

============
bio_add_page
============

*man bio_add_page(9)*

*4.6.0-rc5*

attempt to add page to bio


Synopsis
========

.. c:function:: int bio_add_page( struct bio * bio, struct page * page, unsigned int len, unsigned int offset )

Arguments
=========

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

Attempt to add a page to the bio_vec maplist. This will only fail if
either bio->bi_vcnt == bio->bi_max_vecs or it's a cloned bio.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
