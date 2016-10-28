.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/mpt3sas/mpt3sas_transport.c

.. _`_transport_sas_node_find_by_sas_address`:

_transport_sas_node_find_by_sas_address
=======================================

.. c:function:: struct _sas_node *_transport_sas_node_find_by_sas_address(struct MPT3SAS_ADAPTER *ioc, u64 sas_address)

    sas node search

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u64 sas_address:
        sas address of expander or sas host

.. _`_transport_sas_node_find_by_sas_address.context`:

Context
-------

Calling function should acquire ioc->sas_node_lock.

.. _`_transport_sas_node_find_by_sas_address.description`:

Description
-----------

Search for either hba phys or expander device based on handle, then returns
the sas_node object.

.. _`_transport_convert_phy_link_rate`:

_transport_convert_phy_link_rate
================================

.. c:function:: enum sas_linkrate _transport_convert_phy_link_rate(u8 link_rate)

    :param u8 link_rate:
        link rate returned from mpt firmware

.. _`_transport_convert_phy_link_rate.description`:

Description
-----------

Convert link_rate from mpi fusion into sas_transport form.

.. _`_transport_set_identify`:

_transport_set_identify
=======================

.. c:function:: int _transport_set_identify(struct MPT3SAS_ADAPTER *ioc, u16 handle, struct sas_identify *identify)

    set identify for phys and end devices

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        device handle

    :param struct sas_identify \*identify:
        sas identify info

.. _`_transport_set_identify.description`:

Description
-----------

Populates sas identify info.

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_transport_done`:

mpt3sas_transport_done
======================

.. c:function:: u8 mpt3sas_transport_done(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    internal transport layer callback handler.

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u8 msix_index:
        MSIX table index supplied by the OS

    :param u32 reply:
        reply message frame(lower 32bit addr)

.. _`mpt3sas_transport_done.description`:

Description
-----------

Callback handler when sending internal generated transport cmds.
The callback index passed is \`ioc->transport_cb_idx\`

Return 1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_transport_expander_report_manufacture`:

_transport_expander_report_manufacture
======================================

.. c:function:: int _transport_expander_report_manufacture(struct MPT3SAS_ADAPTER *ioc, u64 sas_address, struct sas_expander_device *edev)

    obtain SMP report_manufacture

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u64 sas_address:
        expander sas address

    :param struct sas_expander_device \*edev:
        the sas_expander_device object

.. _`_transport_expander_report_manufacture.description`:

Description
-----------

Fills in the sas_expander_device object when SMP port is created.

Returns 0 for success, non-zero for failure.

.. _`_transport_delete_port`:

_transport_delete_port
======================

.. c:function:: void _transport_delete_port(struct MPT3SAS_ADAPTER *ioc, struct _sas_port *mpt3sas_port)

    helper function to removing a port

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_port \*mpt3sas_port:
        mpt3sas per port object

.. _`_transport_delete_port.description`:

Description
-----------

Returns nothing.

.. _`_transport_delete_phy`:

_transport_delete_phy
=====================

.. c:function:: void _transport_delete_phy(struct MPT3SAS_ADAPTER *ioc, struct _sas_port *mpt3sas_port, struct _sas_phy *mpt3sas_phy)

    helper function to removing single phy from port

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_port \*mpt3sas_port:
        mpt3sas per port object

    :param struct _sas_phy \*mpt3sas_phy:
        mpt3sas per phy object

.. _`_transport_delete_phy.description`:

Description
-----------

Returns nothing.

.. _`_transport_add_phy`:

_transport_add_phy
==================

.. c:function:: void _transport_add_phy(struct MPT3SAS_ADAPTER *ioc, struct _sas_port *mpt3sas_port, struct _sas_phy *mpt3sas_phy)

    helper function to adding single phy to port

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_port \*mpt3sas_port:
        mpt3sas per port object

    :param struct _sas_phy \*mpt3sas_phy:
        mpt3sas per phy object

.. _`_transport_add_phy.description`:

Description
-----------

Returns nothing.

.. _`_transport_add_phy_to_an_existing_port`:

_transport_add_phy_to_an_existing_port
======================================

