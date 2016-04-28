.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-load:

=================
jbd2_journal_load
=================

*man jbd2_journal_load(9)*

*4.6.0-rc5*

Read journal from disk.


Synopsis
========

.. c:function:: int jbd2_journal_load( journal_t * journal )

Arguments
=========

``journal``
    Journal to act on.


Description
===========

Given a journal_t structure which tells us which disk blocks contain a
journal, read the journal from disk to initialise the in-memory
structures.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
