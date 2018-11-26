.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/host1x/hw/syncpt_hw.c

.. _`syncpt_assign_to_channel`:

syncpt_assign_to_channel
========================

.. c:function:: void syncpt_assign_to_channel(struct host1x_syncpt *sp, struct host1x_channel *ch)

    Assign syncpoint to channel

    :param sp:
        syncpoint
    :type sp: struct host1x_syncpt \*

    :param ch:
        channel
    :type ch: struct host1x_channel \*

.. _`syncpt_assign_to_channel.description`:

Description
-----------

On chips with the syncpoint protection feature (Tegra186+), assign \ ``sp``\  to
\ ``ch``\ , preventing other channels from incrementing the syncpoints. If \ ``ch``\  is
NULL, unassigns the syncpoint.

On older chips, do nothing.

.. _`syncpt_enable_protection`:

syncpt_enable_protection
========================

.. c:function:: void syncpt_enable_protection(struct host1x *host)

    Enable syncpoint protection

    :param host:
        host1x instance
    :type host: struct host1x \*

.. _`syncpt_enable_protection.description`:

Description
-----------

On chips with the syncpoint protection feature (Tegra186+), enable this
feature. On older chips, do nothing.

.. This file was automatic generated / don't edit.

