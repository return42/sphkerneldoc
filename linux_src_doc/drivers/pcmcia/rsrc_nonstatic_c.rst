.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pcmcia/rsrc_nonstatic.c

.. _`readable`:

readable
========

.. c:function:: int readable(struct pcmcia_socket *s, struct resource *res, unsigned int *count)

    iomem validation function for cards with a valid CIS

    :param s:
        *undescribed*
    :type s: struct pcmcia_socket \*

    :param res:
        *undescribed*
    :type res: struct resource \*

    :param count:
        *undescribed*
    :type count: unsigned int \*

.. _`checksum`:

checksum
========

.. c:function:: int checksum(struct pcmcia_socket *s, struct resource *res, unsigned int *value)

    iomem validation function for simple memory cards

    :param s:
        *undescribed*
    :type s: struct pcmcia_socket \*

    :param res:
        *undescribed*
    :type res: struct resource \*

    :param value:
        *undescribed*
    :type value: unsigned int \*

.. _`do_validate_mem`:

do_validate_mem
===============

.. c:function:: int do_validate_mem(struct pcmcia_socket *s, unsigned long base, unsigned long size, int validate (struct pcmcia_socket *s# struct resource *res# unsigned int *value)

    low level validate a memory region for PCMCIA use

    :param s:
        PCMCIA socket to validate
    :type s: struct pcmcia_socket \*

    :param base:
        start address of resource to check
    :type base: unsigned long

    :param size:
        size of resource to check
    :type size: unsigned long

    :param value:
        *undescribed*
    :type value: int validate (struct pcmcia_socket \*s# struct resource \*res# unsigned int \*

.. _`do_validate_mem.description`:

Description
-----------

\ :c:func:`do_validate_mem`\  splits up the memory region which is to be checked
into two parts. Both are passed to the \ ``validate``\ () function. If
\ ``validate``\ () returns non-zero, or the value parameter to \ ``validate``\ ()
is zero, or the value parameter is different between both calls,
the check fails, and -EINVAL is returned. Else, 0 is returned.

.. _`do_mem_probe`:

do_mem_probe
============

.. c:function:: int do_mem_probe(struct pcmcia_socket *s, u_long base, u_long num, int fallback (struct pcmcia_socket *s# struct resource *res# unsigned int *value, int fallback (struct pcmcia_socket *s# struct resource *res# unsigned int *value)

    validate a memory region for PCMCIA use

    :param s:
        PCMCIA socket to validate
    :type s: struct pcmcia_socket \*

    :param base:
        start address of resource to check
    :type base: u_long

    :param num:
        size of resource to check
    :type num: u_long

    :param value:
        *undescribed*
    :type value: int fallback (struct pcmcia_socket \*s# struct resource \*res# unsigned int \*

    :param value:
        *undescribed*
    :type value: int fallback (struct pcmcia_socket \*s# struct resource \*res# unsigned int \*

.. _`do_mem_probe.description`:

Description
-----------

\ :c:func:`do_mem_probe`\  checks a memory region for use by the PCMCIA subsystem.
To do so, the area is split up into sensible parts, and then passed
into the \ ``validate``\ () function. Only if \ ``validate``\ () and \ ``fallback``\ () fail,
the area is marked as unavaibale for use by the PCMCIA subsystem. The
function returns the size of the usable memory area.

.. _`inv_probe`:

inv_probe
=========

.. c:function:: u_long inv_probe(struct resource_map *m, struct pcmcia_socket *s)

    top-to-bottom search for one usuable high memory area

    :param m:
        resource_map to check
    :type m: struct resource_map \*

    :param s:
        PCMCIA socket to validate
    :type s: struct pcmcia_socket \*

.. _`validate_mem`:

validate_mem
============

.. c:function:: int validate_mem(struct pcmcia_socket *s, unsigned int probe_mask)

    memory probe function

    :param s:
        PCMCIA socket to validate
    :type s: struct pcmcia_socket \*

    :param probe_mask:
        MEM_PROBE_LOW \| MEM_PROBE_HIGH
    :type probe_mask: unsigned int

.. _`validate_mem.description`:

Description
-----------

The memory probe.  If the memory list includes a 64K-aligned block
below 1MB, we probe in 64K chunks, and as soon as we accumulate at
least mem_limit free space, we quit. Returns 0 on usuable ports.

.. _`validate_mem`:

validate_mem
============

.. c:function:: int validate_mem(struct pcmcia_socket *s, unsigned int probe_mask)

    memory probe function

    :param s:
        PCMCIA socket to validate
    :type s: struct pcmcia_socket \*

    :param probe_mask:
        ignored
    :type probe_mask: unsigned int

.. _`validate_mem.description`:

Description
-----------

Returns 0 on usuable ports.

.. _`pcmcia_nonstatic_validate_mem`:

pcmcia_nonstatic_validate_mem
=============================

.. c:function:: int pcmcia_nonstatic_validate_mem(struct pcmcia_socket *s)

    try to validate iomem for PCMCIA use

    :param s:
        PCMCIA socket to validate
    :type s: struct pcmcia_socket \*

.. _`pcmcia_nonstatic_validate_mem.description`:

Description
-----------

This is tricky... when we set up CIS memory, we try to validate
the memory window space allocations.

.. _`pcmcia_nonstatic_validate_mem.locking-note`:

Locking note
------------

Must be called with skt_mutex held!

.. This file was automatic generated / don't edit.

