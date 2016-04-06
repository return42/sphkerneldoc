
.. _API-destroy-workqueue:

=================
destroy_workqueue
=================

*man destroy_workqueue(9)*

*4.6.0-rc1*

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

Safely destroy a workqueue. All work currently pending will be done first.
