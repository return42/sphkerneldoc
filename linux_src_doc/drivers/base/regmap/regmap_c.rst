.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/regmap/regmap.c

.. _`devm_regmap_field_alloc`:

devm_regmap_field_alloc
=======================

.. c:function:: struct regmap_field *devm_regmap_field_alloc(struct device *dev, struct regmap *regmap, struct reg_field reg_field)

    Allocate and initialise a register field.

    :param dev:
        Device that will be interacted with
    :type dev: struct device \*

    :param regmap:
        regmap bank in which this register field is located.
    :type regmap: struct regmap \*

    :param reg_field:
        Register field with in the bank.
    :type reg_field: struct reg_field

.. _`devm_regmap_field_alloc.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap_field. The regmap_field will be automatically freed
by the device management code.

.. _`devm_regmap_field_free`:

devm_regmap_field_free
======================

.. c:function:: void devm_regmap_field_free(struct device *dev, struct regmap_field *field)

    Free a register field allocated using devm_regmap_field_alloc.

    :param dev:
        Device that will be interacted with
    :type dev: struct device \*

    :param field:
        regmap field which should be freed.
    :type field: struct regmap_field \*

.. _`devm_regmap_field_free.description`:

Description
-----------

Free register field allocated using \ :c:func:`devm_regmap_field_alloc`\ . Usually
drivers need not call this function, as the memory allocated via devm
will be freed as per device-driver life-cyle.

.. _`regmap_field_alloc`:

regmap_field_alloc
==================

.. c:function:: struct regmap_field *regmap_field_alloc(struct regmap *regmap, struct reg_field reg_field)

    Allocate and initialise a register field.

    :param regmap:
        regmap bank in which this register field is located.
    :type regmap: struct regmap \*

    :param reg_field:
        Register field with in the bank.
    :type reg_field: struct reg_field

.. _`regmap_field_alloc.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap_field. The regmap_field should be freed by the
user once its finished working with it using \ :c:func:`regmap_field_free`\ .

.. _`regmap_field_free`:

regmap_field_free
=================

.. c:function:: void regmap_field_free(struct regmap_field *field)

    Free register field allocated using regmap_field_alloc.

    :param field:
        regmap field which should be freed.
    :type field: struct regmap_field \*

.. _`regmap_reinit_cache`:

regmap_reinit_cache
===================

.. c:function:: int regmap_reinit_cache(struct regmap *map, const struct regmap_config *config)

    Reinitialise the current register cache

    :param map:
        Register map to operate on.
    :type map: struct regmap \*

    :param config:
        New configuration.  Only the cache data will be used.
    :type config: const struct regmap_config \*

.. _`regmap_reinit_cache.description`:

Description
-----------

Discard any existing register cache for the map and initialize a
new cache.  This can be used to restore the cache to defaults or to
update the cache configuration to reflect runtime discovery of the
hardware.

No explicit locking is done here, the user needs to ensure that
this function will not race with other calls to regmap.

.. _`regmap_exit`:

regmap_exit
===========

.. c:function:: void regmap_exit(struct regmap *map)

    Free a previously allocated register map

    :param map:
        Register map to operate on.
    :type map: struct regmap \*

.. _`dev_get_regmap`:

dev_get_regmap
==============

.. c:function:: struct regmap *dev_get_regmap(struct device *dev, const char *name)

    Obtain the regmap (if any) for a device

    :param dev:
        Device to retrieve the map for
    :type dev: struct device \*

    :param name:
        Optional name for the register map, usually NULL.
    :type name: const char \*

.. _`dev_get_regmap.description`:

Description
-----------

Returns the regmap for the device if one is present, or NULL.  If
name is specified then it must match the name specified when
registering the device, if it is NULL then the first regmap found
will be used.  Devices with multiple register maps are very rare,
generic code should normally not need to specify a name.

.. _`regmap_get_device`:

regmap_get_device
=================

.. c:function:: struct device *regmap_get_device(struct regmap *map)

    Obtain the device from a regmap

    :param map:
        Register map to operate on.
    :type map: struct regmap \*

