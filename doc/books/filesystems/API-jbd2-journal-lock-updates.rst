.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-lock-updates:

=========================
jbd2_journal_lock_updates
=========================

*man jbd2_journal_lock_updates(9)*

*4.6.0-rc5*

establish a transaction barrier.


Synopsis
========

.. c:function:: void jbd2_journal_lock_updates( journal_t * journal )

Arguments
=========

``journal``
    Journal to establish a barrier on.


Description
===========

This locks out any further updates from being started, and blocks until
all existing updates have completed, returning only once the journal is
in a quiescent state with no updates running.

The journal lock should not be held on entry.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
