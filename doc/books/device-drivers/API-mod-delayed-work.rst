.. -*- coding: utf-8; mode: rst -*-

.. _API-mod-delayed-work:

================
mod_delayed_work
================

*man mod_delayed_work(9)*

*4.6.0-rc5*

modify delay of or queue a delayed work


Synopsis
========

.. c:function:: bool mod_delayed_work( struct workqueue_struct * wq, struct delayed_work * dwork, unsigned long delay )

Arguments
=========

``wq``
    workqueue to use

``dwork``
    work to queue

``delay``
    number of jiffies to wait before queueing


Description
===========

``mod_delayed_work_on`` on local CPU.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
