.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide-cd.c

.. _`cdrom_decode_status`:

cdrom_decode_status
===================

.. c:function:: int cdrom_decode_status(ide_drive_t *drive, u8 stat)

    0: if the request should be continued. 1: if the request will be going through error recovery. 2: if the request should be ended.

    :param ide_drive_t \*drive:
        *undescribed*

    :param u8 stat:
        *undescribed*

.. This file was automatic generated / don't edit.

