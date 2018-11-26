.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/net/lcs.c

.. _`lcs_tasklet`:

lcs_tasklet
===========

.. c:function:: void lcs_tasklet(unsigned long)

    :param long:
        *undescribed*
    :type long: unsigned

.. _`lcs_unregister_debug_facility`:

lcs_unregister_debug_facility
=============================

.. c:function:: void lcs_unregister_debug_facility( void)

    :param void:
        no arguments
    :type void: 

.. _`lcs_alloc_channel`:

lcs_alloc_channel
=================

.. c:function:: int lcs_alloc_channel(struct lcs_channel *channel)

    :param channel:
        *undescribed*
    :type channel: struct lcs_channel \*

.. _`lcs_free_channel`:

lcs_free_channel
================

.. c:function:: void lcs_free_channel(struct lcs_channel *channel)

    :param channel:
        *undescribed*
    :type channel: struct lcs_channel \*

.. _`lcs_free_card`:

lcs_free_card
=============

.. c:function:: void lcs_free_card(struct lcs_card *card)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

.. _`lcs_alloc_card`:

lcs_alloc_card
==============

.. c:function:: struct lcs_card *lcs_alloc_card( void)

    :param void:
        no arguments
    :type void: 

.. _`lcs_setup_card`:

lcs_setup_card
==============

.. c:function:: void lcs_setup_card(struct lcs_card *card)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

.. _`lcs_cleanup_card`:

lcs_cleanup_card
================

.. c:function:: void lcs_cleanup_card(struct lcs_card *card)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

.. _`lcs_start_channel`:

lcs_start_channel
=================

.. c:function:: int lcs_start_channel(struct lcs_channel *channel)

    :param channel:
        *undescribed*
    :type channel: struct lcs_channel \*

.. _`lcs_stop_channel`:

lcs_stop_channel
================

.. c:function:: int lcs_stop_channel(struct lcs_channel *channel)

    :param channel:
        *undescribed*
    :type channel: struct lcs_channel \*

.. _`lcs_start_channels`:

lcs_start_channels
==================

.. c:function:: int lcs_start_channels(struct lcs_card *card)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

.. _`lcs_stop_channels`:

lcs_stop_channels
=================

.. c:function:: int lcs_stop_channels(struct lcs_card *card)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

.. _`__lcs_get_buffer`:

\__lcs_get_buffer
=================

.. c:function:: struct lcs_buffer *__lcs_get_buffer(struct lcs_channel *channel)

    :param channel:
        *undescribed*
    :type channel: struct lcs_channel \*

.. _`__lcs_resume_channel`:

\__lcs_resume_channel
=====================

.. c:function:: int __lcs_resume_channel(struct lcs_channel *channel)

    :param channel:
        *undescribed*
    :type channel: struct lcs_channel \*

.. _`__lcs_ready_buffer_bits`:

\__lcs_ready_buffer_bits
========================

.. c:function:: void __lcs_ready_buffer_bits(struct lcs_channel *channel, int index)

    :param channel:
        *undescribed*
    :type channel: struct lcs_channel \*

    :param index:
        *undescribed*
    :type index: int

.. _`__lcs_processed_buffer`:

\__lcs_processed_buffer
=======================

.. c:function:: int __lcs_processed_buffer(struct lcs_channel *channel, struct lcs_buffer *buffer)

    of the previous buffer. This function is called from interrupt context, so the lock must not be taken.

    :param channel:
        *undescribed*
    :type channel: struct lcs_channel \*

    :param buffer:
        *undescribed*
    :type buffer: struct lcs_buffer \*

.. _`lcs_release_buffer`:

lcs_release_buffer
==================

.. c:function:: void lcs_release_buffer(struct lcs_channel *channel, struct lcs_buffer *buffer)

    :param channel:
        *undescribed*
    :type channel: struct lcs_channel \*

    :param buffer:
        *undescribed*
    :type buffer: struct lcs_buffer \*

.. _`lcs_get_lancmd`:

lcs_get_lancmd
==============

.. c:function:: struct lcs_buffer *lcs_get_lancmd(struct lcs_card *card, int count)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

    :param count:
        *undescribed*
    :type count: int

.. _`lcs_notify_lancmd_waiters`:

lcs_notify_lancmd_waiters
=========================

