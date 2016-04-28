.. -*- coding: utf-8; mode: rst -*-

.. _API-do-notify-parent-cldstop:

========================
do_notify_parent_cldstop
========================

*man do_notify_parent_cldstop(9)*

*4.6.0-rc5*

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

Notify ``tsk``'s parent that the stopped/continued state has changed. If
``for_ptracer`` is ``false``, ``tsk``'s group leader notifies to its
real parent. If ``true``, ``tsk`` reports to ``tsk``->parent which
should be the ptracer.


CONTEXT
=======

Must be called with tasklist_lock at least read locked.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
