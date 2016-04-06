
.. _API-do-notify-parent-cldstop:

========================
do_notify_parent_cldstop
========================

*man do_notify_parent_cldstop(9)*

*4.6.0-rc1*

notify parent of stopped/continued state change


Synopsis
========

.. c:function:: void do_notify_parent_cldstop( struct task_struct * tsk, bool for_ptracer, int why )

Arguments
=========

``tsk``
    task reporting the state change

``for_ptracer``
    the notification is for ptracer

``why``
    CLD_{CONTINUED|STOPPED|TRAPPED} to report


Description
===========

Notify ``tsk``'s parent that the stopped/continued state has changed. If ``for_ptracer`` is ``false``, ``tsk``'s group leader notifies to its real parent. If ``true``, ``tsk``
reports to ``tsk``->parent which should be the ptracer.


CONTEXT
=======

Must be called with tasklist_lock at least read locked.
