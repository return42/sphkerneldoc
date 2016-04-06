
.. _API---blk-end-request-cur:

=====================
__blk_end_request_cur
=====================

*man __blk_end_request_cur(9)*

*4.6.0-rc1*

Helper function to finish the current request chunk.


Synopsis
========

.. c:function:: bool __blk_end_request_cur( struct request * rq, int error )

Arguments
=========

``rq``
    the request to finish the current chunk for

``error``
    ``0`` for success, < ``0`` for error


Description
===========

Complete the current consecutively mapped chunk from ``rq``. Must be called with queue lock held.


Return
======

``false`` - we are done with this request ``true`` - still buffers pending for this request
