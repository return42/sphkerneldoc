.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/i2c-core-base.c

.. _`i2c_verify_client`:

i2c_verify_client
=================

.. c:function:: struct i2c_client *i2c_verify_client(struct device *dev)

    return parameter as i2c_client, or NULL

    :param struct device \*dev:
        device, probably from some driver model iterator

.. _`i2c_verify_client.description`:

Description
-----------

When traversing the driver model tree, perhaps using driver model
iterators like \ ``device_for_each_child``\ (), you can't assume very much
about the nodes you find.  Use this function to avoid oopses caused
by wrongly treating some non-I2C device as an i2c_client.

.. _`i2c_adapter_lock_bus`:

i2c_adapter_lock_bus
====================

.. c:function:: void i2c_adapter_lock_bus(struct i2c_adapter *adapter, unsigned int flags)

    Get exclusive access to an I2C bus segment

    :param struct i2c_adapter \*adapter:
        Target I2C bus segment

    :param unsigned int flags:
        I2C_LOCK_ROOT_ADAPTER locks the root i2c adapter, I2C_LOCK_SEGMENT
        locks only this branch in the adapter tree

.. _`i2c_adapter_trylock_bus`:

i2c_adapter_trylock_bus
=======================

.. c:function:: int i2c_adapter_trylock_bus(struct i2c_adapter *adapter, unsigned int flags)

    Try to get exclusive access to an I2C bus segment

    :param struct i2c_adapter \*adapter:
        Target I2C bus segment

    :param unsigned int flags:
        I2C_LOCK_ROOT_ADAPTER trylocks the root i2c adapter, I2C_LOCK_SEGMENT
        trylocks only this branch in the adapter tree

.. _`i2c_adapter_unlock_bus`:

i2c_adapter_unlock_bus
======================

.. c:function:: void i2c_adapter_unlock_bus(struct i2c_adapter *adapter, unsigned int flags)

    Release exclusive access to an I2C bus segment

    :param struct i2c_adapter \*adapter:
        Target I2C bus segment

    :param unsigned int flags:
        I2C_LOCK_ROOT_ADAPTER unlocks the root i2c adapter, I2C_LOCK_SEGMENT
        unlocks only this branch in the adapter tree

.. _`i2c_new_device`:

i2c_new_device
==============

.. c:function:: struct i2c_client *i2c_new_device(struct i2c_adapter *adap, struct i2c_board_info const *info)

    instantiate an i2c device

    :param struct i2c_adapter \*adap:
        the adapter managing the device

    :param struct i2c_board_info const \*info:
        describes one I2C device; bus_num is ignored

.. _`i2c_new_device.context`:

Context
-------

can sleep

.. _`i2c_new_device.description`:

Description
-----------

Create an i2c device. Binding is handled through driver model
\ :c:func:`probe`\ /remove() methods.  A driver may be bound to this device when we
return from this function, or any later moment (e.g. maybe hotplugging will
load the driver module).  This call is not appropriate for use by mainboard
initialization logic, which usually runs during an \ :c:func:`arch_initcall`\  long
before any i2c_adapter could exist.

This returns the new i2c client, which may be saved for later use with
\ :c:func:`i2c_unregister_device`\ ; or NULL to indicate an error.

.. _`i2c_unregister_device`:

i2c_unregister_device
=====================

.. c:function:: void i2c_unregister_device(struct i2c_client *client)

    reverse effect of \ :c:func:`i2c_new_device`\ 

    :param struct i2c_client \*client:
        value returned from \ :c:func:`i2c_new_device`\ 

.. _`i2c_unregister_device.context`:

Context
-------

can sleep

.. _`i2c_new_dummy`:

i2c_new_dummy
=============

.. c:function:: struct i2c_client *i2c_new_dummy(struct i2c_adapter *adapter, u16 address)

    return a new i2c device bound to a dummy driver

    :param struct i2c_adapter \*adapter:
        the adapter managing the device

    :param u16 address:
        seven bit address to be used

