.. -*- coding: utf-8; mode: rst -*-

.. _API-bioset-create:

=============
bioset_create
=============

*man bioset_create(9)*

*4.6.0-rc5*

Create a bio_set


Synopsis
========

.. c:function:: struct bio_set * bioset_create( unsigned int pool_size, unsigned int front_pad )

Arguments
=========

``pool_size``
    Number of bio and bio_vecs to cache in the mempool

``front_pad``
    Number of bytes to allocate in front of the returned bio


Description
===========

Set up a bio_set to be used with ``bio_alloc_bioset``. Allows the
caller to ask for a number of bytes to be allocated in front of the bio.
Front pad allocation is useful for embedding the bio inside another
structure, to avoid allocating extra data to go with the bio. Note that
the bio must be embedded at the END of that structure always, or things
will break badly.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
