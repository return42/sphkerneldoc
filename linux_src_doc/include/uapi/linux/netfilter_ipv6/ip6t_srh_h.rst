.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/netfilter_ipv6/ip6t_srh.h

.. _`ip6t_srh`:

struct ip6t_srh
===============

.. c:type:: struct ip6t_srh

    SRH match options \ ````\  next_hdr: Next header field of SRH \ ````\  hdr_len: Extension header length field of SRH \ ````\  segs_left: Segments left field of SRH \ ````\  last_entry: Last entry field of SRH \ ````\  tag: Tag field of SRH \ ````\  mt_flags: match options \ ````\  mt_invflags: Invert the sense of match options

.. _`ip6t_srh.definition`:

Definition
----------

.. code-block:: c

    struct ip6t_srh {
        __u8 next_hdr;
        __u8 hdr_len;
        __u8 segs_left;
        __u8 last_entry;
        __u16 tag;
        __u16 mt_flags;
        __u16 mt_invflags;
    }

.. _`ip6t_srh.members`:

Members
-------

next_hdr
    *undescribed*

hdr_len
    *undescribed*

segs_left
    *undescribed*

last_entry
    *undescribed*

tag
    *undescribed*

mt_flags
    *undescribed*

mt_invflags
    *undescribed*

.. _`ip6t_srh1`:

struct ip6t_srh1
================

.. c:type:: struct ip6t_srh1

    SRH match options (revision 1) \ ````\  next_hdr: Next header field of SRH \ ````\  hdr_len: Extension header length field of SRH \ ````\  segs_left: Segments left field of SRH \ ````\  last_entry: Last entry field of SRH \ ````\  tag: Tag field of SRH \ ````\  psid_addr: Address of previous SID in SRH SID list \ ````\  nsid_addr: Address of NEXT SID in SRH SID list \ ````\  lsid_addr: Address of LAST SID in SRH SID list \ ````\  psid_msk: Mask of previous SID in SRH SID list \ ````\  nsid_msk: Mask of next SID in SRH SID list \ ````\  lsid_msk: MAsk of last SID in SRH SID list \ ````\  mt_flags: match options \ ````\  mt_invflags: Invert the sense of match options

.. _`ip6t_srh1.definition`:

Definition
----------

.. code-block:: c

    struct ip6t_srh1 {
        __u8 next_hdr;
        __u8 hdr_len;
        __u8 segs_left;
        __u8 last_entry;
        __u16 tag;
        struct in6_addr psid_addr;
        struct in6_addr nsid_addr;
        struct in6_addr lsid_addr;
        struct in6_addr psid_msk;
        struct in6_addr nsid_msk;
        struct in6_addr lsid_msk;
        __u16 mt_flags;
        __u16 mt_invflags;
    }

.. _`ip6t_srh1.members`:

Members
-------

next_hdr
    *undescribed*

hdr_len
    *undescribed*

segs_left
    *undescribed*

last_entry
    *undescribed*

tag
    *undescribed*

psid_addr
    *undescribed*

nsid_addr
    *undescribed*

lsid_addr
    *undescribed*

psid_msk
    *undescribed*

nsid_msk
    *undescribed*

lsid_msk
    *undescribed*

mt_flags
    *undescribed*

mt_invflags
    *undescribed*

.. This file was automatic generated / don't edit.