.. _`i2c_new_dummy.context`:

Context
-------

can sleep

.. _`i2c_new_dummy.description`:

Description
-----------

This returns an I2C client bound to the "dummy" driver, intended for use
with devices that consume multiple addresses.  Examples of such chips
include various EEPROMS (like 24c04 and 24c08 models).

These dummy devices have two main uses.  First, most I2C and SMBus calls
except \ :c:func:`i2c_transfer`\  need a client handle; the dummy will be that handle.
And second, this prevents the specified address from being bound to a
different driver.

This returns the new i2c client, which should be saved for later use with
\ :c:func:`i2c_unregister_device`\ ; or NULL to indicate an error.

.. _`i2c_new_secondary_device`:

i2c_new_secondary_device
========================

.. c:function:: struct i2c_client *i2c_new_secondary_device(struct i2c_client *client, const char *name, u16 default_addr)

    Helper to get the instantiated secondary address and create the associated device

    :param struct i2c_client \*client:
        Handle to the primary client

    :param const char \*name:
        Handle to specify which secondary address to get

    :param u16 default_addr:
        Used as a fallback if no secondary address was specified

.. _`i2c_new_secondary_device.context`:

Context
-------

can sleep

.. _`i2c_new_secondary_device.description`:

Description
-----------

I2C clients can be composed of multiple I2C slaves bound together in a single
component. The I2C client driver then binds to the master I2C slave and needs
to create I2C dummy clients to communicate with all the other slaves.

This function creates and returns an I2C dummy client whose I2C address is
retrieved from the platform firmware based on the given slave name. If no
address is specified by the firmware default_addr is used.

On DT-based platforms the address is retrieved from the "reg" property entry
cell whose "reg-names" value matches the slave name.

This returns the new i2c client, which should be saved for later use with
\ :c:func:`i2c_unregister_device`\ ; or NULL to indicate an error.

.. _`i2c_verify_adapter`:

i2c_verify_adapter
==================

.. c:function:: struct i2c_adapter *i2c_verify_adapter(struct device *dev)

    return parameter as i2c_adapter or NULL

    :param struct device \*dev:
        device, probably from some driver model iterator

.. _`i2c_verify_adapter.description`:

Description
-----------

When traversing the driver model tree, perhaps using driver model
iterators like \ ``device_for_each_child``\ (), you can't assume very much
about the nodes you find.  Use this function to avoid oopses caused
by wrongly treating some non-I2C device as an i2c_adapter.

.. _`i2c_handle_smbus_host_notify`:

i2c_handle_smbus_host_notify
============================

.. c:function:: int i2c_handle_smbus_host_notify(struct i2c_adapter *adap, unsigned short addr)

    Forward a Host Notify event to the correct I2C client.

    :param struct i2c_adapter \*adap:
        the adapter

    :param unsigned short addr:
        the I2C address of the notifying device

.. _`i2c_handle_smbus_host_notify.context`:

Context
-------

can't sleep

.. _`i2c_handle_smbus_host_notify.description`:

Description
-----------

Helper function to be called from an I2C bus driver's interrupt
handler. It will schedule the Host Notify IRQ.

.. _`__i2c_add_numbered_adapter`:

__i2c_add_numbered_adapter
==========================

.. c:function:: int __i2c_add_numbered_adapter(struct i2c_adapter *adap)

    i2c_add_numbered_adapter where nr is never -1

    :param struct i2c_adapter \*adap:
        the adapter to register (with adap->nr initialized)

.. _`__i2c_add_numbered_adapter.context`:

Context
-------

can sleep

.. _`__i2c_add_numbered_adapter.description`:

Description
-----------

See \ :c:func:`i2c_add_numbered_adapter`\  for details.

.. _`i2c_add_adapter`:

i2c_add_adapter
===============

.. c:function:: int i2c_add_adapter(struct i2c_adapter *adapter)

    declare i2c adapter, use dynamic bus number

    :param struct i2c_adapter \*adapter:
        the adapter to add