.. c:function:: void lcs_notify_lancmd_waiters(struct lcs_card *card, struct lcs_cmd *cmd)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

    :param cmd:
        *undescribed*
    :type cmd: struct lcs_cmd \*

.. _`lcs_lancmd_timeout`:

lcs_lancmd_timeout
==================

.. c:function:: void lcs_lancmd_timeout(struct timer_list *t)

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`lcs_send_startup`:

lcs_send_startup
================

.. c:function:: int lcs_send_startup(struct lcs_card *card, __u8 initiator)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

    :param initiator:
        *undescribed*
    :type initiator: __u8

.. _`lcs_send_shutdown`:

lcs_send_shutdown
=================

.. c:function:: int lcs_send_shutdown(struct lcs_card *card)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

.. _`__lcs_lanstat_cb`:

\__lcs_lanstat_cb
=================

.. c:function:: void __lcs_lanstat_cb(struct lcs_card *card, struct lcs_cmd *cmd)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

    :param cmd:
        *undescribed*
    :type cmd: struct lcs_cmd \*

.. _`lcs_send_stoplan`:

lcs_send_stoplan
================

.. c:function:: int lcs_send_stoplan(struct lcs_card *card, __u8 initiator)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

    :param initiator:
        *undescribed*
    :type initiator: __u8

.. _`__lcs_send_startlan_cb`:

\__lcs_send_startlan_cb
=======================

.. c:function:: void __lcs_send_startlan_cb(struct lcs_card *card, struct lcs_cmd *cmd)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

    :param cmd:
        *undescribed*
    :type cmd: struct lcs_cmd \*

.. _`lcs_send_setipm`:

lcs_send_setipm
===============

.. c:function:: int lcs_send_setipm(struct lcs_card *card, struct lcs_ipm_list *ipm_list)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

    :param ipm_list:
        *undescribed*
    :type ipm_list: struct lcs_ipm_list \*

.. _`lcs_send_delipm`:

lcs_send_delipm
===============

.. c:function:: int lcs_send_delipm(struct lcs_card *card, struct lcs_ipm_list *ipm_list)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

    :param ipm_list:
        *undescribed*
    :type ipm_list: struct lcs_ipm_list \*

.. _`__lcs_check_multicast_cb`:

\__lcs_check_multicast_cb
=========================

.. c:function:: void __lcs_check_multicast_cb(struct lcs_card *card, struct lcs_cmd *cmd)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

    :param cmd:
        *undescribed*
    :type cmd: struct lcs_cmd \*

.. _`lcs_fix_multicast_list`:

lcs_fix_multicast_list
======================

.. c:function:: void lcs_fix_multicast_list(struct lcs_card *card)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

.. _`lcs_get_mac_for_ipm`:

lcs_get_mac_for_ipm
===================

.. c:function:: void lcs_get_mac_for_ipm(__be32 ipm, char *mac, struct net_device *dev)

    :param ipm:
        *undescribed*
    :type ipm: __be32

    :param mac:
        *undescribed*
    :type mac: char \*

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`lcs_remove_mc_addresses`:

lcs_remove_mc_addresses
=======================

.. c:function:: void lcs_remove_mc_addresses(struct lcs_card *card, struct in_device *in4_dev)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

    :param in4_dev:
        *undescribed*
    :type in4_dev: struct in_device \*

.. _`lcs_set_multicast_list`:

lcs_set_multicast_list
======================

.. c:function:: void lcs_set_multicast_list(struct net_device *dev)

    handle multicast address relevant things

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`lcs_irq`:

lcs_irq
=======

.. c:function:: void lcs_irq(struct ccw_device *cdev, unsigned long intparm, struct irb *irb)

    :param cdev:
        *undescribed*
    :type cdev: struct ccw_device \*

    :param intparm:
        *undescribed*
    :type intparm: unsigned long

    :param irb:
        *undescribed*
    :type irb: struct irb \*

.. _`lcs_tasklet`:

lcs_tasklet
===========

.. c:function:: void lcs_tasklet(unsigned long data)

    :param data:
        *undescribed*
    :type data: unsigned long

.. _`__lcs_emit_txbuffer`:

\__lcs_emit_txbuffer
====================

.. c:function:: void __lcs_emit_txbuffer(struct lcs_card *card)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

.. _`lcs_txbuffer_cb`:

lcs_txbuffer_cb
===============

