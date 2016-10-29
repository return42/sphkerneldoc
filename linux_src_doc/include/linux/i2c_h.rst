.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/i2c.h

.. _`i2c_driver`:

struct i2c_driver
=================

.. c:type:: struct i2c_driver

    represent an I2C device driver

.. _`i2c_driver.definition`:

Definition
----------

.. code-block:: c

    struct i2c_driver {
        unsigned int class;
        int (*attach_adapter)(struct i2c_adapter *);
        int (*probe)(struct i2c_client *, const struct i2c_device_id *);
        int (*remove)(struct i2c_client *);
        void (*shutdown)(struct i2c_client *);
        void (*alert)(struct i2c_client *, unsigned int data);
        int (*command)(struct i2c_client *client, unsigned int cmd, void *arg);
        struct device_driver driver;
        const struct i2c_device_id *id_table;
        int (*detect)(struct i2c_client *, struct i2c_board_info *);
        const unsigned short *address_list;
        struct list_head clients;
    }

.. _`i2c_driver.members`:

Members
-------

class
    What kind of i2c device we instantiate (for detect)

attach_adapter
    Callback for bus addition (deprecated)

probe
    Callback for device binding

remove
    Callback for device unbinding

shutdown
    Callback for device shutdown

alert
    Alert callback, for example for the SMBus alert protocol

command
    Callback for bus-wide signaling (optional)

driver
    Device driver model driver

id_table
    List of I2C devices supported by this driver

detect
    Callback for device detection

address_list
    The I2C addresses to probe (for detect)

clients
    List of detected clients we created (for i2c-core use only)

.. _`i2c_driver.description`:

Description
-----------

The driver.owner field should be set to the module owner of this driver.
The driver.name field should be set to the name of this driver.

For automatic device detection, both \ ``detect``\  and \ ``address_list``\  must
be defined. \ ``class``\  should also be set, otherwise only devices forced
with module parameters will be created. The detect function must
fill at least the name field of the i2c_board_info structure it is
handed upon successful detection, and possibly also the flags field.

If \ ``detect``\  is missing, the driver will still work fine for enumerated
devices. Detected devices simply won't be supported. This is expected
for the many I2C/SMBus devices which can't be detected reliably, and
the ones which can always be enumerated in practice.

The i2c_client structure which is handed to the \ ``detect``\  callback is
not a real i2c_client. It is initialized just enough so that you can
call i2c_smbus_read_byte_data and friends on it. Don't do anything
else with it. In particular, calling dev_dbg and friends on it is
not allowed.

.. _`i2c_client`:

struct i2c_client
=================

.. c:type:: struct i2c_client

    represent an I2C slave device

.. _`i2c_client.definition`:

Definition
----------

.. code-block:: c

    struct i2c_client {
        unsigned short flags;
        unsigned short addr;
        char name[I2C_NAME_SIZE];
        struct i2c_adapter *adapter;
        struct device dev;
        int irq;
        struct list_head detected;
    #if IS_ENABLED(CONFIG_I2C_SLAVE)
        i2c_slave_cb_t slave_cb;
    #endif
    }

.. _`i2c_client.members`:

Members
-------

flags
    I2C_CLIENT_TEN indicates the device uses a ten bit chip address;
    I2C_CLIENT_PEC indicates it uses SMBus Packet Error Checking

addr
    Address used on the I2C bus connected to the parent adapter.

name
    Indicates the type of the device, usually a chip name that's
    generic enough to hide second-sourcing and compatible revisions.

adapter
    manages the bus segment hosting this I2C device

dev
    Driver model device node for the slave.

irq
    indicates the IRQ generated by this device (if any)

detected
    member of an i2c_driver.clients list or i2c-core's
    userspace_devices list

slave_cb
    Callback when I2C slave mode of an adapter is used. The adapter
    calls it to pass on slave events to the slave driver.

.. _`i2c_client.description`:

Description
-----------

An i2c_client identifies a single device (i.e. chip) connected to an
i2c bus. The behaviour exposed to Linux is defined by the driver
managing the device.

.. _`i2c_board_info`:

struct i2c_board_info
=====================

.. c:type:: struct i2c_board_info

    template for device creation

.. _`i2c_board_info.definition`:

Definition
----------

.. code-block:: c

    struct i2c_board_info {
        char type[I2C_NAME_SIZE];
        unsigned short flags;
        unsigned short addr;
        void *platform_data;
        struct dev_archdata *archdata;
        struct device_node *of_node;
        struct fwnode_handle *fwnode;
        int irq;
    }

.. _`i2c_board_info.members`:

Members
-------

type
    chip type, to initialize i2c_client.name

flags
    to initialize i2c_client.flags

addr
    stored in i2c_client.addr

platform_data
    stored in i2c_client.dev.platform_data

archdata
    copied into i2c_client.dev.archdata

of_node
    pointer to OpenFirmware device node

fwnode
    device node supplied by the platform firmware

