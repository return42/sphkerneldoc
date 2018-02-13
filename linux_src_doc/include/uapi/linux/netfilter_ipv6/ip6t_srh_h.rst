.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/netfilter_ipv6/ip6t_srh.h

.. _`ip6t_srh`:

struct ip6t_srh
===============

.. c:type:: struct ip6t_srh

    SRH match options @ next_hdr: Next header field of SRH @ hdr_len: Extension header length field of SRH @ segs_left: Segments left field of SRH @ last_entry: Last entry field of SRH @ tag: Tag field of SRH @ mt_flags: match options @ mt_invflags: Invert the sense of match options

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

.. This file was automatic generated / don't edit.

