
.. _API-blk-end-request-cur:

===================
blk_end_request_cur
===================

*man blk_end_request_cur(9)*

*4.6.0-rc1*

Helper function to finish the current request chunk.


Synopsis
========

.. c:function:: bool blk_end_request_cur( struct request * rq, int error )

Arguments
=========

``rq``
    the request to finish the current chunk for

``error``
    ``0`` for success, < ``0`` for error


Description
===========

Complete the current consecutively mapped chunk from ``rq``.


Return
======

``false`` - we are done with this request ``true`` - still buffers pending for this request
