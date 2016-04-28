.. -*- coding: utf-8; mode: rst -*-

.. _API-atapi-cmd-type:

==============
atapi_cmd_type
==============

*man atapi_cmd_type(9)*

*4.6.0-rc5*

Determine ATAPI command type from SCSI opcode


Synopsis
========

.. c:function:: int atapi_cmd_type( u8 opcode )

Arguments
=========

``opcode``
    SCSI opcode


Description
===========

Determine ATAPI command type from ``opcode``.


LOCKING
=======

None.


RETURNS
=======

ATAPI_{READ|WRITE|READ_CD|PASS_THRU|MISC}


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
