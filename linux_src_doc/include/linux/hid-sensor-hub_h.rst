.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/hid-sensor-hub.h

.. _`hid_sensor_hub_attribute_info`:

struct hid_sensor_hub_attribute_info
====================================

.. c:type:: struct hid_sensor_hub_attribute_info

    Attribute info

.. _`hid_sensor_hub_attribute_info.definition`:

Definition
----------

.. code-block:: c

    struct hid_sensor_hub_attribute_info {
        u32 usage_id;
        u32 attrib_id;
        s32 report_id;
        s32 index;
        s32 units;
        s32 unit_expo;
        s32 size;
        s32 logical_minimum;
        s32 logical_maximum;
    }

.. _`hid_sensor_hub_attribute_info.members`:

Members
-------

usage_id
    Parent usage id of a physical device.

attrib_id
    Attribute id for this attribute.

report_id
    Report id in which this information resides.

index
    Field index in the report.

units
    Measurment unit for this attribute.

unit_expo
    Exponent used in the data.

size
    Size in bytes for data size.

logical_minimum
    Logical minimum value for this attribute.

logical_maximum
    Logical maximum value for this attribute.

.. _`sensor_hub_pending`:

struct sensor_hub_pending
=========================

.. c:type:: struct sensor_hub_pending

    Synchronous read pending information

.. _`sensor_hub_pending.definition`:

Definition
----------

.. code-block:: c

    struct sensor_hub_pending {
        bool status;
        struct completion ready;
        u32 usage_id;
        u32 attr_usage_id;
        int raw_size;
        u8 *raw_data;
    }

.. _`sensor_hub_pending.members`:

Members
-------

status
    Pending status true/false.

ready
    Completion synchronization data.

usage_id
    Usage id for physical device, E.g. Gyro usage id.

attr_usage_id
    Usage Id of a field, E.g. X-AXIS for a gyro.

raw_size
    Response size for a read request.

raw_data
    Place holder for received response.

.. _`hid_sensor_hub_device`:

struct hid_sensor_hub_device
============================

.. c:type:: struct hid_sensor_hub_device

    Stores the hub instance data

.. _`hid_sensor_hub_device.definition`:

Definition
----------

.. code-block:: c

    struct hid_sensor_hub_device {
        struct hid_device *hdev;
        u32 vendor_id;
        u32 product_id;
        u32 usage;
        int start_collection_index;
        int end_collection_index;
        struct mutex *mutex_ptr;
        struct sensor_hub_pending pending;
    }

.. _`hid_sensor_hub_device.members`:

Members
-------

hdev
    Stores the hid instance.

vendor_id
    Vendor id of hub device.

product_id
    Product id of hub device.

usage
    Usage id for this hub device instance.

start_collection_index
    Starting index for a phy type collection

end_collection_index
    Last index for a phy type collection

mutex_ptr
    synchronizing mutex pointer.

pending
    Holds information of pending sync read request.

.. _`hid_sensor_hub_callbacks`:

struct hid_sensor_hub_callbacks
===============================

.. c:type:: struct hid_sensor_hub_callbacks

    Client callback functions

.. _`hid_sensor_hub_callbacks.definition`:

Definition
----------

.. code-block:: c

    struct hid_sensor_hub_callbacks {
        struct platform_device *pdev;
        int (*suspend)(struct hid_sensor_hub_device *hsdev, void *priv);
        int (*resume)(struct hid_sensor_hub_device *hsdev, void *priv);
        int (*capture_sample)(struct hid_sensor_hub_device *hsdev,u32 usage_id, size_t raw_len, char *raw_data,void *priv);
        int (*send_event)(struct hid_sensor_hub_device *hsdev, u32 usage_id,void *priv);
    }

.. _`hid_sensor_hub_callbacks.members`:

Members
-------

pdev
    Platform device instance of the client driver.

suspend
    Suspend callback.

resume
    Resume callback.

capture_sample
    Callback to get a sample.

send_event
    Send notification to indicate all samples are
    captured, process and send event

.. _`sensor_hub_device_open`:

sensor_hub_device_open
======================

.. c:function:: int sensor_hub_device_open(struct hid_sensor_hub_device *hsdev)

    Open hub device

    :param struct hid_sensor_hub_device \*hsdev:
        Hub device instance.

