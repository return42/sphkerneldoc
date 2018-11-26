.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/sysfs.c

.. _`read_dscr`:

read_dscr
=========

.. c:function:: void read_dscr(void *val)

    Fetch the cpu specific DSCR default

    :param val:
        Returned cpu specific DSCR default value
    :type val: void \*

.. _`read_dscr.description`:

Description
-----------

This function returns the per cpu DSCR default value
for any cpu which is contained in it's PACA structure.

.. _`write_dscr`:

write_dscr
==========

.. c:function:: void write_dscr(void *val)

    Update the cpu specific DSCR default

    :param val:
        New cpu specific DSCR default value to update
    :type val: void \*

.. _`write_dscr.description`:

Description
-----------

This function updates the per cpu DSCR default value
for any cpu which is contained in it's PACA structure.

.. _`show_dscr_default`:

show_dscr_default
=================

.. c:function:: ssize_t show_dscr_default(struct device *dev, struct device_attribute *attr, char *buf)

    Fetch the system wide DSCR default

    :param dev:
        Device structure
    :type dev: struct device \*

    :param attr:
        Device attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        Interface buffer
    :type buf: char \*

.. _`show_dscr_default.description`:

Description
-----------

This function returns the system wide DSCR default value.

.. _`store_dscr_default`:

store_dscr_default
==================

.. c:function:: ssize_t __used store_dscr_default(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Update the system wide DSCR default

    :param dev:
        Device structure
    :type dev: struct device \*

    :param attr:
        Device attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        Interface buffer
    :type buf: const char \*

    :param count:
        Size of the update
    :type count: size_t

.. _`store_dscr_default.description`:

Description
-----------

This function updates the system wide DSCR default value.

.. This file was automatic generated / don't edit.

