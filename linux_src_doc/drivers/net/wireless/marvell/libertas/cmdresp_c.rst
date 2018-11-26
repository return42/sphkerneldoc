.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/marvell/libertas/cmdresp.c

.. _`lbs_mac_event_disconnected`:

lbs_mac_event_disconnected
==========================

.. c:function:: void lbs_mac_event_disconnected(struct lbs_private *priv, bool locally_generated)

    handles disconnect event. It reports disconnect to upper layer, clean tx/rx packets, reset link state etc.

    :param priv:
        A pointer to struct lbs_private structure
    :type priv: struct lbs_private \*

    :param locally_generated:
        indicates disconnect was requested locally
        (usually by userspace)
    :type locally_generated: bool

.. _`lbs_mac_event_disconnected.return`:

Return
------

n/a

.. This file was automatic generated / don't edit.

