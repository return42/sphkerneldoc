.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/macvlan.c

.. _`macvlan_changelink_sources`:

macvlan_changelink_sources
==========================

.. c:function:: int macvlan_changelink_sources(struct macvlan_dev *vlan, u32 mode, struct nlattr  *data)

    (only for macvlan devices in source mode)

    :param vlan:
        *undescribed*
    :type vlan: struct macvlan_dev \*

    :param mode:
        *undescribed*
    :type mode: u32

    :param data:
        *undescribed*
    :type data: struct nlattr  \*

.. _`macvlan_changelink_sources.note-regarding-alignment`:

Note regarding alignment
------------------------

all netlink data is aligned to 4 Byte, which
suffices for both ether_addr_copy and ether_addr_equal_64bits usage.

.. This file was automatic generated / don't edit.

