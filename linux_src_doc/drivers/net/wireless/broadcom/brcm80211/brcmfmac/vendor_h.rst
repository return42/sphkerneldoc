.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/vendor.h

.. _`brcmf_nlattrs`:

enum brcmf_nlattrs
==================

.. c:type:: enum brcmf_nlattrs

    nl80211 message attributes

.. _`brcmf_nlattrs.definition`:

Definition
----------

.. code-block:: c

    enum brcmf_nlattrs {
        BRCMF_NLATTR_UNSPEC,
        BRCMF_NLATTR_LEN,
        BRCMF_NLATTR_DATA,
        __BRCMF_NLATTR_AFTER_LAST,
        BRCMF_NLATTR_MAX
    };

.. _`brcmf_nlattrs.constants`:

Constants
---------

BRCMF_NLATTR_UNSPEC
    *undescribed*

BRCMF_NLATTR_LEN
    message body length

BRCMF_NLATTR_DATA
    message body

\__BRCMF_NLATTR_AFTER_LAST
    *undescribed*

BRCMF_NLATTR_MAX
    *undescribed*

.. _`brcmf_vndr_dcmd_hdr`:

struct brcmf_vndr_dcmd_hdr
==========================

.. c:type:: struct brcmf_vndr_dcmd_hdr

    message header for cfg80211 vendor command dcmd support

.. _`brcmf_vndr_dcmd_hdr.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_vndr_dcmd_hdr {
        uint cmd;
        int len;
        uint offset;
        uint set;
        uint magic;
    }

.. _`brcmf_vndr_dcmd_hdr.members`:

Members
-------

cmd
    common dongle cmd definition

len
    length of expecting return buffer

offset
    offset of data buffer

set
    get or set request(optional)

magic
    magic number for verification

.. This file was automatic generated / don't edit.

