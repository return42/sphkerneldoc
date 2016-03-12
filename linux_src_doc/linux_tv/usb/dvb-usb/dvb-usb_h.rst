.. -*- coding: utf-8; mode: rst -*-

=========
dvb-usb.h
=========



.. _xref_struct_dvb_usb_device_description:

struct dvb_usb_device_description
=================================

.. c:type:: struct dvb_usb_device_description

    name and its according USB IDs



Definition
----------

.. code-block:: c

  struct dvb_usb_device_description {
    const char * name;
    #define DVB_USB_ID_MAX_NUM 15
    struct usb_device_id * cold_ids[DVB_USB_ID_MAX_NUM];
    struct usb_device_id * warm_ids[DVB_USB_ID_MAX_NUM];
  };



Members
-------

:``const char * name``:
    real name of the box, regardless which DVB USB device class is in use

:``struct usb_device_id * cold_ids[DVB_USB_ID_MAX_NUM]``:
    array of struct usb_device_id which describe the device in
     pre-firmware state

:``struct usb_device_id * warm_ids[DVB_USB_ID_MAX_NUM]``:
    array of struct usb_device_id which describe the device in
     post-firmware state




Description
-----------

Each DVB USB device class can have one or more actual devices, this struct
assigns a name to it.




.. _xref_struct_dvb_usb_adapter_fe_properties:

struct dvb_usb_adapter_fe_properties
====================================

.. c:type:: struct dvb_usb_adapter_fe_properties

    properties of a dvb-usb-adapter. A DVB-USB-Adapter is basically a dvb_adapter which is present on a USB-device.



Definition
----------

.. code-block:: c

  struct dvb_usb_adapter_fe_properties {
    #define DVB_USB_ADAP_HAS_PID_FILTER               0x01
    #define DVB_USB_ADAP_PID_FILTER_CAN_BE_TURNED_OFF 0x02
    #define DVB_USB_ADAP_NEED_PID_FILTERING           0x04
    #define DVB_USB_ADAP_RECEIVES_204_BYTE_TS         0x08
    #define DVB_USB_ADAP_RECEIVES_RAW_PAYLOAD         0x10
    int caps;
    int pid_filter_count;
    int (* streaming_ctrl) (struct dvb_usb_adapter *, int);
    int (* pid_filter_ctrl) (struct dvb_usb_adapter *, int);
    int (* pid_filter) (struct dvb_usb_adapter *, int, u16, int);
    int (* frontend_attach) (struct dvb_usb_adapter *);
    int (* tuner_attach) (struct dvb_usb_adapter *);
    struct usb_data_stream_properties stream;
  };



Members
-------

:``int caps``:
    capabilities of the DVB USB device.

:``int pid_filter_count``:
    number of PID filter position in the optional hardware
     PID-filter.

:``int (*)  (struct dvb_usb_adapter *, int) streaming_ctrl``:
    called to start and stop the MPEG2-TS streaming of the
     device (not URB submitting/killing).

:``int (*) (struct dvb_usb_adapter *, int) pid_filter_ctrl``:
    called to en/disable the PID filter, if any.

:``int (*)      (struct dvb_usb_adapter *, int, u16, int) pid_filter``:
    called to set/unset a PID for filtering.

:``int (*) (struct dvb_usb_adapter *) frontend_attach``:
    called to attach the possible frontends (fill fe-field
     of struct dvb_usb_device).

:``int (*)    (struct dvb_usb_adapter *) tuner_attach``:
    called to attach the correct tuner and to fill pll_addr,
     pll_desc and pll_init_buf of struct dvb_usb_device).

:``struct usb_data_stream_properties stream``:
    configuration of the USB streaming





.. _xref_struct_dvb_rc_legacy:

struct dvb_rc_legacy
====================

.. c:type:: struct dvb_rc_legacy

    old properties of remote controller



Definition
----------

.. code-block:: c

  struct dvb_rc_legacy {
    #define REMOTE_NO_KEY_PRESSED      0x00
    #define REMOTE_KEY_PRESSED         0x01
    #define REMOTE_KEY_REPEAT          0x02
    struct rc_map_table * rc_map_table;
    int rc_map_size;
    int (* rc_query) (struct dvb_usb_device *, u32 *, int *);
    int rc_interval;
  };



