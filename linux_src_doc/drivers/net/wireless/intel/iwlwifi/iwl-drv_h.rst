.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-drv.h

.. _`driver-system-flows---drv-component`:

Driver system flows - drv component
===================================

This component implements the system flows such as bus enumeration, bus
removal. Bus dependent parts of system flows (such as iwl_pci_probe) are in
bus specific files (transport files). This is the code that is common among
different buses.

This component is also in charge of managing the several implementations of
the wifi flows: it will allow to have several fw API implementation. These
different implementations will differ in the way they implement mac80211's
handlers too.
The init flow wrt to the drv component looks like this:
1) The bus specific component is called from module_init
2) The bus specific component registers the bus driver
3) The bus driver calls the probe function
4) The bus specific component configures the bus
5) The bus specific component calls to the drv bus agnostic part
(iwl_drv_start)
6) iwl_drv_start fetches the fw ASYNC, iwl_req_fw_callback
7) iwl_req_fw_callback parses the fw file
8) iwl_req_fw_callback starts the wifi implementation to matches the fw

.. _`iwl_drv_start`:

iwl_drv_start
=============

.. c:function:: struct iwl_drv *iwl_drv_start(struct iwl_trans *trans)

    start the drv

    :param trans:
        *undescribed*
    :type trans: struct iwl_trans \*

.. _`iwl_drv_start.starts-the-driver`:

starts the driver
-----------------

fetches the firmware. This should be called by bus
specific system flows implementations. For example, the bus specific probe
function should do bus related operations only, and then call to this
function. It returns the driver object or \ ``NULL``\  if an error occurred.

.. _`iwl_drv_stop`:

iwl_drv_stop
============

.. c:function:: void iwl_drv_stop(struct iwl_drv *drv)

    stop the drv

    :param drv:
        *undescribed*
    :type drv: struct iwl_drv \*

.. _`iwl_drv_stop.description`:

Description
-----------

Stop the driver. This should be called by bus specific system flows
implementations. For example, the bus specific remove function should first
call this function and then do the bus related operations only.

.. This file was automatic generated / don't edit.

