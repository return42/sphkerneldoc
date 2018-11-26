.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/regmap/regcache.c

.. _`regcache_read`:

regcache_read
=============

.. c:function:: int regcache_read(struct regmap *map, unsigned int reg, unsigned int *value)

    Fetch the value of a given register from the cache.

    :param map:
        map to configure.
    :type map: struct regmap \*

    :param reg:
        The register index.
    :type reg: unsigned int

    :param value:
        The value to be returned.
    :type value: unsigned int \*

.. _`regcache_read.description`:

Description
-----------

Return a negative value on failure, 0 on success.

.. _`regcache_write`:

regcache_write
==============

.. c:function:: int regcache_write(struct regmap *map, unsigned int reg, unsigned int value)

    Set the value of a given register in the cache.

    :param map:
        map to configure.
    :type map: struct regmap \*

    :param reg:
        The register index.
    :type reg: unsigned int

    :param value:
        The new register value.
    :type value: unsigned int

.. _`regcache_write.description`:

Description
-----------

Return a negative value on failure, 0 on success.

.. _`regcache_sync`:

regcache_sync
=============

.. c:function:: int regcache_sync(struct regmap *map)

    Sync the register cache with the hardware.

    :param map:
        map to configure.
    :type map: struct regmap \*

.. _`regcache_sync.description`:

Description
-----------

Any registers that should not be synced should be marked as
volatile.  In general drivers can choose not to use the provided
syncing functionality if they so require.

Return a negative value on failure, 0 on success.

.. _`regcache_sync_region`:

regcache_sync_region
====================

.. c:function:: int regcache_sync_region(struct regmap *map, unsigned int min, unsigned int max)

    Sync part  of the register cache with the hardware.

    :param map:
        map to sync.
    :type map: struct regmap \*

    :param min:
        first register to sync
    :type min: unsigned int

    :param max:
        last register to sync
    :type max: unsigned int

.. _`regcache_sync_region.description`:

Description
-----------

Write all non-default register values in the specified region to
the hardware.

Return a negative value on failure, 0 on success.

.. _`regcache_drop_region`:

regcache_drop_region
====================

.. c:function:: int regcache_drop_region(struct regmap *map, unsigned int min, unsigned int max)

    Discard part of the register cache

    :param map:
        map to operate on
    :type map: struct regmap \*

    :param min:
        first register to discard
    :type min: unsigned int

    :param max:
        last register to discard
    :type max: unsigned int

.. _`regcache_drop_region.description`:

Description
-----------

Discard part of the register cache.

Return a negative value on failure, 0 on success.

.. _`regcache_cache_only`:

regcache_cache_only
===================

.. c:function:: void regcache_cache_only(struct regmap *map, bool enable)

    Put a register map into cache only mode

    :param map:
        map to configure
    :type map: struct regmap \*

    :param enable:
        flag if changes should be written to the hardware
    :type enable: bool

.. _`regcache_cache_only.description`:

Description
-----------

When a register map is marked as cache only writes to the register
map API will only update the register cache, they will not cause
any hardware changes.  This is useful for allowing portions of
drivers to act as though the device were functioning as normal when
it is disabled for power saving reasons.

.. _`regcache_mark_dirty`:

regcache_mark_dirty
===================

.. c:function:: void regcache_mark_dirty(struct regmap *map)

    Indicate that HW registers were reset to default values

    :param map:
        map to mark
    :type map: struct regmap \*

.. _`regcache_mark_dirty.description`:

Description
-----------

Inform regcache that the device has been powered down or reset, so that
on resume, \ :c:func:`regcache_sync`\  knows to write out all non-default values
stored in the cache.

If this function is not called, \ :c:func:`regcache_sync`\  will assume that
the hardware state still matches the cache state, modulo any writes that
happened when cache_only was true.

.. _`regcache_cache_bypass`:

regcache_cache_bypass
=====================

.. c:function:: void regcache_cache_bypass(struct regmap *map, bool enable)

    Put a register map into cache bypass mode

    :param map:
        map to configure
    :type map: struct regmap \*

    :param enable:
        flag if changes should not be written to the cache
    :type enable: bool

.. _`regcache_cache_bypass.description`:

Description
-----------

When a register map is marked with the cache bypass option, writes
to the register map API will only update the hardware and not the
the cache directly.  This is useful when syncing the cache back to
the hardware.

.. This file was automatic generated / don't edit.

