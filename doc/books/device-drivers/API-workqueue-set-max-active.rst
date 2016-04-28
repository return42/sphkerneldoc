.. -*- coding: utf-8; mode: rst -*-

.. _API-workqueue-set-max-active:

========================
workqueue_set_max_active
========================

*man workqueue_set_max_active(9)*

*4.6.0-rc5*

adjust max_active of a workqueue


Synopsis
========

.. c:function:: void workqueue_set_max_active( struct workqueue_struct * wq, int max_active )

Arguments
=========

``wq``
    target workqueue

``max_active``
    new max_active value.


Description
===========

Set max_active of ``wq`` to ``max_active``.


CONTEXT
=======

Don't call from IRQ context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
