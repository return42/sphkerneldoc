.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide-pm.c

.. _`ide_complete_pm_rq`:

ide_complete_pm_rq
==================

.. c:function:: void ide_complete_pm_rq(ide_drive_t *drive, struct request *rq)

    end the current Power Management request

    :param ide_drive_t \*drive:
        target drive

    :param struct request \*rq:
        request

.. _`ide_complete_pm_rq.description`:

Description
-----------

This function cleans up the current PM request and stops the queue
if necessary.

.. This file was automatic generated / don't edit.

