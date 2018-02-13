.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/hid.h

.. _`hid_driver`:

struct hid_driver
=================

.. c:type:: struct hid_driver


.. _`hid_driver.definition`:

Definition
----------

.. code-block:: c

    struct hid_driver {
        char *name;
        const struct hid_device_id *id_table;
        struct list_head dyn_list;
        spinlock_t dyn_lock;
        bool (*match)(struct hid_device *dev, bool ignore_special_driver);
        int (*probe)(struct hid_device *dev, const struct hid_device_id *id);
        void (*remove)(struct hid_device *dev);
        const struct hid_report_id *report_table;
        int (*raw_event)(struct hid_device *hdev, struct hid_report *report, u8 *data, int size);
        const struct hid_usage_id *usage_table;
        int (*event)(struct hid_device *hdev, struct hid_field *field, struct hid_usage *usage, __s32 value);
        void (*report)(struct hid_device *hdev, struct hid_report *report);
        __u8 *(*report_fixup)(struct hid_device *hdev, __u8 *buf, unsigned int *size);
        int (*input_mapping)(struct hid_device *hdev,struct hid_input *hidinput, struct hid_field *field, struct hid_usage *usage, unsigned long **bit, int *max);
        int (*input_mapped)(struct hid_device *hdev,struct hid_input *hidinput, struct hid_field *field, struct hid_usage *usage, unsigned long **bit, int *max);
        int (*input_configured)(struct hid_device *hdev, struct hid_input *hidinput);
        void (*feature_mapping)(struct hid_device *hdev,struct hid_field *field, struct hid_usage *usage);
        void (*bus_add_driver)(struct hid_driver *driver);
        void (*bus_removed_driver)(struct hid_driver *driver);
    #ifdef CONFIG_PM
        int (*suspend)(struct hid_device *hdev, pm_message_t message);
        int (*resume)(struct hid_device *hdev);
        int (*reset_resume)(struct hid_device *hdev);
    #endif
    }

.. _`hid_driver.members`:

Members
-------

name
    driver name (e.g. "Footech_bar-wheel")

id_table
    which devices is this driver for (must be non-NULL for probe
    to be called)

dyn_list
    list of dynamically added device ids

dyn_lock
    lock protecting \ ``dyn_list``\ 

match
    check if the given device is handled by this driver

probe
    new device inserted

remove
    device removed (NULL if not a hot-plug capable driver)

report_table
    on which reports to call raw_event (NULL means all)

raw_event
    if report in report_table, this hook is called (NULL means nop)

usage_table
    on which events to call event (NULL means all)

event
    if usage in usage_table, this hook is called (NULL means nop)

report
    this hook is called after parsing a report (NULL means nop)

report_fixup
    called before report descriptor parsing (NULL means nop)

input_mapping
    invoked on input registering before mapping an usage

input_mapped
    invoked on input registering after mapping an usage

input_configured
    invoked just before the device is registered

feature_mapping
    invoked on feature registering

bus_add_driver
    invoked when a HID driver is about to be added

bus_removed_driver
    invoked when a HID driver has been removed

suspend
    invoked on suspend (NULL means nop)

resume
    invoked on resume if device was not reset (NULL means nop)

reset_resume
    invoked on resume if device was reset (NULL means nop)

.. _`hid_driver.description`:

Description
-----------

probe should return -errno on error, or 0 on success. During probe,
input will not be passed to raw_event unless hid_device_io_start is
called.

raw_event and event should return 0 on no action performed, 1 when no
further processing should be done and negative on error

input_mapping shall return a negative value to completely ignore this usage
(e.g. doubled or invalid usage), zero to continue with parsing of this
usage by generic code (no special handling needed) or positive to skip
generic parsing (needed special handling which was done in the hook already)
input_mapped shall return negative to inform the layer that this usage
should not be considered for further processing or zero to notify that
no processing was performed and should be done in a generic manner
Both these functions may be NULL which means the same behavior as returning
zero from them.

.. _`module_hid_driver`:

module_hid_driver
=================

.. c:function::  module_hid_driver( __hid_driver)

    Helper macro for registering a HID driver

    :param  __hid_driver:
        hid_driver struct

.. _`module_hid_driver.description`:

Description
-----------

Helper macro for HID drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\ 

.. _`hid_device_io_start`:

hid_device_io_start
===================

.. c:function:: void hid_device_io_start(struct hid_device *hid)

    enable HID input during probe, remove

    :param struct hid_device \*hid:
        *undescribed*

.. _`hid_device_io_start.description`:

Description
-----------

@hid - the device

This should only be called during probe or remove and only be
called by the thread calling probe or remove. It will allow
incoming packets to be delivered to the driver.

.. _`hid_device_io_stop`:

hid_device_io_stop
==================

.. c:function:: void hid_device_io_stop(struct hid_device *hid)

    disable HID input during probe, remove

    :param struct hid_device \*hid:
        *undescribed*

