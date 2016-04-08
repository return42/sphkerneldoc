
.. _API-atapi-cmd-type:

==============
atapi_cmd_type
==============

*man atapi_cmd_type(9)*

*4.6.0-rc1*

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
