.. -*- coding: utf-8; mode: rst -*-

.. _API-destroy-workqueue:

=================
destroy_workqueue
=================

*man destroy_workqueue(9)*

*4.6.0-rc5*

safely terminate a workqueue


Synopsis
========

.. c:function:: void destroy_workqueue( struct workqueue_struct * wq )

Arguments
=========

``wq``
    target workqueue


Description
===========

Safely destroy a workqueue. All work currently pending will be done
first.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
