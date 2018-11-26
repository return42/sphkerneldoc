.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/genwqe/genwqe_driver.h

.. _`drv_version`:

DRV_VERSION
===========

.. c:function::  DRV_VERSION()

.. _`drv_version.description`:

Description
-----------

(C) Copyright IBM Corp. 2013

.. _`drv_version.author`:

Author
------

Frank Haverkamp <haver@linux.vnet.ibm.com>

Joerg-Stephan Vogt <jsvogt@de.ibm.com>

Michael Jung <mijung@gmx.net>

Michael Ruettger <michael@ibmra.de>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 2 only)
as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

.. _`ddcb_requ_alloc`:

ddcb_requ_alloc
===============

.. c:function:: struct genwqe_ddcb_cmd *ddcb_requ_alloc( void)

    Allocate a new DDCB execution request

    :param void:
        no arguments
    :type void: 

.. _`ddcb_requ_alloc.description`:

Description
-----------

This data structure contains the user visiable fields of the DDCB
to be executed.

.. _`ddcb_requ_alloc.return`:

Return
------

ptr to genwqe_ddcb_cmd data structure

.. _`ddcb_requ_free`:

ddcb_requ_free
==============

.. c:function:: void ddcb_requ_free(struct genwqe_ddcb_cmd *req)

    Free DDCB execution request.

    :param req:
        ptr to genwqe_ddcb_cmd data structure.
    :type req: struct genwqe_ddcb_cmd \*

.. This file was automatic generated / don't edit.

