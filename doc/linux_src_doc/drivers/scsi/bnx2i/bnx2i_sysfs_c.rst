.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/bnx2i/bnx2i_sysfs.c

.. _`bnx2i_dev_to_hba`:

bnx2i_dev_to_hba
================

.. c:function:: struct bnx2i_hba *bnx2i_dev_to_hba(struct device *dev)

    maps dev pointer to adapter struct

    :param struct device \*dev:
        device pointer

.. _`bnx2i_dev_to_hba.description`:

Description
-----------

Map device to hba structure

.. _`bnx2i_show_sq_info`:

bnx2i_show_sq_info
==================

.. c:function:: ssize_t bnx2i_show_sq_info(struct device *dev, struct device_attribute *attr, char *buf)

    return(s currently configured send queue (SQ) size

    :param struct device \*dev:
        device pointer

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        buffer to return current SQ size parameter

.. _`bnx2i_show_sq_info.description`:

Description
-----------

Returns current SQ size parameter, this paramater determines the number
outstanding iSCSI commands supported on a connection

.. _`bnx2i_set_sq_info`:

bnx2i_set_sq_info
=================

.. c:function:: ssize_t bnx2i_set_sq_info(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    update send queue (SQ) size parameter

    :param struct device \*dev:
        device pointer

    :param struct device_attribute \*attr:
        *undescribed*

    :param const char \*buf:
        buffer to return current SQ size parameter

    :param size_t count:
        parameter buffer size

.. _`bnx2i_set_sq_info.description`:

Description
-----------

Interface for user to change shared queue size allocated for each conn
Must be within SQ limits and a power of 2. For the latter this is needed
because of how libiscsi preallocates tasks.

.. _`bnx2i_show_ccell_info`:

bnx2i_show_ccell_info
=====================

.. c:function:: ssize_t bnx2i_show_ccell_info(struct device *dev, struct device_attribute *attr, char *buf)

    returns command cell (HQ) size

    :param struct device \*dev:
        device pointer

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        buffer to return current SQ size parameter

.. _`bnx2i_show_ccell_info.description`:

Description
-----------

returns per-connection TCP history queue size parameter

.. _`bnx2i_set_ccell_info`:

bnx2i_set_ccell_info
====================

.. c:function:: ssize_t bnx2i_set_ccell_info(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    set command cell (HQ) size

    :param struct device \*dev:
        device pointer

    :param struct device_attribute \*attr:
        *undescribed*

    :param const char \*buf:
        buffer to return current SQ size parameter

    :param size_t count:
        parameter buffer size

.. _`bnx2i_set_ccell_info.description`:

Description
-----------

updates per-connection TCP history queue size parameter

.. This file was automatic generated / don't edit.

