.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/iio/iio_utils.c

.. _`iioutils_break_up_name`:

iioutils_break_up_name
======================

.. c:function:: int iioutils_break_up_name(const char *full_name, char **generic_name)

    extract generic name from full channel name

    :param full_name:
        the full channel name
    :type full_name: const char \*

    :param generic_name:
        the output generic channel name
    :type generic_name: char \*\*

.. _`iioutils_break_up_name.description`:

Description
-----------

Returns 0 on success, or a negative error code if string extraction failed.

.. _`iioutils_get_type`:

iioutils_get_type
=================

.. c:function:: int iioutils_get_type(unsigned *is_signed, unsigned *bytes, unsigned *bits_used, unsigned *shift, uint64_t *mask, unsigned *be, const char *device_dir, const char *name, const char *generic_name)

    find and process \_type attribute data

    :param is_signed:
        output whether channel is signed
    :type is_signed: unsigned \*

    :param bytes:
        output how many bytes the channel storage occupies
    :type bytes: unsigned \*

    :param bits_used:
        output number of valid bits of data
    :type bits_used: unsigned \*

    :param shift:
        output amount of bits to shift right data before applying bit mask
    :type shift: unsigned \*

    :param mask:
        output a bit mask for the raw data
    :type mask: uint64_t \*

    :param be:
        output if data in big endian
    :type be: unsigned \*

    :param device_dir:
        the IIO device directory
    :type device_dir: const char \*

    :param name:
        the channel name
    :type name: const char \*

    :param generic_name:
        the channel type name
    :type generic_name: const char \*

.. _`iioutils_get_type.description`:

Description
-----------

Returns a value >= 0 on success, otherwise a negative error code.

.. _`iioutils_get_param_float`:

iioutils_get_param_float
========================

.. c:function:: int iioutils_get_param_float(float *output, const char *param_name, const char *device_dir, const char *name, const char *generic_name)

    read a float value from a channel parameter

    :param output:
        output the float value
    :type output: float \*

    :param param_name:
        the parameter name to read
    :type param_name: const char \*

    :param device_dir:
        the IIO device directory in sysfs
    :type device_dir: const char \*

    :param name:
        the channel name
    :type name: const char \*

    :param generic_name:
        the channel type name
    :type generic_name: const char \*

.. _`iioutils_get_param_float.description`:

Description
-----------

Returns a value >= 0 on success, otherwise a negative error code.

.. _`bsort_channel_array_by_index`:

bsort_channel_array_by_index
============================

.. c:function:: void bsort_channel_array_by_index(struct iio_channel_info *ci_array, int cnt)

    sort the array in index order

    :param ci_array:
        the iio_channel_info array to be sorted
    :type ci_array: struct iio_channel_info \*

    :param cnt:
        the amount of array elements
    :type cnt: int

.. _`build_channel_array`:

build_channel_array
===================

.. c:function:: int build_channel_array(const char *device_dir, struct iio_channel_info **ci_array, int *counter)

    function to figure out what channels are present

    :param device_dir:
        the IIO device directory in sysfs
    :type device_dir: const char \*

    :param ci_array:
        output the resulting array of iio_channel_info
    :type ci_array: struct iio_channel_info \*\*

    :param counter:
        output the amount of array elements
    :type counter: int \*

.. _`build_channel_array.description`:

Description
-----------

Returns 0 on success, otherwise a negative error code.

.. _`find_type_by_name`:

find_type_by_name
=================

.. c:function:: int find_type_by_name(const char *name, const char *type)

    function to match top level types by name

    :param name:
        top level type instance name
    :type name: const char \*

    :param type:
        the type of top level instance being searched
    :type type: const char \*

.. _`find_type_by_name.description`:

Description
-----------

Returns the device number of a matched IIO device on success, otherwise a
negative error code.
Typical types this is used for are device and trigger.

.. _`write_sysfs_int`:

write_sysfs_int
===============

.. c:function:: int write_sysfs_int(const char *filename, const char *basedir, int val)

    write an integer value to a sysfs file

    :param filename:
        name of the file to write to
    :type filename: const char \*

    :param basedir:
        the sysfs directory in which the file is to be found
    :type basedir: const char \*

    :param val:
        integer value to write to file
    :type val: int

.. _`write_sysfs_int.description`:

Description
-----------

Returns a value >= 0 on success, otherwise a negative error code.

.. _`write_sysfs_int_and_verify`:

write_sysfs_int_and_verify
==========================

.. c:function:: int write_sysfs_int_and_verify(const char *filename, const char *basedir, int val)

    write an integer value to a sysfs file and verify

    :param filename:
        name of the file to write to
    :type filename: const char \*

    :param basedir:
        the sysfs directory in which the file is to be found
    :type basedir: const char \*

    :param val:
        integer value to write to file
    :type val: int

.. _`write_sysfs_int_and_verify.description`:

Description
-----------

Returns a value >= 0 on success, otherwise a negative error code.

.. _`write_sysfs_string_and_verify`:

write_sysfs_string_and_verify
=============================

.. c:function:: int write_sysfs_string_and_verify(const char *filename, const char *basedir, const char *val)

    string write, readback and verify

    :param filename:
        name of file to write to
    :type filename: const char \*

    :param basedir:
        the sysfs directory in which the file is to be found
    :type basedir: const char \*

    :param val:
        the string to write
    :type val: const char \*

.. _`write_sysfs_string_and_verify.description`:

Description
-----------

Returns a value >= 0 on success, otherwise a negative error code.

.. _`write_sysfs_string`:

write_sysfs_string
==================

.. c:function:: int write_sysfs_string(const char *filename, const char *basedir, const char *val)

    write string to a sysfs file

    :param filename:
        name of file to write to
    :type filename: const char \*

    :param basedir:
        the sysfs directory in which the file is to be found
    :type basedir: const char \*

    :param val:
        the string to write
    :type val: const char \*

.. _`write_sysfs_string.description`:

Description
-----------

Returns a value >= 0 on success, otherwise a negative error code.

.. _`read_sysfs_posint`:

read_sysfs_posint
=================

.. c:function:: int read_sysfs_posint(const char *filename, const char *basedir)

    read an integer value from file

    :param filename:
        name of file to read from
    :type filename: const char \*

    :param basedir:
        the sysfs directory in which the file is to be found
    :type basedir: const char \*

.. _`read_sysfs_posint.description`:

Description
-----------

Returns the read integer value >= 0 on success, otherwise a negative error
code.

.. _`read_sysfs_float`:

read_sysfs_float
================

.. c:function:: int read_sysfs_float(const char *filename, const char *basedir, float *val)

    read a float value from file

    :param filename:
        name of file to read from
    :type filename: const char \*

    :param basedir:
        the sysfs directory in which the file is to be found
    :type basedir: const char \*

    :param val:
        output the read float value
    :type val: float \*

.. _`read_sysfs_float.description`:

Description
-----------

Returns a value >= 0 on success, otherwise a negative error code.

.. _`read_sysfs_string`:

read_sysfs_string
=================

.. c:function:: int read_sysfs_string(const char *filename, const char *basedir, char *str)

    read a string from file

    :param filename:
        name of file to read from
    :type filename: const char \*

    :param basedir:
        the sysfs directory in which the file is to be found
    :type basedir: const char \*

    :param str:
        output the read string
    :type str: char \*

.. _`read_sysfs_string.description`:

Description
-----------

Returns a value >= 0 on success, otherwise a negative error code.

.. This file was automatic generated / don't edit.