.. _`i2c_add_adapter.context`:

Context
-------

can sleep

.. _`i2c_add_adapter.description`:

Description
-----------

This routine is used to declare an I2C adapter when its bus number
doesn't matter or when its bus number is specified by an dt alias.
Examples of bases when the bus number doesn't matter: I2C adapters
dynamically added by USB links or PCI plugin cards.

When this returns zero, a new bus number was allocated and stored
in adap->nr, and the specified adapter became available for clients.
Otherwise, a negative errno value is returned.

.. _`i2c_add_numbered_adapter`:

i2c_add_numbered_adapter
========================

.. c:function:: int i2c_add_numbered_adapter(struct i2c_adapter *adap)

    declare i2c adapter, use static bus number

    :param struct i2c_adapter \*adap:
        the adapter to register (with adap->nr initialized)

.. _`i2c_add_numbered_adapter.context`:

Context
-------

can sleep

.. _`i2c_add_numbered_adapter.description`:

Description
-----------

This routine is used to declare an I2C adapter when its bus number
matters.  For example, use it for I2C adapters from system-on-chip CPUs,
or otherwise built in to the system's mainboard, and where i2c_board_info
is used to properly configure I2C devices.

If the requested bus number is set to -1, then this function will behave
identically to i2c_add_adapter, and will dynamically assign a bus number.

If no devices have pre-been declared for this bus, then be sure to
register the adapter before any dynamically allocated ones.  Otherwise
the required bus ID may not be available.

When this returns zero, the specified adapter became available for
clients using the bus number provided in adap->nr.  Also, the table
of I2C devices pre-declared using \ :c:func:`i2c_register_board_info`\  is scanned,
and the appropriate driver model device nodes are created.  Otherwise, a
negative errno value is returned.

.. _`i2c_del_adapter`:

i2c_del_adapter
===============

.. c:function:: void i2c_del_adapter(struct i2c_adapter *adap)

    unregister I2C adapter

    :param struct i2c_adapter \*adap:
        the adapter being unregistered

.. _`i2c_del_adapter.context`:

Context
-------

can sleep

.. _`i2c_del_adapter.description`:

Description
-----------

This unregisters an I2C adapter which was previously registered
by \ ``i2c_add_adapter``\  or \ ``i2c_add_numbered_adapter``\ .

.. _`i2c_parse_fw_timings`:

i2c_parse_fw_timings
====================

.. c:function:: void i2c_parse_fw_timings(struct device *dev, struct i2c_timings *t, bool use_defaults)

    get I2C related timing parameters from firmware

    :param struct device \*dev:
        The device to scan for I2C timing properties

    :param struct i2c_timings \*t:
        the i2c_timings struct to be filled with values

    :param bool use_defaults:
        bool to use sane defaults derived from the I2C specification
        when properties are not found, otherwise use 0

.. _`i2c_parse_fw_timings.description`:

Description
-----------

Scan the device for the generic I2C properties describing timing parameters
for the signal and fill the given struct with the results. If a property was
not found and use_defaults was true, then maximum timings are assumed which
are derived from the I2C specification. If use_defaults is not used, the
results will be 0, so drivers can apply their own defaults later. The latter
is mainly intended for avoiding regressions of existing drivers which want
to switch to this function. New drivers almost always should use the defaults.

.. _`i2c_del_driver`:

i2c_del_driver
==============

.. c:function:: void i2c_del_driver(struct i2c_driver *driver)

    unregister I2C driver

    :param struct i2c_driver \*driver:
        the driver being unregistered

.. _`i2c_del_driver.context`:

Context
-------

can sleep

.. _`i2c_use_client`:

i2c_use_client
==============

.. c:function:: struct i2c_client *i2c_use_client(struct i2c_client *client)

    increments the reference count of the i2c client structure

    :param struct i2c_client \*client:
        the client being referenced

.. _`i2c_use_client.description`:

