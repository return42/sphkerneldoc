.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mmzone.h

.. _`is_highmem`:

is_highmem
==========

.. c:function:: int is_highmem(struct zone *zone)

    helper function to quickly check if a struct zone is a highmem zone or not.  This is an attempt to keep references to ZONE_{DMA/NORMAL/HIGHMEM/etc} in general code to a minimum. \ ``zone``\  - pointer to struct zone variable

    :param struct zone \*zone:
        *undescribed*

.. _`for_each_online_pgdat`:

for_each_online_pgdat
=====================

.. c:function::  for_each_online_pgdat( pgdat)

    helper macro to iterate over all online nodes \ ``pgdat``\  - pointer to a pg_data_t variable

    :param  pgdat:
        *undescribed*

.. _`for_each_zone`:

for_each_zone
=============

.. c:function::  for_each_zone( zone)

    helper macro to iterate over all memory zones \ ``zone``\  - pointer to struct zone variable

    :param  zone:
        *undescribed*

.. _`for_each_zone.description`:

Description
-----------

The user only needs to declare the zone variable, for_each_zone
fills it in.

.. _`next_zones_zonelist`:

next_zones_zonelist
===================

.. c:function:: struct zoneref *next_zones_zonelist(struct zoneref *z, enum zone_type highest_zoneidx, nodemask_t *nodes)

    Returns the next zone at or below highest_zoneidx within the allowed nodemask using a cursor within a zonelist as a starting point \ ``z``\  - The cursor used as a starting point for the search \ ``highest_zoneidx``\  - The zone index of the highest zone to return \ ``nodes``\  - An optional nodemask to filter the zonelist with

    :param struct zoneref \*z:
        *undescribed*

    :param enum zone_type highest_zoneidx:
        *undescribed*

    :param nodemask_t \*nodes:
        *undescribed*

.. _`next_zones_zonelist.description`:

Description
-----------

This function returns the next zone at or below a given zone index that is
within the allowed nodemask using a cursor as the starting point for the
search. The zoneref returned is a cursor that represents the current zone
being examined. It should be advanced by one before calling
next_zones_zonelist again.

.. _`first_zones_zonelist`:

first_zones_zonelist
====================

.. c:function:: struct zoneref *first_zones_zonelist(struct zonelist *zonelist, enum zone_type highest_zoneidx, nodemask_t *nodes)

    Returns the first zone at or below highest_zoneidx within the allowed nodemask in a zonelist \ ``zonelist``\  - The zonelist to search for a suitable zone \ ``highest_zoneidx``\  - The zone index of the highest zone to return \ ``nodes``\  - An optional nodemask to filter the zonelist with \ ``return``\  - Zoneref pointer for the first suitable zone found (see below)

    :param struct zonelist \*zonelist:
        *undescribed*

    :param enum zone_type highest_zoneidx:
        *undescribed*

    :param nodemask_t \*nodes:
        *undescribed*

.. _`first_zones_zonelist.description`:

Description
-----------

This function returns the first zone at or below a given zone index that is
within the allowed nodemask. The zoneref returned is a cursor that can be
used to iterate the zonelist with next_zones_zonelist by advancing it by
one before calling.

When no eligible zone is found, zoneref->zone is NULL (zoneref itself is
never NULL). This may happen either genuinely, or due to concurrent nodemask
update due to cpuset modification.

.. _`for_each_zone_zonelist_nodemask`:

for_each_zone_zonelist_nodemask
===============================

.. c:function::  for_each_zone_zonelist_nodemask( zone,  z,  zlist,  highidx,  nodemask)

    helper macro to iterate over valid zones in a zonelist at or below a given zone index and within a nodemask \ ``zone``\  - The current zone in the iterator \ ``z``\  - The current pointer within zonelist->zones being iterated \ ``zlist``\  - The zonelist being iterated \ ``highidx``\  - The zone index of the highest zone to return \ ``nodemask``\  - Nodemask allowed by the allocator

    :param  zone:
        *undescribed*

    :param  z:
        *undescribed*

    :param  zlist:
        *undescribed*

    :param  highidx:
        *undescribed*

    :param  nodemask:
        *undescribed*

.. _`for_each_zone_zonelist_nodemask.description`:

Description
-----------

This iterator iterates though all zones at or below a given zone index and
within a given nodemask

.. _`for_each_zone_zonelist`:

for_each_zone_zonelist
======================

.. c:function::  for_each_zone_zonelist( zone,  z,  zlist,  highidx)

    helper macro to iterate over valid zones in a zonelist at or below a given zone index \ ``zone``\  - The current zone in the iterator \ ``z``\  - The current pointer within zonelist->zones being iterated \ ``zlist``\  - The zonelist being iterated \ ``highidx``\  - The zone index of the highest zone to return

    :param  zone:
        *undescribed*

    :param  z:
        *undescribed*

    :param  zlist:
        *undescribed*

    :param  highidx:
        *undescribed*

.. _`for_each_zone_zonelist.description`:

Description
-----------

This iterator iterates though all zones at or below a given zone index.

.. This file was automatic generated / don't edit.

