.. -*- coding: utf-8; mode: rst -*-

=========
if_caif.h
=========


.. _`ifla_caif`:

enum ifla_caif
==============

.. c:type:: ifla_caif

    CAIF NetlinkRT parameters.


.. _`ifla_caif.definition`:

Definition
----------

.. code-block:: c

    enum ifla_caif {
      __IFLA_CAIF_UNSPEC,
      IFLA_CAIF_IPV4_CONNID,
      IFLA_CAIF_IPV6_CONNID,
      IFLA_CAIF_LOOPBACK,
      __IFLA_CAIF_MAX
    };


.. _`ifla_caif.constants`:

Constants
---------

:``__IFLA_CAIF_UNSPEC``:
-- undescribed --

:``IFLA_CAIF_IPV4_CONNID``:
    Connection ID for IPv4 PDP Context.
    The type of attribute is NLA_U32.

:``IFLA_CAIF_IPV6_CONNID``:
    Connection ID for IPv6 PDP Context.
    The type of attribute is NLA_U32.

:``IFLA_CAIF_LOOPBACK``:
    If different from zero, device is doing loopback
    The type of attribute is NLA_U8.

:``__IFLA_CAIF_MAX``:
-- undescribed --


.. _`ifla_caif.description`:

Description
-----------

When using RT Netlink to create, destroy or configure a CAIF IP interface,
enum ifla_caif is used to specify the configuration attributes.

