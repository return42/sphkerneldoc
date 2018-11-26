.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc2/params.c

.. _`dwc2_set_default_params`:

dwc2_set_default_params
=======================

.. c:function:: void dwc2_set_default_params(struct dwc2_hsotg *hsotg)

    Set all core parameters to their auto-detected default values.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_get_device_properties`:

dwc2_get_device_properties
==========================

.. c:function:: void dwc2_get_device_properties(struct dwc2_hsotg *hsotg)

    Read in device properties.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_get_device_properties.description`:

Description
-----------

Read in the device properties and adjust core parameters if needed.

.. _`dwc2_get_hwparams`:

dwc2_get_hwparams
=================

.. c:function:: int dwc2_get_hwparams(struct dwc2_hsotg *hsotg)

    registers and interpret the contents.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. This file was automatic generated / don't edit.

