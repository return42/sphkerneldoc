.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/ulp/opa_vnic/opa_vnic_vema.c

.. _`opa_vnic_vema_port`:

struct opa_vnic_vema_port
=========================

.. c:type:: struct opa_vnic_vema_port

    - VNIC VEMA port details

.. _`opa_vnic_vema_port.definition`:

Definition
----------

.. code-block:: c

    struct opa_vnic_vema_port {
        struct opa_vnic_ctrl_port *cport;
        struct ib_mad_agent *mad_agent;
        struct opa_class_port_info class_port_info;
        u64 tid;
        u8 port_num;
        struct idr vport_idr;
        struct ib_event_handler event_handler;
        struct mutex lock;
    }

.. _`opa_vnic_vema_port.members`:

Members
-------

cport
    pointer to port

mad_agent
    pointer to mad agent for port

class_port_info
    Class port info information.

tid
    Transaction id

port_num
    OPA port number

vport_idr
    vnic ports idr

event_handler
    ib event handler

lock
    adapter interface lock

.. _`vema_get_vport_num`:

vema_get_vport_num
==================

.. c:function:: u8 vema_get_vport_num(struct opa_vnic_vema_mad *recvd_mad)

    - Get the vnic from the mad

    :param struct opa_vnic_vema_mad \*recvd_mad:
        Received mad

.. _`vema_get_vport_num.return`:

Return
------

returns value of the vnic port number

.. _`vema_get_vport_adapter`:

vema_get_vport_adapter
======================

.. c:function:: struct opa_vnic_adapter *vema_get_vport_adapter(struct opa_vnic_vema_mad *recvd_mad, struct opa_vnic_vema_port *port)

    - Get vnic port adapter from recvd mad

    :param struct opa_vnic_vema_mad \*recvd_mad:
        received mad

    :param struct opa_vnic_vema_port \*port:
        ptr to port struct on which MAD was recvd

.. _`vema_get_vport_adapter.return`:

Return
------

vnic adapter

.. _`vema_mac_tbl_req_ok`:

vema_mac_tbl_req_ok
===================

.. c:function:: bool vema_mac_tbl_req_ok(struct opa_veswport_mactable *mac_tbl)

    - Check if mac request has correct values

    :param struct opa_veswport_mactable \*mac_tbl:
        mac table

.. _`vema_mac_tbl_req_ok.description`:

Description
-----------

This function checks for the validity of the offset and number of
entries required.

.. _`vema_mac_tbl_req_ok.return`:

Return
------

true if offset and num_entries are valid

.. _`vema_add_vport`:

vema_add_vport
==============

.. c:function:: struct opa_vnic_adapter *vema_add_vport(struct opa_vnic_vema_port *port, u8 vport_num)

    - Add a new vnic port

    :param struct opa_vnic_vema_port \*port:
        ptr to opa_vnic_vema_port struct

    :param u8 vport_num:
        vnic port number (to be added)

.. _`vema_add_vport.description`:

Description
-----------

Return a pointer to the vnic adapter structure

.. _`vema_get_class_port_info`:

vema_get_class_port_info
========================

.. c:function:: void vema_get_class_port_info(struct opa_vnic_vema_port *port, struct opa_vnic_vema_mad *recvd_mad, struct opa_vnic_vema_mad *rsp_mad)

    - Get class info for port

    :param struct opa_vnic_vema_port \*port:
        Port on whic MAD was received

    :param struct opa_vnic_vema_mad \*recvd_mad:
        pointer to the received mad

    :param struct opa_vnic_vema_mad \*rsp_mad:
        pointer to respose mad

.. _`vema_get_class_port_info.description`:

Description
-----------

This function copies the latest class port info value set for the
port and stores it for generating traps

.. _`vema_set_class_port_info`:

vema_set_class_port_info
========================

