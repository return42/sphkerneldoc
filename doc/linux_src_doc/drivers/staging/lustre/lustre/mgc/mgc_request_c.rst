.. -*- coding: utf-8; mode: rst -*-

=============
mgc_request.c
=============


.. _`mgc_process_recover_log`:

mgc_process_recover_log
=======================

.. c:function:: int mgc_process_recover_log (struct obd_device *obd, struct config_llog_data *cld)

    :param struct obd_device \*obd:

        *undescribed*

    :param struct config_llog_data \*cld:

        *undescribed*



.. _`mgc_process_recover_log.description`:

Description
-----------

by the MGS. A CONFIG_READ RPC is going to send to fetch recovery logs.

