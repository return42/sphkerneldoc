.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinconf.c

.. _`pinconf_dbg_config_print`:

pinconf_dbg_config_print
========================

.. c:function:: int pinconf_dbg_config_print(struct seq_file *s, void *d)

    display the pinctrl config from the pinctrl map, of the dev/pin/state that was last written to pinconf-config file.

    :param s:
        string filled in  with config description
    :type s: struct seq_file \*

    :param d:
        not used
    :type d: void \*

.. _`pinconf_dbg_config_write`:

pinconf_dbg_config_write
========================

.. c:function:: ssize_t pinconf_dbg_config_write(struct file *file, const char __user *user_buf, size_t count, loff_t *ppos)

    modify the pinctrl config in the pinctrl map, of a dev/pin/state entry based on user entries to pinconf-config

    :param file:
        *undescribed*
    :type file: struct file \*

    :param user_buf:
        contains the modification request with expected format:
        modify <config> <devicename> <state> <name> <newvalue>
        modify is literal string, alternatives like add/delete not supported yet
        <config> is the configuration to be changed. Supported configs are
        "config_pin" or "config_group", alternatives like config_mux are not
        supported yet.
        <devicename> <state> <name> are values that should match the pinctrl-maps
        <newvalue> reflects the new config and is driver dependent
    :type user_buf: const char __user \*

    :param count:
        *undescribed*
    :type count: size_t

    :param ppos:
        *undescribed*
    :type ppos: loff_t \*

.. This file was automatic generated / don't edit.

