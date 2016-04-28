.. -*- coding: utf-8; mode: rst -*-

.. _API-srcu-batches-completed:

======================
srcu_batches_completed
======================

*man srcu_batches_completed(9)*

*4.6.0-rc5*

return batches completed.


Synopsis
========

.. c:function:: unsigned long srcu_batches_completed( struct srcu_struct * sp )

Arguments
=========

``sp``
    srcu_struct on which to report batch completion.


Description
===========

Report the number of batches, correlated with, but not necessarily
precisely the same as, the number of grace periods that have elapsed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
