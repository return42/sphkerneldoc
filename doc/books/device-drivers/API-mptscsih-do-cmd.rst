.. -*- coding: utf-8; mode: rst -*-

.. _API-mptscsih-do-cmd:

===============
mptscsih_do_cmd
===============

*man mptscsih_do_cmd(9)*

*4.6.0-rc5*

Do internal command.


Synopsis
========

.. c:function:: int mptscsih_do_cmd( MPT_SCSI_HOST * hd, INTERNAL_CMD * io )

Arguments
=========

``hd``
    MPT_SCSI_HOST pointer

``io``
    INTERNAL_CMD pointer.


Description
===========

Issue the specified internally generated command and do command specific
cleanup. For bus scan / DV only.


NOTES
=====

If command is Inquiry and status is good, initialize a target structure,
save the data


Remark
======

Single threaded access only.


Return
======

< 0 if an illegal command or no resources

0 if good

> 0 if command complete but some type of completion error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
