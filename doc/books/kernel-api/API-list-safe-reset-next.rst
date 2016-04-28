.. -*- coding: utf-8; mode: rst -*-

.. _API-list-safe-reset-next:

====================
list_safe_reset_next
====================

*man list_safe_reset_next(9)*

*4.6.0-rc5*

reset a stale list_for_each_entry_safe loop


Synopsis
========

.. c:function:: list_safe_reset_next( pos, n, member )

Arguments
=========

``pos``
    the loop cursor used in the list_for_each_entry_safe loop

``n``
    temporary storage used in list_for_each_entry_safe

``member``
    the name of the list_head within the struct.


Description
===========

list_safe_reset_next is not safe to use in general if the list may be
modified concurrently (eg. the lock is dropped in the loop body). An
exception to this is if the cursor element (pos) is pinned in the list,
and list_safe_reset_next is called after re-taking the lock and
before completing the current iteration of the loop body.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
