.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/gpio/gpio-utils.c

.. _`gpiotools_request_linehandle`:

gpiotools_request_linehandle
============================

.. c:function:: int gpiotools_request_linehandle(const char *device_name, unsigned int *lines, unsigned int nlines, unsigned int flag, struct gpiohandle_data *data, const char *consumer_label)

    Operation of gpio

    :param const char \*device_name:
        *undescribed*

    :param unsigned int \*lines:
        *undescribed*

    :param unsigned int nlines:
        *undescribed*

    :param unsigned int flag:
        *undescribed*

    :param struct gpiohandle_data \*data:
        *undescribed*

    :param const char \*consumer_label:
        *undescribed*

.. _`gpiotools_request_linehandle.description`:

Description
-----------

Provide the api of gpiochip for chardev interface. There are two
types of api.  The first one provide as same function as each
ioctl, including request and release for lines of gpio, read/write
the value of gpio. If the user want to do lots of read and write of
lines of gpio, user should use this type of api.

The second one provide the easy to use api for user. Each of the
following api will request gpio lines, do the operation and then
release these lines.

.. _`gpiotools_set_values`:

gpiotools_set_values
====================

.. c:function:: int gpiotools_set_values(const int fd, struct gpiohandle_data *data)

    Set the value of gpio(s)

    :param const int fd:
        The fd returned by
        \ :c:func:`gpiotools_request_linehandle`\ .

    :param struct gpiohandle_data \*data:
        The array of values want to set.

.. _`gpiotools_set_values.return`:

Return
------

On success return 0;
On failure return the errno.

.. _`gpiotools_get_values`:

gpiotools_get_values
====================

.. c:function:: int gpiotools_get_values(const int fd, struct gpiohandle_data *data)

    Get the value of gpio(s)

    :param const int fd:
        The fd returned by
        \ :c:func:`gpiotools_request_linehandle`\ .

    :param struct gpiohandle_data \*data:
        The array of values get from hardware.

.. _`gpiotools_get_values.return`:

Return
------

On success return 0;
On failure return the errno.

.. _`gpiotools_release_linehandle`:

gpiotools_release_linehandle
============================

.. c:function:: int gpiotools_release_linehandle(const int fd)

    Release the line(s) of gpiochip

    :param const int fd:
        The fd returned by
        \ :c:func:`gpiotools_request_linehandle`\ .

.. _`gpiotools_release_linehandle.return`:

Return
------

On success return 0;
On failure return the errno.

.. _`gpiotools_get`:

gpiotools_get
=============

.. c:function:: int gpiotools_get(const char *device_name, unsigned int line)

    Get value from specific line

    :param const char \*device_name:
        The name of gpiochip without prefix "/dev/",
        such as "gpiochip0"

    :param unsigned int line:
        number of line, such as 2.

.. _`gpiotools_get.return`:

Return
------

On success return 0;
On failure return the errno.

.. _`gpiotools_gets`:

gpiotools_gets
==============

.. c:function:: int gpiotools_gets(const char *device_name, unsigned int *lines, unsigned int nlines, struct gpiohandle_data *data)

    Get values from specific lines.

    :param const char \*device_name:
        The name of gpiochip without prefix "/dev/",
        such as "gpiochip0".

    :param unsigned int \*lines:
        An array desired lines, specified by offset
        index for the associated GPIO device.

    :param unsigned int nlines:
        *undescribed*

    :param struct gpiohandle_data \*data:
        The array of values get from gpiochip.

.. _`gpiotools_gets.return`:

Return
------

On success return 0;
On failure return the errno.

.. _`gpiotools_set`:

gpiotools_set
=============

.. c:function:: int gpiotools_set(const char *device_name, unsigned int line, unsigned int value)

    Set value to specific line

    :param const char \*device_name:
        The name of gpiochip without prefix "/dev/",
        such as "gpiochip0"

    :param unsigned int line:
        number of line, such as 2.

    :param unsigned int value:
        The value of gpio, must be 0(low) or 1(high).

.. _`gpiotools_set.return`:

Return
------

On success return 0;
On failure return the errno.

.. _`gpiotools_sets`:

gpiotools_sets
==============

.. c:function:: int gpiotools_sets(const char *device_name, unsigned int *lines, unsigned int nlines, struct gpiohandle_data *data)

    Set values to specific lines.

    :param const char \*device_name:
        The name of gpiochip without prefix "/dev/",
        such as "gpiochip0".

    :param unsigned int \*lines:
        An array desired lines, specified by offset
        index for the associated GPIO device.

    :param unsigned int nlines:
        *undescribed*

    :param struct gpiohandle_data \*data:
        The array of values set to gpiochip, must be
        0(low) or 1(high).

.. _`gpiotools_sets.return`:

Return
------

On success return 0;
On failure return the errno.

.. This file was automatic generated / don't edit.

