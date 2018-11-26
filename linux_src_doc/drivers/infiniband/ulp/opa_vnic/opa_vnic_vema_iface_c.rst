.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/ulp/opa_vnic/opa_vnic_vema_iface.c

.. _`opa_vnic_vema_report_event`:

opa_vnic_vema_report_event
==========================

.. c:function:: void opa_vnic_vema_report_event(struct opa_vnic_adapter *adapter, u8 event)

    sent trap to report the specified event

    :param adapter:
        vnic port adapter
    :type adapter: struct opa_vnic_adapter \*

    :param event:
        event to be reported
    :type event: u8

.. _`opa_vnic_vema_report_event.description`:

Description
-----------

This function calls vema api to sent a trap for the given event.

.. _`opa_vnic_get_summary_counters`:

opa_vnic_get_summary_counters
=============================

.. c:function:: void opa_vnic_get_summary_counters(struct opa_vnic_adapter *adapter, struct opa_veswport_summary_counters *cntrs)

    get summary counters

    :param adapter:
        vnic port adapter
    :type adapter: struct opa_vnic_adapter \*

    :param cntrs:
        pointer to destination summary counters structure
    :type cntrs: struct opa_veswport_summary_counters \*

.. _`opa_vnic_get_summary_counters.description`:

Description
-----------

This function populates the summary counters that is maintained by the
given adapter to destination address provided.

.. _`opa_vnic_get_error_counters`:

opa_vnic_get_error_counters
===========================

.. c:function:: void opa_vnic_get_error_counters(struct opa_vnic_adapter *adapter, struct opa_veswport_error_counters *cntrs)

    get error counters

    :param adapter:
        vnic port adapter
    :type adapter: struct opa_vnic_adapter \*

    :param cntrs:
        pointer to destination error counters structure
    :type cntrs: struct opa_veswport_error_counters \*

.. _`opa_vnic_get_error_counters.description`:

Description
-----------

This function populates the error counters that is maintained by the
given adapter to destination address provided.

.. _`opa_vnic_get_vesw_info`:

opa_vnic_get_vesw_info
======================

.. c:function:: void opa_vnic_get_vesw_info(struct opa_vnic_adapter *adapter, struct opa_vesw_info *info)

    - Get the vesw information

    :param adapter:
        vnic port adapter
    :type adapter: struct opa_vnic_adapter \*

    :param info:
        pointer to destination vesw info structure
    :type info: struct opa_vesw_info \*

.. _`opa_vnic_get_vesw_info.description`:

Description
-----------

This function copies the vesw info that is maintained by the
given adapter to destination address provided.

.. _`opa_vnic_set_vesw_info`:

opa_vnic_set_vesw_info
======================

.. c:function:: void opa_vnic_set_vesw_info(struct opa_vnic_adapter *adapter, struct opa_vesw_info *info)

    - Set the vesw information

    :param adapter:
        vnic port adapter
    :type adapter: struct opa_vnic_adapter \*

    :param info:
        pointer to vesw info structure
    :type info: struct opa_vesw_info \*

.. _`opa_vnic_set_vesw_info.description`:

Description
-----------

This function updates the vesw info that is maintained by the
given adapter with vesw info provided. Reserved fields are stored
and returned back to EM as is.

.. _`opa_vnic_get_per_veswport_info`:

opa_vnic_get_per_veswport_info
==============================

.. c:function:: void opa_vnic_get_per_veswport_info(struct opa_vnic_adapter *adapter, struct opa_per_veswport_info *info)

    - Get the vesw per port information

    :param adapter:
        vnic port adapter
    :type adapter: struct opa_vnic_adapter \*

    :param info:
        pointer to destination vport info structure
    :type info: struct opa_per_veswport_info \*

.. _`opa_vnic_get_per_veswport_info.description`:

Description
-----------

This function copies the vesw per port info that is maintained by the
given adapter to destination address provided.
Note that the read only fields are not copied.

.. _`opa_vnic_set_per_veswport_info`:

opa_vnic_set_per_veswport_info
==============================

.. c:function:: void opa_vnic_set_per_veswport_info(struct opa_vnic_adapter *adapter, struct opa_per_veswport_info *info)

    - Set vesw per port information

    :param adapter:
        vnic port adapter
    :type adapter: struct opa_vnic_adapter \*

    :param info:
        pointer to vport info structure
    :type info: struct opa_per_veswport_info \*

.. _`opa_vnic_set_per_veswport_info.description`:

Description
-----------

This function updates the vesw per port info that is maintained by the
given adapter with vesw per port info provided. Reserved fields are
stored and returned back to EM as is.

.. _`opa_vnic_query_mcast_macs`:

opa_vnic_query_mcast_macs
=========================

.. c:function:: void opa_vnic_query_mcast_macs(struct opa_vnic_adapter *adapter, struct opa_veswport_iface_macs *macs)

    query multicast mac list

    :param adapter:
        vnic port adapter
    :type adapter: struct opa_vnic_adapter \*

    :param macs:
        pointer mac list
    :type macs: struct opa_veswport_iface_macs \*

.. _`opa_vnic_query_mcast_macs.description`:

Description
-----------

This function populates the provided mac list with the configured
multicast addresses in the adapter.

.. _`opa_vnic_query_ucast_macs`:

opa_vnic_query_ucast_macs
=========================

.. c:function:: void opa_vnic_query_ucast_macs(struct opa_vnic_adapter *adapter, struct opa_veswport_iface_macs *macs)

    query unicast mac list

    :param adapter:
        vnic port adapter
    :type adapter: struct opa_vnic_adapter \*

    :param macs:
        pointer mac list
    :type macs: struct opa_veswport_iface_macs \*

.. _`opa_vnic_query_ucast_macs.description`:

Description
-----------

This function populates the provided mac list with the configured
unicast addresses in the adapter.

.. This file was automatic generated / don't edit.

