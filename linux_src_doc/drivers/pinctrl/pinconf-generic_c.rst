.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinconf-generic.c

.. _`pinconf_generic_dump_pins`:

pinconf_generic_dump_pins
=========================

.. c:function:: void pinconf_generic_dump_pins(struct pinctrl_dev *pctldev, struct seq_file *s, const char *gname, unsigned pin)

    Print information about pin or group of pins

    :param pctldev:
        Pincontrol device
    :type pctldev: struct pinctrl_dev \*

    :param s:
        File to print to
    :type s: struct seq_file \*

    :param gname:
        Group name specifying pins
    :type gname: const char \*

    :param pin:
        Pin number specyfying pin
    :type pin: unsigned

.. _`pinconf_generic_dump_pins.description`:

Description
-----------

Print the pinconf configuration for the requested pin(s) to \ ``s``\ . Pins can be
specified either by pin using \ ``pin``\  or by group using \ ``gname``\ . Only one needs
to be specified the other can be NULL/0.

.. _`parse_dt_cfg`:

parse_dt_cfg
============

.. c:function:: void parse_dt_cfg(struct device_node *np, const struct pinconf_generic_params *params, unsigned int count, unsigned long *cfg, unsigned int *ncfg)

    Parse DT pinconf parameters

    :param np:
        DT node
    :type np: struct device_node \*

    :param params:
        Array of describing generic parameters
    :type params: const struct pinconf_generic_params \*

    :param count:
        Number of entries in \ ``params``\ 
    :type count: unsigned int

    :param cfg:
        Array of parsed config options
    :type cfg: unsigned long \*

    :param ncfg:
        Number of entries in \ ``cfg``\ 
    :type ncfg: unsigned int \*

.. _`parse_dt_cfg.description`:

Description
-----------

Parse the config options described in \ ``params``\  from \ ``np``\  and puts the result
in \ ``cfg``\ . \ ``cfg``\  does not need to be empty, entries are added beginning at
\ ``ncfg``\ . \ ``ncfg``\  is updated to reflect the number of entries after parsing. \ ``cfg``\ 
needs to have enough memory allocated to hold all possible entries.

.. _`pinconf_generic_parse_dt_config`:

pinconf_generic_parse_dt_config
===============================

.. c:function:: int pinconf_generic_parse_dt_config(struct device_node *np, struct pinctrl_dev *pctldev, unsigned long **configs, unsigned int *nconfigs)

    parse the config properties into generic pinconfig values.

    :param np:
        node containing the pinconfig properties
    :type np: struct device_node \*

    :param pctldev:
        *undescribed*
    :type pctldev: struct pinctrl_dev \*

    :param configs:
        array with nconfigs entries containing the generic pinconf values
        must be freed when no longer necessary.
    :type configs: unsigned long \*\*

    :param nconfigs:
        umber of configurations
    :type nconfigs: unsigned int \*

.. This file was automatic generated / don't edit.

