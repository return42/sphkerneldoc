.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv6/ip6_tunnel.c

.. _`for_each_ip6_tunnel_rcu`:

for_each_ip6_tunnel_rcu
=======================

.. c:function::  for_each_ip6_tunnel_rcu( start)

    fetch tunnel matching the end-point addresses

    :param  start:
        *undescribed*

.. _`for_each_ip6_tunnel_rcu.return`:

Return
------

tunnel matching given end-points if found,
else fallback tunnel if its device is up,
else \ ``NULL``\ 

.. _`ip6_tnl_bucket`:

ip6_tnl_bucket
==============

.. c:function:: struct ip6_tnl __rcu **ip6_tnl_bucket(struct ip6_tnl_net *ip6n, const struct __ip6_tnl_parm *p)

    get head of list matching given tunnel parameters

    :param struct ip6_tnl_net \*ip6n:
        *undescribed*

    :param const struct __ip6_tnl_parm \*p:
        parameters containing tunnel end-points

.. _`ip6_tnl_bucket.description`:

Description
-----------

ip6_tnl_bucket() returns the head of the list matching the
\ :c:type:`struct in6_addr <in6_addr>`\  entries laddr and raddr in \ ``p``\ .

.. _`ip6_tnl_bucket.return`:

Return
------

head of IPv6 tunnel list

.. _`ip6_tnl_link`:

ip6_tnl_link
============

.. c:function:: void ip6_tnl_link(struct ip6_tnl_net *ip6n, struct ip6_tnl *t)

    add tunnel to hash table

    :param struct ip6_tnl_net \*ip6n:
        *undescribed*

    :param struct ip6_tnl \*t:
        tunnel to be added

.. _`ip6_tnl_unlink`:

ip6_tnl_unlink
==============

.. c:function:: void ip6_tnl_unlink(struct ip6_tnl_net *ip6n, struct ip6_tnl *t)

    remove tunnel from hash table

    :param struct ip6_tnl_net \*ip6n:
        *undescribed*

    :param struct ip6_tnl \*t:
        tunnel to be removed

.. _`ip6_tnl_create`:

ip6_tnl_create
==============

.. c:function:: struct ip6_tnl *ip6_tnl_create(struct net *net, struct __ip6_tnl_parm *p)

    create a new tunnel

    :param struct net \*net:
        *undescribed*

    :param struct __ip6_tnl_parm \*p:
        tunnel parameters

.. _`ip6_tnl_create.description`:

Description
-----------

Create tunnel matching given parameters.

.. _`ip6_tnl_create.return`:

Return
------

created tunnel or error pointer

.. _`ip6_tnl_locate`:

ip6_tnl_locate
==============

.. c:function:: struct ip6_tnl *ip6_tnl_locate(struct net *net, struct __ip6_tnl_parm *p, int create)

    find or create tunnel matching given parameters

    :param struct net \*net:
        *undescribed*

    :param struct __ip6_tnl_parm \*p:
        tunnel parameters

    :param int create:
        != 0 if allowed to create new tunnel if no match found

.. _`ip6_tnl_locate.description`:

Description
-----------

ip6_tnl_locate() first tries to locate an existing tunnel
based on \ ``parms``\ . If this is unsuccessful, but \ ``create``\  is set a new
tunnel device is created and registered for use.

.. _`ip6_tnl_locate.return`:

Return
------

matching tunnel or error pointer

.. _`ip6_tnl_dev_uninit`:

ip6_tnl_dev_uninit
==================

.. c:function:: void ip6_tnl_dev_uninit(struct net_device *dev)

    tunnel device uninitializer

    :param struct net_device \*dev:
        the device to be destroyed

.. _`ip6_tnl_dev_uninit.description`:

Description
-----------

ip6_tnl_dev_uninit() removes tunnel from its list

.. _`ip6_tnl_parse_tlv_enc_lim`:

ip6_tnl_parse_tlv_enc_lim
=========================

.. c:function:: __u16 ip6_tnl_parse_tlv_enc_lim(struct sk_buff *skb, __u8 *raw)

    handle encapsulation limit option

    :param struct sk_buff \*skb:
        received socket buffer

    :param __u8 \*raw:
        *undescribed*

.. _`ip6_tnl_parse_tlv_enc_lim.return`:

Return
------

0 if none was found,
else index to encapsulation limit

.. _`ip6_tnl_err`:

ip6_tnl_err
===========

.. c:function:: int ip6_tnl_err(struct sk_buff *skb, __u8 ipproto, struct inet6_skb_parm *opt, u8 *type, u8 *code, int *msg, __u32 *info, int offset)

    tunnel error handler

    :param struct sk_buff \*skb:
        *undescribed*

    :param __u8 ipproto:
        *undescribed*

    :param struct inet6_skb_parm \*opt:
        *undescribed*

    :param u8 \*type:
        *undescribed*

    :param u8 \*code:
        *undescribed*

    :param int \*msg:
        *undescribed*

    :param __u32 \*info:
        *undescribed*

    :param int offset:
        *undescribed*

.. _`ip6_tnl_err.description`:

Description
-----------

ip6_tnl_err() should handle errors in the tunnel according
to the specifications in RFC 2473.

.. _`ip6_tnl_addr_conflict`:

ip6_tnl_addr_conflict
=====================

.. c:function:: bool ip6_tnl_addr_conflict(const struct ip6_tnl *t, const struct ipv6hdr *hdr)

    compare packet addresses to tunnel's own

    :param const struct ip6_tnl \*t:
        the outgoing tunnel device

    :param const struct ipv6hdr \*hdr:
        IPv6 header from the incoming packet