.. _`regmap_get_device.description`:

Description
-----------

Returns the underlying device that the regmap has been created for.

.. _`regmap_can_raw_write`:

regmap_can_raw_write
====================

.. c:function:: bool regmap_can_raw_write(struct regmap *map)

    Test if \ :c:func:`regmap_raw_write`\  is supported

    :param map:
        Map to check.
    :type map: struct regmap \*

.. _`regmap_get_raw_read_max`:

regmap_get_raw_read_max
=======================

.. c:function:: size_t regmap_get_raw_read_max(struct regmap *map)

    Get the maximum size we can read

    :param map:
        Map to check.
    :type map: struct regmap \*

.. _`regmap_get_raw_write_max`:

regmap_get_raw_write_max
========================

.. c:function:: size_t regmap_get_raw_write_max(struct regmap *map)

    Get the maximum size we can read

    :param map:
        Map to check.
    :type map: struct regmap \*

.. _`regmap_write`:

regmap_write
============

.. c:function:: int regmap_write(struct regmap *map, unsigned int reg, unsigned int val)

    Write a value to a single register

    :param map:
        Register map to write to
    :type map: struct regmap \*

    :param reg:
        Register to write to
    :type reg: unsigned int

    :param val:
        Value to be written
    :type val: unsigned int

.. _`regmap_write.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.

.. _`regmap_write_async`:

regmap_write_async
==================

.. c:function:: int regmap_write_async(struct regmap *map, unsigned int reg, unsigned int val)

    Write a value to a single register asynchronously

    :param map:
        Register map to write to
    :type map: struct regmap \*

    :param reg:
        Register to write to
    :type reg: unsigned int

    :param val:
        Value to be written
    :type val: unsigned int

.. _`regmap_write_async.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.

.. _`regmap_raw_write`:

regmap_raw_write
================

.. c:function:: int regmap_raw_write(struct regmap *map, unsigned int reg, const void *val, size_t val_len)

    Write raw values to one or more registers

    :param map:
        Register map to write to
    :type map: struct regmap \*

    :param reg:
        Initial register to write to
    :type reg: unsigned int

    :param val:
        Block of data to be written, laid out for direct transmission to the
        device
    :type val: const void \*

    :param val_len:
        Length of data pointed to by val.
    :type val_len: size_t

.. _`regmap_raw_write.description`:

Description
-----------

This function is intended to be used for things like firmware
download where a large block of data needs to be transferred to the
device.  No formatting will be done on the data provided.

A value of zero will be returned on success, a negative errno will
be returned in error cases.

.. _`regmap_noinc_write`:

regmap_noinc_write
==================

.. c:function:: int regmap_noinc_write(struct regmap *map, unsigned int reg, const void *val, size_t val_len)

    Write data from a register without incrementing the register number

    :param map:
        Register map to write to
    :type map: struct regmap \*

    :param reg:
        Register to write to
    :type reg: unsigned int

    :param val:
        Pointer to data buffer
    :type val: const void \*

    :param val_len:
        Length of output buffer in bytes.
    :type val_len: size_t

.. _`regmap_noinc_write.description`:

Description
-----------

The regmap API usually assumes that bulk bus write operations will write a
range of registers. Some devices have certain registers for which a write
operation can write to an internal FIFO.

The target register must be volatile but registers after it can be
completely unrelated cacheable registers.

This will attempt multiple writes as required to write val_len bytes.

A value of zero will be returned on success, a negative errno will be
returned in error cases.

.. _`regmap_field_update_bits_base`:

regmap_field_update_bits_base
=============================

.. c:function:: int regmap_field_update_bits_base(struct regmap_field *field, unsigned int mask, unsigned int val, bool *change, bool async, bool force)

    Perform a read/modify/write cycle a register field.

    :param field:
        Register field to write to
    :type field: struct regmap_field \*

    :param mask:
        Bitmask to change
    :type mask: unsigned int

    :param val:
        Value to be written
    :type val: unsigned int

    :param change:
        Boolean indicating if a write was done
    :type change: bool \*

    :param async:
        Boolean indicating asynchronously
    :type async: bool

    :param force:
        Boolean indicating use force update
    :type force: bool

