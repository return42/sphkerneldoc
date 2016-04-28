.. -*- coding: utf-8; mode: rst -*-

.. _API-bio-chain:

=========
bio_chain
=========

*man bio_chain(9)*

*4.6.0-rc5*

chain bio completions


Synopsis
========

.. c:function:: void bio_chain( struct bio * bio, struct bio * parent )

Arguments
=========

``bio``
    the target bio

``parent``
    the ``bio``'s parent bio


Description
===========

The caller won't have a bi_end_io called when ``bio`` completes -
instead, ``parent``'s bi_end_io won't be called until both ``parent``
and ``bio`` have completed; the chained bio will also be freed when it
completes.

The caller must not set bi_private or bi_end_io in ``bio``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