irq
    stored in i2c_client.irq

.. _`i2c_board_info.description`:

Description
-----------

I2C doesn't actually support hardware probing, although controllers and
devices may be able to use I2C_SMBUS_QUICK to tell whether or not there's
a device at a given address.  Drivers commonly need more information than
that, such as chip type, configuration, associated IRQ, and so on.

i2c_board_info is used to build tables of information listing I2C devices
that are present.  This information is used to grow the driver model tree.
For mainboards this is done statically using \ :c:func:`i2c_register_board_info`\ ;
bus numbers identify adapters that aren't yet available.  For add-on boards,
\ :c:func:`i2c_new_device`\  does this dynamically with the adapter already known.

.. _`i2c_board_info`:

I2C_BOARD_INFO
==============

.. c:function::  I2C_BOARD_INFO( dev_type,  dev_addr)

    macro used to list an i2c device and its address

    :param  dev_type:
        identifies the device type

    :param  dev_addr:
        the device's address on the bus.

.. _`i2c_board_info.description`:

Description
-----------

This macro initializes essential fields of a struct i2c_board_info,
declaring what has been provided on a particular board.  Optional
fields (such as associated irq, or device-specific platform_data)
are provided using conventional syntax.

.. _`i2c_algorithm`:

struct i2c_algorithm
====================

.. c:type:: struct i2c_algorithm

    represent I2C transfer method

.. _`i2c_algorithm.definition`:

Definition
----------

.. code-block:: c

    struct i2c_algorithm {
        int (*master_xfer)(struct i2c_adapter *adap, struct i2c_msg *msgs,int num);
        int (*smbus_xfer)(struct i2c_adapter *adap, u16 addr,unsigned short flags, char read_write,u8 command, int size, union i2c_smbus_data *data);
        u32 (*functionality)(struct i2c_adapter *);
    #if IS_ENABLED(CONFIG_I2C_SLAVE)
        int (*reg_slave)(struct i2c_client *client);
        int (*unreg_slave)(struct i2c_client *client);
    #endif
    }

.. _`i2c_algorithm.members`:

Members
-------

master_xfer
    Issue a set of i2c transactions to the given I2C adapter
    defined by the msgs array, with num messages available to transfer via
    the adapter specified by adap.

smbus_xfer
    Issue smbus transactions to the given I2C adapter. If this
    is not present, then the bus layer will try and convert the SMBus calls
    into I2C transfers instead.

functionality
    Return the flags that this algorithm/adapter pair supports
    from the I2C_FUNC\_\* flags.

reg_slave
    Register given client to I2C slave mode of this adapter

unreg_slave
    Unregister given client from I2C slave mode of this adapter

.. _`i2c_algorithm.the-following-structs-are-for-those-who-like-to-implement-new-bus-drivers`:

The following structs are for those who like to implement new bus drivers
-------------------------------------------------------------------------

i2c_algorithm is the interface to a class of hardware solutions which can
be addressed using the same bus algorithms - i.e. bit-banging or the PCF8584
to name two of the most common.

The return codes from the \ ``master_xfer``\  field should indicate the type of
error code that occurred during the transfer, as documented in the kernel
Documentation file Documentation/i2c/fault-codes.

.. _`i2c_timings`:

struct i2c_timings
==================

.. c:type:: struct i2c_timings

    I2C timing information

.. _`i2c_timings.definition`:

Definition
----------

.. code-block:: c

    struct i2c_timings {
        u32 bus_freq_hz;
        u32 scl_rise_ns;
        u32 scl_fall_ns;
        u32 scl_int_delay_ns;
        u32 sda_fall_ns;
    }

.. _`i2c_timings.members`:

Members
-------

bus_freq_hz
    the bus frequency in Hz

scl_rise_ns
    time SCL signal takes to rise in ns; t(r) in the I2C specification

scl_fall_ns
    time SCL signal takes to fall in ns; t(f) in the I2C specification

scl_int_delay_ns
    time IP core additionally needs to setup SCL in ns

sda_fall_ns
    time SDA signal takes to fall in ns; t(f) in the I2C specification

.. _`i2c_bus_recovery_info`:

struct i2c_bus_recovery_info
============================

.. c:type:: struct i2c_bus_recovery_info

    I2C bus recovery information

.. _`i2c_bus_recovery_info.definition`:

Definition
----------

.. code-block:: c

    struct i2c_bus_recovery_info {
        int (*recover_bus)(struct i2c_adapter *);
        int (*get_scl)(struct i2c_adapter *);
        void (*set_scl)(struct i2c_adapter *, int val);
        int (*get_sda)(struct i2c_adapter *);
        void (*prepare_recovery)(struct i2c_adapter *);
        void (*unprepare_recovery)(struct i2c_adapter *);
        int scl_gpio;
        int sda_gpio;
    }

.. _`i2c_bus_recovery_info.members`:

Members
-------