.. _`sensor_hub_device_open.description`:

Description
-----------

Used to open hid device for sensor hub.

.. _`sensor_hub_device_close`:

sensor_hub_device_close
=======================

.. c:function:: void sensor_hub_device_close(struct hid_sensor_hub_device *hsdev)

    Close hub device

    :param struct hid_sensor_hub_device \*hsdev:
        Hub device instance.

.. _`sensor_hub_device_close.description`:

Description
-----------

Used to clode hid device for sensor hub.

.. _`sensor_hub_register_callback`:

sensor_hub_register_callback
============================

.. c:function:: int sensor_hub_register_callback(struct hid_sensor_hub_device *hsdev, u32 usage_id, struct hid_sensor_hub_callbacks *usage_callback)

    Register client callbacks

    :param struct hid_sensor_hub_device \*hsdev:
        Hub device instance.

    :param u32 usage_id:
        Usage id of the client (E.g. 0x200076 for Gyro).

    :param struct hid_sensor_hub_callbacks \*usage_callback:
        Callback function storage

.. _`sensor_hub_register_callback.description`:

Description
-----------

Used to register callbacks by client processing drivers. Sensor
hub core driver will call these callbacks to offload processing
of data streams and notifications.

.. _`sensor_hub_remove_callback`:

sensor_hub_remove_callback
==========================

.. c:function:: int sensor_hub_remove_callback(struct hid_sensor_hub_device *hsdev, u32 usage_id)

    Remove client callbacks

    :param struct hid_sensor_hub_device \*hsdev:
        Hub device instance.

    :param u32 usage_id:
        Usage id of the client (E.g. 0x200076 for Gyro).

.. _`sensor_hub_remove_callback.description`:

Description
-----------

If there is a callback registred, this call will remove that
callbacks, so that it will stop data and event notifications.

.. _`sensor_hub_input_get_attribute_info`:

sensor_hub_input_get_attribute_info
===================================

.. c:function:: int sensor_hub_input_get_attribute_info(struct hid_sensor_hub_device *hsdev, u8 type, u32 usage_id, u32 attr_usage_id, struct hid_sensor_hub_attribute_info *info)

    Get an attribute information

    :param struct hid_sensor_hub_device \*hsdev:
        Hub device instance.

    :param u8 type:
        Type of this attribute, input/output/feature

    :param u32 usage_id:
        Attribute usage id of parent physical device as per spec

    :param u32 attr_usage_id:
        Attribute usage id as per spec

    :param struct hid_sensor_hub_attribute_info \*info:
        return information about attribute after parsing report

.. _`sensor_hub_input_get_attribute_info.description`:

Description
-----------

Parses report and returns the attribute information such as report id,
field index, units and exponet etc.

.. _`sensor_hub_set_feature`:

sensor_hub_set_feature
======================

.. c:function:: int sensor_hub_set_feature(struct hid_sensor_hub_device *hsdev, u32 report_id, u32 field_index, int buffer_size, void *buffer)

    Feature set request

    :param struct hid_sensor_hub_device \*hsdev:
        Hub device instance.

    :param u32 report_id:
        Report id to look for

    :param u32 field_index:
        Field index inside a report

    :param int buffer_size:
        size of the buffer

    :param void \*buffer:
        buffer to use in the feature set

.. _`sensor_hub_set_feature.description`:

Description
-----------

Used to set a field in feature report. For example this can set polling
interval, sensitivity, activate/deactivate state.

.. _`sensor_hub_get_feature`:

sensor_hub_get_feature
======================

.. c:function:: int sensor_hub_get_feature(struct hid_sensor_hub_device *hsdev, u32 report_id, u32 field_index, int buffer_size, void *buffer)

    Feature get request

    :param struct hid_sensor_hub_device \*hsdev:
        Hub device instance.

    :param u32 report_id:
        Report id to look for

    :param u32 field_index:
        Field index inside a report

    :param int buffer_size:
        size of the buffer

    :param void \*buffer:
        buffer to copy output

.. _`sensor_hub_get_feature.description`:

Description
-----------

Used to get a field in feature report. For example this can get polling
interval, sensitivity, activate/deactivate state. On success it returns
number of bytes copied to buffer. On failure, it returns value < 0.

.. This file was automatic generated / don't edit.

