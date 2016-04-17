.. -*- coding: utf-8; mode: rst -*-

========
regmap.c
========


.. _`devm_regmap_field_alloc`:

devm_regmap_field_alloc
=======================

.. c:function:: struct regmap_field *devm_regmap_field_alloc (struct device *dev, struct regmap *regmap, struct reg_field reg_field)

    :param struct device \*dev:
        Device that will be interacted with

    :param struct regmap \*regmap:
        regmap bank in which this register field is located.

    :param struct reg_field reg_field:
        Register field with in the bank.



.. _`devm_regmap_field_alloc.description`:

Description
-----------

The return value will be an :c:func:`ERR_PTR` on error or a valid pointer
to a struct regmap_field. The regmap_field will be automatically freed
by the device management code.



.. _`devm_regmap_field_alloc.description`:

Description
-----------

The return value will be an :c:func:`ERR_PTR` on error or a valid pointer
to a struct regmap_field. The regmap_field will be automatically freed
by the device management code.



.. _`devm_regmap_field_free`:

devm_regmap_field_free
======================

.. c:function:: void devm_regmap_field_free (struct device *dev, struct regmap_field *field)

    :param struct device \*dev:
        Device that will be interacted with

    :param struct regmap_field \*field:
        regmap field which should be freed.



.. _`devm_regmap_field_free.description`:

Description
-----------

devm_regmap_field_alloc. Usally drivers need not call this function,
as the memory allocated via devm will be freed as per device-driver
life-cyle.



.. _`regmap_field_alloc`:

regmap_field_alloc
==================

.. c:function:: struct regmap_field *regmap_field_alloc (struct regmap *regmap, struct reg_field reg_field)

    :param struct regmap \*regmap:
        regmap bank in which this register field is located.

    :param struct reg_field reg_field:
        Register field with in the bank.



.. _`regmap_field_alloc.description`:

Description
-----------

The return value will be an :c:func:`ERR_PTR` on error or a valid pointer
to a struct regmap_field. The regmap_field should be freed by the
user once its finished working with it using :c:func:`regmap_field_free`.



.. _`regmap_field_alloc.description`:

Description
-----------

The return value will be an :c:func:`ERR_PTR` on error or a valid pointer
to a struct regmap_field. The regmap_field should be freed by the
user once its finished working with it using :c:func:`regmap_field_free`.



.. _`regmap_field_free`:

regmap_field_free
=================

.. c:function:: void regmap_field_free (struct regmap_field *field)

    :param struct regmap_field \*field:
        regmap field which should be freed.



.. _`regmap_reinit_cache`:

regmap_reinit_cache
===================

.. c:function:: int regmap_reinit_cache (struct regmap *map, const struct regmap_config *config)

    :param struct regmap \*map:
        Register map to operate on.

    :param const struct regmap_config \*config:
        New configuration.  Only the cache data will be used.



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

.. c:function:: void regmap_exit (struct regmap *map)

    :param struct regmap \*map:

        *undescribed*



.. _`dev_get_regmap`:

dev_get_regmap
==============

.. c:function:: struct regmap *dev_get_regmap (struct device *dev, const char *name)

    :param struct device \*dev:
        Device to retrieve the map for

    :param const char \*name:
        Optional name for the register map, usually NULL.



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

.. c:function:: struct device *regmap_get_device (struct regmap *map)

    :param struct regmap \*map:
        Register map to operate on.



.. _`regmap_get_device.description`:

Description
-----------

Returns the underlying device that the regmap has been created for.



.. _`regmap_can_raw_write`:

regmap_can_raw_write
====================

.. c:function:: bool regmap_can_raw_write (struct regmap *map)

    Test if regmap_raw_write() is supported

    :param struct regmap \*map:
        Map to check.



.. _`regmap_get_raw_read_max`:

regmap_get_raw_read_max
=======================

.. c:function:: size_t regmap_get_raw_read_max (struct regmap *map)

    Get the maximum size we can read

    :param struct regmap \*map:
        Map to check.



.. _`regmap_get_raw_write_max`:

regmap_get_raw_write_max
========================

.. c:function:: size_t regmap_get_raw_write_max (struct regmap *map)

    Get the maximum size we can read

    :param struct regmap \*map:
        Map to check.



.. _`regmap_write`:

regmap_write
============

.. c:function:: int regmap_write (struct regmap *map, unsigned int reg, unsigned int val)

    :param struct regmap \*map:
        Register map to write to

    :param unsigned int reg:
        Register to write to

    :param unsigned int val:
        Value to be written



