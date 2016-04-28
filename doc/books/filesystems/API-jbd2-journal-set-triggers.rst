.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-set-triggers:

=========================
jbd2_journal_set_triggers
=========================

*man jbd2_journal_set_triggers(9)*

*4.6.0-rc5*

Add triggers for commit writeout


Synopsis
========

.. c:function:: void jbd2_journal_set_triggers( struct buffer_head * bh, struct jbd2_buffer_trigger_type * type )

Arguments
=========

``bh``
    buffer to trigger on

``type``
    struct jbd2_buffer_trigger_type containing the trigger(s).


Description
===========

Set any triggers on this journal_head. This is always safe, because
triggers for a committing buffer will be saved off, and triggers for a
running transaction will match the buffer in that transaction.

Call with NULL to clear the triggers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