.. c:function:: void _transport_add_phy_to_an_existing_port(struct MPT3SAS_ADAPTER *ioc, struct _sas_node *sas_node, struct _sas_phy *mpt3sas_phy, u64 sas_address)

    adding new phy to existing port

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_node \*sas_node:
        sas node object (either expander or sas host)

    :param struct _sas_phy \*mpt3sas_phy:
        mpt3sas per phy object

    :param u64 sas_address:
        sas address of device/expander were phy needs to be added to

.. _`_transport_add_phy_to_an_existing_port.description`:

Description
-----------

Returns nothing.

.. _`_transport_del_phy_from_an_existing_port`:

_transport_del_phy_from_an_existing_port
========================================

.. c:function:: void _transport_del_phy_from_an_existing_port(struct MPT3SAS_ADAPTER *ioc, struct _sas_node *sas_node, struct _sas_phy *mpt3sas_phy)

    delete phy from existing port

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_node \*sas_node:
        sas node object (either expander or sas host)

    :param struct _sas_phy \*mpt3sas_phy:
        mpt3sas per phy object

.. _`_transport_del_phy_from_an_existing_port.description`:

Description
-----------

Returns nothing.

.. _`_transport_sanity_check`:

_transport_sanity_check
=======================

.. c:function:: void _transport_sanity_check(struct MPT3SAS_ADAPTER *ioc, struct _sas_node *sas_node, u64 sas_address)

    sanity check when adding a new port

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_node \*sas_node:
        sas node object (either expander or sas host)

    :param u64 sas_address:
        sas address of device being added

.. _`_transport_sanity_check.description`:

Description
-----------

See the explanation above from \_transport_delete_duplicate_port

.. _`mpt3sas_transport_port_add`:

mpt3sas_transport_port_add
==========================

.. c:function:: struct _sas_port *mpt3sas_transport_port_add(struct MPT3SAS_ADAPTER *ioc, u16 handle, u64 sas_address)

    insert port to the list

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        handle of attached device

    :param u64 sas_address:
        sas address of parent expander or sas host

.. _`mpt3sas_transport_port_add.context`:

Context
-------

This function will acquire ioc->sas_node_lock.

.. _`mpt3sas_transport_port_add.description`:

Description
-----------

Adding new port object to the sas_node->sas_port_list.

Returns mpt3sas_port.

.. _`mpt3sas_transport_port_remove`:

mpt3sas_transport_port_remove
=============================

.. c:function:: void mpt3sas_transport_port_remove(struct MPT3SAS_ADAPTER *ioc, u64 sas_address, u64 sas_address_parent)

    remove port from the list

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u64 sas_address:
        sas address of attached device

    :param u64 sas_address_parent:
        sas address of parent expander or sas host

.. _`mpt3sas_transport_port_remove.context`:

Context
-------

This function will acquire ioc->sas_node_lock.

.. _`mpt3sas_transport_port_remove.description`:

Description
-----------

Removing object and freeing associated memory from the
ioc->sas_port_list.

Return nothing.

.. _`mpt3sas_transport_add_host_phy`:

mpt3sas_transport_add_host_phy
==============================

.. c:function:: int mpt3sas_transport_add_host_phy(struct MPT3SAS_ADAPTER *ioc, struct _sas_phy *mpt3sas_phy, Mpi2SasPhyPage0_t phy_pg0, struct device *parent_dev)

    report sas_host phy to transport

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_phy \*mpt3sas_phy:
        mpt3sas per phy object

    :param Mpi2SasPhyPage0_t phy_pg0:
        sas phy page 0

    :param struct device \*parent_dev:
        parent device class object

.. _`mpt3sas_transport_add_host_phy.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_transport_add_expander_phy`:

mpt3sas_transport_add_expander_phy
==================================

.. c:function:: int mpt3sas_transport_add_expander_phy(struct MPT3SAS_ADAPTER *ioc, struct _sas_phy *mpt3sas_phy, Mpi2ExpanderPage1_t expander_pg1, struct device *parent_dev)

    report expander phy to transport

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_phy \*mpt3sas_phy:
        mpt3sas per phy object

    :param Mpi2ExpanderPage1_t expander_pg1:
        expander page 1

    :param struct device \*parent_dev:
        parent device class object

.. _`mpt3sas_transport_add_expander_phy.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_transport_update_links`:

mpt3sas_transport_update_links
==============================

