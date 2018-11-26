.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/device_handler/scsi_dh_alua.c

.. _`alua_rtpg_queue`:

alua_rtpg_queue
===============

.. c:function:: bool alua_rtpg_queue(struct alua_port_group *pg, struct scsi_device *sdev, struct alua_queue_data *qdata, bool force)

    cause RTPG to be submitted asynchronously

    :param pg:
        ALUA port group associated with \ ``sdev``\ .
    :type pg: struct alua_port_group \*

    :param sdev:
        SCSI device for which to submit an RTPG.
    :type sdev: struct scsi_device \*

    :param qdata:
        Information about the callback to invoke after the RTPG.
    :type qdata: struct alua_queue_data \*

    :param force:
        Whether or not to submit an RTPG if a work item that will submit an
        RTPG already has been scheduled.
    :type force: bool

.. _`alua_rtpg_queue.description`:

Description
-----------

Returns true if and only if \ :c:func:`alua_rtpg_work`\  will be called asynchronously.
That function is responsible for calling \ ``qdata->fn``\ ().

.. This file was automatic generated / don't edit.