.. _`regmap_write.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.



.. _`regmap_write_async`:

regmap_write_async
==================

.. c:function:: int regmap_write_async (struct regmap *map, unsigned int reg, unsigned int val)

    :param struct regmap \*map:
        Register map to write to

    :param unsigned int reg:
        Register to write to

    :param unsigned int val:
        Value to be written



.. _`regmap_write_async.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.



.. _`regmap_raw_write`:

regmap_raw_write
================

.. c:function:: int regmap_raw_write (struct regmap *map, unsigned int reg, const void *val, size_t val_len)

    :param struct regmap \*map:
        Register map to write to

    :param unsigned int reg:
        Initial register to write to

    :param const void \*val:
        Block of data to be written, laid out for direct transmission to the
        device

    :param size_t val_len:
        Length of data pointed to by val.



.. _`regmap_raw_write.description`:

Description
-----------

This function is intended to be used for things like firmware
download where a large block of data needs to be transferred to the
device.  No formatting will be done on the data provided.

A value of zero will be returned on success, a negative errno will
be returned in error cases.



.. _`regmap_field_update_bits_base`:

regmap_field_update_bits_base
=============================

.. c:function:: int regmap_field_update_bits_base (struct regmap_field *field, unsigned int mask, unsigned int val, bool *change, bool async, bool force)

    :param struct regmap_field \*field:
        Register field to write to

    :param unsigned int mask:
        Bitmask to change

    :param unsigned int val:
        Value to be written

    :param bool \*change:
        Boolean indicating if a write was done

    :param bool async:
        Boolean indicating asynchronously

    :param bool force:
        Boolean indicating use force update



.. _`regmap_field_update_bits_base.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.



.. _`regmap_field_update_bits_base.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.



.. _`regmap_fields_update_bits_base`:

regmap_fields_update_bits_base
==============================

.. c:function:: int regmap_fields_update_bits_base (struct regmap_field *field, unsigned int id, unsigned int mask, unsigned int val, bool *change, bool async, bool force)

    :param struct regmap_field \*field:
        Register field to write to

    :param unsigned int id:
        port ID

    :param unsigned int mask:
        Bitmask to change

    :param unsigned int val:
        Value to be written

    :param bool \*change:
        Boolean indicating if a write was done

    :param bool async:
        Boolean indicating asynchronously

    :param bool force:
        Boolean indicating use force update



.. _`regmap_fields_update_bits_base.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.



.. _`regmap_fields_update_bits_base.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.



.. _`regmap_raw_write_async`:

regmap_raw_write_async
======================

.. c:function:: int regmap_raw_write_async (struct regmap *map, unsigned int reg, const void *val, size_t val_len)

    :param struct regmap \*map:
        Register map to write to

    :param unsigned int reg:
        Initial register to write to

    :param const void \*val:
        Block of data to be written, laid out for direct transmission to the
        device.  Must be valid until :c:func:`regmap_async_complete` is called.

    :param size_t val_len:
        Length of data pointed to by val.



.. _`regmap_raw_write_async.description`:

Description
-----------

This function is intended to be used for things like firmware
download where a large block of data needs to be transferred to the
device.  No formatting will be done on the data provided.

If supported by the underlying bus the write will be scheduled
asynchronously, helping maximise I/O speed on higher speed buses
like SPI.  :c:func:`regmap_async_complete` can be called to ensure that all
asynchrnous writes have been completed.

A value of zero will be returned on success, a negative errno will
be returned in error cases.



.. _`regmap_raw_write_async.description`:

Description
-----------

This function is intended to be used for things like firmware
download where a large block of data needs to be transferred to the
device.  No formatting will be done on the data provided.

If supported by the underlying bus the write will be scheduled
asynchronously, helping maximise I/O speed on higher speed buses
like SPI.  :c:func:`regmap_async_complete` can be called to ensure that all
asynchrnous writes have been completed.

A value of zero will be returned on success, a negative errno will
be returned in error cases.



.. _`regmap_read`:

regmap_read
===========

.. c:function:: int regmap_read (struct regmap *map, unsigned int reg, unsigned int *val)

    :param struct regmap \*map:
        Register map to read from

    :param unsigned int reg:
        Register to be read from

    :param unsigned int \*val:
        Pointer to store read value



.. _`regmap_read.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.



.. _`regmap_raw_read`:

regmap_raw_read
===============

.. c:function:: int regmap_raw_read (struct regmap *map, unsigned int reg, void *val, size_t val_len)

    :param struct regmap \*map:
        Register map to read from

    :param unsigned int reg:
        First register to be read from

    :param void \*val:
        Pointer to store read value

    :param size_t val_len:
        Size of data to read



.. _`regmap_raw_read.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.



