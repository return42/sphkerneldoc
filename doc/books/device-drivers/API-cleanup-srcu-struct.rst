.. -*- coding: utf-8; mode: rst -*-

.. _API-cleanup-srcu-struct:

===================
cleanup_srcu_struct
===================

*man cleanup_srcu_struct(9)*

*4.6.0-rc5*

deconstruct a sleep-RCU structure


Synopsis
========

.. c:function:: void cleanup_srcu_struct( struct srcu_struct * sp )

Arguments
=========

``sp``
    structure to clean up.


Description
===========

Must invoke this after you are finished using a given srcu_struct that
was initialized via ``init_srcu_struct``, else you leak memory.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
