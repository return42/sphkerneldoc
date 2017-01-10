.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/edac/edac_device.h

.. _`edac_device_add_device`:

edac_device_add_device
======================

.. c:function:: int edac_device_add_device(struct edac_device_ctl_info *edac_dev)

    Insert the 'edac_dev' structure into the edac_device global list and create sysfs entries associated with edac_device structure.

    :param struct edac_device_ctl_info \*edac_dev:
        pointer to edac_device structure to be added to the list
        'edac_device' structure.

.. _`edac_device_add_device.return`:

Return
------

     0 on Success, or an error code on failure

.. _`edac_device_del_device`:

edac_device_del_device
======================

.. c:function:: struct edac_device_ctl_info *edac_device_del_device(struct device *dev)

    Remove sysfs entries for specified edac_device structure and then remove edac_device structure from global list

    :param struct device \*dev:
        Pointer to struct \ :c:type:`struct device <device>`\  representing the edac device
        structure to remove.

.. _`edac_device_del_device.return`:

Return
------

     Pointer to removed edac_device structure,
     or \ ``NULL``\  if device not found.

.. _`edac_device_handle_ue`:

edac_device_handle_ue
=====================

.. c:function:: void edac_device_handle_ue(struct edac_device_ctl_info *edac_dev, int inst_nr, int block_nr, const char *msg)

    perform a common output and handling of an 'edac_dev' UE event

    :param struct edac_device_ctl_info \*edac_dev:
        pointer to struct \ :c:type:`struct edac_device_ctl_info <edac_device_ctl_info>`\ 

    :param int inst_nr:
        number of the instance where the UE error happened

    :param int block_nr:
        number of the block where the UE error happened

    :param const char \*msg:
        message to be printed

.. _`edac_device_handle_ce`:

edac_device_handle_ce
=====================

.. c:function:: void edac_device_handle_ce(struct edac_device_ctl_info *edac_dev, int inst_nr, int block_nr, const char *msg)

    perform a common output and handling of an 'edac_dev' CE event

    :param struct edac_device_ctl_info \*edac_dev:
        pointer to struct \ :c:type:`struct edac_device_ctl_info <edac_device_ctl_info>`\ 

    :param int inst_nr:
        number of the instance where the CE error happened

    :param int block_nr:
        number of the block where the CE error happened

    :param const char \*msg:
        message to be printed

.. _`edac_device_alloc_index`:

edac_device_alloc_index
=======================

.. c:function:: int edac_device_alloc_index( void)

    Allocate a unique device index number

    :param  void:
        no arguments

.. _`edac_device_alloc_index.return`:

Return
------

     allocated index number

.. This file was automatic generated / don't edit.

