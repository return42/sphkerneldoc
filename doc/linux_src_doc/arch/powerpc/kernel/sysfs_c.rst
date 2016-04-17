.. -*- coding: utf-8; mode: rst -*-

=======
sysfs.c
=======


.. _`read_dscr`:

read_dscr
=========

.. c:function:: void read_dscr (void *val)

    Fetch the cpu specific DSCR default

    :param void \*val:
        Returned cpu specific DSCR default value



.. _`read_dscr.description`:

Description
-----------

This function returns the per cpu DSCR default value
for any cpu which is contained in it's PACA structure.



.. _`write_dscr`:

write_dscr
==========

.. c:function:: void write_dscr (void *val)

    Update the cpu specific DSCR default

    :param void \*val:
        New cpu specific DSCR default value to update



.. _`write_dscr.description`:

Description
-----------

This function updates the per cpu DSCR default value
for any cpu which is contained in it's PACA structure.



.. _`show_dscr_default`:

show_dscr_default
=================

.. c:function:: ssize_t show_dscr_default (struct device *dev, struct device_attribute *attr, char *buf)

    Fetch the system wide DSCR default

    :param struct device \*dev:
        Device structure

    :param struct device_attribute \*attr:
        Device attribute structure

    :param char \*buf:
        Interface buffer



.. _`show_dscr_default.description`:

Description
-----------

This function returns the system wide DSCR default value.



.. _`store_dscr_default`:

store_dscr_default
==================

.. c:function:: ssize_t __used store_dscr_default (struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Update the system wide DSCR default

    :param struct device \*dev:
        Device structure

    :param struct device_attribute \*attr:
        Device attribute structure

    :param const char \*buf:
        Interface buffer

    :param size_t count:
        Size of the update



.. _`store_dscr_default.description`:

Description
-----------

This function updates the system wide DSCR default value.

