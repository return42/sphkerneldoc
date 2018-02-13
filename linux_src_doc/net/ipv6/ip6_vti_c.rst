.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv6/ip6_vti.c

.. _`vti6_tnl_lookup`:

vti6_tnl_lookup
===============

.. c:function:: struct ip6_tnl *vti6_tnl_lookup(struct net *net, const struct in6_addr *remote, const struct in6_addr *local)

    fetch tunnel matching the end-point addresses

    :param struct net \*net:
        network namespace

    :param const struct in6_addr \*remote:
        the address of the tunnel exit-point

    :param const struct in6_addr \*local:
        the address of the tunnel entry-point

.. _`vti6_tnl_lookup.return`:

Return
------

tunnel matching given end-points if found,
else fallback tunnel if its device is up,
else \ ``NULL``\ 

.. _`vti6_tnl_bucket`:

vti6_tnl_bucket
===============

.. c:function:: struct ip6_tnl __rcu **vti6_tnl_bucket(struct vti6_net *ip6n, const struct __ip6_tnl_parm *p)

    get head of list matching given tunnel parameters

    :param struct vti6_net \*ip6n:
        *undescribed*

    :param const struct __ip6_tnl_parm \*p:
        parameters containing tunnel end-points

.. _`vti6_tnl_bucket.description`:

Description
-----------

\ :c:func:`vti6_tnl_bucket`\  returns the head of the list matching the
\ :c:type:`struct in6_addr <in6_addr>`\  entries laddr and raddr in \ ``p``\ .

.. _`vti6_tnl_bucket.return`:

Return
------

head of IPv6 tunnel list

.. _`vti6_locate`:

vti6_locate
===========

.. c:function:: struct ip6_tnl *vti6_locate(struct net *net, struct __ip6_tnl_parm *p, int create)

    find or create tunnel matching given parameters

    :param struct net \*net:
        network namespace

    :param struct __ip6_tnl_parm \*p:
        tunnel parameters

    :param int create:
        != 0 if allowed to create new tunnel if no match found

.. _`vti6_locate.description`:

Description
-----------

\ :c:func:`vti6_locate`\  first tries to locate an existing tunnel
based on \ ``parms``\ . If this is unsuccessful, but \ ``create``\  is set a new
tunnel device is created and registered for use.

.. _`vti6_locate.return`:

Return
------

matching tunnel or NULL

.. _`vti6_dev_uninit`:

vti6_dev_uninit
===============

.. c:function:: void vti6_dev_uninit(struct net_device *dev)

    tunnel device uninitializer

    :param struct net_device \*dev:
        the device to be destroyed

.. _`vti6_dev_uninit.description`:

Description
-----------

\ :c:func:`vti6_dev_uninit`\  removes tunnel from its list

.. _`vti6_addr_conflict`:

vti6_addr_conflict
==================

.. c:function:: bool vti6_addr_conflict(const struct ip6_tnl *t, const struct ipv6hdr *hdr)

    compare packet addresses to tunnel's own

    :param const struct ip6_tnl \*t:
        the outgoing tunnel device

    :param const struct ipv6hdr \*hdr:
        IPv6 header from the incoming packet

.. _`vti6_addr_conflict.description`:

Description
-----------

Avoid trivial tunneling loop by checking that tunnel exit-point
doesn't match source of incoming packet.

.. _`vti6_addr_conflict.return`:

Return
------

1 if conflict,
0 else

.. _`vti6_xmit`:

vti6_xmit
=========

.. c:function:: int vti6_xmit(struct sk_buff *skb, struct net_device *dev, struct flowi *fl)

    send a packet

    :param struct sk_buff \*skb:
        the outgoing socket buffer

    :param struct net_device \*dev:
        the outgoing tunnel device

    :param struct flowi \*fl:
        the flow informations for the xfrm_lookup

.. _`vti6_tnl_change`:

vti6_tnl_change
===============

.. c:function:: int vti6_tnl_change(struct ip6_tnl *t, const struct __ip6_tnl_parm *p)

    update the tunnel parameters

    :param struct ip6_tnl \*t:
        tunnel to be changed

    :param const struct __ip6_tnl_parm \*p:
        tunnel configuration parameters

.. _`vti6_tnl_change.description`:

Description
-----------

\ :c:func:`vti6_tnl_change`\  updates the tunnel parameters

.. _`vti6_ioctl`:

vti6_ioctl
==========

.. c:function:: int vti6_ioctl(struct net_device *dev, struct ifreq *ifr, int cmd)

    configure vti6 tunnels from userspace

    :param struct net_device \*dev:
        virtual device associated with tunnel

    :param struct ifreq \*ifr:
        parameters passed from userspace

    :param int cmd:
        command to be performed

.. _`vti6_ioctl.description`:

Description
-----------

\ :c:func:`vti6_ioctl`\  is used for managing vti6 tunnels
from userspace.

.. _`vti6_ioctl.the-possible-commands-are-the-following`:

The possible commands are the following
---------------------------------------

\ ``SIOCGETTUNNEL``\ : get tunnel parameters for device
\ ``SIOCADDTUNNEL``\ : add tunnel matching given tunnel parameters
\ ``SIOCCHGTUNNEL``\ : change tunnel parameters to those given
\ ``SIOCDELTUNNEL``\ : delete tunnel

The fallback device "ip6_vti0", created during module
initialization, can be used for creating other tunnel devices.

.. _`vti6_ioctl.return`:

Return
------

0 on success,
\ ``-EFAULT``\  if unable to copy data to or from userspace,
\ ``-EPERM``\  if current process hasn't \ ``CAP_NET_ADMIN``\  set
\ ``-EINVAL``\  if passed tunnel parameters are invalid,
\ ``-EEXIST``\  if changing a tunnel's parameters would cause a conflict
\ ``-ENODEV``\  if attempting to change or delete a nonexisting device

.. _`vti6_dev_setup`:

vti6_dev_setup
==============

.. c:function:: void vti6_dev_setup(struct net_device *dev)

    setup virtual tunnel device

    :param struct net_device \*dev:
        virtual device associated with tunnel

.. _`vti6_dev_setup.description`:

Description
-----------

Initialize function pointers and device parameters

.. _`vti6_dev_init_gen`:

vti6_dev_init_gen
=================

.. c:function:: int vti6_dev_init_gen(struct net_device *dev)

    general initializer for all tunnel devices

    :param struct net_device \*dev:
        virtual device associated with tunnel

.. _`vti6_dev_init`:

vti6_dev_init
=============

.. c:function:: int vti6_dev_init(struct net_device *dev)

    initializer for all non fallback tunnel devices

    :param struct net_device \*dev:
        virtual device associated with tunnel

.. _`vti6_fb_tnl_dev_init`:

vti6_fb_tnl_dev_init
====================

.. c:function:: int __net_init vti6_fb_tnl_dev_init(struct net_device *dev)

    initializer for fallback tunnel device

    :param struct net_device \*dev:
        fallback device

.. _`vti6_fb_tnl_dev_init.return`:

Return
------

0

.. _`vti6_tunnel_init`:

vti6_tunnel_init
================

.. c:function:: int vti6_tunnel_init( void)

    register protocol and reserve needed resources

    :param  void:
        no arguments

.. _`vti6_tunnel_init.return`:

Return
------

0 on success

.. _`vti6_tunnel_cleanup`:

vti6_tunnel_cleanup
===================

.. c:function:: void __exit vti6_tunnel_cleanup( void)

    free resources and unregister protocol

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

