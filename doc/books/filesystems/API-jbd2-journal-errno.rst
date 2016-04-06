
.. _API-jbd2-journal-errno:

==================
jbd2_journal_errno
==================

*man jbd2_journal_errno(9)*

*4.6.0-rc1*

returns the journal's error state.


Synopsis
========

.. c:function:: int jbd2_journal_errno( journal_t * journal )

Arguments
=========

``journal``
    journal to examine.


Description
===========

This is the errno number set with ``jbd2_journal_abort``, the last time the journal was mounted - if the journal was stopped without calling abort this will be 0.

If the journal has been aborted on this mount time -EROFS will be returned.
