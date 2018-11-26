.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/st_slim_rproc.c

.. _`st_slim_rproc_alloc`:

st_slim_rproc_alloc
===================

.. c:function:: struct st_slim_rproc *st_slim_rproc_alloc(struct platform_device *pdev, char *fw_name)

    allocate and initialise slim rproc

    :param pdev:
        Pointer to the platform_device struct
    :type pdev: struct platform_device \*

    :param fw_name:
        Name of firmware for rproc to use
    :type fw_name: char \*

.. _`st_slim_rproc_alloc.description`:

Description
-----------

Function for allocating and initialising a slim rproc for use by
device drivers whose IP is based around the SLIM core. It
obtains and enables any clocks required by the SLIM core and also
ioremaps the various IO.

Returns st_slim_rproc pointer or \ :c:func:`PTR_ERR`\  on error.

.. _`st_slim_rproc_put`:

st_slim_rproc_put
=================

.. c:function:: void st_slim_rproc_put(struct st_slim_rproc *slim_rproc)

    put slim rproc resources

    :param slim_rproc:
        Pointer to the st_slim_rproc struct
    :type slim_rproc: struct st_slim_rproc \*

.. _`st_slim_rproc_put.description`:

Description
-----------

Function for calling respective \_put() functions on slim_rproc resources.

.. This file was automatic generated / don't edit.

