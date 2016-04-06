
.. _API-blk-rq-unprep-clone:

===================
blk_rq_unprep_clone
===================

*man blk_rq_unprep_clone(9)*

*4.6.0-rc1*

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
