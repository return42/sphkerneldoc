
.. _API-jbd2-journal-ack-err:

====================
jbd2_journal_ack_err
====================

*man jbd2_journal_ack_err(9)*

*4.6.0-rc1*

Ack journal err.


Synopsis
========

.. c:function:: void jbd2_journal_ack_err( journal_t * journal )

Arguments
=========

``journal``
    journal to act on.


Description
===========

An error must be cleared or acked to take a FS out of readonly mode.
