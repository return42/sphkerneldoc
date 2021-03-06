.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/i2c.h

.. _`i2c_master_recv`:

i2c_master_recv
===============

.. c:function:: int i2c_master_recv(const struct i2c_client *client, char *buf, int count)

    issue a single I2C message in master receive mode

    :param client:
        Handle to slave device
    :type client: const struct i2c_client \*

    :param buf:
        Where to store data read from slave
    :type buf: char \*

    :param count:
        How many bytes to read, must be less than 64k since msg.len is u16
    :type count: int

.. _`i2c_master_recv.description`:

Description
-----------

Returns negative errno, or else the number of bytes read.

.. _`i2c_master_recv_dmasafe`:

i2c_master_recv_dmasafe
=======================

.. c:function:: int i2c_master_recv_dmasafe(const struct i2c_client *client, char *buf, int count)

    issue a single I2C message in master receive mode using a DMA safe buffer

    :param client:
        Handle to slave device
    :type client: const struct i2c_client \*

    :param buf:
        Where to store data read from slave, must be safe to use with DMA
    :type buf: char \*

    :param count:
        How many bytes to read, must be less than 64k since msg.len is u16
    :type count: int

.. _`i2c_master_recv_dmasafe.description`:

Description
-----------

Returns negative errno, or else the number of bytes read.

.. _`i2c_master_send`:

i2c_master_send
===============

.. c:function:: int i2c_master_send(const struct i2c_client *client, const char *buf, int count)

    issue a single I2C message in master transmit mode

    :param client:
        Handle to slave device
    :type client: const struct i2c_client \*

    :param buf:
        Data that will be written to the slave
    :type buf: const char \*

    :param count:
        How many bytes to write, must be less than 64k since msg.len is u16
    :type count: int

.. _`i2c_master_send.description`:

Description
-----------

Returns negative errno, or else the number of bytes written.

.. _`i2c_master_send_dmasafe`:

i2c_master_send_dmasafe
=======================

.. c:function:: int i2c_master_send_dmasafe(const struct i2c_client *client, const char *buf, int count)

    issue a single I2C message in master transmit mode using a DMA safe buffer

    :param client:
        Handle to slave device
    :type client: const struct i2c_client \*

    :param buf:
        Data that will be written to the slave, must be safe to use with DMA
    :type buf: const char \*

    :param count:
        How many bytes to write, must be less than 64k since msg.len is u16
    :type count: int

.. _`i2c_master_send_dmasafe.description`:

Description
-----------

Returns negative errno, or else the number of bytes written.

.. _`i2c_device_identity`:

struct i2c_device_identity
==========================

.. c:type:: struct i2c_device_identity

    i2c client device identification

.. _`i2c_device_identity.definition`:

Definition
----------

.. code-block:: c

    struct i2c_device_identity {
        u16 manufacturer_id;
    #define I2C_DEVICE_ID_NXP_SEMICONDUCTORS 0
    #define I2C_DEVICE_ID_NXP_SEMICONDUCTORS_1 1
    #define I2C_DEVICE_ID_NXP_SEMICONDUCTORS_2 2
    #define I2C_DEVICE_ID_NXP_SEMICONDUCTORS_3 3
    #define I2C_DEVICE_ID_RAMTRON_INTERNATIONAL 4
    #define I2C_DEVICE_ID_ANALOG_DEVICES 5
    #define I2C_DEVICE_ID_STMICROELECTRONICS 6
    #define I2C_DEVICE_ID_ON_SEMICONDUCTOR 7
    #define I2C_DEVICE_ID_SPRINTEK_CORPORATION 8
    #define I2C_DEVICE_ID_ESPROS_PHOTONICS_AG 9
    #define I2C_DEVICE_ID_FUJITSU_SEMICONDUCTOR 10
    #define I2C_DEVICE_ID_FLIR 11
    #define I2C_DEVICE_ID_O2MICRO 12
    #define I2C_DEVICE_ID_ATMEL 13
    #define I2C_DEVICE_ID_NONE 0xffff
        u16 part_id;
        u8 die_revision;
    }

.. _`i2c_device_identity.members`:

Members
-------

manufacturer_id
    0 - 4095, database maintained by NXP

part_id
    0 - 511, according to manufacturer

