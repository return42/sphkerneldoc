.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/if.h

.. _`net_device_flags`:

enum net_device_flags
=====================

.. c:type:: enum net_device_flags

    \ :c:type:`struct net_device <net_device>`\  flags

.. _`net_device_flags.definition`:

Definition
----------

.. code-block:: c

    enum net_device_flags {
        #if __UAPI_DEF_IF_NET_DEVICE_FLAGS;IFF_UP = 1<<0,
        IFF_BROADCAST,
        IFF_DEBUG,
        IFF_LOOPBACK,
        IFF_POINTOPOINT,
        IFF_NOTRAILERS,
        IFF_RUNNING,
        IFF_NOARP,
        IFF_PROMISC,
        IFF_ALLMULTI,
        IFF_MASTER,
        IFF_SLAVE,
        IFF_MULTICAST,
        IFF_PORTSEL,
        IFF_AUTOMEDIA,
        IFF_DYNAMIC,
         #if __UAPI_DEF_IF_NET_DEVICE_FLAGS_LOWER_UP_DORMANT_ECHO;IFF_LOWER_UP = 1<<16,
        IFF_DORMANT,
        IFF_ECHO
    };

.. _`net_device_flags.constants`:

Constants
---------

#if \__UAPI_DEF_IF_NET_DEVICE_FLAGS;IFF_UP = 1<<0
    *undescribed*

IFF_BROADCAST
    broadcast address valid. Volatile.

IFF_DEBUG
    turn on debugging. Can be toggled through sysfs.

IFF_LOOPBACK
    is a loopback net. Volatile.

IFF_POINTOPOINT
    interface is has p-p link. Volatile.

IFF_NOTRAILERS
    avoid use of trailers. Can be toggled through sysfs.
    Volatile.

IFF_RUNNING
    interface RFC2863 OPER_UP. Volatile.

IFF_NOARP
    no ARP protocol. Can be toggled through sysfs. Volatile.

IFF_PROMISC
    receive all packets. Can be toggled through sysfs.

IFF_ALLMULTI
    receive all multicast packets. Can be toggled through
    sysfs.

IFF_MASTER
    master of a load balancer. Volatile.

IFF_SLAVE
    slave of a load balancer. Volatile.

IFF_MULTICAST
    Supports multicast. Can be toggled through sysfs.

IFF_PORTSEL
    can set media type. Can be toggled through sysfs.

IFF_AUTOMEDIA
    auto media select active. Can be toggled through sysfs.

IFF_DYNAMIC
    dialup device with changing addresses. Can be toggled
    through sysfs.

#if \__UAPI_DEF_IF_NET_DEVICE_FLAGS_LOWER_UP_DORMANT_ECHO;IFF_LOWER_UP = 1<<16
    *undescribed*

IFF_DORMANT
    driver signals dormant. Volatile.

IFF_ECHO
    echo sent packets. Volatile.

.. _`net_device_flags.description`:

Description
-----------

These are the \ :c:type:`struct net_device <net_device>`\  flags, they can be set by drivers, the
kernel and some can be triggered by userspace. Userspace can query and
set these flags using userspace utilities but there is also a sysfs
entry available for all dev flags which can be queried and set. These flags
are shared for all types of net_devices. The sysfs entries are available
via /sys/class/net/<dev>/flags. Flags which can be toggled through sysfs
are annotated below, note that only a few flags can be toggled and some
other flags are always preserved from the original net_device flags
even if you try to set them via sysfs. Flags which are always preserved
are kept under the flag grouping \ ``IFF_VOLATILE``\ . Flags which are volatile
are annotated below as such.

You should have a pretty good reason to be extending these flags.

.. This file was automatic generated / don't edit.

