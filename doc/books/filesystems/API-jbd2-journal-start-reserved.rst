.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-start-reserved:

===========================
jbd2_journal_start_reserved
===========================

*man jbd2_journal_start_reserved(9)*

*4.6.0-rc5*

start reserved handle


Synopsis
========

.. c:function:: int jbd2_journal_start_reserved( handle_t * handle, unsigned int type, unsigned int line_no )

Arguments
=========

``handle``
    handle to start

``type``
    -- undescribed --

``line_no``
    -- undescribed --


Description
===========

Start handle that has been previously reserved with
``jbd2_journal_reserve``. This attaches ``handle`` to the running
transaction (or creates one if there's not transaction running). Unlike
``jbd2_journal_start`` this function cannot block on journal commit,
checkpointing, or similar stuff. It can block on memory allocation or
frozen journal though.

Return 0 on success, non-zero on error - handle is freed in that case.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
