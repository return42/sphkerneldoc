.. -*- coding: utf-8; mode: rst -*-

.. _API-acct-collect:

============
acct_collect
============

*man acct_collect(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
