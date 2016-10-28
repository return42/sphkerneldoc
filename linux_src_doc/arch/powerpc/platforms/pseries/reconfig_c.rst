.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/pseries/reconfig.c

.. _`parse_next_property`:

parse_next_property
===================

.. c:function:: char *parse_next_property(char *buf, char *end, char **name, int *length, unsigned char **value)

    process the next property from raw input buffer

    :param char \*buf:
        input buffer, must be nul-terminated

    :param char \*end:
        end of the input buffer + 1, for validation

    :param char \*\*name:
        return value; set to property name in buf

    :param int \*length:
        return value; set to length of value

    :param unsigned char \*\*value:
        return value; set to the property value in buf

.. _`parse_next_property.description`:

Description
-----------

Note that the caller must make copies of the name and value returned,
this function does no allocation or copying of the data.  Return value
is set to the next name in buf, or NULL on error.

.. _`ofdt_write`:

ofdt_write
==========

.. c:function:: ssize_t ofdt_write(struct file *file, const char __user *buf, size_t count, loff_t *off)

    perform operations on the Open Firmware device tree

    :param struct file \*file:
        not used

    :param const char __user \*buf:
        command and arguments

    :param size_t count:
        size of the command buffer

    :param loff_t \*off:
        not used

.. _`ofdt_write.description`:

Description
-----------

Operations supported at this time are addition and removal of
whole nodes along with their properties.  Operations on individual
properties are not implemented (yet).

.. This file was automatic generated / don't edit.

