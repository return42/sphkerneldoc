.. -*- coding: utf-8; mode: rst -*-

================
flow_dissector.h
================


.. _`flow_dissector_key_control`:

struct flow_dissector_key_control
=================================

.. c:type:: flow_dissector_key_control

    


.. _`flow_dissector_key_control.definition`:

Definition
----------

.. code-block:: c

  struct flow_dissector_key_control {
    u16 thoff;
  };


.. _`flow_dissector_key_control.members`:

Members
-------

:``thoff``:
    Transport header offset




.. _`flow_dissector_key_basic`:

struct flow_dissector_key_basic
===============================

.. c:type:: flow_dissector_key_basic

    


.. _`flow_dissector_key_basic.definition`:

Definition
----------

.. code-block:: c

  struct flow_dissector_key_basic {
    __be16 n_proto;
    u8 ip_proto;
  };


.. _`flow_dissector_key_basic.members`:

Members
-------

:``n_proto``:
    Network header protocol (eg. IPv4/IPv6)

:``ip_proto``:
    Transport header protocol (eg. TCP/UDP)




.. _`flow_dissector_key_ipv4_addrs`:

struct flow_dissector_key_ipv4_addrs
====================================

.. c:type:: flow_dissector_key_ipv4_addrs

    


.. _`flow_dissector_key_ipv4_addrs.definition`:

Definition
----------

.. code-block:: c

  struct flow_dissector_key_ipv4_addrs {
    __be32 src;
    __be32 dst;
  };


.. _`flow_dissector_key_ipv4_addrs.members`:

Members
-------

:``src``:
    source ip address

:``dst``:
    destination ip address




.. _`flow_dissector_key_ipv6_addrs`:

struct flow_dissector_key_ipv6_addrs
====================================

.. c:type:: flow_dissector_key_ipv6_addrs

    


.. _`flow_dissector_key_ipv6_addrs.definition`:

Definition
----------

.. code-block:: c

  struct flow_dissector_key_ipv6_addrs {
    struct in6_addr src;
    struct in6_addr dst;
  };


.. _`flow_dissector_key_ipv6_addrs.members`:

Members
-------

:``src``:
    source ip address

:``dst``:
    destination ip address




.. _`flow_dissector_key_tipc_addrs`:

struct flow_dissector_key_tipc_addrs
====================================

.. c:type:: flow_dissector_key_tipc_addrs

    


.. _`flow_dissector_key_tipc_addrs.definition`:

Definition
----------

.. code-block:: c

  struct flow_dissector_key_tipc_addrs {
    __be32 srcnode;
  };


.. _`flow_dissector_key_tipc_addrs.members`:

Members
-------

:``srcnode``:
    source node address




.. _`flow_dissector_key_addrs`:

struct flow_dissector_key_addrs
===============================

.. c:type:: flow_dissector_key_addrs

    


.. _`flow_dissector_key_addrs.definition`:

Definition
----------

.. code-block:: c

  struct flow_dissector_key_addrs {
    union {unnamed_union};
  };


.. _`flow_dissector_key_addrs.members`:

Members
-------

:``{unnamed_union}``:
    anonymous




.. _`flow_dissector_key_eth_addrs`:

struct flow_dissector_key_eth_addrs
===================================

.. c:type:: flow_dissector_key_eth_addrs

    


.. _`flow_dissector_key_eth_addrs.definition`:

Definition
----------

.. code-block:: c

  struct flow_dissector_key_eth_addrs {
    unsigned char dst[ETH_ALEN];
    unsigned char src[ETH_ALEN];
  };


.. _`flow_dissector_key_eth_addrs.members`:

Members
-------

:``dst[ETH_ALEN]``:
    destination Ethernet address

:``src[ETH_ALEN]``:
    source Ethernet address


