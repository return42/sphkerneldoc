.. -*- coding: utf-8; mode: rst -*-

.. _API-bioset-create-nobvec:

====================
bioset_create_nobvec
====================

*man bioset_create_nobvec(9)*

*4.6.0-rc5*

Create a bio_set without bio_vec mempool


Synopsis
========

.. c:function:: struct bio_set * bioset_create_nobvec( unsigned int pool_size, unsigned int front_pad )

Arguments
=========

``pool_size``
    Number of bio to cache in the mempool

``front_pad``
    Number of bytes to allocate in front of the returned bio


Description
===========

Same functionality as ``bioset_create`` except that mempool is not
created for bio_vecs. Saving some memory for ``bio_clone_fast`` users.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
