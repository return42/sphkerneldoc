.. -*- coding: utf-8; mode: rst -*-

==========
recovery.c
==========

.. _`jbd2_journal_recover`:

jbd2_journal_recover
====================

.. c:function:: int jbd2_journal_recover (journal_t *journal)

    recovers a on-disk journal

    :param journal_t \*journal:
        the journal to recover


.. _`jbd2_journal_recover.description`:

Description
-----------

The primary function for recovering the log contents when mounting a
journaled device.

Recovery is done in three passes.  In the first pass, we look for the
end of the log.  In the second, we assemble the list of revoke
blocks.  In the third and final pass, we replay any un-revoked blocks
in the log.


.. _`jbd2_journal_skip_recovery`:

jbd2_journal_skip_recovery
==========================

.. c:function:: int jbd2_journal_skip_recovery (journal_t *journal)

    Start journal and wipe exiting records

    :param journal_t \*journal:
        journal to startup


.. _`jbd2_journal_skip_recovery.description`:

Description
-----------

Locate any valid recovery information from the journal and set up the
journal structures in memory to ignore it (presumably because the
caller has evidence that it is out of date).
This function does'nt appear to be exorted..

We perform one pass over the journal to allow us to tell the user how
much recovery information is being erased, and to let us initialise
the journal transaction sequence numbers to the next unused ID.

