.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-unlock-updates:

===========================
jbd2_journal_unlock_updates
===========================

*man jbd2_journal_unlock_updates(9)*

*4.6.0-rc5*

release barrier


Synopsis
========

.. c:function:: void jbd2_journal_unlock_updates( journal_t * journal )

Arguments
=========

``journal``
    Journal to release the barrier on.


Description
===========

Release a transaction barrier obtained with
``jbd2_journal_lock_updates``.

Should be called without the journal lock held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