die_revision
    0 - 7, according to manufacturer

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
        int (*probe)(struct i2c_client *, const struct i2c_device_id *);
        int (*remove)(struct i2c_client *);
        int (*probe_new)(struct i2c_client *);
        void (*shutdown)(struct i2c_client *);
        void (*alert)(struct i2c_client *, enum i2c_alert_protocol protocol, unsigned int data);
        int (*command)(struct i2c_client *client, unsigned int cmd, void *arg);
        struct device_driver driver;
        const struct i2c_device_id *id_table;
        int (*detect)(struct i2c_client *, struct i2c_board_info *);
        const unsigned short *address_list;
        struct list_head clients;
        bool disable_i2c_core_irq_mapping;
    }

.. _`i2c_driver.members`:

Members
-------

class
    What kind of i2c device we instantiate (for detect)

probe
    Callback for device binding - soon to be deprecated

remove
    Callback for device unbinding

probe_new
    New callback for device binding

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

disable_i2c_core_irq_mapping
    Tell the i2c-core to not do irq-mapping

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
        const char *dev_name;
        void *platform_data;
        struct device_node *of_node;
        struct fwnode_handle *fwnode;
        const struct property_entry *properties;
        const struct resource *resources;
        unsigned int num_resources;
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

dev_name
    Overrides the default <busnr>-<addr> dev_name if set

platform_data
    stored in i2c_client.dev.platform_data

of_node
    pointer to OpenFirmware device node

fwnode
    device node supplied by the platform firmware

properties
    additional device properties for the device

resources
    resources associated with the device

num_resources
    number of resources in the \ ``resources``\  array

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

    :param dev_type:
        identifies the device type
    :type dev_type: 

    :param dev_addr:
        the device's address on the bus.
    :type dev_addr: 

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
        int (*master_xfer)(struct i2c_adapter *adap, struct i2c_msg *msgs, int num);
        int (*smbus_xfer) (struct i2c_adapter *adap, u16 addr,unsigned short flags, char read_write, u8 command, int size, union i2c_smbus_data *data);
        u32 (*functionality) (struct i2c_adapter *);
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
    from the I2C_FUNC_* flags.

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

.. _`i2c_lock_operations`:

struct i2c_lock_operations
==========================

.. c:type:: struct i2c_lock_operations

    represent I2C locking operations

.. _`i2c_lock_operations.definition`:

Definition
----------

.. code-block:: c

    struct i2c_lock_operations {
        void (*lock_bus)(struct i2c_adapter *, unsigned int flags);
        int (*trylock_bus)(struct i2c_adapter *, unsigned int flags);
        void (*unlock_bus)(struct i2c_adapter *, unsigned int flags);
    }

.. _`i2c_lock_operations.members`:

Members
-------

lock_bus
    Get exclusive access to an I2C bus segment

trylock_bus
    Try to get exclusive access to an I2C bus segment

unlock_bus
    Release exclusive access to an I2C bus segment

.. _`i2c_lock_operations.description`:

Description
-----------

The main operations are wrapped by i2c_lock_bus and i2c_unlock_bus.

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
        u32 sda_hold_ns;
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

sda_hold_ns
    time IP core additionally needs to hold SDA in ns

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
        int (*recover_bus)(struct i2c_adapter *adap);
        int (*get_scl)(struct i2c_adapter *adap);
        void (*set_scl)(struct i2c_adapter *adap, int val);
        int (*get_sda)(struct i2c_adapter *adap);
        void (*set_sda)(struct i2c_adapter *adap, int val);
        int (*get_bus_free)(struct i2c_adapter *adap);
        void (*prepare_recovery)(struct i2c_adapter *adap);
        void (*unprepare_recovery)(struct i2c_adapter *adap);
        struct gpio_desc *scl_gpiod;
        struct gpio_desc *sda_gpiod;
    }

.. _`i2c_bus_recovery_info.members`:

Members
-------

recover_bus
    Recover routine. Either pass driver's \ :c:func:`recover_bus`\  routine, or
    \ :c:func:`i2c_generic_scl_recovery`\ .

get_scl
    This gets current value of SCL line. Mandatory for generic SCL
    recovery. Populated internally for generic GPIO recovery.

set_scl
    This sets/clears the SCL line. Mandatory for generic SCL recovery.
    Populated internally for generic GPIO recovery.

get_sda
    This gets current value of SDA line. This or \ :c:func:`set_sda`\  is mandatory
    for generic SCL recovery. Populated internally, if sda_gpio is a valid
    GPIO, for generic GPIO recovery.

