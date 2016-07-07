.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/usb/dvb-usb/dvb-usb.h

.. _`dvb_usb_device_description`:

struct dvb_usb_device_description
=================================

.. c:type:: struct dvb_usb_device_description

    name and its according USB IDs

.. _`dvb_usb_device_description.definition`:

Definition
----------

.. code-block:: c

    struct dvb_usb_device_description {
        const char *name;
        #define DVB_USB_ID_MAX_NUM 15
        struct usb_device_id  *cold_ids[DVB_USB_ID_MAX_NUM];
        struct usb_device_id  *warm_ids[DVB_USB_ID_MAX_NUM];
    }

.. _`dvb_usb_device_description.members`:

Members
-------

name
    real name of the box, regardless which DVB USB device class is in use

cold_ids
    array of struct usb_device_id which describe the device in
    pre-firmware state

warm_ids
    array of struct usb_device_id which describe the device in
    post-firmware state

.. _`dvb_usb_device_description.description`:

Description
-----------

Each DVB USB device class can have one or more actual devices, this struct
assigns a name to it.

.. _`dvb_usb_adapter_fe_properties`:

struct dvb_usb_adapter_fe_properties
====================================

.. c:type:: struct dvb_usb_adapter_fe_properties

    properties of a dvb-usb-adapter. A DVB-USB-Adapter is basically a dvb_adapter which is present on a USB-device.

.. _`dvb_usb_adapter_fe_properties.definition`:

Definition
----------

.. code-block:: c

    struct dvb_usb_adapter_fe_properties {
        #define DVB_USB_ADAP_HAS_PID_FILTER 0x01
        #define DVB_USB_ADAP_PID_FILTER_CAN_BE_TURNED_OFF 0x02
        #define DVB_USB_ADAP_NEED_PID_FILTERING 0x04
        #define DVB_USB_ADAP_RECEIVES_204_BYTE_TS 0x08
        #define DVB_USB_ADAP_RECEIVES_RAW_PAYLOAD 0x10
        int caps;
        int pid_filter_count;
        int (* streaming_ctrl) (struct dvb_usb_adapter *, int);
        int (* pid_filter_ctrl) (struct dvb_usb_adapter *, int);
        int (* pid_filter) (struct dvb_usb_adapter *, int, u16, int);
        int (* frontend_attach) (struct dvb_usb_adapter *);
        int (* tuner_attach) (struct dvb_usb_adapter *);
        struct usb_data_stream_properties stream;
        int size_of_priv;
    }

.. _`dvb_usb_adapter_fe_properties.members`:

Members
-------

caps
    capabilities of the DVB USB device.

pid_filter_count
    number of PID filter position in the optional hardware
    PID-filter.

streaming_ctrl
    called to start and stop the MPEG2-TS streaming of the
    device (not URB submitting/killing).

pid_filter_ctrl
    called to en/disable the PID filter, if any.

pid_filter
    called to set/unset a PID for filtering.

frontend_attach
    called to attach the possible frontends (fill fe-field
    of struct dvb_usb_device).

tuner_attach
    called to attach the correct tuner and to fill pll_addr,
    pll_desc and pll_init_buf of struct dvb_usb_device).

stream
    configuration of the USB streaming

size_of_priv
    *undescribed*

.. _`dvb_rc_legacy`:

struct dvb_rc_legacy
====================

.. c:type:: struct dvb_rc_legacy

    old properties of remote controller

.. _`dvb_rc_legacy.definition`:

Definition
----------

.. code-block:: c

    struct dvb_rc_legacy {
        #define REMOTE_NO_KEY_PRESSED 0x00
        #define REMOTE_KEY_PRESSED 0x01
        #define REMOTE_KEY_REPEAT 0x02
        struct rc_map_table *rc_map_table;
        int rc_map_size;
        int (* rc_query) (struct dvb_usb_device *, u32 *, int *);
        int rc_interval;
    }

.. _`dvb_rc_legacy.members`:

Members
-------

rc_map_table
    a hard-wired array of struct rc_map_table (NULL to disable
    remote control handling).

rc_map_size
    number of items in \ ``rc_map_table``\ .

rc_query
    called to query an event event.

rc_interval
    time in ms between two queries.

.. _`dvb_rc`:

struct dvb_rc
=============

.. c:type:: struct dvb_rc

    core

.. _`dvb_rc.definition`:

Definition
----------

