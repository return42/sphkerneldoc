.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-rq-unprep-clone:

===================
blk_rq_unprep_clone
===================

*man blk_rq_unprep_clone(9)*

*4.6.0-rc5*

Helper function to free all bios in a cloned request


Synopsis
========

.. c:function:: void blk_rq_unprep_clone( struct request * rq )

Arguments
=========

``rq``
    the clone request to be cleaned up


Description
===========

Free all bios in ``rq`` for a cloned request.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
