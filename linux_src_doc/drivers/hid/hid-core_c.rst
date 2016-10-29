.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/hid-core.c

.. _`hid_parse_report`:

hid_parse_report
================

.. c:function:: int hid_parse_report(struct hid_device *hid, __u8 *start, unsigned size)

    parse device report

    :param struct hid_device \*hid:
        *undescribed*

    :param __u8 \*start:
        report start

    :param unsigned size:
        report size

.. _`hid_parse_report.description`:

Description
-----------

Allocate the device report as read by the bus driver. This function should
only be called from \ :c:func:`parse`\  in ll drivers.

.. _`hid_validate_values`:

hid_validate_values
===================

.. c:function:: struct hid_report *hid_validate_values(struct hid_device *hid, unsigned int type, unsigned int id, unsigned int field_index, unsigned int report_counts)

    validate existing device report's value indexes

    :param struct hid_device \*hid:
        *undescribed*

    :param unsigned int type:
        which report type to examine

    :param unsigned int id:
        which report ID to examine (0 for first)

    :param unsigned int field_index:
        which report field to examine

    :param unsigned int report_counts:
        expected number of values

.. _`hid_validate_values.description`:

Description
-----------

Validate the number of values in a given field of a given report, after
parsing.

.. _`hid_open_report`:

hid_open_report
===============

.. c:function:: int hid_open_report(struct hid_device *device)

    open a driver-specific device report

    :param struct hid_device \*device:
        hid device

.. _`hid_open_report.description`:

Description
-----------

Parse a report description into a hid_device structure. Reports are
enumerated, fields are attached to these reports.
0 returned on success, otherwise nonzero error value.

This function (or the equivalent \ :c:func:`hid_parse`\  macro) should only be
called from \ :c:func:`probe`\  in drivers, before starting the device.

.. _`hid_match_report`:

hid_match_report
================

.. c:function:: int hid_match_report(struct hid_device *hid, struct hid_report *report)

    check if driver's raw_event should be called

    :param struct hid_device \*hid:
        hid device

    :param struct hid_report \*report:
        *undescribed*

.. _`hid_match_report.description`:

Description
-----------

compare hid->driver->report_table->report_type to report->type

.. _`hid_match_usage`:

hid_match_usage
===============

.. c:function:: int hid_match_usage(struct hid_device *hid, struct hid_usage *usage)

    check if driver's event should be called

    :param struct hid_device \*hid:
        hid device

    :param struct hid_usage \*usage:
        usage to match against

.. _`hid_match_usage.description`:

Description
-----------

compare hid->driver->usage_table->usage_{type,code} to
usage->usage_{type,code}

.. _`hid_input_report`:

hid_input_report
================

.. c:function:: int hid_input_report(struct hid_device *hid, int type, u8 *data, int size, int interrupt)

    report data from lower layer (usb, bt...)

    :param struct hid_device \*hid:
        hid device

    :param int type:
        HID report type (HID\_\*\_REPORT)

    :param u8 \*data:
        report contents

    :param int size:
        size of data parameter

    :param int interrupt:
        distinguish between interrupt and control transfers

.. _`hid_input_report.description`:

Description
-----------

This is data entry for lower layers.

.. _`store_new_id`:

store_new_id
============

.. c:function:: ssize_t store_new_id(struct device_driver *drv, const char *buf, size_t count)

    add a new HID device ID to this driver and re-probe devices

    :param struct device_driver \*drv:
        *undescribed*

    :param const char \*buf:
        buffer for scanning device ID data

    :param size_t count:
        input size

.. _`store_new_id.description`:

Description
-----------

Adds a new dynamic hid device ID to this driver,
and causes the driver to probe for all devices again.

.. _`hid_allocate_device`:

hid_allocate_device
===================

.. c:function:: struct hid_device *hid_allocate_device( void)

    allocate new hid device descriptor

    :param  void:
        no arguments

.. _`hid_allocate_device.description`:

Description
-----------

Allocate and initialize hid device, so that hid_destroy_device might be
used to free it.

New hid_device pointer is returned on success, otherwise ERR_PTR encoded
error value.

.. _`hid_destroy_device`:

hid_destroy_device
==================

.. c:function:: void hid_destroy_device(struct hid_device *hdev)

    free previously allocated device

    :param struct hid_device \*hdev:
        hid device

.. _`hid_destroy_device.description`:

Description
-----------

If you allocate hid_device through hid_allocate_device, you should ever
free by this function.

.. This file was automatic generated / don't edit.
