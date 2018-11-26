.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/power/reset/reboot-mode.c

.. _`reboot_mode_register`:

reboot_mode_register
====================

.. c:function:: int reboot_mode_register(struct reboot_mode_driver *reboot)

    register a reboot mode driver

    :param reboot:
        reboot mode driver
    :type reboot: struct reboot_mode_driver \*

.. _`reboot_mode_register.return`:

Return
------

0 on success or a negative error code on failure.

.. _`reboot_mode_unregister`:

reboot_mode_unregister
======================

.. c:function:: int reboot_mode_unregister(struct reboot_mode_driver *reboot)

    unregister a reboot mode driver

    :param reboot:
        reboot mode driver
    :type reboot: struct reboot_mode_driver \*

.. _`devm_reboot_mode_register`:

devm_reboot_mode_register
=========================

.. c:function:: int devm_reboot_mode_register(struct device *dev, struct reboot_mode_driver *reboot)

    resource managed \ :c:func:`reboot_mode_register`\ 

    :param dev:
        device to associate this resource with
    :type dev: struct device \*

    :param reboot:
        reboot mode driver
    :type reboot: struct reboot_mode_driver \*

.. _`devm_reboot_mode_register.return`:

Return
------

0 on success or a negative error code on failure.

.. _`devm_reboot_mode_unregister`:

devm_reboot_mode_unregister
===========================

.. c:function:: void devm_reboot_mode_unregister(struct device *dev, struct reboot_mode_driver *reboot)

    resource managed \ :c:func:`reboot_mode_unregister`\ 

    :param dev:
        device to associate this resource with
    :type dev: struct device \*

    :param reboot:
        reboot mode driver
    :type reboot: struct reboot_mode_driver \*

.. This file was automatic generated / don't edit.

