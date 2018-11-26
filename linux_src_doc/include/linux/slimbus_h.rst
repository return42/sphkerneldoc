.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/slimbus.h

.. _`slim_eaddr`:

struct slim_eaddr
=================

.. c:type:: struct slim_eaddr

    Enumeration address for a SLIMbus device

.. _`slim_eaddr.definition`:

Definition
----------

.. code-block:: c

    struct slim_eaddr {
        u8 instance;
        u8 dev_index;
        u16 prod_code;
        u16 manf_id;
    }

.. _`slim_eaddr.members`:

Members
-------

instance
    Instance value

dev_index
    Device index

prod_code
    Product code

manf_id
    Manufacturer Id for the device

.. _`slim_device_status`:

enum slim_device_status
=======================

.. c:type:: enum slim_device_status

    slim device status

.. _`slim_device_status.definition`:

Definition
----------

.. code-block:: c

    enum slim_device_status {
        SLIM_DEVICE_STATUS_DOWN,
        SLIM_DEVICE_STATUS_UP,
        SLIM_DEVICE_STATUS_RESERVED
    };

.. _`slim_device_status.constants`:

Constants
---------

SLIM_DEVICE_STATUS_DOWN
    Slim device is absent or not reported yet.

SLIM_DEVICE_STATUS_UP
    Slim device is announced on the bus.

SLIM_DEVICE_STATUS_RESERVED
    Reserved for future use.

.. _`slim_device`:

struct slim_device
==================

.. c:type:: struct slim_device

    Slim device handle.

.. _`slim_device.definition`:

Definition
----------

.. code-block:: c

    struct slim_device {
        struct device dev;
        struct slim_eaddr e_addr;
        struct slim_controller *ctrl;
        enum slim_device_status status;
        u8 laddr;
        bool is_laddr_valid;
        struct list_head stream_list;
        spinlock_t stream_list_lock;
    }

.. _`slim_device.members`:

Members
-------

dev
    Driver model representation of the device.

e_addr
    Enumeration address of this device.

ctrl
    slim controller instance.

status
    slim device status

laddr
    1-byte Logical address of this device.

is_laddr_valid
    indicates if the laddr is valid or not

stream_list
    List of streams on this device

stream_list_lock
    lock to protect the stream list

.. _`slim_device.description`:

Description
-----------

This is the client/device handle returned when a SLIMbus
device is registered with a controller.
Pointer to this structure is used by client-driver as a handle.

.. _`slim_driver`:

struct slim_driver
==================

.. c:type:: struct slim_driver

    SLIMbus 'generic device' (slave) device driver (similar to 'spi_device' on SPI)

.. _`slim_driver.definition`:

Definition
----------

.. code-block:: c

    struct slim_driver {
        int (*probe)(struct slim_device *sl);
        void (*remove)(struct slim_device *sl);
        void (*shutdown)(struct slim_device *sl);
        int (*device_status)(struct slim_device *sl, enum slim_device_status s);
        struct device_driver driver;
        const struct slim_device_id *id_table;
    }

.. _`slim_driver.members`:

Members
-------

probe
    Binds this driver to a SLIMbus device.

remove
    Unbinds this driver from the SLIMbus device.

shutdown
    Standard shutdown callback used during powerdown/halt.

device_status
    This callback is called when
    - The device reports present and gets a laddr assigned
    - The device reports absent, or the bus goes down.

driver
    SLIMbus device drivers should initialize name and owner field of
    this structure

id_table
    List of SLIMbus devices supported by this driver

.. _`slim_val_inf`:

struct slim_val_inf
===================

.. c:type:: struct slim_val_inf

    Slimbus value or information element

.. _`slim_val_inf.definition`:

Definition
----------

.. code-block:: c

    struct slim_val_inf {
        u16 start_offset;
        u8 num_bytes;
        u8 *rbuf;
        const u8 *wbuf;
        struct completion *comp;
    }

.. _`slim_val_inf.members`:

Members
-------

start_offset
    Specifies starting offset in information/value element map

num_bytes
    upto 16. This ensures that the message will fit the slicesize
    per SLIMbus spec

rbuf
    buffer to read the values

wbuf
    buffer to write

comp
    completion for asynchronous operations, valid only if TID is
    required for transaction, like REQUEST operations.
    Rest of the transactions are synchronous anyway.

.. _`slim_stream_config`:

struct slim_stream_config
=========================

.. c:type:: struct slim_stream_config

    SLIMbus stream configuration Configuring a stream is done at hw_params or prepare call from audio drivers where they have all the required information regarding rate, number of channels and so on. There is a 1:1 mapping of channel and ports.

.. _`slim_stream_config.definition`:

Definition
----------

.. code-block:: c

    struct slim_stream_config {
        unsigned int rate;
        unsigned int bps;
        unsigned int ch_count;
        unsigned int *chs;
        unsigned long port_mask;
        int direction;
    }

.. _`slim_stream_config.members`:

Members
-------

rate
    data rate

bps
    bits per data sample

ch_count
    number of channels

chs
    pointer to list of channel numbers

port_mask
    port mask of ports to use for this stream

direction
    direction of the stream, SNDRV_PCM_STREAM_PLAYBACK
    or SNDRV_PCM_STREAM_CAPTURE.

.. _`module_slim_driver`:

module_slim_driver
==================

.. c:function::  module_slim_driver( __slim_driver)

    Helper macro for registering a SLIMbus driver

    :param __slim_driver:
        slimbus_driver struct
    :type __slim_driver: 

.. _`module_slim_driver.description`:

Description
-----------

Helper macro for SLIMbus drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\ 

.. This file was automatic generated / don't edit.

