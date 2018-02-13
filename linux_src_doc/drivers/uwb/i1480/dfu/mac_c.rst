.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/i1480/dfu/mac.c

.. _`fw_hdrs_load`:

fw_hdrs_load
============

.. c:function:: int fw_hdrs_load(struct i1480 *i1480, struct fw_hdr **phdr, const char *_data, size_t data_size)

    chain of headers linking them together.

    :param struct i1480 \*i1480:
        *undescribed*

    :param struct fw_hdr \*\*phdr:
        where to place the pointer to the first header (headers link
        to the next via the \ ``hdr``\ ->next ptr); need to free the whole
        chain when done.

    :param const char \*_data:
        Pointer to the data buffer.

    :param size_t data_size:
        *undescribed*

.. _`fw_hdrs_load.description`:

Description
-----------

Goes over the whole binary blob; reads the first chunk and creates
a fw hdr from it (which points to where the data is in \ ``_data``\  and
the length of the chunk); then goes on to the next chunk until
done. Each header is linked to the next.

.. _`i1480_fw_cmp`:

i1480_fw_cmp
============

.. c:function:: ssize_t i1480_fw_cmp(struct i1480 *i1480, struct fw_hdr *hdr)

    :param struct i1480 \*i1480:
        Device instance

    :param struct fw_hdr \*hdr:
        Pointer to the firmware chunk

.. _`i1480_fw_cmp.description`:

Description
-----------

Kind of dirty and simplistic, but does the trick in both the PCI
and USB version. We do a quick[er] \ :c:func:`memcmp`\ , and if it fails, we do
a byte-by-byte to find the offset.

.. _`mac_fw_hdrs_push`:

mac_fw_hdrs_push
================

.. c:function:: int mac_fw_hdrs_push(struct i1480 *i1480, struct fw_hdr *hdr, const char *fw_name, const char *fw_tag)

    :param struct i1480 \*i1480:
        *undescribed*

    :param struct fw_hdr \*hdr:
        Processed firmware

    :param const char \*fw_name:
        *undescribed*

    :param const char \*fw_tag:
        *undescribed*

.. _`__mac_fw_upload`:

\__mac_fw_upload
================

.. c:function:: int __mac_fw_upload(struct i1480 *i1480, const char *fw_name, const char *fw_tag)

    :param struct i1480 \*i1480:
        Device instance

    :param const char \*fw_name:
        Name of firmware file to upload.

    :param const char \*fw_tag:
        Name of the firmware type (for messages)
        [eg: MAC, PRE]

.. _`i1480_pre_fw_upload`:

i1480_pre_fw_upload
===================

.. c:function:: int i1480_pre_fw_upload(struct i1480 *i1480)

    PHY firmware

    :param struct i1480 \*i1480:
        *undescribed*

.. _`i1480_cmd_reset`:

i1480_cmd_reset
===============

.. c:function:: int i1480_cmd_reset(struct i1480 *i1480)

    :param struct i1480 \*i1480:
        Device's instance

.. _`i1480_cmd_reset.description`:

Description
-----------

We put the command on kmalloc'ed memory as some arches cannot do
USB from the stack. The reply event is copied from an stage buffer,
so it can be in the stack. See WUSB1.0[8.6.2.4] for more details.

We issue the reset to make sure the UWB controller reinits the PHY;
this way we can now if the PHY init went ok.

.. _`i1480_mac_fw_upload`:

i1480_mac_fw_upload
===================

.. c:function:: int i1480_mac_fw_upload(struct i1480 *i1480)

    :param struct i1480 \*i1480:
        Device instance

.. _`i1480_mac_fw_upload.description`:

Description
-----------

This has to be called after the pre fw has been uploaded (if
there is any).

.. This file was automatic generated / don't edit.

