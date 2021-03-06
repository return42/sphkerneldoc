.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/device_pgid.c

.. _`ccw_device_verify_start`:

ccw_device_verify_start
=======================

.. c:function:: void ccw_device_verify_start(struct ccw_device *cdev)

    perform path verification

    :param cdev:
        ccw device
    :type cdev: struct ccw_device \*

.. _`ccw_device_verify_start.description`:

Description
-----------

Perform an I/O on each available channel path to \ ``cdev``\  to determine which
paths are operational. The resulting path mask is stored in sch->vpm.
If device options specify pathgrouping, establish a pathgroup for the
operational paths. When finished, call ccw_device_verify_done with a
return code specifying the result.

.. _`ccw_device_disband_start`:

ccw_device_disband_start
========================

.. c:function:: void ccw_device_disband_start(struct ccw_device *cdev)

    disband pathgroup

    :param cdev:
        ccw device
    :type cdev: struct ccw_device \*

.. _`ccw_device_disband_start.description`:

Description
-----------

Execute a SET PGID channel program on \ ``cdev``\  to disband a previously
established pathgroup. When finished, call ccw_device_disband_done with
a return code specifying the result.

.. _`ccw_device_stlck_start`:

ccw_device_stlck_start
======================

.. c:function:: void ccw_device_stlck_start(struct ccw_device *cdev, void *data, void *buf1, void *buf2)

    perform unconditional release

    :param cdev:
        ccw device
    :type cdev: struct ccw_device \*

    :param data:
        data pointer to be passed to ccw_device_stlck_done
    :type data: void \*

    :param buf1:
        data pointer used in channel program
    :type buf1: void \*

    :param buf2:
        data pointer used in channel program
    :type buf2: void \*

.. _`ccw_device_stlck_start.description`:

Description
-----------

Execute a channel program on \ ``cdev``\  to release an existing PGID reservation.

.. This file was automatic generated / don't edit.

