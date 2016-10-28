.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/voltage.c

.. _`voltdm_get_voltage`:

voltdm_get_voltage
==================

.. c:function:: unsigned long voltdm_get_voltage(struct voltagedomain *voltdm)

    Gets the current non-auto-compensated voltage

    :param struct voltagedomain \*voltdm:
        pointer to the voltdm for which current voltage info is needed

.. _`voltdm_get_voltage.description`:

Description
-----------

API to get the current non-auto-compensated voltage for a voltage domain.
Returns 0 in case of error else returns the current voltage.

.. _`voltdm_scale`:

voltdm_scale
============

.. c:function:: int voltdm_scale(struct voltagedomain *voltdm, unsigned long target_volt)

    API to scale voltage of a particular voltage domain.

    :param struct voltagedomain \*voltdm:
        pointer to the voltage domain which is to be scaled.

    :param unsigned long target_volt:
        The target voltage of the voltage domain

.. _`voltdm_scale.description`:

Description
-----------

This API should be called by the kernel to do the voltage scaling
for a particular voltage domain during DVFS.

.. _`voltdm_reset`:

voltdm_reset
============

.. c:function:: void voltdm_reset(struct voltagedomain *voltdm)

    Resets the voltage of a particular voltage domain to that of the current OPP.

    :param struct voltagedomain \*voltdm:
        pointer to the voltage domain whose voltage is to be reset.

.. _`voltdm_reset.description`:

Description
-----------

This API finds out the correct voltage the voltage domain is supposed
to be at and resets the voltage to that level. Should be used especially
while disabling any voltage compensation modules.

.. _`omap_voltage_get_volttable`:

omap_voltage_get_volttable
==========================

.. c:function:: void omap_voltage_get_volttable(struct voltagedomain *voltdm, struct omap_volt_data **volt_data)

    API to get the voltage table associated with a particular voltage domain.

    :param struct voltagedomain \*voltdm:
        pointer to the VDD for which the voltage table is required

    :param struct omap_volt_data \*\*volt_data:
        the voltage table for the particular vdd which is to be
        populated by this API

.. _`omap_voltage_get_volttable.description`:

Description
-----------

This API populates the voltage table associated with a VDD into the
passed parameter pointer. Returns the count of distinct voltages
supported by this vdd.

.. _`omap_voltage_get_voltdata`:

omap_voltage_get_voltdata
=========================

.. c:function:: struct omap_volt_data *omap_voltage_get_voltdata(struct voltagedomain *voltdm, unsigned long volt)

    API to get the voltage table entry for a particular voltage

    :param struct voltagedomain \*voltdm:
        pointer to the VDD whose voltage table has to be searched

    :param unsigned long volt:
        the voltage to be searched in the voltage table

.. _`omap_voltage_get_voltdata.description`:

Description
-----------

This API searches through the voltage table for the required voltage
domain and tries to find a matching entry for the passed voltage volt.
If a matching entry is found volt_data is populated with that entry.
This API searches only through the non-compensated voltages int the
voltage table.
Returns pointer to the voltage table entry corresponding to volt on
success. Returns -ENODATA if no voltage table exisits for the passed voltage
domain or if there is no matching entry.

.. _`omap_voltage_register_pmic`:

omap_voltage_register_pmic
==========================

.. c:function:: int omap_voltage_register_pmic(struct voltagedomain *voltdm, struct omap_voltdm_pmic *pmic)

    API to register PMIC specific data

    :param struct voltagedomain \*voltdm:
        pointer to the VDD for which the PMIC specific data is
        to be registered

    :param struct omap_voltdm_pmic \*pmic:
        the structure containing pmic info

.. _`omap_voltage_register_pmic.description`:

Description
-----------

This API is to be called by the SOC/PMIC file to specify the
pmic specific info as present in omap_voltdm_pmic structure.

.. _`omap_voltage_late_init`:

omap_voltage_late_init
======================

.. c:function:: int omap_voltage_late_init( void)

    Init the various voltage parameters

    :param  void:
        no arguments

.. _`omap_voltage_late_init.description`:

Description
-----------

This API is to be called in the later stages of the
system boot to init the voltage controller and
voltage processors.

.. _`voltdm_lookup`:

voltdm_lookup
=============

.. c:function:: struct voltagedomain *voltdm_lookup(const char *name)

    look up a voltagedomain by name, return a pointer

    :param const char \*name:
        name of voltagedomain

.. _`voltdm_lookup.description`:

Description
-----------

Find a registered voltagedomain by its name \ ``name``\ .  Returns a pointer
to the struct voltagedomain if found, or NULL otherwise.

.. _`voltdm_init`:

voltdm_init
===========

.. c:function:: void voltdm_init(struct voltagedomain **voltdms)

    set up the voltagedomain layer

    :param struct voltagedomain \*\*voltdms:
        *undescribed*

.. _`voltdm_init.description`:

Description
-----------

Loop through the array of voltagedomains \ ``voltdm_list``\ , registering all
that are available on the current CPU. If voltdm_list is supplied
and not null, all of the referenced voltagedomains will be
registered.  No return value.

.. This file was automatic generated / don't edit.

