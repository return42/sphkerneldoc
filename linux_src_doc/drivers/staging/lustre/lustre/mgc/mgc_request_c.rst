.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/mgc/mgc_request.c

.. _`mgc_process_recover_log`:

mgc_process_recover_log
=======================

.. c:function:: int mgc_process_recover_log(struct obd_device *obd, struct config_llog_data *cld)

    by the MGS. A CONFIG_READ RPC is going to send to fetch recovery logs.

    :param struct obd_device \*obd:
        *undescribed*

    :param struct config_llog_data \*cld:
        *undescribed*

.. _`mgc_process_log`:

mgc_process_log
===============

.. c:function:: int mgc_process_log(struct obd_device *mgc, struct config_llog_data *cld)

    :param struct obd_device \*mgc:
        *undescribed*

    :param struct config_llog_data \*cld:
        *undescribed*

.. _`mgc_process_log.description`:

Description
-----------

This function is called for both clients and servers to process the
configuration log from the MGS.  The MGC enqueues a DLM lock on the
log from the MGS, and if the lock gets revoked the MGC will be notified
by the lock cancellation callback that the config log has changed,
and will enqueue another MGS lock on it, and then continue processing
the new additions to the end of the log.

Since the MGC import is not replayable, if the import is being evicted
(rcl == -ESHUTDOWN, \see \ :c:func:`ptlrpc_import_delay_req`\ ), retry to process
the log until recovery is finished or the import is closed.

Make a local copy of the log before parsing it if appropriate (non-MGS
server) so that the server can start even when the MGS is down.

There shouldn't be multiple processes running process_log at once --
sounds like badness.  It actually might be fine, as long as they're not
trying to update from the same log simultaneously, in which case we
should use a per-log semaphore instead of cld_lock.

\param[in] mgc       MGC device by which to fetch the configuration log
\param[in] cld       log processing state (stored in lock callback data)

\retval              0 on success
\retval              negative errno on failure

.. This file was automatic generated / don't edit.

