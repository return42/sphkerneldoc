.. -*- coding: utf-8; mode: rst -*-

.. _API-cancel-delayed-work:

===================
cancel_delayed_work
===================

*man cancel_delayed_work(9)*

*4.6.0-rc5*

cancel a delayed work


Synopsis
========

.. c:function:: bool cancel_delayed_work( struct delayed_work * dwork )

Arguments
=========

``dwork``
    delayed_work to cancel


Description
===========

Kill off a pending delayed_work.


Return
======

``true`` if ``dwork`` was pending and canceled; ``false`` if it wasn't
pending.


Note
====

The work callback function may still be running on return, unless it
returns ``true`` and the work doesn't re-arm itself. Explicitly flush or
use ``cancel_delayed_work_sync`` to wait on it.

This function is safe to call from any context including IRQ handler.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
