.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/mpt3sas/mpt3sas_transport.c

.. _`_transport_sas_node_find_by_sas_address`:

\_transport_sas_node_find_by_sas_address
========================================

.. c:function:: struct _sas_node *_transport_sas_node_find_by_sas_address(struct MPT3SAS_ADAPTER *ioc, u64 sas_address)

    sas node search

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param sas_address:
        sas address of expander or sas host
    :type sas_address: u64

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

\_transport_convert_phy_link_rate
=================================

.. c:function:: enum sas_linkrate _transport_convert_phy_link_rate(u8 link_rate)

    :param link_rate:
        link rate returned from mpt firmware
    :type link_rate: u8

.. _`_transport_convert_phy_link_rate.description`:

Description
-----------

Convert link_rate from mpi fusion into sas_transport form.

.. _`_transport_set_identify`:

\_transport_set_identify
========================

.. c:function:: int _transport_set_identify(struct MPT3SAS_ADAPTER *ioc, u16 handle, struct sas_identify *identify)

    set identify for phys and end devices

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param handle:
        device handle
    :type handle: u16

    :param identify:
        sas identify info
    :type identify: struct sas_identify \*

.. _`_transport_set_identify.description`:

Description
-----------

Populates sas identify info.

.. _`_transport_set_identify.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_transport_done`:

mpt3sas_transport_done
======================

