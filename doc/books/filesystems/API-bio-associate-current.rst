.. -*- coding: utf-8; mode: rst -*-

.. _API-bio-associate-current:

=====================
bio_associate_current
=====================

*man bio_associate_current(9)*

*4.6.0-rc5*

associate a bio with ``current``


Synopsis
========

.. c:function:: int bio_associate_current( struct bio * bio )

Arguments
=========

``bio``
    target bio


Description
===========

Associate ``bio`` with ``current`` if it hasn't been associated yet.
Block layer will treat ``bio`` as if it were issued by ``current`` no
matter which task actually issues it.

This function takes an extra reference of ``task``'s io_context and
blkcg which will be put when ``bio`` is released. The caller must own
``bio``, ensure ``current-``>io_context exists, and is responsible for
synchronizing calls to this function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
