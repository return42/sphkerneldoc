
.. _API-flush-delayed-work:

==================
flush_delayed_work
==================

*man flush_delayed_work(9)*

*4.6.0-rc1*

wait for a dwork to finish executing the last queueing


Synopsis
========

.. c:function:: bool flush_delayed_work( struct delayed_work * dwork )

Arguments
=========

``dwork``
    the delayed work to flush


Description
===========

Delayed timer is cancelled and the pending work is queued for immediate execution. Like ``flush_work``, this function only considers the last queueing instance of ``dwork``.


Return
======

``true`` if ``flush_work`` waited for the work to finish execution, ``false`` if it was already idle.
