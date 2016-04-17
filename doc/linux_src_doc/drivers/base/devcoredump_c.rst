.. -*- coding: utf-8; mode: rst -*-

=============
devcoredump.c
=============


.. _`dev_coredumpv`:

dev_coredumpv
=============

.. c:function:: void dev_coredumpv (struct device *dev, const void *data, size_t datalen, gfp_t gfp)

    create device coredump with vmalloc data

    :param struct device \*dev:
        the struct device for the crashed device

    :param const void \*data:
        vmalloc data containing the device coredump

    :param size_t datalen:
        length of the data

    :param gfp_t gfp:
        allocation flags



.. _`dev_coredumpv.description`:

Description
-----------

This function takes ownership of the vmalloc'ed data and will free
it when it is no longer used. See :c:func:`dev_coredumpm` for more information.



.. _`dev_coredumpm`:

dev_coredumpm
=============

.. c:function:: void dev_coredumpm (struct device *dev, struct module *owner, const void *data, size_t datalen, gfp_t gfp, ssize_t (*read) (char *buffer, loff_t offset, size_t count, const void *data, size_t datalen, void (*free) (const void *data)

    create device coredump with read/free methods

    :param struct device \*dev:
        the struct device for the crashed device

    :param struct module \*owner:
        the module that contains the read/free functions, use ``THIS_MODULE``

    :param const void \*data:
        data cookie for the ``read``\ /\ ``free`` functions

    :param size_t datalen:
        length of the data

    :param gfp_t gfp:
        allocation flags

    :param ssize_t (\*read) (char \*buffer, loff_t offset, size_t count, const void \*data, size_t datalen):
        function to read from the given buffer

    :param void (\*free) (const void \*data):
        function to free the given buffer



.. _`dev_coredumpm.description`:

Description
-----------

Creates a new device coredump for the given device. If a previous one hasn't
been read yet, the new coredump is discarded. The data lifetime is determined
by the device coredump framework and when it is no longer needed the ``free``
function will be called to free the data.

