.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40evf/i40evf_virtchnl.c

.. _`i40evf_send_pf_msg`:

i40evf_send_pf_msg
==================

.. c:function:: int i40evf_send_pf_msg(struct i40evf_adapter *adapter, enum virtchnl_ops op, u8 *msg, u16 len)

    :param struct i40evf_adapter \*adapter:
        adapter structure

    :param enum virtchnl_ops op:
        virtual channel opcode

    :param u8 \*msg:
        pointer to message buffer

    :param u16 len:
        message length

.. _`i40evf_send_pf_msg.description`:

Description
-----------

Send message to PF and print status if failure.

.. _`i40evf_send_api_ver`:

i40evf_send_api_ver
===================

.. c:function:: int i40evf_send_api_ver(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_send_api_ver.description`:

Description
-----------

Send API version admin queue message to the PF. The reply is not checked
in this function. Returns 0 if the message was successfully
sent, or one of the I40E_ADMIN_QUEUE_ERROR\_ statuses if not.

.. _`i40evf_verify_api_ver`:

i40evf_verify_api_ver
=====================

.. c:function:: int i40evf_verify_api_ver(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_verify_api_ver.description`:

Description
-----------

Compare API versions with the PF. Must be called after admin queue is
initialized. Returns 0 if API versions match, -EIO if they do not,
I40E_ERR_ADMIN_QUEUE_NO_WORK if the admin queue is empty, and any errors
from the firmware are propagated.

.. _`i40evf_send_vf_config_msg`:

i40evf_send_vf_config_msg
=========================

.. c:function:: int i40evf_send_vf_config_msg(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_send_vf_config_msg.description`:

Description
-----------

Send VF configuration request admin queue message to the PF. The reply
is not checked in this function. Returns 0 if the message was
successfully sent, or one of the I40E_ADMIN_QUEUE_ERROR\_ statuses if not.

.. _`i40evf_get_vf_config`:

i40evf_get_vf_config
====================

.. c:function:: int i40evf_get_vf_config(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        *undescribed*

.. _`i40evf_get_vf_config.description`:

Description
-----------

Get VF configuration from PF and populate hw structure. Must be called after
admin queue is initialized. Busy waits until response is received from PF,
with maximum timeout. Response from PF is returned in the buffer for further
processing by the caller.

.. _`i40evf_configure_queues`:

i40evf_configure_queues
=======================

.. c:function:: void i40evf_configure_queues(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_configure_queues.description`:

Description
-----------

Request that the PF set up our (previously allocated) queues.

.. _`i40evf_enable_queues`:

i40evf_enable_queues
====================

.. c:function:: void i40evf_enable_queues(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_enable_queues.description`:

Description
-----------

Request that the PF enable all of our queues.

.. _`i40evf_disable_queues`:

i40evf_disable_queues
=====================

.. c:function:: void i40evf_disable_queues(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_disable_queues.description`:

Description
-----------

Request that the PF disable all of our queues.

.. _`i40evf_map_queues`:

i40evf_map_queues
=================

.. c:function:: void i40evf_map_queues(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_map_queues.description`:

Description
-----------

Request that the PF map queues to interrupt vectors. Misc causes, including
admin queue, are always mapped to vector 0.

.. _`i40evf_add_ether_addrs`:

i40evf_add_ether_addrs
======================

.. c:function:: void i40evf_add_ether_addrs(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_add_ether_addrs.description`:

Description
-----------

Request that the PF add one or more addresses to our filters.

.. _`i40evf_del_ether_addrs`:

i40evf_del_ether_addrs
======================

.. c:function:: void i40evf_del_ether_addrs(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_del_ether_addrs.description`:

Description
-----------

Request that the PF remove one or more addresses from our filters.

.. _`i40evf_add_vlans`:

i40evf_add_vlans
================

.. c:function:: void i40evf_add_vlans(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_add_vlans.description`:

Description
-----------

Request that the PF add one or more VLAN filters to our VSI.

.. _`i40evf_del_vlans`:

i40evf_del_vlans
================

.. c:function:: void i40evf_del_vlans(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_del_vlans.description`:

Description
-----------

Request that the PF remove one or more VLAN filters from our VSI.

.. _`i40evf_set_promiscuous`:

i40evf_set_promiscuous
======================

.. c:function:: void i40evf_set_promiscuous(struct i40evf_adapter *adapter, int flags)

    :param struct i40evf_adapter \*adapter:
        adapter structure

    :param int flags:
        bitmask to control unicast/multicast promiscuous.

.. _`i40evf_set_promiscuous.description`:

Description
-----------

Request that the PF enable promiscuous mode for our VSI.

.. _`i40evf_request_stats`:

i40evf_request_stats
====================

.. c:function:: void i40evf_request_stats(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_request_stats.description`:

Description
-----------

Request VSI statistics from PF.

.. _`i40evf_get_hena`:

i40evf_get_hena
===============

.. c:function:: void i40evf_get_hena(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_get_hena.description`:

Description
-----------

Request hash enable capabilities from PF

.. _`i40evf_set_hena`:

i40evf_set_hena
===============

.. c:function:: void i40evf_set_hena(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_set_hena.description`:

Description
-----------

Request the PF to set our RSS hash capabilities

.. _`i40evf_set_rss_key`:

i40evf_set_rss_key
==================

.. c:function:: void i40evf_set_rss_key(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_set_rss_key.description`:

Description
-----------

Request the PF to set our RSS hash key

.. _`i40evf_set_rss_lut`:

i40evf_set_rss_lut
==================

.. c:function:: void i40evf_set_rss_lut(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_set_rss_lut.description`:

Description
-----------

Request the PF to set our RSS lookup table

.. _`i40evf_enable_vlan_stripping`:

i40evf_enable_vlan_stripping
============================

.. c:function:: void i40evf_enable_vlan_stripping(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_enable_vlan_stripping.description`:

Description
-----------

Request VLAN header stripping to be enabled

.. _`i40evf_disable_vlan_stripping`:

i40evf_disable_vlan_stripping
=============================

.. c:function:: void i40evf_disable_vlan_stripping(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_disable_vlan_stripping.description`:

Description
-----------

Request VLAN header stripping to be disabled

.. _`i40evf_print_link_message`:

i40evf_print_link_message
=========================

.. c:function:: void i40evf_print_link_message(struct i40evf_adapter *adapter)

    print link up or down

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_print_link_message.description`:

Description
-----------

Log a message telling the world of our wonderous link status

.. _`i40evf_request_reset`:

i40evf_request_reset
====================

.. c:function:: void i40evf_request_reset(struct i40evf_adapter *adapter)

    :param struct i40evf_adapter \*adapter:
        adapter structure

.. _`i40evf_request_reset.description`:

Description
-----------

Request that the PF reset this VF. No response is expected.

.. _`i40evf_virtchnl_completion`:

i40evf_virtchnl_completion
==========================

.. c:function:: void i40evf_virtchnl_completion(struct i40evf_adapter *adapter, enum virtchnl_ops v_opcode, i40e_status v_retval, u8 *msg, u16 msglen)

    :param struct i40evf_adapter \*adapter:
        adapter structure

    :param enum virtchnl_ops v_opcode:
        opcode sent by PF

    :param i40e_status v_retval:
        retval sent by PF

    :param u8 \*msg:
        message sent by PF

    :param u16 msglen:
        message length

.. _`i40evf_virtchnl_completion.description`:

Description
-----------

Asynchronous completion function for admin queue messages. Rather than busy
wait, we fire off our requests and assume that no errors will be returned.
This function handles the reply messages.

.. This file was automatic generated / don't edit.

