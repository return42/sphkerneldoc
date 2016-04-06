
.. _API-workqueue-set-max-active:

========================
workqueue_set_max_active
========================

*man workqueue_set_max_active(9)*

*4.6.0-rc1*

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
