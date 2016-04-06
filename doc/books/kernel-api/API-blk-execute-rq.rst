
.. _API-blk-execute-rq:

==============
blk_execute_rq
==============

*man blk_execute_rq(9)*

*4.6.0-rc1*

insert a request into queue for execution


Synopsis
========

.. c:function:: int blk_execute_rq( struct request_queue * q, struct gendisk * bd_disk, struct request * rq, int at_head )

Arguments
=========

``q``
    queue to insert the request in

``bd_disk``
    matching gendisk

``rq``
    request to insert

``at_head``
    insert request at head or tail of queue


Description
===========

Insert a fully prepared request at the back of the I/O scheduler queue for execution and wait for completion.