.. _`regmap_field_update_bits_base.description`:

Description
-----------

Perform a read/modify/write cycle on the register field with change,
async, force option.

A value of zero will be returned on success, a negative errno will
be returned in error cases.

.. _`regmap_fields_update_bits_base`:

regmap_fields_update_bits_base
==============================

.. c:function:: int regmap_fields_update_bits_base(struct regmap_field *field, unsigned int id, unsigned int mask, unsigned int val, bool *change, bool async, bool force)

    Perform a read/modify/write cycle a register field with port ID

    :param field:
        Register field to write to
    :type field: struct regmap_field \*

    :param id:
        port ID
    :type id: unsigned int

    :param mask:
        Bitmask to change
    :type mask: unsigned int

    :param val:
        Value to be written
    :type val: unsigned int

    :param change:
        Boolean indicating if a write was done
    :type change: bool \*

    :param async:
        Boolean indicating asynchronously
    :type async: bool

    :param force:
        Boolean indicating use force update
    :type force: bool

.. _`regmap_fields_update_bits_base.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.

.. _`regmap_bulk_write`:

regmap_bulk_write
=================

.. c:function:: int regmap_bulk_write(struct regmap *map, unsigned int reg, const void *val, size_t val_count)

    Write multiple registers to the device

    :param map:
        Register map to write to
    :type map: struct regmap \*

    :param reg:
        First register to be write from
    :type reg: unsigned int

    :param val:
        Block of data to be written, in native register size for device
    :type val: const void \*

    :param val_count:
        Number of registers to write
    :type val_count: size_t

.. _`regmap_bulk_write.description`:

Description
-----------

This function is intended to be used for writing a large block of
data to the device either in single transfer or multiple transfer.

A value of zero will be returned on success, a negative errno will
be returned in error cases.

.. _`regmap_multi_reg_write`:

regmap_multi_reg_write
======================

.. c:function:: int regmap_multi_reg_write(struct regmap *map, const struct reg_sequence *regs, int num_regs)

    Write multiple registers to the device

    :param map:
        Register map to write to
    :type map: struct regmap \*

    :param regs:
        Array of structures containing register,value to be written
    :type regs: const struct reg_sequence \*

    :param num_regs:
        Number of registers to write
    :type num_regs: int

.. _`regmap_multi_reg_write.description`:

Description
-----------

Write multiple registers to the device where the set of register, value
pairs are supplied in any order, possibly not all in a single range.

The 'normal' block write mode will send ultimately send data on the
target bus as R,V1,V2,V3,..,Vn where successively higher registers are
addressed. However, this alternative block multi write mode will send
the data as R1,V1,R2,V2,..,Rn,Vn on the target bus. The target device
must of course support the mode.

A value of zero will be returned on success, a negative errno will be
returned in error cases.

.. _`regmap_multi_reg_write_bypassed`:

regmap_multi_reg_write_bypassed
===============================

.. c:function:: int regmap_multi_reg_write_bypassed(struct regmap *map, const struct reg_sequence *regs, int num_regs)

    Write multiple registers to the device but not the cache

    :param map:
        Register map to write to
    :type map: struct regmap \*

    :param regs:
        Array of structures containing register,value to be written
    :type regs: const struct reg_sequence \*

    :param num_regs:
        Number of registers to write
    :type num_regs: int

.. _`regmap_multi_reg_write_bypassed.description`:

Description
-----------

Write multiple registers to the device but not the cache where the set
of register are supplied in any order.

This function is intended to be used for writing a large block of data
atomically to the device in single transfer for those I2C client devices
that implement this alternative block write mode.

A value of zero will be returned on success, a negative errno will
be returned in error cases.

.. _`regmap_raw_write_async`:

regmap_raw_write_async
======================

.. c:function:: int regmap_raw_write_async(struct regmap *map, unsigned int reg, const void *val, size_t val_len)

    Write raw values to one or more registers asynchronously

    :param map:
        Register map to write to
    :type map: struct regmap \*

    :param reg:
        Initial register to write to
    :type reg: unsigned int

    :param val:
        Block of data to be written, laid out for direct transmission to the
        device.  Must be valid until \ :c:func:`regmap_async_complete`\  is called.
    :type val: const void \*

    :param val_len:
        Length of data pointed to by val.
    :type val_len: size_t

.. _`regmap_raw_write_async.description`:

Description
-----------

This function is intended to be used for things like firmware
download where a large block of data needs to be transferred to the
device.  No formatting will be done on the data provided.

If supported by the underlying bus the write will be scheduled
asynchronously, helping maximise I/O speed on higher speed buses
like SPI.  \ :c:func:`regmap_async_complete`\  can be called to ensure that all
asynchrnous writes have been completed.

A value of zero will be returned on success, a negative errno will
be returned in error cases.

.. _`regmap_read`:

regmap_read
===========

.. c:function:: int regmap_read(struct regmap *map, unsigned int reg, unsigned int *val)

    Read a value from a single register

    :param map:
        Register map to read from
    :type map: struct regmap \*

    :param reg:
        Register to be read from
    :type reg: unsigned int

    :param val:
        Pointer to store read value
    :type val: unsigned int \*

.. _`regmap_read.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.

