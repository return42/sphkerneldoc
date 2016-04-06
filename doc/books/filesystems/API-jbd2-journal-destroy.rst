
.. _API-jbd2-journal-destroy:

====================
jbd2_journal_destroy
====================

*man jbd2_journal_destroy(9)*

*4.6.0-rc1*

Release a journal_t structure.


Synopsis
========

.. c:function:: int jbd2_journal_destroy( journal_t * journal )

Arguments
=========

``journal``
    Journal to act on.


Description
===========

Release a journal_t structure once it is no longer in use by the journaled object. Return <0 if we couldn't clean up the journal.
