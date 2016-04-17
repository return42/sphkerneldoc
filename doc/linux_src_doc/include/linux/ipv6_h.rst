.. -*- coding: utf-8; mode: rst -*-

======
ipv6.h
======


.. _`ipv6_pinfo`:

struct ipv6_pinfo
=================

.. c:type:: ipv6_pinfo

    ipv6 private area


.. _`ipv6_pinfo.definition`:

Definition
----------

.. code-block:: c

  struct ipv6_pinfo {
    #ifdef CONFIG_IPV6_SUBTREES
    #endif
    #if defined(__BIG_ENDIAN_BITFIELD)
    #else
    #endif
    #if defined(__BIG_ENDIAN_BITFIELD)
    #else
    #endif
  };


.. _`ipv6_pinfo.members`:

Members
-------




.. _`ipv6_pinfo.description`:

Description
-----------


In the struct sock hierarchy (tcp6_sock, upd6_sock, etc)
this _must_ be the last member, so that inet6_sk_generic
is able to calculate its offset from the base struct sock
by using the struct proto->slab_obj_size member. -acme