.. _`regmap_raw_read`:

regmap_raw_read
===============

.. c:function:: int regmap_raw_read(struct regmap *map, unsigned int reg, void *val, size_t val_len)

    Read raw data from the device

    :param map:
        Register map to read from
    :type map: struct regmap \*

    :param reg:
        First register to be read from
    :type reg: unsigned int

    :param val:
        Pointer to store read value
    :type val: void \*

    :param val_len:
        Size of data to read
    :type val_len: size_t

.. _`regmap_raw_read.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.

.. _`regmap_noinc_read`:

regmap_noinc_read
=================

.. c:function:: int regmap_noinc_read(struct regmap *map, unsigned int reg, void *val, size_t val_len)

    Read data from a register without incrementing the register number

    :param map:
        Register map to read from
    :type map: struct regmap \*

    :param reg:
        Register to read from
    :type reg: unsigned int

    :param val:
        Pointer to data buffer
    :type val: void \*

    :param val_len:
        Length of output buffer in bytes.
    :type val_len: size_t

.. _`regmap_noinc_read.description`:

Description
-----------

The regmap API usually assumes that bulk bus read operations will read a
range of registers. Some devices have certain registers for which a read
operation read will read from an internal FIFO.

The target register must be volatile but registers after it can be
completely unrelated cacheable registers.

This will attempt multiple reads as required to read val_len bytes.

A value of zero will be returned on success, a negative errno will be
returned in error cases.

.. _`regmap_field_read`:

regmap_field_read
=================

.. c:function:: int regmap_field_read(struct regmap_field *field, unsigned int *val)

    Read a value to a single register field

    :param field:
        Register field to read from
    :type field: struct regmap_field \*

    :param val:
        Pointer to store read value
    :type val: unsigned int \*

.. _`regmap_field_read.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.

.. _`regmap_fields_read`:

regmap_fields_read
==================

.. c:function:: int regmap_fields_read(struct regmap_field *field, unsigned int id, unsigned int *val)

    Read a value to a single register field with port ID

    :param field:
        Register field to read from
    :type field: struct regmap_field \*

    :param id:
        port ID
    :type id: unsigned int

    :param val:
        Pointer to store read value
    :type val: unsigned int \*

