.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/iw_portmap.h

.. _`iwpm_init`:

iwpm_init
=========

.. c:function:: int iwpm_init( u8)

    Allocate resources for the iwarp port mapper

    :param u8:
        *undescribed*
    :type u8: 

.. _`iwpm_init.description`:

Description
-----------

Should be called when network interface goes up.

.. _`iwpm_exit`:

iwpm_exit
=========

.. c:function:: int iwpm_exit( u8)

    Deallocate resources for the iwarp port mapper

    :param u8:
        *undescribed*
    :type u8: 

.. _`iwpm_exit.description`:

Description
-----------

Should be called when network interface goes down.

.. _`iwpm_valid_pid`:

iwpm_valid_pid
==============

.. c:function:: int iwpm_valid_pid( void)

    Check if the userspace iwarp port mapper pid is valid

    :param void:
        no arguments
    :type void: 

.. _`iwpm_valid_pid.description`:

Description
-----------

Returns true if the pid is greater than zero, otherwise returns false

.. _`iwpm_register_pid`:

iwpm_register_pid
=================

.. c:function:: int iwpm_register_pid(struct iwpm_dev_data *pm_msg, u8 nl_client)

    Send a netlink query to userspace to get the iwarp port mapper pid

    :param pm_msg:
        Contains driver info to send to the userspace port mapper
    :type pm_msg: struct iwpm_dev_data \*

    :param nl_client:
        The index of the netlink client
    :type nl_client: u8

.. _`iwpm_add_mapping`:

iwpm_add_mapping
================

.. c:function:: int iwpm_add_mapping(struct iwpm_sa_data *pm_msg, u8 nl_client)

    Send a netlink add mapping request to the userspace port mapper

    :param pm_msg:
        Contains the local ip/tcp address info to send
    :type pm_msg: struct iwpm_sa_data \*

    :param nl_client:
        The index of the netlink client
    :type nl_client: u8

.. _`iwpm_add_mapping.description`:

Description
-----------

If the request is successful, the pm_msg stores
the port mapper response (mapped address info)

.. _`iwpm_add_and_query_mapping`:

iwpm_add_and_query_mapping
==========================

.. c:function:: int iwpm_add_and_query_mapping(struct iwpm_sa_data *pm_msg, u8 nl_client)

    Send a netlink add and query mapping request to the userspace port mapper

    :param pm_msg:
        Contains the local and remote ip/tcp address info to send
    :type pm_msg: struct iwpm_sa_data \*

    :param nl_client:
        The index of the netlink client
    :type nl_client: u8

.. _`iwpm_add_and_query_mapping.description`:

Description
-----------

If the request is successful, the pm_msg stores the
port mapper response (mapped local and remote address info)

.. _`iwpm_remove_mapping`:

iwpm_remove_mapping
===================

.. c:function:: int iwpm_remove_mapping(struct sockaddr_storage *local_addr, u8 nl_client)

    Send a netlink remove mapping request to the userspace port mapper

    :param local_addr:
        Local ip/tcp address to remove
    :type local_addr: struct sockaddr_storage \*

    :param nl_client:
        The index of the netlink client
    :type nl_client: u8

.. _`iwpm_register_pid_cb`:

iwpm_register_pid_cb
====================

.. c:function:: int iwpm_register_pid_cb(struct netlink_callback *, struct netlink_callback *)

    Process the port mapper response to iwpm_register_pid query

    :param :
        *undescribed*
    :type : struct netlink_callback \*

    :param :
        *undescribed*
    :type : struct netlink_callback \*

.. _`iwpm_register_pid_cb.description`:

Description
-----------

If successful, the function receives the userspace port mapper pid
which is used in future communication with the port mapper

.. _`iwpm_add_mapping_cb`:

iwpm_add_mapping_cb
===================

.. c:function:: int iwpm_add_mapping_cb(struct netlink_callback *, struct netlink_callback *)

    Process the port mapper response to iwpm_add_mapping request

    :param :
        *undescribed*
    :type : struct netlink_callback \*

    :param :
        *undescribed*
    :type : struct netlink_callback \*

.. _`iwpm_add_and_query_mapping_cb`:

iwpm_add_and_query_mapping_cb
=============================

