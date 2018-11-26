.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8188eu/os_dep/mon.c

.. _`unprotect_frame`:

unprotect_frame
===============

.. c:function:: void unprotect_frame(struct sk_buff *skb, int iv_len, int icv_len)

    unset Protected flag and strip off IV and ICV/MIC

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param iv_len:
        *undescribed*
    :type iv_len: int

    :param icv_len:
        *undescribed*
    :type icv_len: int

.. _`rtl88eu_mon_recv_hook`:

rtl88eu_mon_recv_hook
=====================

.. c:function:: void rtl88eu_mon_recv_hook(struct net_device *dev, struct recv_frame *frame)

    forward received frame to the monitor interface

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param frame:
        *undescribed*
    :type frame: struct recv_frame \*

.. _`rtl88eu_mon_recv_hook.description`:

Description
-----------

Assumes that the frame contains an IV and an ICV/MIC, and that
encrypt field in frame->attrib have been set accordingly.

.. _`rtl88eu_mon_xmit_hook`:

rtl88eu_mon_xmit_hook
=====================

.. c:function:: void rtl88eu_mon_xmit_hook(struct net_device *dev, struct xmit_frame *frame, uint frag_len)

    forward trasmitted frame to the monitor interface

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param frame:
        *undescribed*
    :type frame: struct xmit_frame \*

    :param frag_len:
        *undescribed*
    :type frag_len: uint

.. _`rtl88eu_mon_xmit_hook.assumes-that`:

Assumes that
------------

- frame header contains an IV and frame->attrib.iv_len is set accordingly,
- data is not encrypted and ICV/MIC has not been appended yet.

.. This file was automatic generated / don't edit.

