.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-skip-recovery:

==========================
jbd2_journal_skip_recovery
==========================

*man jbd2_journal_skip_recovery(9)*

*4.6.0-rc5*

Start journal and wipe exiting records


Synopsis
========

.. c:function:: int jbd2_journal_skip_recovery( journal_t * journal )

Arguments
=========

``journal``
    journal to startup


Description
===========

Locate any valid recovery information from the journal and set up the
journal structures in memory to ignore it (presumably because the caller
has evidence that it is out of date). This function does'nt appear to be
exorted..

We perform one pass over the journal to allow us to tell the user how
much recovery information is being erased, and to let us initialise the
journal transaction sequence numbers to the next unused ID.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
