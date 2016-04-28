.. -*- coding: utf-8; mode: rst -*-

.. _API-srcu-barrier:

============
srcu_barrier
============

*man srcu_barrier(9)*

*4.6.0-rc5*

Wait until all in-flight ``call_srcu`` callbacks complete.


Synopsis
========

.. c:function:: void srcu_barrier( struct srcu_struct * sp )

Arguments
=========

``sp``
    srcu_struct on which to wait for in-flight callbacks.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
