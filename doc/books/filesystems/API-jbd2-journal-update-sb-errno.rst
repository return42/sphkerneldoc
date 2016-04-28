.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-update-sb-errno:

============================
jbd2_journal_update_sb_errno
============================

*man jbd2_journal_update_sb_errno(9)*

*4.6.0-rc5*

Update error in the journal.


Synopsis
========

.. c:function:: void jbd2_journal_update_sb_errno( journal_t * journal )

Arguments
=========

``journal``
    The journal to update.


Description
===========

Update a journal's errno. Write updated superblock to disk waiting for
IO to complete.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
