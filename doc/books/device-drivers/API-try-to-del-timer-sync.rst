
.. _API-try-to-del-timer-sync:

=====================
try_to_del_timer_sync
=====================

*man try_to_del_timer_sync(9)*

*4.6.0-rc1*

Try to deactivate a timer


Synopsis
========

.. c:function:: int try_to_del_timer_sync( struct timer_list * timer )

Arguments
=========

``timer``
    timer do del


Description
===========

This function tries to deactivate a timer. Upon successful (ret >= 0) exit the timer is not queued and the handler is not running on any CPU.