.. c:function:: void vema_set_class_port_info(struct opa_vnic_vema_port *port, struct opa_vnic_vema_mad *recvd_mad, struct opa_vnic_vema_mad *rsp_mad)

    - Get class info for port

    :param struct opa_vnic_vema_port \*port:
        Port on whic MAD was received

    :param struct opa_vnic_vema_mad \*recvd_mad:
        pointer to the received mad

    :param struct opa_vnic_vema_mad \*rsp_mad:
        pointer to respose mad

.. _`vema_set_class_port_info.description`:

Description
-----------

This function updates the port class info for the specific vnic
and sets up the response mad data

.. _`vema_get_veswport_info`:

vema_get_veswport_info
======================

.. c:function:: void vema_get_veswport_info(struct opa_vnic_vema_port *port, struct opa_vnic_vema_mad *recvd_mad, struct opa_vnic_vema_mad *rsp_mad)

    - Get veswport info

    :param struct opa_vnic_vema_port \*port:
        source port on which MAD was received

    :param struct opa_vnic_vema_mad \*recvd_mad:
        pointer to the received mad

    :param struct opa_vnic_vema_mad \*rsp_mad:
        pointer to respose mad

.. _`vema_set_veswport_info`:

vema_set_veswport_info
======================

.. c:function:: void vema_set_veswport_info(struct opa_vnic_vema_port *port, struct opa_vnic_vema_mad *recvd_mad, struct opa_vnic_vema_mad *rsp_mad)

    - Set veswport info

    :param struct opa_vnic_vema_port \*port:
        source port on which MAD was received

    :param struct opa_vnic_vema_mad \*recvd_mad:
        pointer to the received mad

    :param struct opa_vnic_vema_mad \*rsp_mad:
        pointer to respose mad

.. _`vema_set_veswport_info.description`:

Description
-----------

This function gets the port class infor for vnic

.. _`vema_get_mac_entries`:

vema_get_mac_entries
====================

.. c:function:: void vema_get_mac_entries(struct opa_vnic_vema_port *port, struct opa_vnic_vema_mad *recvd_mad, struct opa_vnic_vema_mad *rsp_mad)

    - Get MAC entries in VNIC MAC table

    :param struct opa_vnic_vema_port \*port:
        source port on which MAD was received

    :param struct opa_vnic_vema_mad \*recvd_mad:
        pointer to the received mad

    :param struct opa_vnic_vema_mad \*rsp_mad:
        pointer to respose mad

.. _`vema_get_mac_entries.description`:

Description
-----------

This function gets the MAC entries that are programmed into
the VNIC MAC forwarding table. It checks for the validity of
the index into the MAC table and the number of entries that
are to be retrieved.

.. _`vema_set_mac_entries`:

vema_set_mac_entries
====================

.. c:function:: void vema_set_mac_entries(struct opa_vnic_vema_port *port, struct opa_vnic_vema_mad *recvd_mad, struct opa_vnic_vema_mad *rsp_mad)

    - Set MAC entries in VNIC MAC table

    :param struct opa_vnic_vema_port \*port:
        source port on which MAD was received

    :param struct opa_vnic_vema_mad \*recvd_mad:
        pointer to the received mad

    :param struct opa_vnic_vema_mad \*rsp_mad:
        pointer to respose mad

.. _`vema_set_mac_entries.description`:

Description
-----------

This function sets the MAC entries in the VNIC forwarding table
It checks for the validity of the index and the number of forwarding
table entries to be programmed.

.. _`vema_set_delete_vesw`:

vema_set_delete_vesw
====================

.. c:function:: void vema_set_delete_vesw(struct opa_vnic_vema_port *port, struct opa_vnic_vema_mad *recvd_mad, struct opa_vnic_vema_mad *rsp_mad)

    - Reset VESW info to POD values

    :param struct opa_vnic_vema_port \*port:
        source port on which MAD was received

    :param struct opa_vnic_vema_mad \*recvd_mad:
        pointer to the received mad

    :param struct opa_vnic_vema_mad \*rsp_mad:
        pointer to respose mad

.. _`vema_set_delete_vesw.description`:

Description
-----------

