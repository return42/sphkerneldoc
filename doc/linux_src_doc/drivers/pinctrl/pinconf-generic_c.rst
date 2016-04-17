.. -*- coding: utf-8; mode: rst -*-

=================
pinconf-generic.c
=================


.. _`pinconf_generic_dump_pins`:

pinconf_generic_dump_pins
=========================

.. c:function:: void pinconf_generic_dump_pins (struct pinctrl_dev *pctldev, struct seq_file *s, const char *gname, unsigned pin)

    Print information about pin or group of pins

    :param struct pinctrl_dev \*pctldev:
        Pincontrol device

    :param struct seq_file \*s:
        File to print to

    :param const char \*gname:
        Group name specifying pins

    :param unsigned pin:
        Pin number specyfying pin



.. _`pinconf_generic_dump_pins.description`:

Description
-----------

Print the pinconf configuration for the requested pin(s) to ``s``\ . Pins can be
specified either by pin using ``pin`` or by group using ``gname``\ . Only one needs
to be specified the other can be NULL/0.



.. _`parse_dt_cfg`:

parse_dt_cfg
============

.. c:function:: void parse_dt_cfg (struct device_node *np, const struct pinconf_generic_params *params, unsigned int count, unsigned long *cfg, unsigned int *ncfg)

    Parse DT pinconf parameters

    :param struct device_node \*np:
        DT node

    :param const struct pinconf_generic_params \*params:
        Array of describing generic parameters

    :param unsigned int count:
        Number of entries in ``params``

    :param unsigned long \*cfg:
        Array of parsed config options

    :param unsigned int \*ncfg:
        Number of entries in ``cfg``



.. _`parse_dt_cfg.description`:

Description
-----------

Parse the config options described in ``params`` from ``np`` and puts the result
in ``cfg``\ . ``cfg`` does not need to be empty, entries are added beggining at
``ncfg``\ . ``ncfg`` is updated to reflect the number of entries after parsing. ``cfg``
needs to have enough memory allocated to hold all possible entries.



.. _`pinconf_generic_parse_dt_config`:

pinconf_generic_parse_dt_config
===============================

.. c:function:: int pinconf_generic_parse_dt_config (struct device_node *np, struct pinctrl_dev *pctldev, unsigned long **configs, unsigned int *nconfigs)

    :param struct device_node \*np:
        node containing the pinconfig properties

    :param struct pinctrl_dev \*pctldev:

        *undescribed*

    :param unsigned long \*\*configs:
        array with nconfigs entries containing the generic pinconf values
        must be freed when no longer necessary.

    :param unsigned int \*nconfigs:
        umber of configurations



.. _`pinconf_generic_parse_dt_config.description`:

Description
-----------

parse the config properties into generic pinconfig values.