recover_bus
    Recover routine. Either pass driver's \ :c:func:`recover_bus`\  routine, or
    \ :c:func:`i2c_generic_scl_recovery`\  or \ :c:func:`i2c_generic_gpio_recovery`\ .

get_scl
    This gets current value of SCL line. Mandatory for generic SCL
    recovery. Used internally for generic GPIO recovery.

set_scl
    This sets/clears SCL line. Mandatory for generic SCL recovery. Used
    internally for generic GPIO recovery.

get_sda
    This gets current value of SDA line. Optional for generic SCL
    recovery. Used internally, if sda_gpio is a valid GPIO, for generic GPIO
    recovery.

prepare_recovery
    This will be called before starting recovery. Platform may
    configure padmux here for SDA/SCL line or something else they want.

unprepare_recovery
    This will be called after completing recovery. Platform
    may configure padmux here for SDA/SCL line or something else they want.

scl_gpio
    gpio number of the SCL line. Only required for GPIO recovery.

sda_gpio
    gpio number of the SDA line. Only required for GPIO recovery.

.. _`i2c_adapter_quirks`:

struct i2c_adapter_quirks
=========================

.. c:type:: struct i2c_adapter_quirks

    describe flaws of an i2c adapter

.. _`i2c_adapter_quirks.definition`:

Definition
----------

.. code-block:: c

    struct i2c_adapter_quirks {
        u64 flags;
        int max_num_msgs;
        u16 max_write_len;
        u16 max_read_len;
        u16 max_comb_1st_msg_len;
        u16 max_comb_2nd_msg_len;
    }

.. _`i2c_adapter_quirks.members`:

Members
-------

flags
    see I2C_AQ\_\* for possible flags and read below

max_num_msgs
    maximum number of messages per transfer

max_write_len
    maximum length of a write message

max_read_len
    maximum length of a read message

max_comb_1st_msg_len
    maximum length of the first msg in a combined message

max_comb_2nd_msg_len
    maximum length of the second msg in a combined message

.. _`i2c_adapter_quirks.note-about-combined-messages`:

Note about combined messages
----------------------------

Some I2C controllers can only send one message
per transfer, plus something called combined message or write-then-read.
This is (usually) a small write message followed by a read message and
barely enough to access register based devices like EEPROMs. There is a flag
to support this mode. It implies max_num_msg = 2 and does the length checks
with max_comb\_\*\_len because combined message mode usually has its own
limitations. Because of HW implementations, some controllers can actually do
write-then-anything or other variants. To support that, write-then-read has
been broken out into smaller bits like write-first and read-second which can
be combined as needed.

.. _`i2c_lock_bus`:

i2c_lock_bus
============

.. c:function:: void i2c_lock_bus(struct i2c_adapter *adapter, unsigned int flags)

    Get exclusive access to an I2C bus segment

    :param struct i2c_adapter \*adapter:
        Target I2C bus segment

    :param unsigned int flags:
        I2C_LOCK_ROOT_ADAPTER locks the root i2c adapter, I2C_LOCK_SEGMENT
        locks only this branch in the adapter tree

.. _`i2c_unlock_bus`:

i2c_unlock_bus
==============

.. c:function:: void i2c_unlock_bus(struct i2c_adapter *adapter, unsigned int flags)

    Release exclusive access to an I2C bus segment

    :param struct i2c_adapter \*adapter:
        Target I2C bus segment

    :param unsigned int flags:
        I2C_LOCK_ROOT_ADAPTER unlocks the root i2c adapter, I2C_LOCK_SEGMENT
        unlocks only this branch in the adapter tree

.. _`i2c_check_quirks`:

i2c_check_quirks
================

.. c:function:: bool i2c_check_quirks(struct i2c_adapter *adap, u64 quirks)

    Function for checking the quirk flags in an i2c adapter

    :param struct i2c_adapter \*adap:
        i2c adapter

    :param u64 quirks:
        quirk flags

.. _`i2c_check_quirks.return`:

Return
------

true if the adapter has all the specified quirk flags, false if not

.. _`module_i2c_driver`:

module_i2c_driver
=================

.. c:function::  module_i2c_driver( __i2c_driver)

    Helper macro for registering a modular I2C driver

    :param  __i2c_driver:
        i2c_driver struct

.. _`module_i2c_driver.description`:

Description
-----------

Helper macro for I2C drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\ 

.. _`builtin_i2c_driver`:

builtin_i2c_driver
==================

.. c:function::  builtin_i2c_driver( __i2c_driver)

    Helper macro for registering a builtin I2C driver

    :param  __i2c_driver:
        i2c_driver struct

.. _`builtin_i2c_driver.description`:

Description
-----------

Helper macro for I2C drivers which do not do anything special in their
init. This eliminates a lot of boilerplate. Each driver may only
use this macro once, and calling it replaces \ :c:func:`device_initcall`\ .

.. This file was automatic generated / don't edit.