.. _`ip6_tnl_addr_conflict.description`:

Description
-----------

Avoid trivial tunneling loop by checking that tunnel exit-point
doesn't match source of incoming packet.

.. _`ip6_tnl_addr_conflict.return`:

Return
------

1 if conflict,
0 else

.. _`ip6_tnl_xmit`:

ip6_tnl_xmit
============

.. c:function:: int ip6_tnl_xmit(struct sk_buff *skb, struct net_device *dev, __u8 dsfield, struct flowi6 *fl6, int encap_limit, __u32 *pmtu, __u8 proto)

    encapsulate packet and send

    :param struct sk_buff \*skb:
        the outgoing socket buffer

    :param struct net_device \*dev:
        the outgoing tunnel device

    :param __u8 dsfield:
        dscp code for outer header

    :param struct flowi6 \*fl6:
        flow of tunneled packet

    :param int encap_limit:
        encapsulation limit

    :param __u32 \*pmtu:
        Path MTU is stored if packet is too big

    :param __u8 proto:
        next header value

.. _`ip6_tnl_xmit.description`:

Description
-----------

Build new header and do some sanity checks on the packet before sending
it.

.. _`ip6_tnl_xmit.return`:

Return
------

0 on success
-1 fail
\ ``-EMSGSIZE``\  message too big. return mtu in this case.

.. _`ip6_tnl_change`:

ip6_tnl_change
==============

.. c:function:: int ip6_tnl_change(struct ip6_tnl *t, const struct __ip6_tnl_parm *p)

    update the tunnel parameters

    :param struct ip6_tnl \*t:
        tunnel to be changed

    :param const struct __ip6_tnl_parm \*p:
        tunnel configuration parameters

.. _`ip6_tnl_change.description`:

Description
-----------

ip6_tnl_change() updates the tunnel parameters

.. _`ip6_tnl_ioctl`:

ip6_tnl_ioctl
=============

.. c:function:: int ip6_tnl_ioctl(struct net_device *dev, struct ifreq *ifr, int cmd)

    configure ipv6 tunnels from userspace

    :param struct net_device \*dev:
        virtual device associated with tunnel

    :param struct ifreq \*ifr:
        parameters passed from userspace

    :param int cmd:
        command to be performed

.. _`ip6_tnl_ioctl.description`:

Description
-----------

ip6_tnl_ioctl() is used for managing IPv6 tunnels
from userspace.

.. _`ip6_tnl_ioctl.the-possible-commands-are-the-following`:

The possible commands are the following
---------------------------------------

%SIOCGETTUNNEL: get tunnel parameters for device
\ ``SIOCADDTUNNEL``\ : add tunnel matching given tunnel parameters
\ ``SIOCCHGTUNNEL``\ : change tunnel parameters to those given
\ ``SIOCDELTUNNEL``\ : delete tunnel

The fallback device "ip6tnl0", created during module
initialization, can be used for creating other tunnel devices.

.. _`ip6_tnl_ioctl.return`:

Return
------

0 on success,
\ ``-EFAULT``\  if unable to copy data to or from userspace,
\ ``-EPERM``\  if current process hasn't \ ``CAP_NET_ADMIN``\  set
\ ``-EINVAL``\  if passed tunnel parameters are invalid,
\ ``-EEXIST``\  if changing a tunnel's parameters would cause a conflict
\ ``-ENODEV``\  if attempting to change or delete a nonexisting device

.. _`ip6_tnl_change_mtu`:

ip6_tnl_change_mtu
==================

.. c:function:: int ip6_tnl_change_mtu(struct net_device *dev, int new_mtu)

    change mtu manually for tunnel device

    :param struct net_device \*dev:
        virtual device associated with tunnel

    :param int new_mtu:
        the new mtu

.. _`ip6_tnl_change_mtu.return`:

Return
------

0 on success,
\ ``-EINVAL``\  if mtu too small

.. _`ip6_tnl_dev_setup`:

ip6_tnl_dev_setup
=================

.. c:function:: void ip6_tnl_dev_setup(struct net_device *dev)

    setup virtual tunnel device

    :param struct net_device \*dev:
        virtual device associated with tunnel

.. _`ip6_tnl_dev_setup.description`:

Description
-----------

Initialize function pointers and device parameters

.. _`ip6_tnl_dev_init_gen`:

ip6_tnl_dev_init_gen
====================

.. c:function:: int ip6_tnl_dev_init_gen(struct net_device *dev)

    general initializer for all tunnel devices

    :param struct net_device \*dev:
        virtual device associated with tunnel

.. _`ip6_tnl_dev_init`:

ip6_tnl_dev_init
================

.. c:function:: int ip6_tnl_dev_init(struct net_device *dev)

    initializer for all non fallback tunnel devices

    :param struct net_device \*dev:
        virtual device associated with tunnel

.. _`ip6_fb_tnl_dev_init`:

ip6_fb_tnl_dev_init
===================

.. c:function:: int __net_init ip6_fb_tnl_dev_init(struct net_device *dev)

    initializer for fallback tunnel device

    :param struct net_device \*dev:
        fallback device

.. _`ip6_fb_tnl_dev_init.return`:

Return
------

0

.. _`ip6_tunnel_init`:

ip6_tunnel_init
===============

.. c:function:: int ip6_tunnel_init( void)

    register protocol and reserve needed resources

    :param  void:
        no arguments

.. _`ip6_tunnel_init.return`:

Return
------

0 on success

.. _`ip6_tunnel_cleanup`:

ip6_tunnel_cleanup
==================

.. c:function:: void __exit ip6_tunnel_cleanup( void)

    free resources and unregister protocol

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

