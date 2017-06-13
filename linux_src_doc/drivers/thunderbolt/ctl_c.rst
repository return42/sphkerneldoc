.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/ctl.c

.. _`tb_ctl`:

struct tb_ctl
=============

.. c:type:: struct tb_ctl

    thunderbolt control channel

.. _`tb_ctl.definition`:

Definition
----------

.. code-block:: c

    struct tb_ctl {
        struct tb_nhi *nhi;
        struct tb_ring *tx;
        struct tb_ring *rx;
        struct dma_pool *frame_pool;
        struct ctl_pkg  *rx_packets;
        DECLARE_KFIFO(response_fifo# struct ctl_pkg*# 16;
        struct completion response_ready;
        hotplug_cb callback;
        void *callback_data;
    }

.. _`tb_ctl.members`:

Members
-------

nhi
    *undescribed*

tx
    *undescribed*

rx
    *undescribed*

frame_pool
    *undescribed*

rx_packets
    *undescribed*

16
    *undescribed*

response_ready
    *undescribed*

callback
    *undescribed*

callback_data
    *undescribed*

.. _`tb_ctl_tx`:

tb_ctl_tx
=========

.. c:function:: int tb_ctl_tx(struct tb_ctl *ctl, void *data, size_t len, enum tb_cfg_pkg_type type)

    transmit a packet on the control channel

    :param struct tb_ctl \*ctl:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param size_t len:
        *undescribed*

    :param enum tb_cfg_pkg_type type:
        *undescribed*

.. _`tb_ctl_tx.description`:

Description
-----------

len must be a multiple of four.

.. _`tb_ctl_tx.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_ctl_handle_plug_event`:

tb_ctl_handle_plug_event
========================

.. c:function:: void tb_ctl_handle_plug_event(struct tb_ctl *ctl, struct ctl_pkg *response)

    acknowledge a plug event, invoke ctl->callback

    :param struct tb_ctl \*ctl:
        *undescribed*

    :param struct ctl_pkg \*response:
        *undescribed*

.. _`tb_ctl_rx`:

tb_ctl_rx
=========

.. c:function:: struct tb_cfg_result tb_ctl_rx(struct tb_ctl *ctl, void *buffer, size_t length, int timeout_msec, u64 route, enum tb_cfg_pkg_type type)

    receive a packet from the control channel

    :param struct tb_ctl \*ctl:
        *undescribed*

    :param void \*buffer:
        *undescribed*

    :param size_t length:
        *undescribed*

    :param int timeout_msec:
        *undescribed*

    :param u64 route:
        *undescribed*

    :param enum tb_cfg_pkg_type type:
        *undescribed*

.. _`tb_ctl_alloc`:

tb_ctl_alloc
============

.. c:function:: struct tb_ctl *tb_ctl_alloc(struct tb_nhi *nhi, hotplug_cb cb, void *cb_data)

    allocate a control channel

    :param struct tb_nhi \*nhi:
        *undescribed*

    :param hotplug_cb cb:
        *undescribed*

    :param void \*cb_data:
        *undescribed*

.. _`tb_ctl_alloc.description`:

Description
-----------

cb will be invoked once for every hot plug event.

.. _`tb_ctl_alloc.return`:

Return
------

Returns a pointer on success or NULL on failure.

.. _`tb_ctl_free`:

tb_ctl_free
===========

.. c:function:: void tb_ctl_free(struct tb_ctl *ctl)

    free a control channel

    :param struct tb_ctl \*ctl:
        *undescribed*

.. _`tb_ctl_free.description`:

Description
-----------

Must be called after tb_ctl_stop.

Must NOT be called from ctl->callback.

.. _`tb_ctl_start`:

tb_ctl_start
============

.. c:function:: void tb_ctl_start(struct tb_ctl *ctl)

    start/resume the control channel

    :param struct tb_ctl \*ctl:
        *undescribed*

.. _`tb_ctl_stop`:

tb_ctl_stop
===========

.. c:function:: void tb_ctl_stop(struct tb_ctl *ctl)

    pause the control channel

    :param struct tb_ctl \*ctl:
        *undescribed*

.. _`tb_ctl_stop.description`:

Description
-----------

All invocations of ctl->callback will have finished after this method
returns.

Must NOT be called from ctl->callback.

.. _`tb_cfg_error`:

tb_cfg_error
============

.. c:function:: int tb_cfg_error(struct tb_ctl *ctl, u64 route, u32 port, enum tb_cfg_error error)

    send error packet

    :param struct tb_ctl \*ctl:
        *undescribed*

    :param u64 route:
        *undescribed*

    :param u32 port:
        *undescribed*

    :param enum tb_cfg_error error:
        *undescribed*

.. _`tb_cfg_error.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_cfg_reset`:

tb_cfg_reset
============

.. c:function:: struct tb_cfg_result tb_cfg_reset(struct tb_ctl *ctl, u64 route, int timeout_msec)

    send a reset packet and wait for a response

    :param struct tb_ctl \*ctl:
        *undescribed*

    :param u64 route:
        *undescribed*

    :param int timeout_msec:
        *undescribed*

.. _`tb_cfg_reset.description`:

Description
-----------

If the switch at route is incorrectly configured then we will not receive a
reply (even though the switch will reset). The caller should check for
-ETIMEDOUT and attempt to reconfigure the switch.

.. _`tb_cfg_read_raw`:

tb_cfg_read_raw
===============

.. c:function:: struct tb_cfg_result tb_cfg_read_raw(struct tb_ctl *ctl, void *buffer, u64 route, u32 port, enum tb_cfg_space space, u32 offset, u32 length, int timeout_msec)

    read from config space into buffer

    :param struct tb_ctl \*ctl:
        *undescribed*

    :param void \*buffer:
        *undescribed*

    :param u64 route:
        *undescribed*

    :param u32 port:
        *undescribed*

    :param enum tb_cfg_space space:
        *undescribed*

    :param u32 offset:
        *undescribed*

    :param u32 length:
        *undescribed*

    :param int timeout_msec:
        *undescribed*

.. _`tb_cfg_read_raw.description`:

Description
-----------

Offset and length are in dwords.

.. _`tb_cfg_write_raw`:

tb_cfg_write_raw
================

.. c:function:: struct tb_cfg_result tb_cfg_write_raw(struct tb_ctl *ctl, void *buffer, u64 route, u32 port, enum tb_cfg_space space, u32 offset, u32 length, int timeout_msec)

    write from buffer into config space

    :param struct tb_ctl \*ctl:
        *undescribed*

    :param void \*buffer:
        *undescribed*

    :param u64 route:
        *undescribed*

    :param u32 port:
        *undescribed*

    :param enum tb_cfg_space space:
        *undescribed*

    :param u32 offset:
        *undescribed*

    :param u32 length:
        *undescribed*

    :param int timeout_msec:
        *undescribed*

.. _`tb_cfg_write_raw.description`:

Description
-----------

Offset and length are in dwords.

.. _`tb_cfg_get_upstream_port`:

tb_cfg_get_upstream_port
========================

.. c:function:: int tb_cfg_get_upstream_port(struct tb_ctl *ctl, u64 route)

    get upstream port number of switch at route

    :param struct tb_ctl \*ctl:
        *undescribed*

    :param u64 route:
        *undescribed*

.. _`tb_cfg_get_upstream_port.description`:

Description
-----------

Reads the first dword from the switches TB_CFG_SWITCH config area and
returns the port number from which the reply originated.

.. _`tb_cfg_get_upstream_port.return`:

Return
------

Returns the upstream port number on success or an error code on
failure.

.. This file was automatic generated / don't edit.

