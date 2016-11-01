.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/tvlv.c

.. _`batadv_tvlv_handler_release`:

batadv_tvlv_handler_release
===========================

.. c:function:: void batadv_tvlv_handler_release(struct kref *ref)

    release tvlv handler from lists and queue for free after rcu grace period

    :param struct kref \*ref:
        kref pointer of the tvlv

.. _`batadv_tvlv_handler_put`:

batadv_tvlv_handler_put
=======================

.. c:function:: void batadv_tvlv_handler_put(struct batadv_tvlv_handler *tvlv_handler)

    decrement the tvlv container refcounter and possibly release it

    :param struct batadv_tvlv_handler \*tvlv_handler:
        the tvlv handler to free

.. _`batadv_tvlv_handler_get`:

batadv_tvlv_handler_get
=======================

.. c:function:: struct batadv_tvlv_handler *batadv_tvlv_handler_get(struct batadv_priv *bat_priv, u8 type, u8 version)

    retrieve tvlv handler from the tvlv handler list based on the provided type and version (both need to match)

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 type:
        tvlv handler type to look for

    :param u8 version:
        tvlv handler version to look for

.. _`batadv_tvlv_handler_get.return`:

Return
------

tvlv handler if found or NULL otherwise.

.. _`batadv_tvlv_container_release`:

batadv_tvlv_container_release
=============================

.. c:function:: void batadv_tvlv_container_release(struct kref *ref)

    release tvlv from lists and free

    :param struct kref \*ref:
        kref pointer of the tvlv

.. _`batadv_tvlv_container_put`:

batadv_tvlv_container_put
=========================

.. c:function:: void batadv_tvlv_container_put(struct batadv_tvlv_container *tvlv)

    decrement the tvlv container refcounter and possibly release it

    :param struct batadv_tvlv_container \*tvlv:
        the tvlv container to free

.. _`batadv_tvlv_container_get`:

batadv_tvlv_container_get
=========================

.. c:function:: struct batadv_tvlv_container *batadv_tvlv_container_get(struct batadv_priv *bat_priv, u8 type, u8 version)

    retrieve tvlv container from the tvlv container list based on the provided type and version (both need to match)

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 type:
        tvlv container type to look for

    :param u8 version:
        tvlv container version to look for

.. _`batadv_tvlv_container_get.description`:

Description
-----------

Has to be called with the appropriate locks being acquired
(tvlv.container_list_lock).

.. _`batadv_tvlv_container_get.return`:

Return
------

tvlv container if found or NULL otherwise.

.. _`batadv_tvlv_container_list_size`:

batadv_tvlv_container_list_size
===============================

