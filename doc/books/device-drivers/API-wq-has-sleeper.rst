.. -*- coding: utf-8; mode: rst -*-

.. _API-wq-has-sleeper:

==============
wq_has_sleeper
==============

*man wq_has_sleeper(9)*

*4.6.0-rc5*

check if there are any waiting processes


Synopsis
========

.. c:function:: bool wq_has_sleeper( wait_queue_head_t * wq )

Arguments
=========

``wq``
    wait queue head


Description
===========

Returns true if wq has waiting processes

Please refer to the comment for waitqueue_active.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
