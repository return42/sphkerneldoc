.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/power/avs/smartreflex.c

.. _`sr_configure_errgen`:

sr_configure_errgen
===================

.. c:function:: int sr_configure_errgen(struct omap_sr *sr)

    Configures the SmartReflex to perform AVS using the error generator module.

    :param struct omap_sr \*sr:
        SR module to be configured.

.. _`sr_configure_errgen.description`:

Description
-----------

This API is to be called from the smartreflex class driver to
configure the error generator module inside the smartreflex module.
SR settings if using the ERROR module inside Smartreflex.
SR CLASS 3 by default uses only the ERROR module where as
SR CLASS 2 can choose between ERROR module and MINMAXAVG
module. Returns 0 on success and error value in case of failure.

.. _`sr_disable_errgen`:

sr_disable_errgen
=================

.. c:function:: int sr_disable_errgen(struct omap_sr *sr)

    Disables SmartReflex AVS module's errgen component

    :param struct omap_sr \*sr:
        SR module to be configured.

.. _`sr_disable_errgen.description`:

Description
-----------

This API is to be called from the smartreflex class driver to
disable the error generator module inside the smartreflex module.

Returns 0 on success and error value in case of failure.

.. _`sr_configure_minmax`:

sr_configure_minmax
===================

.. c:function:: int sr_configure_minmax(struct omap_sr *sr)

    Configures the SmartReflex to perform AVS using the minmaxavg module.

    :param struct omap_sr \*sr:
        SR module to be configured.

.. _`sr_configure_minmax.description`:

Description
-----------

This API is to be called from the smartreflex class driver to
configure the minmaxavg module inside the smartreflex module.
SR settings if using the ERROR module inside Smartreflex.
SR CLASS 3 by default uses only the ERROR module where as
SR CLASS 2 can choose between ERROR module and MINMAXAVG
module. Returns 0 on success and error value in case of failure.

.. _`sr_enable`:

sr_enable
=========

.. c:function:: int sr_enable(struct omap_sr *sr, unsigned long volt)

    Enables the smartreflex module.

    :param struct omap_sr \*sr:
        pointer to which the SR module to be configured belongs to.

    :param unsigned long volt:
        The voltage at which the Voltage domain associated with
        the smartreflex module is operating at.
        This is required only to program the correct Ntarget value.

.. _`sr_enable.description`:

Description
-----------

This API is to be called from the smartreflex class driver to
enable a smartreflex module. Returns 0 on success. Returns error
value if the voltage passed is wrong or if ntarget value is wrong.

.. _`sr_disable`:

sr_disable
==========

.. c:function:: void sr_disable(struct omap_sr *sr)

    Disables the smartreflex module.

    :param struct omap_sr \*sr:
        pointer to which the SR module to be configured belongs to.

.. _`sr_disable.description`:

Description
-----------

This API is to be called from the smartreflex class driver to
disable a smartreflex module.

.. _`sr_register_class`:

sr_register_class
=================

.. c:function:: int sr_register_class(struct omap_sr_class_data *class_data)

    API to register a smartreflex class parameters.

    :param struct omap_sr_class_data \*class_data:
        The structure containing various sr class specific data.

.. _`sr_register_class.description`:

Description
-----------

This API is to be called by the smartreflex class driver to register itself
with the smartreflex driver during init. Returns 0 on success else the
error value.

.. _`omap_sr_enable`:

omap_sr_enable
==============

.. c:function:: void omap_sr_enable(struct voltagedomain *voltdm)

    API to enable SR clocks and to call into the registered smartreflex class enable API.

    :param struct voltagedomain \*voltdm:
        VDD pointer to which the SR module to be configured belongs to.

.. _`omap_sr_enable.description`:

Description
-----------

This API is to be called from the kernel in order to enable
a particular smartreflex module. This API will do the initial
configurations to turn on the smartreflex module and in turn call
into the registered smartreflex class enable API.

.. _`omap_sr_disable`:

omap_sr_disable
===============

.. c:function:: void omap_sr_disable(struct voltagedomain *voltdm)

    API to disable SR without resetting the voltage processor voltage

    :param struct voltagedomain \*voltdm:
        VDD pointer to which the SR module to be configured belongs to.

.. _`omap_sr_disable.description`:

Description
-----------

This API is to be called from the kernel in order to disable
a particular smartreflex module. This API will in turn call
into the registered smartreflex class disable API. This API will tell
the smartreflex class disable not to reset the VP voltage after
disabling smartreflex.

.. _`omap_sr_disable_reset_volt`:

omap_sr_disable_reset_volt
==========================

.. c:function:: void omap_sr_disable_reset_volt(struct voltagedomain *voltdm)

    API to disable SR and reset the voltage processor voltage

    :param struct voltagedomain \*voltdm:
        VDD pointer to which the SR module to be configured belongs to.

.. _`omap_sr_disable_reset_volt.description`:

Description
-----------

This API is to be called from the kernel in order to disable
a particular smartreflex module. This API will in turn call
into the registered smartreflex class disable API. This API will tell
the smartreflex class disable to reset the VP voltage after
disabling smartreflex.

.. _`omap_sr_register_pmic`:

omap_sr_register_pmic
=====================

.. c:function:: void omap_sr_register_pmic(struct omap_sr_pmic_data *pmic_data)

    API to register pmic specific info.

    :param struct omap_sr_pmic_data \*pmic_data:
        The structure containing pmic specific data.

.. _`omap_sr_register_pmic.description`:

Description
-----------

This API is to be called from the PMIC specific code to register with
smartreflex driver pmic specific info. Currently the only info required
is the smartreflex init on the PMIC side.

.. This file was automatic generated / don't edit.

