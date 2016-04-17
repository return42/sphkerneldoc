.. -*- coding: utf-8; mode: rst -*-

========
ide-eh.c
========


.. _`ide_error`:

ide_error
=========

.. c:function:: ide_startstop_t ide_error (ide_drive_t *drive, const char *msg, u8 stat)

    handle an error on the IDE

    :param ide_drive_t \*drive:
        drive the error occurred on

    :param const char \*msg:
        message to report

    :param u8 stat:
        status bits



.. _`ide_error.description`:

Description
-----------

:c:func:`ide_error` takes action based on the error returned by the drive.
For normal I/O that may well include retries. We deal with
both new-style (taskfile) and old style command handling here.
In the case of taskfile command handling there is work left to
do

