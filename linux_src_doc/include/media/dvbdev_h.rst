.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/dvbdev.h

.. _`dvb_device_type`:

enum dvb_device_type
====================

.. c:type:: enum dvb_device_type

    type of the Digital TV device

.. _`dvb_device_type.definition`:

Definition
----------

.. code-block:: c

    enum dvb_device_type {
        DVB_DEVICE_SEC,
        DVB_DEVICE_FRONTEND,
        DVB_DEVICE_DEMUX,
        DVB_DEVICE_DVR,
        DVB_DEVICE_CA,
        DVB_DEVICE_NET,
        DVB_DEVICE_VIDEO,
        DVB_DEVICE_AUDIO,
        DVB_DEVICE_OSD
    };

.. _`dvb_device_type.constants`:

Constants
---------

DVB_DEVICE_SEC
    Digital TV standalone Common Interface (CI)

DVB_DEVICE_FRONTEND
    Digital TV frontend.

DVB_DEVICE_DEMUX
    Digital TV demux.

DVB_DEVICE_DVR
    Digital TV digital video record (DVR).

DVB_DEVICE_CA
    Digital TV Conditional Access (CA).

DVB_DEVICE_NET
    Digital TV network.

DVB_DEVICE_VIDEO
    Digital TV video decoder.
    Deprecated. Used only on av7110-av.

DVB_DEVICE_AUDIO
    Digital TV audio decoder.
    Deprecated. Used only on av7110-av.

DVB_DEVICE_OSD
    Digital TV On Screen Display (OSD).
    Deprecated. Used only on av7110.

.. _`dvb_adapter`:

struct dvb_adapter
==================

.. c:type:: struct dvb_adapter

    represents a Digital TV adapter using Linux DVB API

.. _`dvb_adapter.definition`:

Definition
----------

.. code-block:: c

    struct dvb_adapter {
        int num;
        struct list_head list_head;
        struct list_head device_list;
        const char *name;
        u8 proposed_mac [6];
        void* priv;
        struct device *device;
        struct module *module;
        int mfe_shared;
        struct dvb_device *mfe_dvbdev;
        struct mutex mfe_lock;
    #if defined(CONFIG_MEDIA_CONTROLLER_DVB)
        struct media_device *mdev;
        struct media_entity *conn;
        struct media_pad *conn_pads;
    #endif
    }

.. _`dvb_adapter.members`:

Members
-------

num
    Number of the adapter

list_head
    List with the DVB adapters

device_list
    List with the DVB devices

name
    Name of the adapter

proposed_mac
    proposed MAC address for the adapter

priv
    private data

device
    pointer to struct device

module
    pointer to struct module

mfe_shared
    mfe shared: indicates mutually exclusive frontends
    Thie usage of this flag is currently deprecated

mfe_dvbdev
    Frontend device in use, in the case of MFE

mfe_lock
    Lock to prevent using the other frontends when MFE is
    used.

mdev
    pointer to struct media_device, used when the media
    controller is used.

conn
    RF connector. Used only if the device has no separate
    tuner.

conn_pads
    pointer to struct media_pad associated with \ ``conn``\ ;

.. _`dvb_device`:

struct dvb_device
=================

.. c:type:: struct dvb_device

    represents a DVB device node

.. _`dvb_device.definition`:

Definition
----------

.. code-block:: c

    struct dvb_device {
        struct list_head list_head;
        const struct file_operations *fops;
        struct dvb_adapter *adapter;
        enum dvb_device_type type;
        int minor;
        u32 id;
        int readers;
        int writers;
        int users;
        wait_queue_head_t wait_queue;
        int (*kernel_ioctl)(struct file *file, unsigned int cmd, void *arg);
    #if defined(CONFIG_MEDIA_CONTROLLER_DVB)
        const char *name;
        struct media_intf_devnode *intf_devnode;
        unsigned tsout_num_entities;
        struct media_entity *entity, *tsout_entity;
        struct media_pad *pads, *tsout_pads;
    #endif
        void *priv;
    }

.. _`dvb_device.members`:

Members
-------

list_head
    List head with all DVB devices

fops
    pointer to struct file_operations

adapter
    pointer to the adapter that holds this device node

type
    type of the device, as defined by \ :c:type:`enum dvb_device_type <dvb_device_type>`\ .

minor
    devnode minor number. Major number is always DVB_MAJOR.

id
    device ID number, inside the adapter

readers
    Initialized by the caller. Each call to \ :c:func:`open`\  in Read Only mode
    decreases this counter by one.

writers
    Initialized by the caller. Each call to \ :c:func:`open`\  in Read/Write
    mode decreases this counter by one.

