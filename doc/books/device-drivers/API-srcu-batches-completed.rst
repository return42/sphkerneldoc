
.. _API-srcu-batches-completed:

======================
srcu_batches_completed
======================

*man srcu_batches_completed(9)*

*4.6.0-rc1*

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

Report the number of batches, correlated with, but not necessarily precisely the same as, the number of grace periods that have elapsed.
