.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/nx/nx-842-pseries.c

.. _`nx842_pseries_compress`:

nx842_pseries_compress
======================

.. c:function:: int nx842_pseries_compress(const unsigned char *in, unsigned int inlen, unsigned char *out, unsigned int *outlen, void *wmem)

    Compress data using the 842 algorithm

    :param const unsigned char \*in:
        Pointer to input buffer

    :param unsigned int inlen:
        Length of input buffer

    :param unsigned char \*out:
        Pointer to output buffer

    :param unsigned int \*outlen:
        Length of output buffer

    :param void \*wmem:
        *undescribed*

.. _`nx842_pseries_compress.description`:

Description
-----------

Compression provide by the NX842 coprocessor on IBM Power systems.
The input buffer is compressed and the result is stored in the
provided output buffer.

Upon return from this function \ ``outlen``\  contains the length of the
compressed data.  If there is an error then \ ``outlen``\  will be 0 and an
error will be specified by the return code from this function.

.. _`nx842_pseries_compress.return`:

Return
------

0          Success, output of length \ ``outlen``\  stored in the buffer at \ ``out``\ 
-ENOMEM    Unable to allocate internal buffers
-ENOSPC    Output buffer is to small
-EIO       Internal error
-ENODEV    Hardware unavailable

.. _`nx842_pseries_decompress`:

nx842_pseries_decompress
========================

.. c:function:: int nx842_pseries_decompress(const unsigned char *in, unsigned int inlen, unsigned char *out, unsigned int *outlen, void *wmem)

    Decompress data using the 842 algorithm

    :param const unsigned char \*in:
        Pointer to input buffer

    :param unsigned int inlen:
        Length of input buffer

    :param unsigned char \*out:
        Pointer to output buffer

    :param unsigned int \*outlen:
        Length of output buffer

    :param void \*wmem:
        *undescribed*

.. _`nx842_pseries_decompress.description`:

Description
-----------

Decompression provide by the NX842 coprocessor on IBM Power systems.
The input buffer is decompressed and the result is stored in the
provided output buffer.  The size allocated to the output buffer is
provided by the caller of this function in \ ``outlen``\ .  Upon return from
this function \ ``outlen``\  contains the length of the decompressed data.
If there is an error then \ ``outlen``\  will be 0 and an error will be
specified by the return code from this function.

.. _`nx842_pseries_decompress.return`:

Return
------

0          Success, output of length \ ``outlen``\  stored in the buffer at \ ``out``\ 
-ENODEV    Hardware decompression device is unavailable
-ENOMEM    Unable to allocate internal buffers
-ENOSPC    Output buffer is to small
-EINVAL    Bad input data encountered when attempting decompress
-EIO       Internal error

.. _`nx842_of_set_defaults`:

nx842_OF_set_defaults
=====================

.. c:function:: int nx842_OF_set_defaults(struct nx842_devdata *devdata)

    - Set default (disabled) values for devdata

    :param struct nx842_devdata \*devdata:
        *undescribed*

.. _`nx842_of_set_defaults.description`:

Description
-----------

\ ``devdata``\  - struct nx842_devdata to update

.. _`nx842_of_set_defaults.return`:

Return
------

0 on success
-ENOENT if \ ``devdata``\  ptr is NULL

.. _`nx842_of_upd_status`:

nx842_OF_upd_status
===================

.. c:function:: int nx842_OF_upd_status(struct property *prop)

    - Check the device info from OF status prop

    :param struct property \*prop:
        *undescribed*

.. _`nx842_of_upd_status.description`:

Description
-----------

The status property indicates if the accelerator is enabled.  If the
device is in the OF tree it indicates that the hardware is present.
The status field indicates if the device is enabled when the status
is 'okay'.  Otherwise the device driver will be disabled.

\ ``prop``\  - struct property point containing the maxsyncop for the update

.. _`nx842_of_upd_status.return`:

Return
------

0 - Device is available
-ENODEV - Device is not available

.. _`nx842_of_upd_maxsglen`:

nx842_OF_upd_maxsglen
=====================

.. c:function:: int nx842_OF_upd_maxsglen(struct nx842_devdata *devdata, struct property *prop)

    - Update the device info from OF maxsglen prop

    :param struct nx842_devdata \*devdata:
        *undescribed*

    :param struct property \*prop:
        *undescribed*

.. _`nx842_of_upd_maxsglen.description`:

Description
-----------

Definition of the 'ibm,max-sg-len' OF property:
This field indicates the maximum byte length of a scatter list
for the platform facility. It is a single cell encoded as with encode-int.

.. _`nx842_of_upd_maxsglen.example`:

Example
-------

.. code-block:: c

     # od -x ibm,max-sg-len
     0000000 0000 0ff0

     In this example, the maximum byte length of a scatter list is
     0x0ff0 (4,080).

    @devdata - struct nx842_devdata to update
    @prop - struct property point containing the maxsyncop for the update


.. _`nx842_of_upd_maxsglen.return`:

Return
------

0 on success
-EINVAL on failure

.. _`nx842_of_upd_maxsyncop`:

nx842_OF_upd_maxsyncop
======================

.. c:function:: int nx842_OF_upd_maxsyncop(struct nx842_devdata *devdata, struct property *prop)

    - Update the device info from OF maxsyncop prop

    :param struct nx842_devdata \*devdata:
        *undescribed*

    :param struct property \*prop:
        *undescribed*

.. _`nx842_of_upd_maxsyncop.description`:

Description
-----------

Definition of the 'ibm,max-sync-cop' OF property:
Two series of cells.  The first series of cells represents the maximums
that can be synchronously compressed. The second series of cells
represents the maximums that can be synchronously decompressed.
1. The first cell in each series contains the count of the number of
data length, scatter list elements pairs that follow – each being
of the form
a. One cell data byte length
b. One cell total number of scatter list elements

.. _`nx842_of_upd_maxsyncop.example`:

Example
-------

.. code-block:: c

     # od -x ibm,max-sync-cop
     0000000 0000 0001 0000 1000 0000 01fe 0000 0001
     0000020 0000 1000 0000 01fe

     In this example, compression supports 0x1000 (4,096) data byte length
     and 0x1fe (510) total scatter list elements.  Decompression supports
     0x1000 (4,096) data byte length and 0x1f3 (510) total scatter list
     elements.

    @devdata - struct nx842_devdata to update
    @prop - struct property point containing the maxsyncop for the update


.. _`nx842_of_upd_maxsyncop.return`:

Return
------

0 on success
-EINVAL on failure

.. _`nx842_of_notifier`:

nx842_OF_notifier
=================

.. c:function:: int nx842_OF_notifier(struct notifier_block *np, unsigned long action, void *data)

    Process updates to OF properties for the device

    :param struct notifier_block \*np:
        notifier block

    :param unsigned long action:
        notifier action

    :param void \*data:
        *undescribed*

.. _`nx842_of_notifier.return`:

Return
------

NOTIFY_OK on success
NOTIFY_BAD encoded with error number on failure, use
\ :c:func:`notifier_to_errno`\  to decode this value

.. This file was automatic generated / don't edit.

