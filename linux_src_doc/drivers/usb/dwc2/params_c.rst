.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc2/params.c

.. _`dwc2_set_param`:

dwc2_set_param
==============

.. c:function:: void dwc2_set_param(struct dwc2_hsotg *hsotg, void *param, bool lookup, char *property, u64 legacy, u64 def, u64 min, u64 max, u8 size)

    Set a core parameter

    :param struct dwc2_hsotg \*hsotg:
        Programming view of the DWC_otg controller

    :param void \*param:
        Pointer to the parameter to set

    :param bool lookup:
        True if the property should be looked up

    :param char \*property:
        The device property to read

    :param u64 legacy:
        The param value to set if \ ``property``\  is not available. This
        will typically be the legacy value set in the static
        params structure.

    :param u64 def:
        The default value

    :param u64 min:
        The minimum value

    :param u64 max:
        The maximum value

    :param u8 size:
        The size of the core parameter in bytes, or 0 for bool.

.. _`dwc2_set_param.description`:

Description
-----------

This function looks up \ ``property``\  and sets the \ ``param``\  to that value.
If the property doesn't exist it uses the passed-in \ ``value``\ . It will
verify that the value falls between \ ``min``\  and \ ``max``\ . If it doesn't,
it will output an error and set the parameter to either \ ``def``\  or,
failing that, to \ ``min``\ .

The \ ``size``\  is used to write to \ ``param``\  and to query the device
properties so that this same function can be used with different
types of parameters.

.. _`dwc2_set_param_u16`:

dwc2_set_param_u16
==================

.. c:function:: void dwc2_set_param_u16(struct dwc2_hsotg *hsotg, u16 *param, bool lookup, char *property, u16 legacy, u16 def, u16 min, u16 max)

    Set a u16 parameter

    :param struct dwc2_hsotg \*hsotg:
        *undescribed*

    :param u16 \*param:
        *undescribed*

    :param bool lookup:
        *undescribed*

    :param char \*property:
        *undescribed*

    :param u16 legacy:
        *undescribed*

    :param u16 def:
        *undescribed*

    :param u16 min:
        *undescribed*

    :param u16 max:
        *undescribed*

.. _`dwc2_set_param_u16.description`:

Description
-----------

See \ :c:func:`dwc2_set_param`\ .

.. _`dwc2_set_param_bool`:

dwc2_set_param_bool
===================

.. c:function:: void dwc2_set_param_bool(struct dwc2_hsotg *hsotg, bool *param, bool lookup, char *property, bool def, bool min, bool max)

    Set a bool parameter

    :param struct dwc2_hsotg \*hsotg:
        *undescribed*

    :param bool \*param:
        *undescribed*

    :param bool lookup:
        *undescribed*

    :param char \*property:
        *undescribed*

    :param bool def:
        *undescribed*

    :param bool min:
        *undescribed*

    :param bool max:
        *undescribed*

.. _`dwc2_set_param_bool.description`:

Description
-----------

See \ :c:func:`dwc2_set_param`\ .

.. _`dwc2_set_param_bool.note`:

Note
----

there is no 'legacy' argument here because there is no legacy
source of bool params.

.. _`dwc2_set_parameters`:

dwc2_set_parameters
===================

.. c:function:: void dwc2_set_parameters(struct dwc2_hsotg *hsotg, const struct dwc2_core_params *params)

    Set all core parameters.

    :param struct dwc2_hsotg \*hsotg:
        Programming view of the DWC_otg controller

    :param const struct dwc2_core_params \*params:
        The parameters to set

.. _`dwc2_get_hwparams`:

dwc2_get_hwparams
=================

.. c:function:: int dwc2_get_hwparams(struct dwc2_hsotg *hsotg)

    registers and interpret the contents.

    :param struct dwc2_hsotg \*hsotg:
        *undescribed*

.. This file was automatic generated / don't edit.

