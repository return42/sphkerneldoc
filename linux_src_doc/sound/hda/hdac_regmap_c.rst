.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/hdac_regmap.c

.. _`snd_hdac_regmap_init`:

snd_hdac_regmap_init
====================

.. c:function:: int snd_hdac_regmap_init(struct hdac_device *codec)

    Initialize regmap for HDA register accesses

    :param codec:
        the codec object
    :type codec: struct hdac_device \*

.. _`snd_hdac_regmap_init.description`:

Description
-----------

Returns zero for success or a negative error code.

.. _`snd_hdac_regmap_exit`:

snd_hdac_regmap_exit
====================

.. c:function:: void snd_hdac_regmap_exit(struct hdac_device *codec)

    Release the regmap from HDA codec

    :param codec:
        the codec object
    :type codec: struct hdac_device \*

.. _`snd_hdac_regmap_add_vendor_verb`:

snd_hdac_regmap_add_vendor_verb
===============================

.. c:function:: int snd_hdac_regmap_add_vendor_verb(struct hdac_device *codec, unsigned int verb)

    add a vendor-specific verb to regmap

    :param codec:
        the codec object
    :type codec: struct hdac_device \*

    :param verb:
        verb to allow accessing via regmap
    :type verb: unsigned int

.. _`snd_hdac_regmap_add_vendor_verb.description`:

Description
-----------

Returns zero for success or a negative error code.

.. _`snd_hdac_regmap_write_raw`:

snd_hdac_regmap_write_raw
=========================

.. c:function:: int snd_hdac_regmap_write_raw(struct hdac_device *codec, unsigned int reg, unsigned int val)

    write a pseudo register with power mgmt

    :param codec:
        the codec object
    :type codec: struct hdac_device \*

    :param reg:
        pseudo register
    :type reg: unsigned int

    :param val:
        value to write
    :type val: unsigned int

.. _`snd_hdac_regmap_write_raw.description`:

Description
-----------

Returns zero if successful or a negative error code.

.. _`snd_hdac_regmap_read_raw`:

snd_hdac_regmap_read_raw
========================

.. c:function:: int snd_hdac_regmap_read_raw(struct hdac_device *codec, unsigned int reg, unsigned int *val)

    read a pseudo register with power mgmt

    :param codec:
        the codec object
    :type codec: struct hdac_device \*

    :param reg:
        pseudo register
    :type reg: unsigned int

    :param val:
        pointer to store the read value
    :type val: unsigned int \*

.. _`snd_hdac_regmap_read_raw.description`:

Description
-----------

Returns zero if successful or a negative error code.

.. _`snd_hdac_regmap_update_raw`:

snd_hdac_regmap_update_raw
==========================

.. c:function:: int snd_hdac_regmap_update_raw(struct hdac_device *codec, unsigned int reg, unsigned int mask, unsigned int val)

    update a pseudo register with power mgmt

    :param codec:
        the codec object
    :type codec: struct hdac_device \*

    :param reg:
        pseudo register
    :type reg: unsigned int

    :param mask:
        bit mask to udpate
    :type mask: unsigned int

    :param val:
        value to update
    :type val: unsigned int

.. _`snd_hdac_regmap_update_raw.description`:

Description
-----------

Returns zero if successful or a negative error code.

.. This file was automatic generated / don't edit.

