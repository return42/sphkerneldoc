
.. _API-mpt-fault-reset-work:

====================
mpt_fault_reset_work
====================

*man mpt_fault_reset_work(9)*

*4.6.0-rc1*

work performed on workq after ioc fault


Synopsis
========

.. c:function:: void mpt_fault_reset_work( struct work_struct * work )

Arguments
=========

``work``
    input argument, used to derive ioc
