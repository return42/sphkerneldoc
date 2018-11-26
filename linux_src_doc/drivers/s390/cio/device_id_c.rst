.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/device_id.c

.. _`diag210_to_senseid`:

diag210_to_senseid
==================

.. c:function:: int diag210_to_senseid(struct senseid *senseid, struct diag210 *diag)

    convert diag 0x210 data to sense id information

    :param senseid:
        sense id
    :type senseid: struct senseid \*

    :param diag:
        diag 0x210 data
    :type diag: struct diag210 \*

.. _`diag210_to_senseid.description`:

Description
-----------

Return 0 on success, non-zero otherwise.

.. _`diag210_get_dev_info`:

diag210_get_dev_info
====================

.. c:function:: int diag210_get_dev_info(struct ccw_device *cdev)

    retrieve device information via diag 0x210

    :param cdev:
        ccw device
    :type cdev: struct ccw_device \*

.. _`diag210_get_dev_info.description`:

Description
-----------

Returns zero on success, non-zero otherwise.

.. _`ccw_device_sense_id_start`:

ccw_device_sense_id_start
=========================

.. c:function:: void ccw_device_sense_id_start(struct ccw_device *cdev)

    perform SENSE ID

    :param cdev:
        ccw device
    :type cdev: struct ccw_device \*

.. _`ccw_device_sense_id_start.description`:

Description
-----------

Execute a SENSE ID channel program on \ ``cdev``\  to update its sense id
information. When finished, call ccw_device_sense_id_done with a
return code specifying the result.

.. This file was automatic generated / don't edit.

