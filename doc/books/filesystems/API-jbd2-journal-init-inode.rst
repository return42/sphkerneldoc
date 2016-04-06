
.. _API-jbd2-journal-init-inode:

=======================
jbd2_journal_init_inode
=======================

*man jbd2_journal_init_inode(9)*

*4.6.0-rc1*

creates a journal which maps to a inode.


Synopsis
========

.. c:function:: journal_t ⋆ jbd2_journal_init_inode( struct inode * inode )

Arguments
=========

``inode``
    An inode to create the journal in


Description
===========

jbd2_journal_init_inode creates a journal which maps an on-disk inode as the journal. The inode must exist already, must support ``bmap`` and must have all data blocks
preallocated.
