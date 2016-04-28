.. -*- coding: utf-8; mode: rst -*-

.. _API-bio-uncopy-user:

===============
bio_uncopy_user
===============

*man bio_uncopy_user(9)*

*4.6.0-rc5*

finish previously mapped bio


Synopsis
========

.. c:function:: int bio_uncopy_user( struct bio * bio )

Arguments
=========

``bio``
    bio being terminated


Description
===========

Free pages allocated from ``bio_copy_user_iov`` and write back data to
user space in case of a read.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
