.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinconf.c

.. _`pinconf_dbg_config_print`:

pinconf_dbg_config_print
========================

.. c:function:: int pinconf_dbg_config_print(struct seq_file *s, void *d)

    display the pinctrl config from the pinctrl map, of the dev/pin/state that was last written to pinconf-config file.

    :param struct seq_file \*s:
        string filled in  with config description

    :param void \*d:
        not used

.. _`pinconf_dbg_config_write`:

pinconf_dbg_config_write
========================

.. c:function:: ssize_t pinconf_dbg_config_write(struct file *file, const char __user *user_buf, size_t count, loff_t *ppos)

    modify the pinctrl config in the pinctrl map, of a dev/pin/state entry based on user entries to pinconf-config

    :param struct file \*file:
        *undescribed*

    :param const char __user \*user_buf:
        contains the modification request with expected format:
        modify <config> <devicename> <state> <name> <newvalue>
        modify is literal string, alternatives like add/delete not supported yet
        <config> is the configuration to be changed. Supported configs are
        "config_pin" or "config_group", alternatives like config_mux are not
        supported yet.
        <devicename> <state> <name> are values that should match the pinctrl-maps
        <newvalue> reflects the new config and is driver dependant

    :param size_t count:
        *undescribed*

    :param loff_t \*ppos:
        *undescribed*

.. This file was automatic generated / don't edit.

