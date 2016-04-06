
.. _API-jbd2-journal-recover:

====================
jbd2_journal_recover
====================

*man jbd2_journal_recover(9)*

*4.6.0-rc1*

recovers a on-disk journal


Synopsis
========

.. c:function:: int jbd2_journal_recover( journal_t * journal )

Arguments
=========

``journal``
    the journal to recover


Description
===========

The primary function for recovering the log contents when mounting a journaled device.

Recovery is done in three passes. In the first pass, we look for the end of the log. In the second, we assemble the list of revoke blocks. In the third and final pass, we replay
any un-revoked blocks in the log.