users
    Initialized by the caller. Each call to \ :c:func:`open`\  in any mode
    decreases this counter by one.

wait_queue
    wait queue, used to wait for certain events inside one of
    the DVB API callers

kernel_ioctl
    callback function used to handle ioctl calls from userspace.

name
    Name to be used for the device at the Media Controller

intf_devnode
    Pointer to media_intf_devnode. Used by the dvbdev core to
    store the MC device node interface

tsout_num_entities
    Number of Transport Stream output entities

entity
    pointer to struct media_entity associated with the device node

tsout_entity
    array with MC entities associated to each TS output node

pads
    pointer to struct media_pad associated with \ ``entity``\ ;

tsout_pads
    array with the source pads for each \ ``tsout_entity``\ 

priv
    private data

.. _`dvb_device.description`:

Description
-----------

This structure is used by the DVB core (frontend, CA, net, demux) in
order to create the device nodes. Usually, driver should not initialize
this struct diretly.

.. _`dvb_register_adapter`:

dvb_register_adapter
====================

.. c:function:: int dvb_register_adapter(struct dvb_adapter *adap, const char *name, struct module *module, struct device *device, short *adapter_nums)

    Registers a new DVB adapter

    :param struct dvb_adapter \*adap:
        pointer to struct dvb_adapter

    :param const char \*name:
        Adapter's name

    :param struct module \*module:
        initialized with THIS_MODULE at the caller

    :param struct device \*device:
        pointer to struct device that corresponds to the device driver

    :param short \*adapter_nums:
        Array with a list of the numbers for \ ``dvb_register_adapter``\ ;
        to select among them. Typically, initialized with:
        DVB_DEFINE_MOD_OPT_ADAPTER_NR(adapter_nums)

.. _`dvb_unregister_adapter`:

dvb_unregister_adapter
======================

.. c:function:: int dvb_unregister_adapter(struct dvb_adapter *adap)

    Unregisters a DVB adapter

    :param struct dvb_adapter \*adap:
        pointer to struct dvb_adapter

.. _`dvb_register_device`:

dvb_register_device
===================

.. c:function:: int dvb_register_device(struct dvb_adapter *adap, struct dvb_device **pdvbdev, const struct dvb_device *template, void *priv, enum dvb_device_type type, int demux_sink_pads)

    Registers a new DVB device

    :param struct dvb_adapter \*adap:
        pointer to struct dvb_adapter

    :param struct dvb_device \*\*pdvbdev:
        pointer to the place where the new struct dvb_device will be
        stored

    :param const struct dvb_device \*template:
        Template used to create \ :c:type:`struct pdvbdev <pdvbdev>`\ ;

    :param void \*priv:
        private data

    :param enum dvb_device_type type:
        type of the device, as defined by \ :c:type:`enum dvb_device_type <dvb_device_type>`\ .

    :param int demux_sink_pads:
        Number of demux outputs, to be used to create the TS
        outputs via the Media Controller.

.. _`dvb_remove_device`:

dvb_remove_device
=================

.. c:function:: void dvb_remove_device(struct dvb_device *dvbdev)

    Remove a registered DVB device

    :param struct dvb_device \*dvbdev:
        pointer to struct dvb_device

.. _`dvb_remove_device.description`:

Description
-----------

This does not free memory.  To do that, call \ :c:func:`dvb_free_device`\ .

.. _`dvb_free_device`:

dvb_free_device
===============

.. c:function:: void dvb_free_device(struct dvb_device *dvbdev)

    Free memory occupied by a DVB device.

    :param struct dvb_device \*dvbdev:
        pointer to struct dvb_device

.. _`dvb_free_device.description`:

Description
-----------

Call \ :c:func:`dvb_unregister_device`\  before calling this function.

.. _`dvb_unregister_device`:

dvb_unregister_device
=====================

.. c:function:: void dvb_unregister_device(struct dvb_device *dvbdev)

    Unregisters a DVB device

    :param struct dvb_device \*dvbdev:
        pointer to struct dvb_device

.. _`dvb_unregister_device.description`:

Description
-----------

This is a combination of \ :c:func:`dvb_remove_device`\  and \ :c:func:`dvb_free_device`\ .
Using this function is usually a mistake, and is often an indicator
for a use-after-free bug (when a userspace process keeps a file
handle to a detached device).

.. _`dvb_create_media_graph`:

dvb_create_media_graph
======================

.. c:function:: int dvb_create_media_graph(struct dvb_adapter *adap, bool create_rf_connector)

    Creates media graph for the Digital TV part of the device.

    :param struct dvb_adapter \*adap:
        pointer to \ :c:type:`struct dvb_adapter <dvb_adapter>`\ 

    :param bool create_rf_connector:
        if true, it creates the RF connector too

