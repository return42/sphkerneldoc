.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-execute-rq-nowait:

=====================
blk_execute_rq_nowait
=====================

*man blk_execute_rq_nowait(9)*

*4.6.0-rc5*

insert a request into queue for execution


Synopsis
========

.. c:function:: void blk_execute_rq_nowait( struct request_queue * q, struct gendisk * bd_disk, struct request * rq, int at_head, rq_end_io_fn * done )

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

``done``
    I/O completion handler


Description
===========

Insert a fully prepared request at the back of the I/O scheduler queue
for execution. Don't wait for completion.


Note
====

This function will invoke ``done`` directly if the queue is dead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
