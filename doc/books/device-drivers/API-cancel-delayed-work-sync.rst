
.. _API-cancel-delayed-work-sync:

========================
cancel_delayed_work_sync
========================

*man cancel_delayed_work_sync(9)*

*4.6.0-rc1*

cancel a delayed work and wait for it to finish


Synopsis
========

.. c:function:: bool cancel_delayed_work_sync( struct delayed_work * dwork )

Arguments
=========

``dwork``
    the delayed work cancel


Description
===========

This is ``cancel_work_sync`` for delayed works.


Return
======

``true`` if ``dwork`` was pending, ``false`` otherwise.
