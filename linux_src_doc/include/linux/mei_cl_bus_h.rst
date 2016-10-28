.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mei_cl_bus.h

.. _`mei_cl_device`:

struct mei_cl_device
====================

.. c:type:: struct mei_cl_device

    MEI device handle An mei_cl_device pointer is returned from \ :c:func:`mei_add_device`\  and links MEI bus clients to their actual ME host client pointer. Drivers for MEI devices will get an mei_cl_device pointer when being probed and shall use it for doing ME bus I/O.

.. _`mei_cl_device.definition`:

Definition
----------

.. code-block:: c

    struct mei_cl_device {
        struct list_head bus_list;
        struct mei_device *bus;
        struct device dev;
        struct mei_me_client *me_cl;
        struct mei_cl *cl;
        char name[MEI_CL_NAME_SIZE];
        struct work_struct event_work;
        mei_cldev_event_cb_t event_cb;
        void *event_context;
        unsigned long events_mask;
        unsigned long events;
        unsigned int do_match:1;
        unsigned int is_added:1;
        void *priv_data;
    }

.. _`mei_cl_device.members`:

Members
-------

bus_list
    device on the bus list

bus
    parent mei device

dev
    linux driver model device pointer

me_cl
    me client

cl
    mei client

name
    device name

event_work
    async work to execute event callback

event_cb
    Drivers register this callback to get asynchronous ME
    events (e.g. Rx buffer pending) notifications.

event_context
    event callback run context

events_mask
    Events bit mask requested by driver.

events
    Events bitmask sent to the driver.

do_match
    wheather device can be matched with a driver

is_added
    device is already scanned

priv_data
    client private data

.. This file was automatic generated / don't edit.

