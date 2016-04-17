.. -*- coding: utf-8; mode: rst -*-

========
uinput.h
========


.. _`ui_dev_setup`:

UI_DEV_SETUP
============

.. c:function:: UI_DEV_SETUP ()

    Set device parameters for setup



.. _`ui_dev_setup.description`:

Description
-----------


This ioctl sets parameters for the input device to be created.  It
supersedes the old "struct uinput_user_dev" method, which wrote this data
via :c:func:`write`. To actually set the absolute axes UI_ABS_SETUP should be
used.

The ioctl takes a "struct uinput_setup" object as argument. The fields of



.. _`ui_dev_setup.id`:

id
--

See the description of "struct input_id". This field is
copied unchanged into the new device.



.. _`ui_dev_setup.name`:

name
----

This is used unchanged as name for the new device.



.. _`ui_dev_setup.ff_effects_max`:

ff_effects_max
--------------

This limits the maximum numbers of force-feedback effects.
See below for a description of FF with uinput.

This ioctl can be called multiple times and will overwrite previous values.
If this ioctl fails with -EINVAL, it is recommended to use the old
"uinput_user_dev" method via :c:func:`write` as a fallback, in case you run on an
old kernel that does not support this ioctl.

This ioctl may fail with -EINVAL if it is not supported or if you passed
incorrect values, -ENOMEM if the kernel runs out of memory or -EFAULT if the
passed uinput_setup object cannot be read/written.
If this call fails, partial data may have already been applied to the
internal device.



.. _`ui_abs_setup`:

UI_ABS_SETUP
============

.. c:function:: UI_ABS_SETUP ()

    Set absolute axis information for the device to setup



.. _`ui_abs_setup.description`:

Description
-----------


This ioctl sets one absolute axis information for the input device to be
created. It supersedes the old "struct uinput_user_dev" method, which wrote
part of this data and the content of UI_DEV_SETUP via :c:func:`write`.

The ioctl takes a "struct uinput_abs_setup" object as argument. The fields



.. _`ui_abs_setup.code`:

code
----

The corresponding input code associated with this axis
(ABS_X, ABS_Y, etc...)



.. _`ui_abs_setup.absinfo`:

absinfo
-------

See "struct input_absinfo" for a description of this field.
This field is copied unchanged into the kernel for the
specified axis. If the axis is not enabled via
UI_SET_ABSBIT, this ioctl will enable it.

This ioctl can be called multiple times and will overwrite previous values.
If this ioctl fails with -EINVAL, it is recommended to use the old
"uinput_user_dev" method via :c:func:`write` as a fallback, in case you run on an
old kernel that does not support this ioctl.

This ioctl may fail with -EINVAL if it is not supported or if you passed
incorrect values, -ENOMEM if the kernel runs out of memory or -EFAULT if the
passed uinput_setup object cannot be read/written.
If this call fails, partial data may have already been applied to the
internal device.



.. _`ui_get_sysname`:

UI_GET_SYSNAME
==============

.. c:function:: UI_GET_SYSNAME ( len)

    get the sysfs name of the created uinput device

    :param len:

        *undescribed*



.. _`ui_get_sysname.description`:

Description
-----------


``return`` the sysfs name of the created virtual input device.
The complete sysfs path is then /sys/devices/virtual/input/--NAME--
Usually, it is in the form "inputN"



.. _`ui_get_version`:

UI_GET_VERSION
==============

.. c:function:: UI_GET_VERSION ()

    Return version of uinput protocol



.. _`ui_get_version.description`:

Description
-----------


This writes uinput protocol version implemented by the kernel into
the integer pointed to by the ioctl argument. The protocol version
is hard-coded in the kernel and is independent of the uinput device.