This function clears all the fields of veswport info for the requested vesw
and sets them back to the power-on default values. It does not delete the
vesw.

.. _`vema_get_mac_list`:

vema_get_mac_list
=================

.. c:function:: void vema_get_mac_list(struct opa_vnic_vema_port *port, struct opa_vnic_vema_mad *recvd_mad, struct opa_vnic_vema_mad *rsp_mad, u16 attr_id)

    - Get the unicast/multicast macs.

    :param struct opa_vnic_vema_port \*port:
        source port on which MAD was received

    :param struct opa_vnic_vema_mad \*recvd_mad:
        Received mad contains fields to set vnic parameters

    :param struct opa_vnic_vema_mad \*rsp_mad:
        Response mad to be built

    :param u16 attr_id:
        Attribute ID indicating multicast or unicast mac list

.. _`vema_get_summary_counters`:

vema_get_summary_counters
=========================

.. c:function:: void vema_get_summary_counters(struct opa_vnic_vema_port *port, struct opa_vnic_vema_mad *recvd_mad, struct opa_vnic_vema_mad *rsp_mad)

    - Gets summary counters.

    :param struct opa_vnic_vema_port \*port:
        source port on which MAD was received

    :param struct opa_vnic_vema_mad \*recvd_mad:
        Received mad contains fields to set vnic parameters

    :param struct opa_vnic_vema_mad \*rsp_mad:
        Response mad to be built

.. _`vema_get_error_counters`:

vema_get_error_counters
=======================

.. c:function:: void vema_get_error_counters(struct opa_vnic_vema_port *port, struct opa_vnic_vema_mad *recvd_mad, struct opa_vnic_vema_mad *rsp_mad)

    - Gets summary counters.

    :param struct opa_vnic_vema_port \*port:
        source port on which MAD was received

    :param struct opa_vnic_vema_mad \*recvd_mad:
        Received mad contains fields to set vnic parameters

    :param struct opa_vnic_vema_mad \*rsp_mad:
        Response mad to be built

.. _`vema_get`:

vema_get
========

.. c:function:: void vema_get(struct opa_vnic_vema_port *port, struct opa_vnic_vema_mad *recvd_mad, struct opa_vnic_vema_mad *rsp_mad)

    - Process received get MAD

    :param struct opa_vnic_vema_port \*port:
        source port on which MAD was received

    :param struct opa_vnic_vema_mad \*recvd_mad:
        Received mad

    :param struct opa_vnic_vema_mad \*rsp_mad:
        Response mad to be built

.. _`vema_set`:

vema_set
========

.. c:function:: void vema_set(struct opa_vnic_vema_port *port, struct opa_vnic_vema_mad *recvd_mad, struct opa_vnic_vema_mad *rsp_mad)

    - Process received set MAD

    :param struct opa_vnic_vema_port \*port:
        source port on which MAD was received

    :param struct opa_vnic_vema_mad \*recvd_mad:
        Received mad contains fields to set vnic parameters

    :param struct opa_vnic_vema_mad \*rsp_mad:
        Response mad to be built

.. _`vema_send`:

vema_send
=========

.. c:function:: void vema_send(struct ib_mad_agent *mad_agent, struct ib_mad_send_wc *mad_wc)

    - Send handler for VEMA MAD agent

    :param struct ib_mad_agent \*mad_agent:
        pointer to the mad agent

    :param struct ib_mad_send_wc \*mad_wc:
        pointer to mad send work completion information

.. _`vema_send.description`:

Description
-----------

Free all the data structures associated with the sent MAD

.. _`vema_recv`:

vema_recv
=========

.. c:function:: void vema_recv(struct ib_mad_agent *mad_agent, struct ib_mad_send_buf *send_buf, struct ib_mad_recv_wc *mad_wc)

    - Recv handler for VEMA MAD agent

    :param struct ib_mad_agent \*mad_agent:
        pointer to the mad agent

    :param struct ib_mad_send_buf \*send_buf:
        Send buffer if found, else NULL

    :param struct ib_mad_recv_wc \*mad_wc:
        pointer to mad send work completion information

