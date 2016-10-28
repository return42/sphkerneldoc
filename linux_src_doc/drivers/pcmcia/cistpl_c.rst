.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pcmcia/cistpl.c

.. _`set_cis_map`:

set_cis_map
===========

.. c:function:: void __iomem *set_cis_map(struct pcmcia_socket *s, unsigned int card_offset, unsigned int flags)

    map the card memory at "card_offset" into virtual space.

    :param struct pcmcia_socket \*s:
        *undescribed*

    :param unsigned int card_offset:
        *undescribed*

    :param unsigned int flags:
        *undescribed*

.. _`set_cis_map.description`:

Description
-----------

If flags & MAP_ATTRIB, map the attribute space, otherwise
map the memory space.

Must be called with ops_mutex held.

.. _`pcmcia_read_cis_mem`:

pcmcia_read_cis_mem
===================

.. c:function:: int pcmcia_read_cis_mem(struct pcmcia_socket *s, int attr, u_int addr, u_int len, void *ptr)

    low-level function to read CIS memory

    :param struct pcmcia_socket \*s:
        *undescribed*

    :param int attr:
        *undescribed*

    :param u_int addr:
        *undescribed*

    :param u_int len:
        *undescribed*

    :param void \*ptr:
        *undescribed*

.. _`pcmcia_read_cis_mem.description`:

Description
-----------

must be called with ops_mutex held

.. _`pcmcia_write_cis_mem`:

pcmcia_write_cis_mem
====================

.. c:function:: int pcmcia_write_cis_mem(struct pcmcia_socket *s, int attr, u_int addr, u_int len, void *ptr)

    low-level function to write CIS memory

    :param struct pcmcia_socket \*s:
        *undescribed*

    :param int attr:
        *undescribed*

    :param u_int addr:
        *undescribed*

    :param u_int len:
        *undescribed*

    :param void \*ptr:
        *undescribed*

.. _`pcmcia_write_cis_mem.description`:

Description
-----------

Probably only useful for writing one-byte registers. Must be called
with ops_mutex held.

.. _`read_cis_cache`:

read_cis_cache
==============

.. c:function:: int read_cis_cache(struct pcmcia_socket *s, int attr, u_int addr, size_t len, void *ptr)

    read CIS memory or its associated cache

    :param struct pcmcia_socket \*s:
        *undescribed*

    :param int attr:
        *undescribed*

    :param u_int addr:
        *undescribed*

    :param size_t len:
        *undescribed*

    :param void \*ptr:
        *undescribed*

.. _`read_cis_cache.description`:

Description
-----------

This is a wrapper around read_cis_mem, with the same interface,
but which caches information, for cards whose CIS may not be
readable all the time.

.. _`destroy_cis_cache`:

destroy_cis_cache
=================

.. c:function:: void destroy_cis_cache(struct pcmcia_socket *s)

    destroy the CIS cache

    :param struct pcmcia_socket \*s:
        pcmcia_socket for which CIS cache shall be destroyed

.. _`destroy_cis_cache.description`:

Description
-----------

This destroys the CIS cache but keeps any fake CIS alive. Must be
called with ops_mutex held.

.. _`verify_cis_cache`:

verify_cis_cache
================

.. c:function:: int verify_cis_cache(struct pcmcia_socket *s)

    does the CIS match what is in the CIS cache?

    :param struct pcmcia_socket \*s:
        *undescribed*

.. _`pcmcia_replace_cis`:

pcmcia_replace_cis
==================

.. c:function:: int pcmcia_replace_cis(struct pcmcia_socket *s, const u8 *data, const size_t len)

    use a replacement CIS instead of the card's CIS

    :param struct pcmcia_socket \*s:
        *undescribed*

    :param const u8 \*data:
        *undescribed*

    :param const size_t len:
        *undescribed*

.. _`pcmcia_replace_cis.description`:

Description
-----------

For really bad cards, we provide a facility for uploading a
replacement CIS.

.. _`pccard_validate_cis`:

pccard_validate_cis
===================

.. c:function:: int pccard_validate_cis(struct pcmcia_socket *s, unsigned int *info)

    check whether card has a sensible CIS

    :param struct pcmcia_socket \*s:
        the struct pcmcia_socket we are to check

    :param unsigned int \*info:
        returns the number of tuples in the (valid) CIS, or 0

.. _`pccard_validate_cis.description`:

Description
-----------

This tries to determine if a card has a sensible CIS.  In \ ``info``\ , it
returns the number of tuples in the CIS, or 0 if the CIS looks bad. The
checks include making sure several critical tuples are present and
valid; seeing if the total number of tuples is reasonable; and
looking for tuples that use reserved codes.

The function returns 0 on success.

.. This file was automatic generated / don't edit.

