.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/pm8001/pm8001_ctl.c

.. _`pm8001_ctl_mpi_interface_rev_show`:

pm8001_ctl_mpi_interface_rev_show
=================================

.. c:function:: ssize_t pm8001_ctl_mpi_interface_rev_show(struct device *cdev, struct device_attribute *attr, char *buf)

    MPI interface revision number

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned

.. _`pm8001_ctl_mpi_interface_rev_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`pm8001_ctl_fw_version_show`:

pm8001_ctl_fw_version_show
==========================

.. c:function:: ssize_t pm8001_ctl_fw_version_show(struct device *cdev, struct device_attribute *attr, char *buf)

    firmware version

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned

.. _`pm8001_ctl_fw_version_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`pm8001_ctl_ila_version_show`:

pm8001_ctl_ila_version_show
===========================

.. c:function:: ssize_t pm8001_ctl_ila_version_show(struct device *cdev, struct device_attribute *attr, char *buf)

    ila version

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned

.. _`pm8001_ctl_ila_version_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`pm8001_ctl_inactive_fw_version_show`:

pm8001_ctl_inactive_fw_version_show
===================================

.. c:function:: ssize_t pm8001_ctl_inactive_fw_version_show(struct device *cdev, struct device_attribute *attr, char *buf)

    Inacative firmware version number

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned

.. _`pm8001_ctl_inactive_fw_version_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`pm8001_ctl_max_out_io_show`:

pm8001_ctl_max_out_io_show
==========================

.. c:function:: ssize_t pm8001_ctl_max_out_io_show(struct device *cdev, struct device_attribute *attr, char *buf)

    max outstanding io supported

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned

.. _`pm8001_ctl_max_out_io_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`pm8001_ctl_max_devices_show`:

pm8001_ctl_max_devices_show
===========================

.. c:function:: ssize_t pm8001_ctl_max_devices_show(struct device *cdev, struct device_attribute *attr, char *buf)

    max devices support

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned

.. _`pm8001_ctl_max_devices_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`pm8001_ctl_max_sg_list_show`:

pm8001_ctl_max_sg_list_show
===========================

.. c:function:: ssize_t pm8001_ctl_max_sg_list_show(struct device *cdev, struct device_attribute *attr, char *buf)

    max sg list supported iff not 0.0 for no hardware limitation

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned

.. _`pm8001_ctl_max_sg_list_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`pm8001_ctl_sas_spec_support_show`:

pm8001_ctl_sas_spec_support_show
================================

.. c:function:: ssize_t pm8001_ctl_sas_spec_support_show(struct device *cdev, struct device_attribute *attr, char *buf)

    sas spec supported

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned

.. _`pm8001_ctl_sas_spec_support_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`pm8001_ctl_host_sas_address_show`:

pm8001_ctl_host_sas_address_show
================================

.. c:function:: ssize_t pm8001_ctl_host_sas_address_show(struct device *cdev, struct device_attribute *attr, char *buf)

    sas address

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned

.. _`pm8001_ctl_host_sas_address_show.description`:

Description
-----------

This is the controller sas address

A sysfs 'read-only' shost attribute.

.. _`pm8001_ctl_logging_level_show`:

pm8001_ctl_logging_level_show
=============================

.. c:function:: ssize_t pm8001_ctl_logging_level_show(struct device *cdev, struct device_attribute *attr, char *buf)

    logging level

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned

.. _`pm8001_ctl_logging_level_show.description`:

Description
-----------

A sysfs 'read/write' shost attribute.

.. _`pm8001_ctl_aap_log_show`:

pm8001_ctl_aap_log_show
=======================

.. c:function:: ssize_t pm8001_ctl_aap_log_show(struct device *cdev, struct device_attribute *attr, char *buf)

    aap1 event log

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned

.. _`pm8001_ctl_aap_log_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`pm8001_ctl_ib_queue_log_show`:

pm8001_ctl_ib_queue_log_show
============================

.. c:function:: ssize_t pm8001_ctl_ib_queue_log_show(struct device *cdev, struct device_attribute *attr, char *buf)

    Out bound Queue log

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned
        A sysfs 'read-only' shost attribute.

.. _`pm8001_ctl_ob_queue_log_show`:

pm8001_ctl_ob_queue_log_show
============================

.. c:function:: ssize_t pm8001_ctl_ob_queue_log_show(struct device *cdev, struct device_attribute *attr, char *buf)

    Out bound Queue log

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned
        A sysfs 'read-only' shost attribute.

.. _`pm8001_ctl_bios_version_show`:

pm8001_ctl_bios_version_show
============================

.. c:function:: ssize_t pm8001_ctl_bios_version_show(struct device *cdev, struct device_attribute *attr, char *buf)

    Bios version Display

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned
        A sysfs 'read-only' shost attribute.

.. _`pm8001_ctl_iop_log_show`:

pm8001_ctl_iop_log_show
=======================

.. c:function:: ssize_t pm8001_ctl_iop_log_show(struct device *cdev, struct device_attribute *attr, char *buf)

    IOP event log

    :param struct device \*cdev:
        pointer to embedded class device

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        the buffer returned

.. _`pm8001_ctl_iop_log_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. This file was automatic generated / don't edit.