.. _`dvb_create_media_graph.description`:

Description
-----------

This function checks all DVB-related functions at the media controller
entities and creates the needed links for the media graph. It is
capable of working with multiple tuners or multiple frontends, but it
won't create links if the device has multiple tuners and multiple frontends
or if the device has multiple muxes. In such case, the caller driver should
manually create the remaining links.

.. _`dvb_register_media_controller`:

dvb_register_media_controller
=============================

.. c:function:: void dvb_register_media_controller(struct dvb_adapter *adap, struct media_device *mdev)

    registers a media controller at DVB adapter

    :param struct dvb_adapter \*adap:
        pointer to \ :c:type:`struct dvb_adapter <dvb_adapter>`\ 

    :param struct media_device \*mdev:
        pointer to \ :c:type:`struct media_device <media_device>`\ 

.. _`dvb_get_media_controller`:

dvb_get_media_controller
========================

.. c:function:: struct media_device *dvb_get_media_controller(struct dvb_adapter *adap)

    gets the associated media controller

    :param struct dvb_adapter \*adap:
        pointer to \ :c:type:`struct dvb_adapter <dvb_adapter>`\ 

.. _`dvb_generic_open`:

dvb_generic_open
================

.. c:function:: int dvb_generic_open(struct inode *inode, struct file *file)

    Digital TV open function, used by DVB devices

    :param struct inode \*inode:
        pointer to \ :c:type:`struct inode <inode>`\ .

    :param struct file \*file:
        pointer to \ :c:type:`struct file <file>`\ .

.. _`dvb_generic_open.description`:

Description
-----------

Checks if a DVB devnode is still valid, and if the permissions are
OK and increment negative use count.

.. _`dvb_generic_release`:

dvb_generic_release
===================

.. c:function:: int dvb_generic_release(struct inode *inode, struct file *file)

    Digital TV close function, used by DVB devices

    :param struct inode \*inode:
        pointer to \ :c:type:`struct inode <inode>`\ .

    :param struct file \*file:
        pointer to \ :c:type:`struct file <file>`\ .

.. _`dvb_generic_release.description`:

Description
-----------

Checks if a DVB devnode is still valid, and if the permissions are
OK and decrement negative use count.

.. _`dvb_generic_ioctl`:

dvb_generic_ioctl
=================

.. c:function:: long dvb_generic_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    Digital TV close function, used by DVB devices

    :param struct file \*file:
        pointer to \ :c:type:`struct file <file>`\ .

    :param unsigned int cmd:
        Ioctl name.

    :param unsigned long arg:
        Ioctl argument.

.. _`dvb_generic_ioctl.description`:

Description
-----------

Checks if a DVB devnode and struct dvbdev.kernel_ioctl is still valid.
If so, calls \ :c:func:`dvb_usercopy`\ .

.. _`dvb_usercopy`:

dvb_usercopy
============

.. c:function:: int dvb_usercopy(struct file *file, unsigned int cmd, unsigned long arg, int (*func)(struct file *file, unsigned int cmd, void *arg))

    copies data from/to userspace memory when an ioctl is issued.

    :param struct file \*file:
        Pointer to struct \ :c:type:`struct file <file>`\ .

    :param unsigned int cmd:
        Ioctl name.

    :param unsigned long arg:
        Ioctl argument.

    :param int (\*func)(struct file \*file, unsigned int cmd, void \*arg):
        function that will actually handle the ioctl

.. _`dvb_usercopy.description`:

Description
-----------

Ancillary function that uses ioctl direction and size to copy from
userspace. Then, it calls \ ``func``\ , and, if needed, data is copied back
to userspace.

.. _`dvb_attach`:

dvb_attach
==========

.. c:function::  dvb_attach( FUNCTION,  ARGS...)

    attaches a DVB frontend into the DVB core.

    :param  FUNCTION:
        function on a frontend module to be called.

.. _`dvb_attach.description`:

Description
-----------

This ancillary function loads a frontend module in runtime and runs
the \ ``FUNCTION``\  function there, with \ ``ARGS``\ .
As it increments symbol usage cont, at unregister, \ :c:func:`dvb_detach`\ 
should be called.

.. _`dvb_detach`:

dvb_detach
==========

.. c:function::  dvb_detach( FUNC)

    detaches a DVB frontend loaded via \ :c:func:`dvb_attach`\ 

    :param  FUNC:
        attach function

.. _`dvb_detach.description`:

Description
-----------

Decrements usage count for a function previously called via \ :c:func:`dvb_attach`\ .

.. This file was automatic generated / don't edit.

