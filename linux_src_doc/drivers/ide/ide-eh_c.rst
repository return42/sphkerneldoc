.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide-eh.c

.. _`ide_error`:

ide_error
=========

.. c:function:: ide_startstop_t ide_error(ide_drive_t *drive, const char *msg, u8 stat)

    handle an error on the IDE

    :param drive:
        drive the error occurred on
    :type drive: ide_drive_t \*

    :param msg:
        message to report
    :type msg: const char \*

    :param stat:
        status bits
    :type stat: u8

.. _`ide_error.description`:

Description
-----------

\ :c:func:`ide_error`\  takes action based on the error returned by the drive.
For normal I/O that may well include retries. We deal with
both new-style (taskfile) and old style command handling here.
In the case of taskfile command handling there is work left to
do

.. This file was automatic generated / don't edit.