.. c:function:: void lcs_txbuffer_cb(struct lcs_channel *channel, struct lcs_buffer *buffer)

    :param channel:
        *undescribed*
    :type channel: struct lcs_channel \*

    :param buffer:
        *undescribed*
    :type buffer: struct lcs_buffer \*

.. _`__lcs_start_xmit`:

\__lcs_start_xmit
=================

.. c:function:: int __lcs_start_xmit(struct lcs_card *card, struct sk_buff *skb, struct net_device *dev)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`lcs_startlan_auto`:

lcs_startlan_auto
=================

.. c:function:: int lcs_startlan_auto(struct lcs_card *card)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

.. _`lcs_detect`:

lcs_detect
==========

.. c:function:: int lcs_detect(struct lcs_card *card)

    setup channels and make them I/O ready

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

.. _`lcs_stopcard`:

lcs_stopcard
============

.. c:function:: int lcs_stopcard(struct lcs_card *card)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

.. _`lcs_start_kernel_thread`:

lcs_start_kernel_thread
=======================

.. c:function:: void lcs_start_kernel_thread(struct work_struct *work)

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`lcs_get_control`:

lcs_get_control
===============

.. c:function:: void lcs_get_control(struct lcs_card *card, struct lcs_cmd *cmd)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

    :param cmd:
        *undescribed*
    :type cmd: struct lcs_cmd \*

.. _`lcs_get_skb`:

lcs_get_skb
===========

.. c:function:: void lcs_get_skb(struct lcs_card *card, char *skb_data, unsigned int skb_len)

    :param card:
        *undescribed*
    :type card: struct lcs_card \*

    :param skb_data:
        *undescribed*
    :type skb_data: char \*

    :param skb_len:
        *undescribed*
    :type skb_len: unsigned int

.. _`lcs_get_frames_cb`:

lcs_get_frames_cb
=================

.. c:function:: void lcs_get_frames_cb(struct lcs_channel *channel, struct lcs_buffer *buffer)

    :param channel:
        *undescribed*
    :type channel: struct lcs_channel \*

    :param buffer:
        *undescribed*
    :type buffer: struct lcs_buffer \*

.. _`lcs_getstats`:

lcs_getstats
============

.. c:function:: struct net_device_stats *lcs_getstats(struct net_device *dev)

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`lcs_stop_device`:

lcs_stop_device
===============

.. c:function:: int lcs_stop_device(struct net_device *dev)

    This function will be called by user doing ifconfig xxx down

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`lcs_open_device`:

lcs_open_device
===============

.. c:function:: int lcs_open_device(struct net_device *dev)

    This function will be called by user doing ifconfig xxx up

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`lcs_portno_show`:

lcs_portno_show
===============

.. c:function:: ssize_t lcs_portno_show(struct device *dev, struct device_attribute *attr, char *buf)

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`lcs_portno_store`:

lcs_portno_store
================

.. c:function:: ssize_t lcs_portno_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        *undescribed*
    :type buf: const char \*

    :param count:
        *undescribed*
    :type count: size_t

.. _`lcs_probe_device`:

lcs_probe_device
================

.. c:function:: int lcs_probe_device(struct ccwgroup_device *ccwgdev)

    :param ccwgdev:
        *undescribed*
    :type ccwgdev: struct ccwgroup_device \*

.. _`__lcs_shutdown_device`:

\__lcs_shutdown_device
======================

.. c:function:: int __lcs_shutdown_device(struct ccwgroup_device *ccwgdev, int recovery_mode)

    :param ccwgdev:
        *undescribed*
    :type ccwgdev: struct ccwgroup_device \*

    :param recovery_mode:
        *undescribed*
    :type recovery_mode: int

.. _`lcs_recovery`:

lcs_recovery
============

.. c:function:: int lcs_recovery(void *ptr)

    :param ptr:
        *undescribed*
    :type ptr: void \*

.. _`lcs_remove_device`:

lcs_remove_device
=================

.. c:function:: void lcs_remove_device(struct ccwgroup_device *ccwgdev)

    :param ccwgdev:
        *undescribed*
    :type ccwgdev: struct ccwgroup_device \*

.. _`lcs_init_module`:

lcs_init_module
===============

.. c:function:: int lcs_init_module( void)

    :param void:
        no arguments
    :type void: 

.. _`lcs_cleanup_module`:

lcs_cleanup_module
==================

.. c:function:: void __exit lcs_cleanup_module( void)

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