Description
-----------

Each live reference to a client should be refcounted. The driver model does
that automatically as part of driver binding, so that most drivers don't
need to do this explicitly: they hold a reference until they're unbound
from the device.

A pointer to the client with the incremented reference counter is returned.

.. _`i2c_release_client`:

i2c_release_client
==================

.. c:function:: void i2c_release_client(struct i2c_client *client)

    release a use of the i2c client structure

    :param struct i2c_client \*client:
        the client being no longer referenced

.. _`i2c_release_client.description`:

Description
-----------

Must be called when a user of a client is finished with it.

.. _`__i2c_transfer`:

__i2c_transfer
==============

.. c:function:: int __i2c_transfer(struct i2c_adapter *adap, struct i2c_msg *msgs, int num)

    unlocked flavor of i2c_transfer

    :param struct i2c_adapter \*adap:
        Handle to I2C bus

    :param struct i2c_msg \*msgs:
        One or more messages to execute before STOP is issued to
        terminate the operation; each message begins with a START.

    :param int num:
        Number of messages to be executed.

.. _`__i2c_transfer.description`:

Description
-----------

Returns negative errno, else the number of messages executed.

Adapter lock must be held when calling this function. No debug logging
takes place. adap->algo->master_xfer existence isn't checked.

.. _`i2c_transfer`:

i2c_transfer
============

.. c:function:: int i2c_transfer(struct i2c_adapter *adap, struct i2c_msg *msgs, int num)

    execute a single or combined I2C message

    :param struct i2c_adapter \*adap:
        Handle to I2C bus

    :param struct i2c_msg \*msgs:
        One or more messages to execute before STOP is issued to
        terminate the operation; each message begins with a START.

    :param int num:
        Number of messages to be executed.

.. _`i2c_transfer.description`:

Description
-----------

Returns negative errno, else the number of messages executed.

Note that there is no requirement that each message be sent to
the same slave address, although that is the most common model.

.. _`i2c_transfer_buffer_flags`:

i2c_transfer_buffer_flags
=========================

.. c:function:: int i2c_transfer_buffer_flags(const struct i2c_client *client, char *buf, int count, u16 flags)

    issue a single I2C message transferring data to/from a buffer

    :param const struct i2c_client \*client:
        Handle to slave device

    :param char \*buf:
        Where the data is stored

    :param int count:
        How many bytes to transfer, must be less than 64k since msg.len is u16

    :param u16 flags:
        The flags to be used for the message, e.g. I2C_M_RD for reads

.. _`i2c_transfer_buffer_flags.description`:

Description
-----------

Returns negative errno, or else the number of bytes transferred.

.. _`i2c_get_dma_safe_msg_buf`:

i2c_get_dma_safe_msg_buf
========================

.. c:function:: u8 *i2c_get_dma_safe_msg_buf(struct i2c_msg *msg, unsigned int threshold)

    get a DMA safe buffer for the given i2c_msg

    :param struct i2c_msg \*msg:
        the message to be checked

    :param unsigned int threshold:
        the minimum number of bytes for which using DMA makes sense

.. _`i2c_get_dma_safe_msg_buf.return`:

Return
------

NULL if a DMA safe buffer was not obtained. Use msg->buf with PIO.
        Or a valid pointer to be used with DMA. After use, release it by
        calling \ :c:func:`i2c_release_dma_safe_msg_buf`\ .

This function must only be called from process context!

.. _`i2c_release_dma_safe_msg_buf`:

i2c_release_dma_safe_msg_buf
============================

.. c:function:: void i2c_release_dma_safe_msg_buf(struct i2c_msg *msg, u8 *buf)

    release DMA safe buffer and sync with i2c_msg

    :param struct i2c_msg \*msg:
        the message to be synced with

    :param u8 \*buf:
        the buffer obtained from \ :c:func:`i2c_get_dma_safe_msg_buf`\ . May be NULL.

.. This file was automatic generated / don't edit.

