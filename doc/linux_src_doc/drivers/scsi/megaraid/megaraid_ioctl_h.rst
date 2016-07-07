.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/megaraid/megaraid_ioctl.h

.. _`con_log`:

con_log
=======

.. c:function::  con_log( level,  fmt)

    console log routine

    :param  level:
        indicates the severity of the message.

    :param  fmt:
        format string

.. _`con_log.description`:

Description
-----------

con_log displays the error messages on the console based on the current
debug level. Also it attaches the appropriate kernel severity level with
the message.

.. This file was automatic generated / don't edit.