.. c:function:: void mpt3sas_transport_update_links(struct MPT3SAS_ADAPTER *ioc, u64 sas_address, u16 handle, u8 phy_number, u8 link_rate)

    refreshing phy link changes

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u64 sas_address:
        sas address of parent expander or sas host

    :param u16 handle:
        attached device handle

    :param u8 phy_number:
        *undescribed*

    :param u8 link_rate:
        new link rate

.. _`mpt3sas_transport_update_links.description`:

Description
-----------

Returns nothing.

.. _`_transport_get_expander_phy_error_log`:

_transport_get_expander_phy_error_log
=====================================

.. c:function:: int _transport_get_expander_phy_error_log(struct MPT3SAS_ADAPTER *ioc, struct sas_phy *phy)

    return expander counters

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct sas_phy \*phy:
        The sas phy object

.. _`_transport_get_expander_phy_error_log.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_transport_get_linkerrors`:

_transport_get_linkerrors
=========================

.. c:function:: int _transport_get_linkerrors(struct sas_phy *phy)

    return phy counters for both hba and expanders

    :param struct sas_phy \*phy:
        The sas phy object

.. _`_transport_get_linkerrors.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_transport_get_enclosure_identifier`:

_transport_get_enclosure_identifier
===================================

.. c:function:: int _transport_get_enclosure_identifier(struct sas_rphy *rphy, u64 *identifier)

    :param struct sas_rphy \*rphy:
        *undescribed*

    :param u64 \*identifier:
        *undescribed*

.. _`_transport_get_enclosure_identifier.description`:

Description
-----------

Obtain the enclosure logical id for an expander.
Returns 0 for success, non-zero for failure.

.. _`_transport_get_bay_identifier`:

_transport_get_bay_identifier
=============================

.. c:function:: int _transport_get_bay_identifier(struct sas_rphy *rphy)

    :param struct sas_rphy \*rphy:
        *undescribed*

.. _`_transport_get_bay_identifier.description`:

Description
-----------

Returns the slot id for a device that resides inside an enclosure.

.. _`_transport_expander_phy_control`:

_transport_expander_phy_control
===============================

.. c:function:: int _transport_expander_phy_control(struct MPT3SAS_ADAPTER *ioc, struct sas_phy *phy, u8 phy_operation)

    expander phy control

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct sas_phy \*phy:
        The sas phy object

    :param u8 phy_operation:
        *undescribed*

.. _`_transport_expander_phy_control.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_transport_phy_reset`:

_transport_phy_reset
====================

.. c:function:: int _transport_phy_reset(struct sas_phy *phy, int hard_reset)

    :param struct sas_phy \*phy:
        The sas phy object

    :param int hard_reset:
        *undescribed*

.. _`_transport_phy_reset.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_transport_phy_enable`:

_transport_phy_enable
=====================

.. c:function:: int _transport_phy_enable(struct sas_phy *phy, int enable)

    enable/disable phys

    :param struct sas_phy \*phy:
        The sas phy object

    :param int enable:
        enable phy when true

.. _`_transport_phy_enable.description`:

Description
-----------

Only support sas_host direct attached phys.
Returns 0 for success, non-zero for failure.

.. _`_transport_phy_speed`:

_transport_phy_speed
====================

.. c:function:: int _transport_phy_speed(struct sas_phy *phy, struct sas_phy_linkrates *rates)

    set phy min/max link rates

    :param struct sas_phy \*phy:
        The sas phy object

    :param struct sas_phy_linkrates \*rates:
        rates defined in sas_phy_linkrates

.. _`_transport_phy_speed.description`:

Description
-----------

Only support sas_host direct attached phys.
Returns 0 for success, non-zero for failure.

.. _`_transport_smp_handler`:

_transport_smp_handler
======================

.. c:function:: int _transport_smp_handler(struct Scsi_Host *shost, struct sas_rphy *rphy, struct request *req)

    transport portal for smp passthru

    :param struct Scsi_Host \*shost:
        shost object

    :param struct sas_rphy \*rphy:
        sas transport rphy object

    :param struct request \*req:
        *undescribed*

.. _`_transport_smp_handler.description`:

Description
-----------

This used primarily for smp_utils.

.. _`_transport_smp_handler.example`:

Example
-------

.. code-block:: c

    smp_rep_general /sys/class/bsg/expander-5:0


.. This file was automatic generated / don't edit.