.. _`vema_recv.description`:

Description
-----------

Handle only set and get methods and respond to other methods
as unsupported. Allocate response buffer and address handle
for the response MAD.

.. _`vema_get_port`:

vema_get_port
=============

.. c:function:: struct opa_vnic_vema_port *vema_get_port(struct opa_vnic_ctrl_port *cport, u8 port_num)

    - Gets the opa_vnic_vema_port

    :param struct opa_vnic_ctrl_port \*cport:
        pointer to control dev

    :param u8 port_num:
        Port number

.. _`vema_get_port.description`:

Description
-----------

This function loops through the ports and returns
the opa_vnic_vema port structure that is associated
with the OPA port number

.. _`vema_get_port.return`:

Return
------

ptr to requested opa_vnic_vema_port strucure
if success, NULL if not

.. _`opa_vnic_vema_send_trap`:

opa_vnic_vema_send_trap
=======================

.. c:function:: void opa_vnic_vema_send_trap(struct opa_vnic_adapter *adapter, struct __opa_veswport_trap *data, u32 lid)

    - This function sends a trap to the EM

    :param struct opa_vnic_adapter \*adapter:
        *undescribed*

    :param struct __opa_veswport_trap \*data:
        pointer to trap data filled by calling function

    :param u32 lid:
        issuers lid (encap_slid from vesw_port_info)

.. _`opa_vnic_vema_send_trap.description`:

Description
-----------

This function is called from the VNIC driver to send a trap if there
is somethng the EM should be notified about. These events currently
are
1) UNICAST INTERFACE MACADDRESS changes
2) MULTICAST INTERFACE MACADDRESS changes
3) ETHERNET LINK STATUS changes
While allocating the send mad the remote site qpn used is 1
as this is the well known QP.

.. _`vema_unregister`:

vema_unregister
===============

.. c:function:: void vema_unregister(struct opa_vnic_ctrl_port *cport)

    - Unregisters agent

    :param struct opa_vnic_ctrl_port \*cport:
        pointer to control port

.. _`vema_unregister.description`:

Description
-----------

This deletes the registration by VEMA for MADs

.. _`vema_register`:

vema_register
=============

.. c:function:: int vema_register(struct opa_vnic_ctrl_port *cport)

    - Registers agent

    :param struct opa_vnic_ctrl_port \*cport:
        pointer to control port

.. _`vema_register.description`:

Description
-----------

This function registers the handlers for the VEMA MADs

.. _`vema_register.return`:

Return
------

returns 0 on success. non zero otherwise

.. _`opa_vnic_ctrl_config_dev`:

opa_vnic_ctrl_config_dev
========================

.. c:function:: void opa_vnic_ctrl_config_dev(struct opa_vnic_ctrl_port *cport, bool en)

    - This function sends a trap to the EM by way of ib_modify_port to indicate support for ethernet on the fabric.

    :param struct opa_vnic_ctrl_port \*cport:
        pointer to control port

    :param bool en:
        enable or disable ethernet on fabric support

.. _`opa_vnic_vema_add_one`:

opa_vnic_vema_add_one
=====================

.. c:function:: void opa_vnic_vema_add_one(struct ib_device *device)

    - Handle new ib device

    :param struct ib_device \*device:
        ib device pointer

.. _`opa_vnic_vema_add_one.description`:

Description
-----------

Allocate the vnic control port and initialize it.

.. _`opa_vnic_vema_rem_one`:

opa_vnic_vema_rem_one
=====================

.. c:function:: void opa_vnic_vema_rem_one(struct ib_device *device, void *client_data)

    - Handle ib device removal

    :param struct ib_device \*device:
        ib device pointer

    :param void \*client_data:
        ib client data

.. _`opa_vnic_vema_rem_one.description`:

Description
-----------

Uninitialize and free the vnic control port.

.. This file was automatic generated / don't edit.

