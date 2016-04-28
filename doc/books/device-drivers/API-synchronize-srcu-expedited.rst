.. -*- coding: utf-8; mode: rst -*-

.. _API-synchronize-srcu-expedited:

==========================
synchronize_srcu_expedited
==========================

*man synchronize_srcu_expedited(9)*

*4.6.0-rc5*

Brute-force SRCU grace period


Synopsis
========

.. c:function:: void synchronize_srcu_expedited( struct srcu_struct * sp )

Arguments
=========

``sp``
    srcu_struct with which to synchronize.


Description
===========

Wait for an SRCU grace period to elapse, but be more aggressive about
spinning rather than blocking when waiting.

Note that ``synchronize_srcu_expedited`` has the same deadlock and
memory-ordering properties as does ``synchronize_srcu``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