set_sda
    This sets/clears the SDA line. This or \ :c:func:`get_sda`\  is mandatory for
    generic SCL recovery. Populated internally, if sda_gpio is a valid GPIO,
    for generic GPIO recovery.

get_bus_free
    Returns the bus free state as seen from the IP core in case it
    has a more complex internal logic than just reading SDA. Optional.

prepare_recovery
    This will be called before starting recovery. Platform may
    configure padmux here for SDA/SCL line or something else they want.

unprepare_recovery
    This will be called after completing recovery. Platform
    may configure padmux here for SDA/SCL line or something else they want.

scl_gpiod
    gpiod of the SCL line. Only required for GPIO recovery.

sda_gpiod
    gpiod of the SDA line. Only required for GPIO recovery.

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
    see I2C_AQ_* for possible flags and read below

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

.. _`i2c_adapter_quirks.description`:

Description
-----------

Note about combined messages: Some I2C controllers can only send one message
per transfer, plus something called combined message or write-then-read.
This is (usually) a small write message followed by a read message and
barely enough to access register based devices like EEPROMs. There is a flag
to support this mode. It implies max_num_msg = 2 and does the length checks
with max_comb_*_len because combined message mode usually has its own
limitations. Because of HW implementations, some controllers can actually do
write-then-anything or other variants. To support that, write-then-read has
been broken out into smaller bits like write-first and read-second which can
be combined as needed.

.. _`i2c_lock_bus`:

i2c_lock_bus
============

.. c:function:: void i2c_lock_bus(struct i2c_adapter *adapter, unsigned int flags)

    Get exclusive access to an I2C bus segment

    :param adapter:
        Target I2C bus segment
    :type adapter: struct i2c_adapter \*

    :param flags:
        I2C_LOCK_ROOT_ADAPTER locks the root i2c adapter, I2C_LOCK_SEGMENT
        locks only this branch in the adapter tree
    :type flags: unsigned int

.. _`i2c_trylock_bus`:

i2c_trylock_bus
===============

.. c:function:: int i2c_trylock_bus(struct i2c_adapter *adapter, unsigned int flags)

    Try to get exclusive access to an I2C bus segment

    :param adapter:
        Target I2C bus segment
    :type adapter: struct i2c_adapter \*

    :param flags:
        I2C_LOCK_ROOT_ADAPTER tries to locks the root i2c adapter,
        I2C_LOCK_SEGMENT tries to lock only this branch in the adapter tree
    :type flags: unsigned int

.. _`i2c_trylock_bus.return`:

Return
------

true if the I2C bus segment is locked, false otherwise

.. _`i2c_unlock_bus`:

i2c_unlock_bus
==============

.. c:function:: void i2c_unlock_bus(struct i2c_adapter *adapter, unsigned int flags)

    Release exclusive access to an I2C bus segment

    :param adapter:
        Target I2C bus segment
    :type adapter: struct i2c_adapter \*

    :param flags:
        I2C_LOCK_ROOT_ADAPTER unlocks the root i2c adapter, I2C_LOCK_SEGMENT
        unlocks only this branch in the adapter tree
    :type flags: unsigned int

.. _`i2c_check_quirks`:

i2c_check_quirks
================

.. c:function:: bool i2c_check_quirks(struct i2c_adapter *adap, u64 quirks)

    Function for checking the quirk flags in an i2c adapter

    :param adap:
        i2c adapter
    :type adap: struct i2c_adapter \*

    :param quirks:
        quirk flags
    :type quirks: u64

.. _`i2c_check_quirks.return`:

Return
------

true if the adapter has all the specified quirk flags, false if not

.. _`module_i2c_driver`:

module_i2c_driver
=================

.. c:function::  module_i2c_driver( __i2c_driver)

    Helper macro for registering a modular I2C driver

    :param __i2c_driver:
        i2c_driver struct
    :type __i2c_driver: 

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

    :param __i2c_driver:
        i2c_driver struct
    :type __i2c_driver: 

.. _`builtin_i2c_driver.description`:

Description
-----------

Helper macro for I2C drivers which do not do anything special in their
init. This eliminates a lot of boilerplate. Each driver may only
use this macro once, and calling it replaces \ :c:func:`device_initcall`\ .

.. This file was automatic generated / don't edit.

