.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/addr.c

.. _`in_own_cluster`:

in_own_cluster
==============

.. c:function:: int in_own_cluster(struct net *net, u32 addr)

    test for cluster inclusion; <0.0.0> always matches

    :param struct net \*net:
        *undescribed*

    :param u32 addr:
        *undescribed*

.. _`in_own_node`:

in_own_node
===========

.. c:function:: int in_own_node(struct net *net, u32 addr)

    test for node inclusion; <0.0.0> always matches

    :param struct net \*net:
        *undescribed*

    :param u32 addr:
        *undescribed*

.. _`addr_domain`:

addr_domain
===========

.. c:function:: u32 addr_domain(struct net *net, u32 sc)

    convert 2-bit scope value to equivalent message lookup domain

    :param struct net \*net:
        *undescribed*

    :param u32 sc:
        *undescribed*

.. _`addr_domain.description`:

Description
-----------

Needed when address of a named message must be looked up a second time
after a network hop.

.. _`tipc_addr_domain_valid`:

tipc_addr_domain_valid
======================

.. c:function:: int tipc_addr_domain_valid(u32 addr)

    validates a network domain address

    :param u32 addr:
        *undescribed*

.. _`tipc_addr_domain_valid.description`:

Description
-----------

Accepts <Z.C.N>, <Z.C.0>, <Z.0.0>, and <0.0.0>,
where Z, C, and N are non-zero.

Returns 1 if domain address is valid, otherwise 0

.. _`tipc_addr_node_valid`:

tipc_addr_node_valid
====================

.. c:function:: int tipc_addr_node_valid(u32 addr)

    validates a proposed network address for this node

    :param u32 addr:
        *undescribed*

.. _`tipc_addr_node_valid.description`:

Description
-----------

Accepts <Z.C.N>, where Z, C, and N are non-zero.

Returns 1 if address can be used, otherwise 0

.. _`tipc_addr_scope`:

tipc_addr_scope
===============

.. c:function:: int tipc_addr_scope(u32 domain)

    convert message lookup domain to a 2-bit scope value

    :param u32 domain:
        *undescribed*

.. This file was automatic generated / don't edit.