.. code-block:: c

    struct dvb_rc {
        char *rc_codes;
        u64 protocol;
        u64 allowed_protos;
        enum rc_driver_type driver_type;
        int (* change_protocol) (struct rc_dev *dev, u64 *rc_type);
        char *module_name;
        int (* rc_query) (struct dvb_usb_device *d);
        int rc_interval;
        bool bulk_mode;
    }

.. _`dvb_rc.members`:

Members
-------

rc_codes
    name of rc codes table

protocol
    type of protocol(s) currently used by the driver

allowed_protos
    protocol(s) supported by the driver

driver_type
    Used to point if a device supports raw mode

change_protocol
    callback to change protocol

module_name
    *undescribed*

rc_query
    called to query an event event.

rc_interval
    time in ms between two queries.

bulk_mode
    device supports bulk mode for RC (disable polling mode)

.. _`dvb_usb_mode`:

enum dvb_usb_mode
=================

.. c:type:: enum dvb_usb_mode

    Specifies if it is using a legacy driver or a new one based on rc-core This is initialized/used only inside dvb-usb-remote.c. It shouldn't be set by the drivers.

.. _`dvb_usb_mode.definition`:

Definition
----------

.. code-block:: c

    enum dvb_usb_mode {
        DVB_RC_LEGACY,
        DVB_RC_CORE
    };

.. _`dvb_usb_mode.constants`:

Constants
---------

DVB_RC_LEGACY
    *undescribed*

DVB_RC_CORE
    *undescribed*

.. _`dvb_usb_fe_adapter`:

struct dvb_usb_fe_adapter
=========================

.. c:type:: struct dvb_usb_fe_adapter

    a DVB adapter on a USB device

.. _`dvb_usb_fe_adapter.definition`:

Definition
----------

.. code-block:: c

    struct dvb_usb_fe_adapter {
        struct dvb_frontend *fe;
        int (* fe_init) (struct dvb_frontend *);
        int (* fe_sleep) (struct dvb_frontend *);
        struct usb_data_stream stream;
        int pid_filtering;
        int max_feed_count;
        void *priv;
    }

.. _`dvb_usb_fe_adapter.members`:

Members
-------

fe
    *undescribed*

fe_init
    rerouted frontend-init (wakeup) function.

fe_sleep
    rerouted frontend-sleep function.

stream
    the usb data stream.

pid_filtering
    is hardware pid_filtering used or not.

max_feed_count
    how many feeds can be handled simultaneously by this
    device

priv
    *undescribed*

.. _`dvb_usb_device`:

struct dvb_usb_device
=====================

.. c:type:: struct dvb_usb_device

    object of a DVB USB device

.. _`dvb_usb_device.definition`:

Definition
----------

.. code-block:: c

    struct dvb_usb_device {
        struct dvb_usb_device_properties props;
        struct dvb_usb_device_description *desc;
        struct usb_device *udev;
        #define DVB_USB_STATE_INIT 0x000
        #define DVB_USB_STATE_I2C 0x001
        #define DVB_USB_STATE_DVB 0x002
        #define DVB_USB_STATE_REMOTE 0x004
        int state;
        int powered;
        struct mutex usb_mutex;
        struct mutex i2c_mutex;
        struct i2c_adapter i2c_adap;
        int num_adapters_initialized;
        struct dvb_usb_adapter adapter[MAX_NO_OF_ADAPTER_PER_DEVICE];
        struct rc_dev *rc_dev;
        struct input_dev *input_dev;
        char rc_phys[64];
        struct delayed_work rc_query_work;
        u32 last_event;
        int last_state;
        struct module *owner;
        void *priv;
    }

.. _`dvb_usb_device.members`:

Members
-------

props
    copy of the struct dvb_usb_properties this device belongs to.

desc
    pointer to the device's struct dvb_usb_device_description.

udev
    pointer to the device's struct usb_device.

state
    initialization and runtime state of the device.

powered
    indicated whether the device is power or not.
    Powered is in/decremented for each call to modify the state.

usb_mutex
    semaphore of USB control messages (reading needs two messages)

i2c_mutex
    semaphore for i2c-transfers

i2c_adap
    device's i2c_adapter if it uses I2CoverUSB

num_adapters_initialized
    *undescribed*

rc_dev
    rc device for the remote control (rc-core mode)

input_dev
    input device for the remote control (legacy mode)

rc_query_work
    struct work_struct frequent rc queries

last_event
    last triggered event

last_state
    last state (no, pressed, repeat)

owner
    owner of the dvb_adapter

priv
    private data of the actual driver (allocate by dvb-usb, size defined
    in size_of_priv of dvb_usb_properties).

.. This file was automatic generated / don't edit.

