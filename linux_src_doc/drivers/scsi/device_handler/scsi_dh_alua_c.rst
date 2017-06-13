.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/device_handler/scsi_dh_alua.c

.. _`alua_rtpg_queue`:

alua_rtpg_queue
===============

.. c:function:: bool alua_rtpg_queue(struct alua_port_group *pg, struct scsi_device *sdev, struct alua_queue_data *qdata, bool force)

    cause RTPG to be submitted asynchronously

    :param struct alua_port_group \*pg:
        *undescribed*

    :param struct scsi_device \*sdev:
        *undescribed*

    :param struct alua_queue_data \*qdata:
        *undescribed*

    :param bool force:
        *undescribed*

.. _`alua_rtpg_queue.description`:

Description
-----------

Returns true if and only if \ :c:func:`alua_rtpg_work`\  will be called asynchronously.
That function is responsible for calling \ ``qdata``\ ->fn().

.. This file was automatic generated / don't edit.

