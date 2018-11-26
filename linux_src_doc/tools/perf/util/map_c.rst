.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/map.c

.. _`map__rip_2objdump`:

map__rip_2objdump
=================

.. c:function:: u64 map__rip_2objdump(struct map *map, u64 rip)

    convert symbol start address to objdump address.

    :param map:
        memory map
    :type map: struct map \*

    :param rip:
        symbol start address
    :type rip: u64

.. _`map__rip_2objdump.description`:

Description
-----------

objdump wants/reports absolute IPs for ET_EXEC, and RIPs for ET_DYN.
map->dso->adjust_symbols==1 for ET_EXEC-like cases except ET_REL which is
relative to section start.

.. _`map__rip_2objdump.return`:

Return
------

Address suitable for passing to "objdump --start-address="

.. _`map__objdump_2mem`:

map__objdump_2mem
=================

.. c:function:: u64 map__objdump_2mem(struct map *map, u64 ip)

    convert objdump address to a memory address.

    :param map:
        memory map
    :type map: struct map \*

    :param ip:
        objdump address
    :type ip: u64

.. _`map__objdump_2mem.description`:

Description
-----------

Closely related to \ :c:func:`map__rip_2objdump`\ , this function takes an address from
objdump and converts it to a memory address.  Note this assumes that \ ``map``\ 
contains the address.  To be sure the result is valid, check it forwards
e.g. map__rip_2objdump(map->map_ip(map, map__objdump_2mem(map, ip))) == ip

.. _`map__objdump_2mem.return`:

Return
------

Memory address.

.. This file was automatic generated / don't edit.

