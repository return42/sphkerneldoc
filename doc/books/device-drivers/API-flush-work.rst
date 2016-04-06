
.. _API-flush-work:

==========
flush_work
==========

*man flush_work(9)*

*4.6.0-rc1*

wait for a work to finish executing the last queueing instance


Synopsis
========

.. c:function:: bool flush_work( struct work_struct * work )

Arguments
=========

``work``
    the work to flush


Description
===========

Wait until ``work`` has finished execution. ``work`` is guaranteed to be idle on return if it hasn't been requeued since flush started.


Return
======

``true`` if ``flush_work`` waited for the work to finish execution, ``false`` if it was already idle.