.. c:function:: u8 mpt3sas_transport_done(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    internal transport layer callback handler.

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

    :param msix_index:
        MSIX table index supplied by the OS
    :type msix_index: u8

    :param reply:
        reply message frame(lower 32bit addr)
    :type reply: u32

.. _`mpt3sas_transport_done.description`:

Description
-----------

Callback handler when sending internal generated transport cmds.
The callback index passed is \`ioc->transport_cb_idx\`

.. _`mpt3sas_transport_done.return`:

Return
------

1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_transport_expander_report_manufacture`:

\_transport_expander_report_manufacture
=======================================

.. c:function:: int _transport_expander_report_manufacture(struct MPT3SAS_ADAPTER *ioc, u64 sas_address, struct sas_expander_device *edev)

    obtain SMP report_manufacture

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param sas_address:
        expander sas address
    :type sas_address: u64

    :param edev:
        the sas_expander_device object
    :type edev: struct sas_expander_device \*

.. _`_transport_expander_report_manufacture.description`:

Description
-----------

Fills in the sas_expander_device object when SMP port is created.

.. _`_transport_expander_report_manufacture.return`:

Return
------

0 for success, non-zero for failure.

.. _`_transport_delete_port`:

\_transport_delete_port
=======================

.. c:function:: void _transport_delete_port(struct MPT3SAS_ADAPTER *ioc, struct _sas_port *mpt3sas_port)

    helper function to removing a port

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpt3sas_port:
        mpt3sas per port object
    :type mpt3sas_port: struct _sas_port \*

.. _`_transport_delete_phy`:

\_transport_delete_phy
======================

.. c:function:: void _transport_delete_phy(struct MPT3SAS_ADAPTER *ioc, struct _sas_port *mpt3sas_port, struct _sas_phy *mpt3sas_phy)

    helper function to removing single phy from port

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpt3sas_port:
        mpt3sas per port object
    :type mpt3sas_port: struct _sas_port \*

    :param mpt3sas_phy:
        mpt3sas per phy object
    :type mpt3sas_phy: struct _sas_phy \*

.. _`_transport_add_phy`:

\_transport_add_phy
===================

.. c:function:: void _transport_add_phy(struct MPT3SAS_ADAPTER *ioc, struct _sas_port *mpt3sas_port, struct _sas_phy *mpt3sas_phy)

    helper function to adding single phy to port

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpt3sas_port:
        mpt3sas per port object
    :type mpt3sas_port: struct _sas_port \*

    :param mpt3sas_phy:
        mpt3sas per phy object
    :type mpt3sas_phy: struct _sas_phy \*

.. _`_transport_add_phy_to_an_existing_port`:

\_transport_add_phy_to_an_existing_port
=======================================

.. c:function:: void _transport_add_phy_to_an_existing_port(struct MPT3SAS_ADAPTER *ioc, struct _sas_node *sas_node, struct _sas_phy *mpt3sas_phy, u64 sas_address)

    adding new phy to existing port

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param sas_node:
        sas node object (either expander or sas host)
    :type sas_node: struct _sas_node \*

    :param mpt3sas_phy:
        mpt3sas per phy object
    :type mpt3sas_phy: struct _sas_phy \*

    :param sas_address:
        sas address of device/expander were phy needs to be added to
    :type sas_address: u64

.. _`_transport_del_phy_from_an_existing_port`:

\_transport_del_phy_from_an_existing_port
=========================================

.. c:function:: void _transport_del_phy_from_an_existing_port(struct MPT3SAS_ADAPTER *ioc, struct _sas_node *sas_node, struct _sas_phy *mpt3sas_phy)

    delete phy from existing port

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param sas_node:
        sas node object (either expander or sas host)
    :type sas_node: struct _sas_node \*

    :param mpt3sas_phy:
        mpt3sas per phy object
    :type mpt3sas_phy: struct _sas_phy \*

.. _`_transport_sanity_check`:

\_transport_sanity_check
========================

.. c:function:: void _transport_sanity_check(struct MPT3SAS_ADAPTER *ioc, struct _sas_node *sas_node, u64 sas_address)

    sanity check when adding a new port

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param sas_node:
        sas node object (either expander or sas host)
    :type sas_node: struct _sas_node \*

    :param sas_address:
        sas address of device being added
    :type sas_address: u64

.. _`_transport_sanity_check.description`:

Description
-----------

See the explanation above from \_transport_delete_duplicate_port

.. _`mpt3sas_transport_port_add`:

mpt3sas_transport_port_add
==========================

.. c:function:: struct _sas_port *mpt3sas_transport_port_add(struct MPT3SAS_ADAPTER *ioc, u16 handle, u64 sas_address)

    insert port to the list

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param handle:
        handle of attached device
    :type handle: u16

    :param sas_address:
        sas address of parent expander or sas host
    :type sas_address: u64

.. _`mpt3sas_transport_port_add.context`:

Context
-------

This function will acquire ioc->sas_node_lock.

.. _`mpt3sas_transport_port_add.description`:

Description
-----------

Adding new port object to the sas_node->sas_port_list.

.. _`mpt3sas_transport_port_add.return`:

Return
------

mpt3sas_port.

.. _`mpt3sas_transport_port_remove`:

mpt3sas_transport_port_remove
=============================

.. c:function:: void mpt3sas_transport_port_remove(struct MPT3SAS_ADAPTER *ioc, u64 sas_address, u64 sas_address_parent)

    remove port from the list

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param sas_address:
        sas address of attached device
    :type sas_address: u64

    :param sas_address_parent:
        sas address of parent expander or sas host
    :type sas_address_parent: u64

.. _`mpt3sas_transport_port_remove.context`:

Context
-------

This function will acquire ioc->sas_node_lock.

.. _`mpt3sas_transport_port_remove.description`:

Description
-----------

Removing object and freeing associated memory from the
ioc->sas_port_list.

.. _`mpt3sas_transport_add_host_phy`:

mpt3sas_transport_add_host_phy
==============================

.. c:function:: int mpt3sas_transport_add_host_phy(struct MPT3SAS_ADAPTER *ioc, struct _sas_phy *mpt3sas_phy, Mpi2SasPhyPage0_t phy_pg0, struct device *parent_dev)

    report sas_host phy to transport

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpt3sas_phy:
        mpt3sas per phy object
    :type mpt3sas_phy: struct _sas_phy \*

    :param phy_pg0:
        sas phy page 0
    :type phy_pg0: Mpi2SasPhyPage0_t

    :param parent_dev:
        parent device class object
    :type parent_dev: struct device \*

.. _`mpt3sas_transport_add_host_phy.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_transport_add_expander_phy`:

mpt3sas_transport_add_expander_phy
==================================

.. c:function:: int mpt3sas_transport_add_expander_phy(struct MPT3SAS_ADAPTER *ioc, struct _sas_phy *mpt3sas_phy, Mpi2ExpanderPage1_t expander_pg1, struct device *parent_dev)

    report expander phy to transport

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpt3sas_phy:
        mpt3sas per phy object
    :type mpt3sas_phy: struct _sas_phy \*

    :param expander_pg1:
        expander page 1
    :type expander_pg1: Mpi2ExpanderPage1_t

    :param parent_dev:
        parent device class object
    :type parent_dev: struct device \*

.. _`mpt3sas_transport_add_expander_phy.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_transport_update_links`:

mpt3sas_transport_update_links
==============================

.. c:function:: void mpt3sas_transport_update_links(struct MPT3SAS_ADAPTER *ioc, u64 sas_address, u16 handle, u8 phy_number, u8 link_rate)

    refreshing phy link changes

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param sas_address:
        sas address of parent expander or sas host
    :type sas_address: u64

    :param handle:
        attached device handle
    :type handle: u16

    :param phy_number:
        phy number
    :type phy_number: u8

    :param link_rate:
        new link rate
    :type link_rate: u8

.. _`_transport_get_expander_phy_error_log`:

\_transport_get_expander_phy_error_log
======================================

.. c:function:: int _transport_get_expander_phy_error_log(struct MPT3SAS_ADAPTER *ioc, struct sas_phy *phy)

    return expander counters

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param phy:
        The sas phy object
    :type phy: struct sas_phy \*

.. _`_transport_get_expander_phy_error_log.return`:

Return
------

0 for success, non-zero for failure.

.. _`_transport_get_linkerrors`:

\_transport_get_linkerrors
==========================

.. c:function:: int _transport_get_linkerrors(struct sas_phy *phy)

    return phy counters for both hba and expanders

    :param phy:
        The sas phy object
    :type phy: struct sas_phy \*

.. _`_transport_get_linkerrors.return`:

Return
------

0 for success, non-zero for failure.

.. _`_transport_get_enclosure_identifier`:

\_transport_get_enclosure_identifier
====================================

.. c:function:: int _transport_get_enclosure_identifier(struct sas_rphy *rphy, u64 *identifier)

    :param rphy:
        The sas phy object
    :type rphy: struct sas_rphy \*

    :param identifier:
        ?
    :type identifier: u64 \*

.. _`_transport_get_enclosure_identifier.description`:

Description
-----------

Obtain the enclosure logical id for an expander.

.. _`_transport_get_enclosure_identifier.return`:

Return
------

0 for success, non-zero for failure.

.. _`_transport_get_bay_identifier`:

\_transport_get_bay_identifier
==============================

.. c:function:: int _transport_get_bay_identifier(struct sas_rphy *rphy)

    :param rphy:
        The sas phy object
    :type rphy: struct sas_rphy \*

.. _`_transport_get_bay_identifier.return`:

Return
------

the slot id for a device that resides inside an enclosure.

.. _`_transport_expander_phy_control`:

\_transport_expander_phy_control
================================

.. c:function:: int _transport_expander_phy_control(struct MPT3SAS_ADAPTER *ioc, struct sas_phy *phy, u8 phy_operation)

    expander phy control

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param phy:
        The sas phy object
    :type phy: struct sas_phy \*

    :param phy_operation:
        ?
    :type phy_operation: u8

.. _`_transport_expander_phy_control.return`:

Return
------

0 for success, non-zero for failure.

.. _`_transport_phy_reset`:

\_transport_phy_reset
=====================

.. c:function:: int _transport_phy_reset(struct sas_phy *phy, int hard_reset)

    :param phy:
        The sas phy object
    :type phy: struct sas_phy \*

    :param hard_reset:
        *undescribed*
    :type hard_reset: int

.. _`_transport_phy_reset.return`:

Return
------

0 for success, non-zero for failure.

.. _`_transport_phy_enable`:

\_transport_phy_enable
======================

.. c:function:: int _transport_phy_enable(struct sas_phy *phy, int enable)

    enable/disable phys

    :param phy:
        The sas phy object
    :type phy: struct sas_phy \*

    :param enable:
        enable phy when true
    :type enable: int

.. _`_transport_phy_enable.description`:

Description
-----------

Only support sas_host direct attached phys.

.. _`_transport_phy_enable.return`:

Return
------

0 for success, non-zero for failure.

.. _`_transport_phy_speed`:

\_transport_phy_speed
=====================

.. c:function:: int _transport_phy_speed(struct sas_phy *phy, struct sas_phy_linkrates *rates)

    set phy min/max link rates

    :param phy:
        The sas phy object
    :type phy: struct sas_phy \*

    :param rates:
        rates defined in sas_phy_linkrates
    :type rates: struct sas_phy_linkrates \*

.. _`_transport_phy_speed.description`:

Description
-----------

Only support sas_host direct attached phys.

.. _`_transport_phy_speed.return`:

Return
------

0 for success, non-zero for failure.

.. _`_transport_smp_handler`:

\_transport_smp_handler
=======================

.. c:function:: void _transport_smp_handler(struct bsg_job *job, struct Scsi_Host *shost, struct sas_rphy *rphy)

    transport portal for smp passthru

    :param job:
        ?
    :type job: struct bsg_job \*

    :param shost:
        shost object
    :type shost: struct Scsi_Host \*

    :param rphy:
        sas transport rphy object
    :type rphy: struct sas_rphy \*

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

