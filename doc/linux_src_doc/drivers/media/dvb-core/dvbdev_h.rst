.. -*- coding: utf-8; mode: rst -*-

========
dvbdev.h
========



.. _xref_struct_dvb_adapter:

struct dvb_adapter
==================

.. c:type:: struct dvb_adapter

    represents a Digital TV adapter using Linux DVB API



Definition
----------

.. code-block:: c

  struct dvb_adapter {
    int num;
    struct list_head list_head;
    struct list_head device_list;
    const char * name;
    u8 proposed_mac[6];
    void * priv;
    struct device * device;
    struct module * module;
    int mfe_shared;
    struct dvb_device * mfe_dvbdev;
    struct mutex mfe_lock;
    #if defined(CONFIG_MEDIA_CONTROLLER_DVB)
    struct media_device * mdev;
    struct media_entity * conn;
    struct media_pad * conn_pads;
    #endif
  };



Members
-------

:``int num``:
    Number of the adapter

:``struct list_head list_head``:
    List with the DVB adapters

:``struct list_head device_list``:
    List with the DVB devices

:``const char * name``:
    Name of the adapter

:``u8 proposed_mac[6]``:
    proposed MAC address for the adapter

:``void * priv``:
    private data

:``struct device * device``:
    pointer to struct device

:``struct module * module``:
    pointer to struct module

:``int mfe_shared``:
    mfe shared: indicates mutually exclusive frontends
    			Thie usage of this flag is currently deprecated

:``struct dvb_device * mfe_dvbdev``:
    Frontend device in use, in the case of MFE

:``struct mutex mfe_lock``:
    Lock to prevent using the other frontends when MFE is
    			used.

:``struct media_device * mdev``:
    pointer to struct media_device, used when the media
    			controller is used.

:``struct media_entity * conn``:
    RF connector. Used only if the device has no separate
    			tuner.

:``struct media_pad * conn_pads``:
    pointer to struct media_pad associated with **conn**;





.. _xref_struct_dvb_device:

struct dvb_device
=================

.. c:type:: struct dvb_device

    represents a DVB device node



Definition
----------

.. code-block:: c

  struct dvb_device {
    struct list_head list_head;
    const struct file_operations * fops;
    struct dvb_adapter * adapter;
    int type;
    int minor;
    u32 id;
    int readers;
    int writers;
    int users;
    wait_queue_head_t wait_queue;
    int (* kernel_ioctl) (struct file *file, unsigned int cmd, void *arg);
    #if defined(CONFIG_MEDIA_CONTROLLER_DVB)
    const char * name;
    struct media_intf_devnode * intf_devnode;
    unsigned tsout_num_entities;
    struct media_entity * entity;
    struct media_entity * tsout_entity;
    struct media_pad * pads;
    struct media_pad * tsout_pads;
    #endif
    void * priv;
  };



Members
-------

:``struct list_head list_head``:
    List head with all DVB devices

:``const struct file_operations * fops``:
    pointer to struct file_operations

:``struct dvb_adapter * adapter``:
    pointer to the adapter that holds this device node

:``int type``:
    type of the device: DVB_DEVICE_SEC, DVB_DEVICE_FRONTEND,
    		DVB_DEVICE_DEMUX, DVB_DEVICE_DVR, DVB_DEVICE_CA, DVB_DEVICE_NET

:``int minor``:
    devnode minor number. Major number is always DVB_MAJOR.

:``u32 id``:
    device ID number, inside the adapter

:``int readers``:
    Initialized by the caller. Each call to :c:func:`open` in Read Only mode
    		decreases this counter by one.

:``int writers``:
    Initialized by the caller. Each call to :c:func:`open` in Read/Write
    		mode decreases this counter by one.

:``int users``:
    Initialized by the caller. Each call to :c:func:`open` in any mode
    		decreases this counter by one.

:``wait_queue_head_t wait_queue``:
    wait queue, used to wait for certain events inside one of
    		the DVB API callers

