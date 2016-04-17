.. -*- coding: utf-8; mode: rst -*-

==========
regcache.c
==========


.. _`regcache_read`:

regcache_read
=============

.. c:function:: int regcache_read (struct regmap *map, unsigned int reg, unsigned int *value)

    :param struct regmap \*map:
        map to configure.

    :param unsigned int reg:
        The register index.

    :param unsigned int \*value:
        The value to be returned.



.. _`regcache_read.description`:

Description
-----------

Return a negative value on failure, 0 on success.



.. _`regcache_write`:

regcache_write
==============

.. c:function:: int regcache_write (struct regmap *map, unsigned int reg, unsigned int value)

    :param struct regmap \*map:
        map to configure.

    :param unsigned int reg:
        The register index.

    :param unsigned int value:
        The new register value.



.. _`regcache_write.description`:

Description
-----------

Return a negative value on failure, 0 on success.



.. _`regcache_sync`:

regcache_sync
=============

.. c:function:: int regcache_sync (struct regmap *map)

    :param struct regmap \*map:
        map to configure.



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

.. c:function:: int regcache_sync_region (struct regmap *map, unsigned int min, unsigned int max)

    :param struct regmap \*map:
        map to sync.

    :param unsigned int min:
        first register to sync

    :param unsigned int max:
        last register to sync



.. _`regcache_sync_region.description`:

Description
-----------

Write all non-default register values in the specified region to
the hardware.

Return a negative value on failure, 0 on success.



.. _`regcache_drop_region`:

regcache_drop_region
====================

.. c:function:: int regcache_drop_region (struct regmap *map, unsigned int min, unsigned int max)

    :param struct regmap \*map:
        map to operate on

    :param unsigned int min:
        first register to discard

    :param unsigned int max:
        last register to discard



.. _`regcache_drop_region.description`:

Description
-----------

Discard part of the register cache.

Return a negative value on failure, 0 on success.



.. _`regcache_cache_only`:

regcache_cache_only
===================

.. c:function:: void regcache_cache_only (struct regmap *map, bool enable)

    :param struct regmap \*map:
        map to configure

    :param bool enable:

        *undescribed*



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

.. c:function:: void regcache_mark_dirty (struct regmap *map)

    :param struct regmap \*map:
        map to mark



.. _`regcache_mark_dirty.description`:

Description
-----------

Inform regcache that the device has been powered down or reset, so that
on resume, :c:func:`regcache_sync` knows to write out all non-default values
stored in the cache.

If this function is not called, :c:func:`regcache_sync` will assume that
the hardware state still matches the cache state, modulo any writes that
happened when cache_only was true.



.. _`regcache_cache_bypass`:

regcache_cache_bypass
=====================

.. c:function:: void regcache_cache_bypass (struct regmap *map, bool enable)

    :param struct regmap \*map:
        map to configure

    :param bool enable:

        *undescribed*



.. _`regcache_cache_bypass.description`:

Description
-----------

When a register map is marked with the cache bypass option, writes
to the register map API will only update the hardware and not the
the cache directly.  This is useful when syncing the cache back to
the hardware.

