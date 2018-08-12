.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/dst_cache.h

.. _`dst_cache_get`:

dst_cache_get
=============

.. c:function:: struct dst_entry *dst_cache_get(struct dst_cache *dst_cache)

    perform cache lookup

    :param struct dst_cache \*dst_cache:
        the cache

.. _`dst_cache_get.description`:

Description
-----------

The caller should use \ :c:func:`dst_cache_get_ip4`\  if it need to retrieve the
source address to be used when xmitting to the cached dst.
local BH must be disabled.

.. _`dst_cache_get_ip4`:

dst_cache_get_ip4
=================

.. c:function:: struct rtable *dst_cache_get_ip4(struct dst_cache *dst_cache, __be32 *saddr)

    perform cache lookup and fetch ipv4 source address

    :param struct dst_cache \*dst_cache:
        the cache

    :param __be32 \*saddr:
        return value for the retrieved source address

.. _`dst_cache_get_ip4.description`:

Description
-----------

local BH must be disabled.

.. _`dst_cache_set_ip4`:

dst_cache_set_ip4
=================

.. c:function:: void dst_cache_set_ip4(struct dst_cache *dst_cache, struct dst_entry *dst, __be32 saddr)

    store the ipv4 dst into the cache

    :param struct dst_cache \*dst_cache:
        the cache

    :param struct dst_entry \*dst:
        the entry to be cached

    :param __be32 saddr:
        the source address to be stored inside the cache

.. _`dst_cache_set_ip4.description`:

Description
-----------

local BH must be disabled.

.. _`dst_cache_set_ip6`:

dst_cache_set_ip6
=================

.. c:function:: void dst_cache_set_ip6(struct dst_cache *dst_cache, struct dst_entry *dst, const struct in6_addr *saddr)

    store the ipv6 dst into the cache

    :param struct dst_cache \*dst_cache:
        the cache

    :param struct dst_entry \*dst:
        the entry to be cached

    :param const struct in6_addr \*saddr:
        the source address to be stored inside the cache

.. _`dst_cache_set_ip6.description`:

Description
-----------

local BH must be disabled.

.. _`dst_cache_get_ip6`:

dst_cache_get_ip6
=================

.. c:function:: struct dst_entry *dst_cache_get_ip6(struct dst_cache *dst_cache, struct in6_addr *saddr)

    perform cache lookup and fetch ipv6 source address

    :param struct dst_cache \*dst_cache:
        the cache

    :param struct in6_addr \*saddr:
        return value for the retrieved source address

.. _`dst_cache_get_ip6.description`:

Description
-----------

local BH must be disabled.

.. _`dst_cache_reset`:

dst_cache_reset
===============

.. c:function:: void dst_cache_reset(struct dst_cache *dst_cache)

    invalidate the cache contents

    :param struct dst_cache \*dst_cache:
        the cache

.. _`dst_cache_reset.description`:

Description
-----------

This does not free the cached dst to avoid races and contentions.
the dst will be freed on later cache lookup.

.. _`dst_cache_init`:

dst_cache_init
==============

.. c:function:: int dst_cache_init(struct dst_cache *dst_cache, gfp_t gfp)

    initialize the cache, allocating the required storage

    :param struct dst_cache \*dst_cache:
        the cache

    :param gfp_t gfp:
        allocation flags

.. _`dst_cache_destroy`:

dst_cache_destroy
=================

.. c:function:: void dst_cache_destroy(struct dst_cache *dst_cache)

    empty the cache and free the allocated storage

    :param struct dst_cache \*dst_cache:
        the cache

.. _`dst_cache_destroy.no-synchronization-is-enforced`:

No synchronization is enforced
------------------------------

it must be called only when the cache
is unsed.

.. This file was automatic generated / don't edit.

