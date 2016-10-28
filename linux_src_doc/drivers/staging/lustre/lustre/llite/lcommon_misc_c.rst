.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/lcommon_misc.c

.. _`cl_ocd_update`:

cl_ocd_update
=============

.. c:function:: int cl_ocd_update(struct obd_device *host, struct obd_device *watched, enum obd_notify_event ev, void *owner, void *data)

    callback hooked by liblustre and llite clients into \ :c:func:`obd_notify`\  listeners chain to handle notifications about change of import connect_flags. See \ :c:func:`llu_fsswop_mount`\  and \ :c:func:`lustre_common_fill_super`\ .

    :param struct obd_device \*host:
        *undescribed*

    :param struct obd_device \*watched:
        *undescribed*

    :param enum obd_notify_event ev:
        *undescribed*

    :param void \*owner:
        *undescribed*

    :param void \*data:
        *undescribed*

.. This file was automatic generated / don't edit.

