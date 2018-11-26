.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/nx/nx.c

.. _`nx_hcall_sync`:

nx_hcall_sync
=============

.. c:function:: int nx_hcall_sync(struct nx_crypto_ctx *nx_ctx, struct vio_pfo_op *op, u32 may_sleep)

    :param nx_ctx:
        *undescribed*
    :type nx_ctx: struct nx_crypto_ctx \*

    :param op:
        *undescribed*
    :type op: struct vio_pfo_op \*

    :param may_sleep:
        *undescribed*
    :type may_sleep: u32

.. _`nx_hcall_sync.description`:

Description
-----------

Copyright (C) 2011-2012 International Business Machines Inc.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 2 only.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

.. _`nx_hcall_sync.author`:

Author
------

Kent Yoder <yoder1@us.ibm.com>

.. _`nx_build_sg_list`:

nx_build_sg_list
================

.. c:function:: struct nx_sg *nx_build_sg_list(struct nx_sg *sg_head, u8 *start_addr, unsigned int *len, u32 sgmax)

    build an NX scatter list describing a single  buffer

    :param sg_head:
        pointer to the first scatter list element to build
    :type sg_head: struct nx_sg \*

    :param start_addr:
        pointer to the linear buffer
    :type start_addr: u8 \*

    :param len:
        length of the data at \ ``start_addr``\ 
    :type len: unsigned int \*

    :param sgmax:
        the largest number of scatter list elements we're allowed to create
    :type sgmax: u32

.. _`nx_build_sg_list.description`:

Description
-----------

This function will start writing nx_sg elements at \ ``sg_head``\  and keep
writing them until all of the data from \ ``start_addr``\  is described or
until sgmax elements have been written. Scatter list elements will be
created such that none of the elements describes a buffer that crosses a 4K
boundary.

.. _`nx_walk_and_build`:

nx_walk_and_build
=================

.. c:function:: struct nx_sg *nx_walk_and_build(struct nx_sg *nx_dst, unsigned int sglen, struct scatterlist *sg_src, unsigned int start, unsigned int *src_len)

    walk a linux scatterlist and build an nx scatterlist

    :param nx_dst:
        pointer to the first nx_sg element to write
    :type nx_dst: struct nx_sg \*

    :param sglen:
        max number of nx_sg entries we're allowed to write
    :type sglen: unsigned int

    :param sg_src:
        pointer to the source linux scatterlist to walk
    :type sg_src: struct scatterlist \*

    :param start:
        number of bytes to fast-forward past at the beginning of \ ``sg_src``\ 
    :type start: unsigned int

    :param src_len:
        number of bytes to walk in \ ``sg_src``\ 
    :type src_len: unsigned int \*

.. _`trim_sg_list`:

trim_sg_list
============

.. c:function:: long int trim_sg_list(struct nx_sg *sg, struct nx_sg *end, unsigned int delta, unsigned int *nbytes)

    ensures the bound in sg list.

    :param sg:
        sg list head
    :type sg: struct nx_sg \*

    :param end:
        sg lisg end
    :type end: struct nx_sg \*

    :param delta:
        is the amount we need to crop in order to bound the list.
    :type delta: unsigned int

    :param nbytes:
        *undescribed*
    :type nbytes: unsigned int \*

.. _`nx_build_sg_lists`:

nx_build_sg_lists
=================

.. c:function:: int nx_build_sg_lists(struct nx_crypto_ctx *nx_ctx, struct blkcipher_desc *desc, struct scatterlist *dst, struct scatterlist *src, unsigned int *nbytes, unsigned int offset, u8 *iv)

    walk the input scatterlists and build arrays of NX scatterlists based on them.

    :param nx_ctx:
        NX crypto context for the lists we're building
    :type nx_ctx: struct nx_crypto_ctx \*

    :param desc:
        the block cipher descriptor for the operation
    :type desc: struct blkcipher_desc \*

    :param dst:
        destination scatterlist
    :type dst: struct scatterlist \*

    :param src:
        source scatterlist
    :type src: struct scatterlist \*

    :param nbytes:
        length of data described in the scatterlists
    :type nbytes: unsigned int \*

    :param offset:
        number of bytes to fast-forward past at the beginning of
        scatterlists.
    :type offset: unsigned int

    :param iv:
        destination for the iv data, if the algorithm requires it
    :type iv: u8 \*

.. _`nx_build_sg_lists.description`:

Description
-----------

This is common code shared by all the AES algorithms. It uses the block
cipher walk routines to traverse input and output scatterlists, building
corresponding NX scatterlists

.. _`nx_ctx_init`:

nx_ctx_init
===========

.. c:function:: void nx_ctx_init(struct nx_crypto_ctx *nx_ctx, unsigned int function)

    initialize an nx_ctx's vio_pfo_op struct

    :param nx_ctx:
        the nx context to initialize
    :type nx_ctx: struct nx_crypto_ctx \*

    :param function:
        the function code for the op
    :type function: unsigned int

.. _`nx_of_init`:

nx_of_init
==========

.. c:function:: void nx_of_init(struct device *dev, struct nx_of *props)

    read openFirmware values from the device tree

    :param dev:
        device handle
    :type dev: struct device \*

    :param props:
        pointer to struct to hold the properties values
    :type props: struct nx_of \*

.. _`nx_of_init.description`:

Description
-----------

Called once at driver probe time, this function will read out the
openFirmware properties we use at runtime. If all the OF properties are
acceptable, when we exit this function props->flags will indicate that
we're ready to register our crypto algorithms.

.. _`nx_register_algs`:

nx_register_algs
================

.. c:function:: int nx_register_algs( void)

    register algorithms with the crypto API

    :param void:
        no arguments
    :type void: 

.. _`nx_register_algs.description`:

Description
-----------

Called from \ :c:func:`nx_probe`\ 

If all OF properties are in an acceptable state, the driver flags will
indicate that we're ready and we'll create our debugfs files and register
out crypto algorithms.

.. _`nx_crypto_ctx_init`:

nx_crypto_ctx_init
==================

.. c:function:: int nx_crypto_ctx_init(struct nx_crypto_ctx *nx_ctx, u32 fc, u32 mode)

    create and initialize a crypto api context

    :param nx_ctx:
        the crypto api context
    :type nx_ctx: struct nx_crypto_ctx \*

    :param fc:
        function code for the context
    :type fc: u32

    :param mode:
        the function code specific mode for this context
    :type mode: u32

.. _`nx_crypto_ctx_exit`:

nx_crypto_ctx_exit
==================

.. c:function:: void nx_crypto_ctx_exit(struct crypto_tfm *tfm)

    destroy a crypto api context

    :param tfm:
        the crypto transform pointer for the context
    :type tfm: struct crypto_tfm \*

.. _`nx_crypto_ctx_exit.description`:

Description
-----------

As crypto API contexts are destroyed, this exit hook is called to free the
memory associated with it.

.. This file was automatic generated / don't edit.

