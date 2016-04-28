.. -*- coding: utf-8; mode: rst -*-

.. _API-flush-delayed-work:

==================
flush_delayed_work
==================

*man flush_delayed_work(9)*

*4.6.0-rc5*

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

Delayed timer is cancelled and the pending work is queued for immediate
execution. Like ``flush_work``, this function only considers the last
queueing instance of ``dwork``.


Return
======

``true`` if ``flush_work`` waited for the work to finish execution,
``false`` if it was already idle.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