:``int (*)(struct file *file, unsigned int cmd, void *arg) kernel_ioctl``:
    callback function used to handle ioctl calls from userspace.

:``const char * name``:
    Name to be used for the device at the Media Controller

:``struct media_intf_devnode * intf_devnode``:
    Pointer to media_intf_devnode. Used by the dvbdev core to
    		store the MC device node interface

:``unsigned tsout_num_entities``:
    Number of Transport Stream output entities

:``struct media_entity * entity``:
    pointer to struct media_entity associated with the device node

:``struct media_entity * tsout_entity``:
    array with MC entities associated to each TS output node

:``struct media_pad * pads``:
    pointer to struct media_pad associated with **entity**;

:``struct media_pad * tsout_pads``:
    array with the source pads for each **tsout_entity**

:``void * priv``:
    private data




Description
-----------

This structure is used by the DVB core (frontend, CA, net, demux) in
order to create the device nodes. Usually, driver should not initialize
this struct diretly.




.. _xref_dvb_register_adapter:

dvb_register_adapter
====================

.. c:function:: int dvb_register_adapter (struct dvb_adapter * adap, const char * name, struct module * module, struct device * device, short * adapter_nums)

    Registers a new DVB adapter

    :param struct dvb_adapter * adap:
        pointer to struct dvb_adapter

    :param const char * name:
        Adapter's name

    :param struct module * module:
        initialized with THIS_MODULE at the caller

    :param struct device * device:
        pointer to struct device that corresponds to the device driver

    :param short * adapter_nums:
        Array with a list of the numbers for **dvb_register_adapter**;
        		to select among them. Typically, initialized with:
        		DVB_DEFINE_MOD_OPT_ADAPTER_NR(adapter_nums)




.. _xref_dvb_unregister_adapter:

dvb_unregister_adapter
======================

.. c:function:: int dvb_unregister_adapter (struct dvb_adapter * adap)

    Unregisters a DVB adapter

    :param struct dvb_adapter * adap:
        pointer to struct dvb_adapter




.. _xref_dvb_register_device:

dvb_register_device
===================

.. c:function:: int dvb_register_device (struct dvb_adapter * adap, struct dvb_device ** pdvbdev, const struct dvb_device * template, void * priv, int type, int demux_sink_pads)

    Registers a new DVB device

    :param struct dvb_adapter * adap:
        pointer to struct dvb_adapter

    :param struct dvb_device ** pdvbdev:
        pointer to the place where the new struct dvb_device will be
        		stored

    :param const struct dvb_device * template:
        Template used to create :c:type:`struct pdvbdev <pdvbdev>`;

    :param void * priv:
        private data

    :param int type:
        type of the device: ``DVB_DEVICE_SEC``, ``DVB_DEVICE_FRONTEND``,
        		``DVB_DEVICE_DEMUX``, ``DVB_DEVICE_DVR``, ``DVB_DEVICE_CA``,
        		``DVB_DEVICE_NET``

    :param int demux_sink_pads:
        Number of demux outputs, to be used to create the TS
        		outputs via the Media Controller.




.. _xref_dvb_unregister_device:

dvb_unregister_device
=====================

.. c:function:: void dvb_unregister_device (struct dvb_device * dvbdev)

    Unregisters a DVB device

    :param struct dvb_device * dvbdev:
        pointer to struct dvb_device




.. _xref_dvb_create_media_graph:

dvb_create_media_graph
======================

.. c:function:: int dvb_create_media_graph (struct dvb_adapter * adap, bool create_rf_connector)

    Creates media graph for the Digital TV part of the device.

    :param struct dvb_adapter * adap:
        pointer to struct dvb_adapter

    :param bool create_rf_connector:
        if true, it creates the RF connector too



Description
-----------

This function checks all DVB-related functions at the media controller
entities and creates the needed links for the media graph. It is
capable of working with multiple tuners or multiple frontends, but it
won't create links if the device has multiple tuners and multiple frontends
or if the device has multiple muxes. In such case, the caller driver should
manually create the remaining links.


