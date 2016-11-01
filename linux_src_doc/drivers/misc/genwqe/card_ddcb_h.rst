.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/genwqe/card_ddcb.h

.. _`asiv_length`:

ASIV_LENGTH
===========

.. c:function::  ASIV_LENGTH()

.. _`asiv_length.description`:

Description
-----------

(C) Copyright IBM Corp. 2013

.. _`asiv_length.author`:

Author
------

Frank Haverkamp <haver@linux.vnet.ibm.com>

Joerg-Stephan Vogt <jsvogt@de.ibm.com>

Michael Jung <mijung@gmx.net>

Michael Ruettger <michael@ibmra.de>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2, or (at your option)
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

.. _`sg_entry`:

struct sg_entry
===============

.. c:type:: struct sg_entry

    Scatter gather list

.. _`sg_entry.definition`:

Definition
----------

.. code-block:: c

    struct sg_entry {
        __be64 target_addr;
        __be32 len;
        __be32 flags;
    }

.. _`sg_entry.members`:

Members
-------

target_addr
    Either a dma addr of memory to work on or a
    dma addr or a subsequent sglist block.

len
    Length of the data block.

flags
    See above.

.. _`sg_entry.description`:

Description
-----------

Depending on the command the GenWQE card can use a scatter gather
list to describe the memory it works on. Always 8 sg_entry's form
a block.

.. This file was automatic generated / don't edit.