.. _`regmap_field_read`:

regmap_field_read
=================

.. c:function:: int regmap_field_read (struct regmap_field *field, unsigned int *val)

    :param struct regmap_field \*field:
        Register field to read from

    :param unsigned int \*val:
        Pointer to store read value



.. _`regmap_field_read.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.



.. _`regmap_fields_read`:

regmap_fields_read
==================

.. c:function:: int regmap_fields_read (struct regmap_field *field, unsigned int id, unsigned int *val)

    :param struct regmap_field \*field:
        Register field to read from

    :param unsigned int id:
        port ID

    :param unsigned int \*val:
        Pointer to store read value



.. _`regmap_fields_read.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.



.. _`regmap_bulk_read`:

regmap_bulk_read
================

.. c:function:: int regmap_bulk_read (struct regmap *map, unsigned int reg, void *val, size_t val_count)

    :param struct regmap \*map:
        Register map to read from

    :param unsigned int reg:
        First register to be read from

    :param void \*val:
        Pointer to store read value, in native register size for device

    :param size_t val_count:
        Number of registers to read



.. _`regmap_bulk_read.description`:

Description
-----------

A value of zero will be returned on success, a negative errno will
be returned in error cases.



.. _`regmap_update_bits_base`:

regmap_update_bits_base
=======================

.. c:function:: int regmap_update_bits_base (struct regmap *map, unsigned int reg, unsigned int mask, unsigned int val, bool *change, bool async, bool force)

    :param struct regmap \*map:
        Register map to update

    :param unsigned int reg:
        Register to update

    :param unsigned int mask:
        Bitmask to change

    :param unsigned int val:
        New value for bitmask

    :param bool \*change:
        Boolean indicating if a write was done

    :param bool async:
        Boolean indicating asynchronously

    :param bool force:
        Boolean indicating use force update



.. _`regmap_update_bits_base.description`:

Description
-----------

if async was true,
With most buses the read must be done synchronously so this is most
useful for devices with a cache which do not need to interact with
the hardware to determine the current register value.

Returns zero for success, a negative number on error.



.. _`regmap_update_bits_base.description`:

Description
-----------

if async was true,
With most buses the read must be done synchronously so this is most
useful for devices with a cache which do not need to interact with
the hardware to determine the current register value.

Returns zero for success, a negative number on error.



.. _`regmap_async_complete`:

regmap_async_complete
=====================

.. c:function:: int regmap_async_complete (struct regmap *map)

    :param struct regmap \*map:
        Map to operate on.



.. _`regmap_async_complete.description`:

Description
-----------

Blocks until any pending asynchronous I/O has completed.  Returns
an error code for any failed I/O operations.



.. _`regmap_register_patch`:

regmap_register_patch
=====================

.. c:function:: int regmap_register_patch (struct regmap *map, const struct reg_sequence *regs, int num_regs)

    :param struct regmap \*map:
        Register map to apply updates to.

    :param const struct reg_sequence \*regs:
        Values to update.

    :param int num_regs:
        Number of entries in regs.



.. _`regmap_register_patch.description`:

Description
-----------

Register a set of register updates to be applied to the device
whenever the device registers are synchronised with the cache and
apply them immediately.  Typically this is used to apply
corrections to be applied to the device defaults on startup, such
as the updates some vendors provide to undocumented registers.

The caller must ensure that this function cannot be called
concurrently with either itself or :c:func:`regcache_sync`.



.. _`regmap_register_patch.description`:

Description
-----------

Register a set of register updates to be applied to the device
whenever the device registers are synchronised with the cache and
apply them immediately.  Typically this is used to apply
corrections to be applied to the device defaults on startup, such
as the updates some vendors provide to undocumented registers.

The caller must ensure that this function cannot be called
concurrently with either itself or :c:func:`regcache_sync`.



.. _`regmap_get_max_register`:

regmap_get_max_register
=======================

.. c:function:: int regmap_get_max_register (struct regmap *map)

    :param struct regmap \*map:

        *undescribed*



.. _`regmap_get_max_register.description`:

Description
-----------


Report the max register value, mainly intended to for use by
generic infrastructure built on top of regmap.



.. _`regmap_get_reg_stride`:

regmap_get_reg_stride
=====================

.. c:function:: int regmap_get_reg_stride (struct regmap *map)

    :param struct regmap \*map:

        *undescribed*



.. _`regmap_get_reg_stride.description`:

Description
-----------


Report the register address stride, mainly intended to for use by
generic infrastructure built on top of regmap.