.. c:function:: u16 batadv_tvlv_container_list_size(struct batadv_priv *bat_priv)

    calculate the size of the tvlv container list entries

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_tvlv_container_list_size.description`:

Description
-----------

Has to be called with the appropriate locks being acquired
(tvlv.container_list_lock).

.. _`batadv_tvlv_container_list_size.return`:

Return
------

size of all currently registered tvlv containers in bytes.

.. _`batadv_tvlv_container_remove`:

batadv_tvlv_container_remove
============================

.. c:function:: void batadv_tvlv_container_remove(struct batadv_priv *bat_priv, struct batadv_tvlv_container *tvlv)

    remove tvlv container from the tvlv container list

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_tvlv_container \*tvlv:
        the to be removed tvlv container

.. _`batadv_tvlv_container_remove.description`:

Description
-----------

Has to be called with the appropriate locks being acquired
(tvlv.container_list_lock).

.. _`batadv_tvlv_container_unregister`:

batadv_tvlv_container_unregister
================================

.. c:function:: void batadv_tvlv_container_unregister(struct batadv_priv *bat_priv, u8 type, u8 version)

    unregister tvlv container based on the provided type and version (both need to match)

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 type:
        tvlv container type to unregister

    :param u8 version:
        tvlv container type to unregister

.. _`batadv_tvlv_container_register`:

batadv_tvlv_container_register
==============================

.. c:function:: void batadv_tvlv_container_register(struct batadv_priv *bat_priv, u8 type, u8 version, void *tvlv_value, u16 tvlv_value_len)

    register tvlv type, version and content to be propagated with each (primary interface) OGM

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 type:
        tvlv container type

    :param u8 version:
        tvlv container version

    :param void \*tvlv_value:
        tvlv container content

    :param u16 tvlv_value_len:
        tvlv container content length

.. _`batadv_tvlv_container_register.description`:

Description
-----------

If a container of the same type and version was already registered the new
content is going to replace the old one.

.. _`batadv_tvlv_realloc_packet_buff`:

batadv_tvlv_realloc_packet_buff
===============================

.. c:function:: bool batadv_tvlv_realloc_packet_buff(unsigned char **packet_buff, int *packet_buff_len, int min_packet_len, int additional_packet_len)

    reallocate packet buffer to accommodate requested packet size

    :param unsigned char \*\*packet_buff:
        packet buffer

    :param int \*packet_buff_len:
        packet buffer size

    :param int min_packet_len:
        requested packet minimum size

    :param int additional_packet_len:
        requested additional packet size on top of minimum
        size

.. _`batadv_tvlv_realloc_packet_buff.return`:

Return
------

true of the packet buffer could be changed to the requested size,
false otherwise.

.. _`batadv_tvlv_container_ogm_append`:

batadv_tvlv_container_ogm_append
================================

.. c:function:: u16 batadv_tvlv_container_ogm_append(struct batadv_priv *bat_priv, unsigned char **packet_buff, int *packet_buff_len, int packet_min_len)

    append tvlv container content to given OGM packet buffer

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param unsigned char \*\*packet_buff:
        ogm packet buffer

    :param int \*packet_buff_len:
        ogm packet buffer size including ogm header and tvlv
        content

    :param int packet_min_len:
        ogm header size to be preserved for the OGM itself

.. _`batadv_tvlv_container_ogm_append.description`:

Description
-----------

The ogm packet might be enlarged or shrunk depending on the current size
and the size of the to-be-appended tvlv containers.

.. _`batadv_tvlv_container_ogm_append.return`:

Return
------

size of all appended tvlv containers in bytes.

.. _`batadv_tvlv_call_handler`:

batadv_tvlv_call_handler
========================

.. c:function:: int batadv_tvlv_call_handler(struct batadv_priv *bat_priv, struct batadv_tvlv_handler *tvlv_handler, bool ogm_source, struct batadv_orig_node *orig_node, u8 *src, u8 *dst, void *tvlv_value, u16 tvlv_value_len)

    parse the given tvlv buffer to call the appropriate handlers

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_tvlv_handler \*tvlv_handler:
        tvlv callback function handling the tvlv content

    :param bool ogm_source:
        flag indicating whether the tvlv is an ogm or a unicast packet

    :param struct batadv_orig_node \*orig_node:
        orig node emitting the ogm packet

    :param u8 \*src:
        source mac address of the unicast packet

    :param u8 \*dst:
        destination mac address of the unicast packet

    :param void \*tvlv_value:
        tvlv content

    :param u16 tvlv_value_len:
        tvlv content length

.. _`batadv_tvlv_call_handler.return`:

Return
------

success if handler was not found or the return value of the handler
callback.

.. _`batadv_tvlv_containers_process`:

batadv_tvlv_containers_process
==============================

.. c:function:: int batadv_tvlv_containers_process(struct batadv_priv *bat_priv, bool ogm_source, struct batadv_orig_node *orig_node, u8 *src, u8 *dst, void *tvlv_value, u16 tvlv_value_len)

    parse the given tvlv buffer to call the appropriate handlers

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param bool ogm_source:
        flag indicating whether the tvlv is an ogm or a unicast packet

    :param struct batadv_orig_node \*orig_node:
        orig node emitting the ogm packet

    :param u8 \*src:
        source mac address of the unicast packet

    :param u8 \*dst:
        destination mac address of the unicast packet

    :param void \*tvlv_value:
        tvlv content

    :param u16 tvlv_value_len:
        tvlv content length

.. _`batadv_tvlv_containers_process.return`:

Return
------

success when processing an OGM or the return value of all called
handler callbacks.

.. _`batadv_tvlv_ogm_receive`:

batadv_tvlv_ogm_receive
=======================

.. c:function:: void batadv_tvlv_ogm_receive(struct batadv_priv *bat_priv, struct batadv_ogm_packet *batadv_ogm_packet, struct batadv_orig_node *orig_node)

    process an incoming ogm and call the appropriate handlers

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_ogm_packet \*batadv_ogm_packet:
        ogm packet containing the tvlv containers

    :param struct batadv_orig_node \*orig_node:
        orig node emitting the ogm packet

.. _`batadv_tvlv_handler_register`:

batadv_tvlv_handler_register
============================

.. c:function:: void batadv_tvlv_handler_register(struct batadv_priv *bat_priv, void (*optr)(struct batadv_priv *bat_priv, struct batadv_orig_node *orig, u8 flags, void *tvlv_value, u16 tvlv_value_len), int (*uptr)(struct batadv_priv *bat_priv, u8 *src, u8 *dst, void *tvlv_value, u16 tvlv_value_len), u8 type, u8 version, u8 flags)

    register tvlv handler based on the provided type and version (both need to match) for ogm tvlv payload and/or unicast payload

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param void (\*optr)(struct batadv_priv \*bat_priv, struct batadv_orig_node \*orig, u8 flags, void \*tvlv_value, u16 tvlv_value_len):
        ogm tvlv handler callback function. This function receives the orig
        node, flags and the tvlv content as argument to process.

    :param int (\*uptr)(struct batadv_priv \*bat_priv, u8 \*src, u8 \*dst, void \*tvlv_value, u16 tvlv_value_len):
        unicast tvlv handler callback function. This function receives the
        source & destination of the unicast packet as well as the tvlv content
        to process.

    :param u8 type:
        tvlv handler type to be registered

    :param u8 version:
        tvlv handler version to be registered

    :param u8 flags:
        flags to enable or disable TVLV API behavior

.. _`batadv_tvlv_handler_unregister`:

batadv_tvlv_handler_unregister
==============================

.. c:function:: void batadv_tvlv_handler_unregister(struct batadv_priv *bat_priv, u8 type, u8 version)

    unregister tvlv handler based on the provided type and version (both need to match)

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 type:
        tvlv handler type to be unregistered

    :param u8 version:
        tvlv handler version to be unregistered

.. _`batadv_tvlv_unicast_send`:

batadv_tvlv_unicast_send
========================

.. c:function:: void batadv_tvlv_unicast_send(struct batadv_priv *bat_priv, u8 *src, u8 *dst, u8 type, u8 version, void *tvlv_value, u16 tvlv_value_len)

    send a unicast packet with tvlv payload to the specified host

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 \*src:
        source mac address of the unicast packet

    :param u8 \*dst:
        destination mac address of the unicast packet

    :param u8 type:
        tvlv type

    :param u8 version:
        tvlv version

    :param void \*tvlv_value:
        tvlv content

    :param u16 tvlv_value_len:
        tvlv content length

.. This file was automatic generated / don't edit.