.. _`regmap_fields_read.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.

.. _`regmap_bulk_read`:

regmap_bulk_read
================

.. c:function:: int regmap_bulk_read(struct regmap *map, unsigned int reg, void *val, size_t val_count)

    Read multiple registers from the device

    :param map:
        Register map to read from
    :type map: struct regmap \*

    :param reg:
        First register to be read from
    :type reg: unsigned int

    :param val:
        Pointer to store read value, in native register size for device
    :type val: void \*

    :param val_count:
        Number of registers to read
    :type val_count: size_t

.. _`regmap_bulk_read.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.

.. _`regmap_update_bits_base`:

regmap_update_bits_base
=======================

.. c:function:: int regmap_update_bits_base(struct regmap *map, unsigned int reg, unsigned int mask, unsigned int val, bool *change, bool async, bool force)

    Perform a read/modify/write cycle on a register

    :param map:
        Register map to update
    :type map: struct regmap \*

    :param reg:
        Register to update
    :type reg: unsigned int

    :param mask:
        Bitmask to change
    :type mask: unsigned int

    :param val:
        New value for bitmask
    :type val: unsigned int

    :param change:
        Boolean indicating if a write was done
    :type change: bool \*

    :param async:
        Boolean indicating asynchronously
    :type async: bool

    :param force:
        Boolean indicating use force update
    :type force: bool

.. _`regmap_update_bits_base.description`:

Description
-----------

Perform a read/modify/write cycle on a register map with change, async, force
options.

.. _`regmap_update_bits_base.if-async-is-true`:

If async is true
----------------


With most buses the read must be done synchronously so this is most useful
for devices with a cache which do not need to interact with the hardware to
determine the current register value.

Returns zero for success, a negative number on error.

.. _`regmap_async_complete`:

regmap_async_complete
=====================

.. c:function:: int regmap_async_complete(struct regmap *map)

    Ensure all asynchronous I/O has completed.

    :param map:
        Map to operate on.
    :type map: struct regmap \*

.. _`regmap_async_complete.description`:

Description
-----------

Blocks until any pending asynchronous I/O has completed.  Returns
an error code for any failed I/O operations.

.. _`regmap_register_patch`:

regmap_register_patch
=====================

.. c:function:: int regmap_register_patch(struct regmap *map, const struct reg_sequence *regs, int num_regs)

    Register and apply register updates to be applied on device initialistion

    :param map:
        Register map to apply updates to.
    :type map: struct regmap \*

    :param regs:
        Values to update.
    :type regs: const struct reg_sequence \*

    :param num_regs:
        Number of entries in regs.
    :type num_regs: int

.. _`regmap_register_patch.description`:

Description
-----------

Register a set of register updates to be applied to the device
whenever the device registers are synchronised with the cache and
apply them immediately.  Typically this is used to apply
corrections to be applied to the device defaults on startup, such
as the updates some vendors provide to undocumented registers.

The caller must ensure that this function cannot be called
concurrently with either itself or \ :c:func:`regcache_sync`\ .

.. _`regmap_get_val_bytes`:

regmap_get_val_bytes
====================

.. c:function:: int regmap_get_val_bytes(struct regmap *map)

    Report the size of a register value

    :param map:
        Register map to operate on.
    :type map: struct regmap \*

.. _`regmap_get_val_bytes.description`:

Description
-----------

Report the size of a register value, mainly intended to for use by
generic infrastructure built on top of regmap.

.. _`regmap_get_max_register`:

regmap_get_max_register
=======================

.. c:function:: int regmap_get_max_register(struct regmap *map)

    Report the max register value

    :param map:
        Register map to operate on.
    :type map: struct regmap \*

.. _`regmap_get_max_register.description`:

Description
-----------

Report the max register value, mainly intended to for use by
generic infrastructure built on top of regmap.

.. _`regmap_get_reg_stride`:

regmap_get_reg_stride
=====================

.. c:function:: int regmap_get_reg_stride(struct regmap *map)

    Report the register address stride

    :param map:
        Register map to operate on.
    :type map: struct regmap \*

.. _`regmap_get_reg_stride.description`:

Description
-----------

Report the register address stride, mainly intended to for use by
generic infrastructure built on top of regmap.

.. This file was automatic generated / don't edit.

