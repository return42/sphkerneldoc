.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/caam/jr.c

.. _`caam_jr_alloc`:

caam_jr_alloc
=============

.. c:function:: struct device *caam_jr_alloc( void)

    Alloc a job ring for someone to use as needed.

    :param  void:
        no arguments

.. _`caam_jr_alloc.description`:

Description
-----------

returns :  pointer to the newly allocated physical
JobR dev can be written to if successful.

.. _`caam_jr_free`:

caam_jr_free
============

.. c:function:: void caam_jr_free(struct device *rdev)

    Free the Job Ring \ ``rdev``\      - points to the dev that identifies the Job ring to be released.

    :param struct device \*rdev:
        *undescribed*

.. _`caam_jr_enqueue`:

caam_jr_enqueue
===============

.. c:function:: int caam_jr_enqueue(struct device *dev, u32 *desc, void (*) cbk (struct device *dev, u32 *desc, u32 status, void *areq, void *areq)

    Enqueue a job descriptor head. Returns 0 if OK, -EBUSY if the queue is full, -EIO if it cannot map the caller's descriptor.

    :param struct device \*dev:
        contains the job ring device that processed this
        response.

    :param u32 \*desc:
        descriptor that initiated the request, same as
        "desc" being argued to \ :c:func:`caam_jr_enqueue`\ .

    :param (void (\*) cbk (struct device \*dev, u32 \*desc, u32 status, void \*areq):
        pointer to a callback function to be invoked upon completion
        of this request. This has the form:
        callback(struct device \*dev, u32 \*desc, u32 stat, void \*arg)

    :param void \*areq:
        optional pointer to a user argument for use at callback
        time.

.. This file was automatic generated / don't edit.

