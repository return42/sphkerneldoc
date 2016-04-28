.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2--journal-restart:

=====================
jbd2__journal_restart
=====================

*man jbd2__journal_restart(9)*

*4.6.0-rc5*

restart a handle .


Synopsis
========

.. c:function:: int jbd2__journal_restart( handle_t * handle, int nblocks, gfp_t gfp_mask )

Arguments
=========

``handle``
    handle to restart

``nblocks``
    nr credits requested

``gfp_mask``
    -- undescribed --


Description
===========

Restart a handle for a multi-transaction filesystem operation.

If the ``jbd2_journal_extend`` call above fails to grant new buffer
credits to a running handle, a call to jbd2_journal_restart will
commit the handle's transaction so far and reattach the handle to a new
transaction capabable of guaranteeing the requested number of credits.
We preserve reserved handle if there's any attached to the passed in
handle.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