.. _`hid_device_io_stop.description`:

Description
-----------

@hid - the device

Should only be called after hid_device_io_start. It will prevent
incoming packets from going to the driver for the duration of
probe, remove. If called during probe, packets will still go to the
driver after probe is complete. This function should only be called
by the thread calling probe or remove.

.. _`hid_map_usage`:

hid_map_usage
=============

.. c:function:: void hid_map_usage(struct hid_input *hidinput, struct hid_usage *usage, unsigned long **bit, int *max, __u8 type, __u16 c)

    map usage input bits

    :param struct hid_input \*hidinput:
        hidinput which we are interested in

    :param struct hid_usage \*usage:
        usage to fill in

    :param unsigned long \*\*bit:
        pointer to input->{}bit (out parameter)

    :param int \*max:
        maximal valid usage->code to consider later (out parameter)

    :param __u8 type:
        input event type (EV_KEY, EV_REL, ...)

    :param __u16 c:
        code which corresponds to this usage and type

.. _`hid_map_usage_clear`:

hid_map_usage_clear
===================

.. c:function:: void hid_map_usage_clear(struct hid_input *hidinput, struct hid_usage *usage, unsigned long **bit, int *max, __u8 type, __u16 c)

    map usage input bits and clear the input bit

    :param struct hid_input \*hidinput:
        *undescribed*

    :param struct hid_usage \*usage:
        *undescribed*

    :param unsigned long \*\*bit:
        *undescribed*

    :param int \*max:
        *undescribed*

    :param __u8 type:
        *undescribed*

    :param __u16 c:
        *undescribed*

.. _`hid_map_usage_clear.description`:

Description
-----------

The same as hid_map_usage, except the \ ``c``\  bit is also cleared in supported
bits (@bit).

.. _`hid_parse`:

hid_parse
=========

.. c:function:: int hid_parse(struct hid_device *hdev)

    parse HW reports

    :param struct hid_device \*hdev:
        hid device

.. _`hid_parse.description`:

Description
-----------

Call this from probe after you set up the device (if needed). Your
report_fixup will be called (if non-NULL) after reading raw report from
device before passing it to hid layer for real parsing.

.. _`hid_hw_power`:

hid_hw_power
============

.. c:function:: int hid_hw_power(struct hid_device *hdev, int level)

    requests underlying HW to go into given power mode

    :param struct hid_device \*hdev:
        hid device

    :param int level:
        requested power level (one of \ ``PM_HINT``\ \_\* defines)

.. _`hid_hw_power.description`:

Description
-----------

This function requests underlying hardware to enter requested power
mode.

.. _`hid_hw_request`:

hid_hw_request
==============

.. c:function:: void hid_hw_request(struct hid_device *hdev, struct hid_report *report, int reqtype)

    send report request to device

    :param struct hid_device \*hdev:
        hid device

    :param struct hid_report \*report:
        report to send

    :param int reqtype:
        hid request type

.. _`hid_hw_raw_request`:

hid_hw_raw_request
==================

.. c:function:: int hid_hw_raw_request(struct hid_device *hdev, unsigned char reportnum, __u8 *buf, size_t len, unsigned char rtype, int reqtype)

    send report request to device

    :param struct hid_device \*hdev:
        hid device

    :param unsigned char reportnum:
        report ID

    :param __u8 \*buf:
        in/out data to transfer

    :param size_t len:
        length of buf

    :param unsigned char rtype:
        HID report type

    :param int reqtype:
        HID_REQ_GET_REPORT or HID_REQ_SET_REPORT

.. _`hid_hw_raw_request.description`:

Description
-----------

Same behavior as hid_hw_request, but with raw buffers instead.

.. _`hid_hw_output_report`:

hid_hw_output_report
====================

.. c:function:: int hid_hw_output_report(struct hid_device *hdev, __u8 *buf, size_t len)

    send output report to device

    :param struct hid_device \*hdev:
        hid device

    :param __u8 \*buf:
        raw data to transfer

    :param size_t len:
        length of buf

.. _`hid_hw_idle`:

hid_hw_idle
===========

.. c:function:: int hid_hw_idle(struct hid_device *hdev, int report, int idle, int reqtype)

    send idle request to device

    :param struct hid_device \*hdev:
        hid device

    :param int report:
        report to control

    :param int idle:
        idle state

    :param int reqtype:
        hid request type

.. _`hid_hw_wait`:

hid_hw_wait
===========

.. c:function:: void hid_hw_wait(struct hid_device *hdev)

    wait for buffered io to complete

    :param struct hid_device \*hdev:
        hid device

.. _`hid_report_len`:

hid_report_len
==============

.. c:function:: int hid_report_len(struct hid_report *report)

    calculate the report length

    :param struct hid_report \*report:
        the report we want to know the length

.. This file was automatic generated / don't edit.

