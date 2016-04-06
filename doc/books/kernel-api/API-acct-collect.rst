
.. _API-acct-collect:

============
acct_collect
============

*man acct_collect(9)*

*4.6.0-rc1*

collect accounting information into pacct_struct


Synopsis
========

.. c:function:: void acct_collect( long exitcode, int group_dead )

Arguments
=========

``exitcode``
    task exit code

``group_dead``
    not 0, if this thread is the last one in the process.
