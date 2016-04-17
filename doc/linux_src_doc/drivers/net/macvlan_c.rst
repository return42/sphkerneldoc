.. -*- coding: utf-8; mode: rst -*-

=========
macvlan.c
=========


.. _`macvlan_changelink_sources`:

macvlan_changelink_sources
==========================

.. c:function:: int macvlan_changelink_sources (struct macvlan_dev *vlan, u32 mode, struct nlattr *data[])

    :param struct macvlan_dev \*vlan:

        *undescribed*

    :param u32 mode:

        *undescribed*

    :param struct nlattr \*data:

        *undescribed*



.. _`macvlan_changelink_sources.description`:

Description
-----------

(only for macvlan devices in source mode)



.. _`macvlan_changelink_sources.note-regarding-alignment`:

Note regarding alignment
------------------------

all netlink data is aligned to 4 Byte, which
suffices for both ether_addr_copy and ether_addr_equal_64bits usage.

