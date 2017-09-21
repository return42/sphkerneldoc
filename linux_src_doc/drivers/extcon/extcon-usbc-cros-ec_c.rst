.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/extcon/extcon-usbc-cros-ec.c

.. _`cros_ec_pd_command`:

cros_ec_pd_command
==================

.. c:function:: int cros_ec_pd_command(struct cros_ec_extcon_info *info, unsigned int command, unsigned int version, void *outdata, unsigned int outsize, void *indata, unsigned int insize)

    Send a command to the EC.

    :param struct cros_ec_extcon_info \*info:
        pointer to struct cros_ec_extcon_info

    :param unsigned int command:
        EC command

    :param unsigned int version:
        EC command version

    :param void \*outdata:
        EC command output data

    :param unsigned int outsize:
        Size of outdata

    :param void \*indata:
        EC command input data

    :param unsigned int insize:
        Size of indata

.. _`cros_ec_pd_command.return`:

Return
------

0 on success, <0 on failure.

.. _`cros_ec_usb_get_power_type`:

cros_ec_usb_get_power_type
==========================

.. c:function:: int cros_ec_usb_get_power_type(struct cros_ec_extcon_info *info)

    Get power type info about PD device attached to given port.

    :param struct cros_ec_extcon_info \*info:
        pointer to struct cros_ec_extcon_info

.. _`cros_ec_usb_get_power_type.return`:

Return
------

power type on success, <0 on failure.

.. _`cros_ec_usb_get_pd_mux_state`:

cros_ec_usb_get_pd_mux_state
============================

.. c:function:: int cros_ec_usb_get_pd_mux_state(struct cros_ec_extcon_info *info)

    Get PD mux state for given port.

    :param struct cros_ec_extcon_info \*info:
        pointer to struct cros_ec_extcon_info

.. _`cros_ec_usb_get_pd_mux_state.return`:

Return
------

PD mux state on success, <0 on failure.

.. _`cros_ec_usb_get_role`:

cros_ec_usb_get_role
====================

.. c:function:: int cros_ec_usb_get_role(struct cros_ec_extcon_info *info, bool *polarity)

    Get role info about possible PD device attached to a given port.

    :param struct cros_ec_extcon_info \*info:
        pointer to struct cros_ec_extcon_info

    :param bool \*polarity:
        pointer to cable polarity (return value)

.. _`cros_ec_usb_get_role.return`:

Return
------

role info on success, -ENOTCONN if no cable is connected, <0 on
failure.

.. _`cros_ec_pd_get_num_ports`:

cros_ec_pd_get_num_ports
========================

.. c:function:: int cros_ec_pd_get_num_ports(struct cros_ec_extcon_info *info)

    Get number of EC charge ports.

    :param struct cros_ec_extcon_info \*info:
        pointer to struct cros_ec_extcon_info

.. _`cros_ec_pd_get_num_ports.return`:

Return
------

number of ports on success, <0 on failure.

.. This file was automatic generated / don't edit.

