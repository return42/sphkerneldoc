.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pinctrl/pinconf.h

.. _`pinconf_ops`:

struct pinconf_ops
==================

.. c:type:: struct pinconf_ops

    pin config operations, to be implemented by pin configuration capable drivers.

.. _`pinconf_ops.definition`:

Definition
----------

.. code-block:: c

    struct pinconf_ops {
    #ifdef CONFIG_GENERIC_PINCONF
        bool is_generic;
    #endif
        int (*pin_config_get) (struct pinctrl_dev *pctldev,unsigned pin, unsigned long *config);
        int (*pin_config_set) (struct pinctrl_dev *pctldev,unsigned pin,unsigned long *configs, unsigned num_configs);
        int (*pin_config_group_get) (struct pinctrl_dev *pctldev,unsigned selector, unsigned long *config);
        int (*pin_config_group_set) (struct pinctrl_dev *pctldev,unsigned selector,unsigned long *configs, unsigned num_configs);
        int (*pin_config_dbg_parse_modify) (struct pinctrl_dev *pctldev,const char *arg, unsigned long *config);
        void (*pin_config_dbg_show) (struct pinctrl_dev *pctldev,struct seq_file *s, unsigned offset);
        void (*pin_config_group_dbg_show) (struct pinctrl_dev *pctldev,struct seq_file *s, unsigned selector);
        void (*pin_config_config_dbg_show) (struct pinctrl_dev *pctldev,struct seq_file *s, unsigned long config);
    }

.. _`pinconf_ops.members`:

Members
-------

is_generic
    for pin controllers that want to use the generic interface,
    this flag tells the framework that it's generic.

pin_config_get
    get the config of a certain pin, if the requested config
    is not available on this controller this should return -ENOTSUPP
    and if it is available but disabled it should return -EINVAL

pin_config_set
    configure an individual pin

pin_config_group_get
    get configurations for an entire pin group

pin_config_group_set
    configure all pins in a group

pin_config_dbg_parse_modify
    optional debugfs to modify a pin configuration

pin_config_dbg_show
    optional debugfs display hook that will provide
    per-device info for a certain pin in debugfs

pin_config_group_dbg_show
    optional debugfs display hook that will provide
    per-device info for a certain group in debugfs

pin_config_config_dbg_show
    optional debugfs display hook that will decode
    and display a driver's pin configuration parameter

.. This file was automatic generated / don't edit.

