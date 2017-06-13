.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-drv.h

.. _`iwl_drv_start`:

iwl_drv_start
=============

.. c:function:: struct iwl_drv *iwl_drv_start(struct iwl_trans *trans)

    start the drv

    :param struct iwl_trans \*trans:
        *undescribed*

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

    :param struct iwl_drv \*drv:
        *undescribed*

.. _`iwl_drv_stop.description`:

Description
-----------

Stop the driver. This should be called by bus specific system flows
implementations. For example, the bus specific remove function should first
call this function and then do the bus related operations only.

.. This file was automatic generated / don't edit.