Members
-------

:``struct rc_map_table * rc_map_table``:
    a hard-wired array of struct rc_map_table (NULL to disable
     remote control handling).

:``int rc_map_size``:
    number of items in **rc_map_table**.

:``int (*) (struct dvb_usb_device *, u32 *, int *) rc_query``:
    called to query an event event.

:``int rc_interval``:
    time in ms between two queries.





.. _xref_enum dvb_usb_mode:

enum dvb_usb_mode
=================

.. c:type:: enum dvb_usb_mode

    Specifies if it is using a legacy driver or a new one based on rc-core This is initialized/used only inside dvb-usb-remote.c. It shouldn't be set by the drivers.



Constants
---------

:``DVB_RC_LEGACY``:
    -- undescribed --

:``DVB_RC_CORE``:
    -- undescribed --




.. _xref_struct_dvb_usb_fe_adapter:

struct dvb_usb_fe_adapter
=========================

.. c:type:: struct dvb_usb_fe_adapter

    a DVB adapter on a USB device



Definition
----------

.. code-block:: c

  struct dvb_usb_fe_adapter {
    int (* fe_init) (struct dvb_frontend *);
    int (* fe_sleep) (struct dvb_frontend *);
    struct usb_data_stream stream;
    int pid_filtering;
    int max_feed_count;
  };



Members
-------

:``int (*)  (struct dvb_frontend *) fe_init``:
    rerouted frontend-init (wakeup) function.

:``int (*) (struct dvb_frontend *) fe_sleep``:
    rerouted frontend-sleep function.

:``struct usb_data_stream stream``:
    the usb data stream.

:``int pid_filtering``:
    is hardware pid_filtering used or not.

:``int max_feed_count``:
    how many feeds can be handled simultaneously by this
     device





.. _xref_struct_dvb_usb_device:

struct dvb_usb_device
=====================

.. c:type:: struct dvb_usb_device

    object of a DVB USB device



Definition
----------

.. code-block:: c

  struct dvb_usb_device {
    struct dvb_usb_device_properties props;
    struct dvb_usb_device_description * desc;
    struct usb_device * udev;
    #define DVB_USB_STATE_INIT        0x000
    #define DVB_USB_STATE_I2C         0x001
    #define DVB_USB_STATE_DVB         0x002
    #define DVB_USB_STATE_REMOTE      0x004
    int state;
    int powered;
    struct mutex usb_mutex;
    struct mutex i2c_mutex;
    struct i2c_adapter i2c_adap;
    struct rc_dev * rc_dev;
    struct input_dev * input_dev;
    struct delayed_work rc_query_work;
    u32 last_event;
    int last_state;
    struct module * owner;
    void * priv;
  };



Members
-------

:``struct dvb_usb_device_properties props``:
    copy of the struct dvb_usb_properties this device belongs to.

:``struct dvb_usb_device_description * desc``:
    pointer to the device's struct dvb_usb_device_description.

:``struct usb_device * udev``:
    pointer to the device's struct usb_device.

:``int state``:
    initialization and runtime state of the device.

:``int powered``:
    indicated whether the device is power or not.
     Powered is in/decremented for each call to modify the state.

:``struct mutex usb_mutex``:
    semaphore of USB control messages (reading needs two messages)

:``struct mutex i2c_mutex``:
    semaphore for i2c-transfers

:``struct i2c_adapter i2c_adap``:
    device's i2c_adapter if it uses I2CoverUSB

:``struct rc_dev * rc_dev``:
    rc device for the remote control (rc-core mode)

:``struct input_dev * input_dev``:
    input device for the remote control (legacy mode)

:``struct delayed_work rc_query_work``:
    struct work_struct frequent rc queries

:``u32 last_event``:
    last triggered event

:``int last_state``:
    last state (no, pressed, repeat)

:``struct module * owner``:
    owner of the dvb_adapter

:``void * priv``:
    private data of the actual driver (allocate by dvb-usb, size defined
     in size_of_priv of dvb_usb_properties).