.. c:function:: int iwpm_add_and_query_mapping_cb(struct netlink_callback *, struct netlink_callback *)

    Process the port mapper response to iwpm_add_and_query_mapping request

    :param :
        *undescribed*
    :type : struct netlink_callback \*

    :param :
        *undescribed*
    :type : struct netlink_callback \*

.. _`iwpm_remote_info_cb`:

iwpm_remote_info_cb
===================

.. c:function:: int iwpm_remote_info_cb(struct netlink_callback *, struct netlink_callback *)

    Process remote connecting peer address info, which the port mapper has received from the connecting peer

    :param :
        *undescribed*
    :type : struct netlink_callback \*

    :param :
        *undescribed*
    :type : struct netlink_callback \*

.. _`iwpm_remote_info_cb.description`:

Description
-----------

Stores the IPv4/IPv6 address info in a hash table

.. _`iwpm_mapping_error_cb`:

iwpm_mapping_error_cb
=====================

.. c:function:: int iwpm_mapping_error_cb(struct netlink_callback *, struct netlink_callback *)

    Process port mapper notification for error

    :param :
        *undescribed*
    :type : struct netlink_callback \*

    :param :
        *undescribed*
    :type : struct netlink_callback \*

.. _`iwpm_mapping_info_cb`:

iwpm_mapping_info_cb
====================

.. c:function:: int iwpm_mapping_info_cb(struct netlink_callback *, struct netlink_callback *)

    Process a notification that the userspace port mapper daemon is started

    :param :
        *undescribed*
    :type : struct netlink_callback \*

    :param :
        *undescribed*
    :type : struct netlink_callback \*

.. _`iwpm_mapping_info_cb.description`:

Description
-----------

Using the received port mapper pid, send all the local mapping
info records to the userspace port mapper

.. _`iwpm_ack_mapping_info_cb`:

iwpm_ack_mapping_info_cb
========================

.. c:function:: int iwpm_ack_mapping_info_cb(struct netlink_callback *, struct netlink_callback *)

    Process the port mapper ack for the provided local mapping info records

    :param :
        *undescribed*
    :type : struct netlink_callback \*

    :param :
        *undescribed*
    :type : struct netlink_callback \*

.. _`iwpm_get_remote_info`:

iwpm_get_remote_info
====================

.. c:function:: int iwpm_get_remote_info(struct sockaddr_storage *mapped_loc_addr, struct sockaddr_storage *mapped_rem_addr, struct sockaddr_storage *remote_addr, u8 nl_client)

    Get the remote connecting peer address info

    :param mapped_loc_addr:
        Mapped local address of the listening peer
    :type mapped_loc_addr: struct sockaddr_storage \*

    :param mapped_rem_addr:
        Mapped remote address of the connecting peer
    :type mapped_rem_addr: struct sockaddr_storage \*

    :param remote_addr:
        To store the remote address of the connecting peer
    :type remote_addr: struct sockaddr_storage \*

    :param nl_client:
        The index of the netlink client
    :type nl_client: u8

.. _`iwpm_get_remote_info.description`:

Description
-----------

The remote address info is retrieved and provided to the client in
the remote_addr. After that it is removed from the hash table

.. _`iwpm_create_mapinfo`:

iwpm_create_mapinfo
===================

.. c:function:: int iwpm_create_mapinfo(struct sockaddr_storage *local_addr, struct sockaddr_storage *mapped_addr, u8 nl_client)

    Store local and mapped IPv4/IPv6 address info in a hash table

    :param local_addr:
        Local ip/tcp address
    :type local_addr: struct sockaddr_storage \*

    :param mapped_addr:
        Mapped local ip/tcp address
    :type mapped_addr: struct sockaddr_storage \*

    :param nl_client:
        The index of the netlink client
    :type nl_client: u8

.. _`iwpm_remove_mapinfo`:

iwpm_remove_mapinfo
===================

.. c:function:: int iwpm_remove_mapinfo(struct sockaddr_storage *local_addr, struct sockaddr_storage *mapped_addr)

    Remove local and mapped IPv4/IPv6 address info from the hash table

    :param local_addr:
        Local ip/tcp address
    :type local_addr: struct sockaddr_storage \*

    :param mapped_addr:
        Mapped local ip/tcp address
    :type mapped_addr: struct sockaddr_storage \*

.. _`iwpm_remove_mapinfo.description`:

Description
-----------

Returns err code if mapping info is not found in the hash table,
otherwise returns 0

.. This file was automatic generated / don't edit.

